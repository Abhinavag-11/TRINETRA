@echo off
setlocal enabledelayedexpansion

echo ============================================================
echo   TRINETRA — Standalone Windows Executable Builder (PyInstaller)
echo   SIH 2026 Prototype • Problem Statement ID: SIH26187
echo ============================================================

echo [1/3] Checking dependencies...
python -m pip install -r requirements.txt
python -m pip install pyinstaller

echo [2/3] Building TRINETRA.exe using trinetra.spec...
pyinstaller --noconfirm trinetra.spec

if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Build failed! Check the error log above.
    pause
    exit /b %ERRORLEVEL%
)

echo [3/3] Creating exportable ZIP package...
powershell -Command "if (Test-Path 'dist\TRINETRA') { Compress-Archive -Path 'dist\TRINETRA' -DestinationPath 'dist\TRINETRA_Standalone_Windows_x64.zip' -Force; Write-Host 'ZIP package generated successfully: dist\TRINETRA_Standalone_Windows_x64.zip' }"

echo ============================================================
echo   BUILD & EXPORT COMPLETED SUCCESSFULLY!
echo ============================================================
echo   Executable Folder : dist\TRINETRA\
echo   Direct Launch EXE : dist\TRINETRA\TRINETRA.exe
echo   Exportable ZIP    : dist\TRINETRA_Standalone_Windows_x64.zip
echo ============================================================
pause
