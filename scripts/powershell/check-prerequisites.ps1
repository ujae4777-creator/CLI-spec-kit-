#!/usr/bin/env pwsh
# HYspec — SDD 선행 조건 검사 (Spec Kit check-prerequisites.ps1 축소판)
#
# Usage: ./check-prerequisites.ps1 [OPTIONS] [feature-folder-name]
#
# OPTIONS:
#   -Json           JSON 출력
#   -RequireSpec    spec.md 필요 (plan 단계 전)
#   -RequireTasks   tasks.md 필요 (implement 단계 전)
#   -IncludeTasks   AVAILABLE_DOCS 에 tasks.md 포함
#   -PathsOnly      경로만 출력 (검사 안 함)
#   -Help           도움말

[CmdletBinding()]
param(
    [string]$Feature,
    [switch]$Json,
    [switch]$RequireSpec,
    [switch]$RequireTasks,
    [switch]$IncludeTasks,
    [switch]$PathsOnly,
    [switch]$Help
)

$ErrorActionPreference = 'Stop'

if ($Help) {
    Write-Output @"
Usage: check-prerequisites.ps1 [OPTIONS] [feature-folder-name]

HYspec SDD prerequisite checks.

OPTIONS:
  -Json           Output in JSON format
  -RequireSpec    Require spec.md (before plan / checklist on spec)
  -RequireTasks   Require tasks.md (before implement)
  -IncludeTasks   Include tasks.md in AVAILABLE_DOCS when present
  -PathsOnly      Output paths only (no validation)
  -Help           Show this help

EXAMPLES:
  # Paths for active feature (Agent / skill setup)
  .\check-prerequisites.ps1 -Json -PathsOnly

  # Before plan (spec.md required)
  .\check-prerequisites.ps1 -Json -RequireSpec -PathsOnly

  # Before tasks / analyze (plan.md required) — default validation
  .\check-prerequisites.ps1 -Json

  # Before implement (plan + tasks required)
  .\check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks
"@
    exit 0
}

function Find-ProjectRoot {
    $current = (Get-Location).Path
    while ($current) {
        if (Test-Path -LiteralPath (Join-Path $current '.specify') -PathType Container) {
            return $current
        }
        $parent = Split-Path $current -Parent
        if ([string]::IsNullOrEmpty($parent) -or $parent -eq $current) {
            return $null
        }
        $current = $parent
    }
    return $null
}

