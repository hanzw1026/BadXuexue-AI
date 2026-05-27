@echo off
chcp 936 >nul
title SnowAI Installer

echo ========================================
echo SnowAI Assistant - Full Installer
echo ========================================
echo.
echo This script will:
echo   1. Install Python (if not installed)
echo   2. Install all Python dependencies
echo   3. Install Poppler and Tesseract
echo   4. Download AI Model
echo   5. Create launcher and desktop shortcut
echo.

set "APP_DIR=%~dp0"
cd /d "%APP_DIR%"

echo Install dir: %APP_DIR%
echo.

net session >nul 2>&1
if errorlevel 1 (
    echo Requesting administrator privileges...
    powershell start -verb runas '%0'
    exit /b
)

REM ========== 0. Extract ForWindows.zip if needed ==========
if not exist "%APP_DIR%ForWindows\" (
    if exist "%APP_DIR%ForWindows.zip" (
        echo Extracting ForWindows.zip...
        powershell -Command "Expand-Archive -Force -Path '%APP_DIR%ForWindows.zip' -DestinationPath '%APP_DIR%'"
        echo Extract completed.
    ) else (
        echo ForWindows.zip not found, skipping.
    )
) else (
    echo ForWindows folder already exists.
)

REM ========== 1. Install VC Runtime ==========
echo.
echo [1/7] Installing Visual C++ Runtime...
if exist "%APP_DIR%ForWindows\VC_redist.x64.exe" (
    start /wait %APP_DIR%ForWindows\VC_redist.x64.exe /quiet /norestart
    echo   VC++ Runtime installed
) else (
    echo   VC_redist.x64.exe not found, skipped
)

REM ========== 2. Install Poppler ==========
echo.
echo [2/7] Installing Poppler...
if exist "%APP_DIR%ForWindows\poppler" (
    echo   Copying Poppler to C:\poppler...
    xcopy /E /I /Y "%APP_DIR%ForWindows\poppler" "C:\poppler" >nul
    echo   Adding Poppler to system PATH...
    setx /M PATH "%PATH%;C:\poppler\Library\bin" >nul
    echo   Poppler installed
) else (
    echo   Poppler folder not found, skipped
)

REM ========== 3. Install Tesseract ==========
echo.
echo [3/7] Installing Tesseract...
if exist "%APP_DIR%ForWindows\tesseract.exe" (
    echo   Installing Tesseract...
    start /wait %APP_DIR%ForWindows\tesseract.exe /S
    echo   Tesseract installed
) else (
    echo   tesseract.exe not found, skipped
)

REM ========== 4. Check/Install Python ==========
echo.
echo [4/7] Setting up Python...
set "PYTHON_DIR=%USERPROFILE%\Python314"
set "PYTHON_EXE=%PYTHON_DIR%\python.exe"
set "PYTHON_INSTALLER=%TEMP%\python-3.14.3-amd64.exe"

if exist "%PYTHON_EXE%" (
    echo   Python already installed: %PYTHON_EXE%
    goto :install_deps
)

echo   Downloading Python 3.14...
powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe' -OutFile '%PYTHON_INSTALLER%'"

if errorlevel 1 (
    echo   Download failed! Please check network.
    pause
    exit /b 1
)

echo   Installing Python...
%PYTHON_INSTALLER% /quiet InstallAllUsers=0 TargetDir=%PYTHON_DIR% Include_launcher=0 PrependPath=1

:install_deps
echo.
echo [5/7] Installing Python Dependencies...
set "PIP_INDEX=https://pypi.tuna.tsinghua.edu.cn/simple"

%PYTHON_EXE% -m pip install --upgrade pip -i %PIP_INDEX%

%PYTHON_EXE% -m pip install PySide6 openai requests markdown python-dotenv pandas -i %PIP_INDEX%
%PYTHON_EXE% -m pip install python-docx PyPDF2 pdf2image pytesseract pycryptodome -i %PIP_INDEX%
%PYTHON_EXE% -m pip install chromadb sentence-transformers transformers torch -i %PIP_INDEX%
%PYTHON_EXE% -m pip install openpyxl python-pptx -i %PIP_INDEX%

if errorlevel 1 (
    echo   Dependency install failed! Please check network.
    pause
    exit /b 1
)
echo   Dependencies installed

REM ========== 7. Create launcher and shortcut ==========
echo.
echo [7/7] Creating launcher and shortcut...

set "LAUNCHER=%APP_DIR%start.bat"
(
    echo @echo off
    echo chcp 936 ^>nul
    echo title SnowAI
    echo set QT_ENABLE_HIGHDPI_SCALING=0
    echo set QT_AUTO_SCREEN_SCALE_FACTOR=0
    echo set QT_SCALE_FACTOR=1
    echo set QT_SCREEN_SCALE_FACTORS=1
    echo set __COMPAT_LAYER=HighDPIAware
    echo cd /d "%APP_DIR%"
    echo %PYTHON_EXE% main.py
    echo pause
) > "%LAUNCHER%"

echo   Launcher created: %LAUNCHER%

powershell -Command "& { $WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%USERPROFILE%\Desktop\SnowAI.lnk'); $SC.TargetPath = '%LAUNCHER%'; $SC.WorkingDirectory = '%APP_DIR%'; $SC.IconLocation = '%%SYSTEMROOT%%\System32\imageres.dll,3'; $SC.Save() }"

if exist "%USERPROFILE%\Desktop\SnowAI.lnk" (
    echo   Desktop shortcut created
) else (
    echo   Shortcut creation failed, please create manually
)

echo.
echo ========================================
echo      Installation Complete!
echo ========================================
echo.
echo IMPORTANT:
echo   1. Please RESTART your computer
echo   2. After restart, double-click SnowAI on desktop
echo.
echo If you have problems, please send error message to BadXuexue~
echo.
pause