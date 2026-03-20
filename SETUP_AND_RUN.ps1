#!/usr/bin/env pwsh
<#
.SYNOPSIS
    SETUP_AND_RUN.ps1 - PowerShell Setup Script for Fact-Checker
.DESCRIPTION
    One-command setup for the Automated Fact-Checker system on Windows
.NOTES
    Run with: powershell -ExecutionPolicy Bypass -File SETUP_AND_RUN.ps1
#>

Write-Host "`n" -ForegroundColor Green
Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║          🚀 AUTOMATED FACT-CHECKER SETUP (PowerShell)        ║" -ForegroundColor Cyan
Write-Host "║        Installs everything and runs the application          ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python is not installed!" -ForegroundColor Red
    Write-Host "   Please install Python from: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "   Make sure to check 'Add Python to PATH'" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Run the Python setup script
Write-Host "`nStarting the setup process..." -ForegroundColor Yellow
Write-Host "This may take a few minutes on first run..." -ForegroundColor Gray
Write-Host ""

python SETUP_AND_RUN.py

Write-Host "`nSetup complete!" -ForegroundColor Green