function Get-FeatureDir {
    param(
        [string]$ProjectRoot,
        [string]$Name
    )

    $specsDir = Join-Path $ProjectRoot 'specs'
    if (-not (Test-Path -LiteralPath $specsDir -PathType Container)) {
        Write-Error "No specs/ folder. Run hyspec feature first."
        exit 1
    }

    if ($Name) {
        $dir = Join-Path $specsDir $Name
        if (-not (Test-Path -LiteralPath $dir -PathType Container)) {
            Write-Error "Feature not found: $dir"
            exit 1
        }
        return $dir
    }

    $featureJson = Join-Path (Join-Path $ProjectRoot '.specify') 'feature.json'
    if (Test-Path -LiteralPath $featureJson -PathType Leaf) {
        $data = Get-Content -LiteralPath $featureJson -Raw | ConvertFrom-Json
        if ($data.feature_directory) {
            $dir = Join-Path $ProjectRoot ($data.feature_directory -replace '/', '\')
            if (Test-Path -LiteralPath $dir -PathType Container) {
                return $dir
            }
            Write-Error "Feature in feature.json not found: $($data.feature_directory)"
            exit 1
        }
    }

    $candidates = Get-ChildItem -LiteralPath $specsDir -Directory | Where-Object {
        $_.Name -match '^\d{3}-'
    }
    if (-not $candidates) {
        Write-Error "No feature folders in specs/."
        exit 1
    }
    return ($candidates | Sort-Object { [int]$_.Name.Substring(0, 3) } -Descending | Select-Object -First 1).FullName
}

function Write-CheckError {
    param([string]$Message, [string]$Hint)
    [Console]::Error.WriteLine("ERROR: $Message")
    if ($Hint) {
        [Console]::Error.WriteLine($Hint)
    }
    exit 1
}

$projectRoot = Find-ProjectRoot
if (-not $projectRoot) {
    Write-CheckError 'No .specify/ found.' 'Run hyspec init first.'
}

$featureDir = Get-FeatureDir -ProjectRoot $projectRoot -Name $Feature
$featureName = Split-Path $featureDir -Leaf

$paths = [ordered]@{
    REPO_ROOT    = $projectRoot
    FEATURE_DIR  = $featureDir
    FEATURE_NAME = $featureName
    FEATURE_SPEC = Join-Path $featureDir 'spec.md'
    IMPL_PLAN    = Join-Path $featureDir 'plan.md'
    TASKS        = Join-Path $featureDir 'tasks.md'
    CONSTITUTION = Join-Path $projectRoot '.specify\memory\constitution.md'
    CHECKLISTS   = Join-Path $featureDir 'checklists'
}

if ($PathsOnly) {
    if ($Json) {
        [PSCustomObject]$paths | ConvertTo-Json -Compress
    } else {
        foreach ($key in $paths.Keys) {
            Write-Output "${key}: $($paths[$key])"
        }
    }
    exit 0
}

if (-not (Test-Path -LiteralPath $paths.FEATURE_DIR -PathType Container)) {
    Write-CheckError "Feature directory not found: $($paths.FEATURE_DIR)" 'Run hyspec feature first.'
}

if ($RequireSpec) {
    if (-not (Test-Path -LiteralPath $paths.FEATURE_SPEC -PathType Leaf)) {
        Write-CheckError "spec.md not found: $($paths.FEATURE_SPEC)" 'Run hyspec feature or hyspec-specify skill first.'
    }
} else {
    if (-not (Test-Path -LiteralPath $paths.IMPL_PLAN -PathType Leaf)) {
        Write-CheckError "plan.md not found: $($paths.IMPL_PLAN)" 'Run hyspec plan first.'
    }
}

if ($RequireTasks) {
    if (-not (Test-Path -LiteralPath $paths.TASKS -PathType Leaf)) {
        Write-CheckError "tasks.md not found: $($paths.TASKS)" 'Run hyspec tasks first.'
    }
}

$docs = @()
if (Test-Path -LiteralPath $paths.FEATURE_SPEC -PathType Leaf) { $docs += 'spec.md' }
if (Test-Path -LiteralPath $paths.IMPL_PLAN -PathType Leaf) { $docs += 'plan.md' }
if ($IncludeTasks -and (Test-Path -LiteralPath $paths.TASKS -PathType Leaf)) {
    $docs += 'tasks.md'
}
if ((Test-Path -LiteralPath $paths.CHECKLISTS -PathType Container) -and
    (Get-ChildItem -LiteralPath $paths.CHECKLISTS -File -ErrorAction SilentlyContinue | Select-Object -First 1)) {
    $docs += 'checklists/'
}
if (Test-Path -LiteralPath $paths.CONSTITUTION -PathType Leaf) {
    $docs += 'constitution.md'
}

if ($Json) {
    [PSCustomObject]@{
        REPO_ROOT      = $paths.REPO_ROOT
        FEATURE_DIR    = $paths.FEATURE_DIR
        FEATURE_NAME   = $paths.FEATURE_NAME
        FEATURE_SPEC   = $paths.FEATURE_SPEC
        IMPL_PLAN      = $paths.IMPL_PLAN
        TASKS          = $paths.TASKS
        CONSTITUTION   = $paths.CONSTITUTION
        AVAILABLE_DOCS = $docs
    } | ConvertTo-Json -Compress
} else {
    Write-Output "FEATURE_DIR: $($paths.FEATURE_DIR)"
    Write-Output "AVAILABLE_DOCS: $($docs -join ', ')"
    foreach ($doc in @('spec.md', 'plan.md', 'tasks.md', 'checklists/', 'constitution.md')) {
        $label = $doc.TrimEnd('/')
        $ok = $docs -contains $doc
        Write-Output "  $label`: $(if ($ok) { 'yes' } else { 'no' })"
    }
}
