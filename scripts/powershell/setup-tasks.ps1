#!/usr/bin/env pwsh
# HYspec 학습용 — tasks.md 템플릿 깔기 (hyspec tasks 와 동일)
# Usage: ./setup-tasks.ps1 [feature-folder-name]

param(
    [string]$Feature
)

$ErrorActionPreference = 'Stop'

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

$projectRoot = Find-ProjectRoot
if (-not $projectRoot) {
    Write-Error "No .specify/ found. Run hyspec init first."
    exit 1
}

$featureDir = Get-FeatureDir -ProjectRoot $projectRoot -Name $Feature
$planFile = Join-Path $featureDir 'plan.md'
if (-not (Test-Path -LiteralPath $planFile -PathType Leaf)) {
    Write-Error "plan.md required before tasks: $planFile"
    exit 1
}

$tasksFile = Join-Path $featureDir 'tasks.md'
if (Test-Path -LiteralPath $tasksFile -PathType Leaf) {
    Write-Output "EXISTS: $tasksFile"
    Write-Output "Use hyspec-tasks skill to update tasks.md (script does not overwrite)"
    exit 0
}

$template = Join-Path $projectRoot '.specify\templates\tasks-template.md'
if (-not (Test-Path -LiteralPath $template -PathType Leaf)) {
    Write-Error "Tasks template not found: $template"
    exit 1
}

Copy-Item -LiteralPath $template -Destination $tasksFile -Force
Write-Output "CREATED: $tasksFile"
Write-Output "Next: use hyspec-tasks skill in Cursor to fill tasks.md from plan.md"
