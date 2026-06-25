#!/usr/bin/env pwsh
# HYspec 학습용 — feature 폴더 만들기 (Spec Kit create-new-feature.ps1 축소판)
# Usage: ./create-new-feature.ps1 "Add user login"

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Description
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

function Get-NextFeatureNumber {
    param([string]$SpecsDir)

    $highest = 0
    if (Test-Path -LiteralPath $SpecsDir -PathType Container) {
        Get-ChildItem -LiteralPath $SpecsDir -Directory | ForEach-Object {
            if ($_.Name -match '^(\d{3})-') {
                $num = [int]$matches[1]
                if ($num -gt $highest) { $highest = $num }
            }
        }
    }
    return $highest + 1
}

function Get-Slug {
    param([string]$Text)

    $clean = ($Text.ToLower() -replace '[^a-z0-9\s]', ' ').Trim()
    $words = $clean -split '\s+' | Where-Object { $_.Length -ge 3 } | Select-Object -First 3
    if ($words.Count -gt 0) {
        return ($words -join '-')
    }
    return 'feature'
}

$projectRoot = Find-ProjectRoot
if (-not $projectRoot) {
    Write-Error "No .specify/ found. Run hyspec init first."
    exit 1
}

$specsDir = Join-Path $projectRoot 'specs'
New-Item -ItemType Directory -Path $specsDir -Force | Out-Null

$number = Get-NextFeatureNumber -SpecsDir $specsDir
$branchName = ('{0:000}' -f $number) + '-' + (Get-Slug -Text $Description)
$featureDir = Join-Path $specsDir $branchName
$specFile = Join-Path $featureDir 'spec.md'
$template = Join-Path $projectRoot '.specify\templates\spec-template.md'

New-Item -ItemType Directory -Path $featureDir -Force | Out-Null

if (Test-Path -LiteralPath $template -PathType Leaf) {
    Copy-Item -LiteralPath $template -Destination $specFile -Force
} else {
    Write-Error "Spec template not found: $template"
    exit 1
}

Write-Output "FEATURE_DIR: $featureDir"
Write-Output "SPEC_FILE: $specFile"
