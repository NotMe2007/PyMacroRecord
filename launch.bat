@echo off
REM Launch script for PyMacroRecord
REM Uses the project's .venv python if available, otherwise falls back to system python.
setlocal
set "VENV_PY=%~dp0.venv\Scripts\python.exe"
if exist "%VENV_PY%" (
    "%VENV_PY%" "%~dp0src\main.py" %*
) else (
    python "%~dp0src\main.py" %*
)
endlocal
exit /b %ERRORLEVEL%
