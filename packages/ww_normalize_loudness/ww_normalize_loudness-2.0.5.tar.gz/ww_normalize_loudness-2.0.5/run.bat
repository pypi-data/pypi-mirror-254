@echo off
setlocal EnableExtensions DisableDelayedExpansion
:: protect cwd
pushd

:: script is at proj_root/
cd /d %~dp0
for %%I in (%cd%) do set myServName=%%~nxI
poetry run python src\%myServName%_cli.py %*
if NOT %errorlevel% == 0 (
	goto :fail
)
popd
goto :EOF

:fail
popd

