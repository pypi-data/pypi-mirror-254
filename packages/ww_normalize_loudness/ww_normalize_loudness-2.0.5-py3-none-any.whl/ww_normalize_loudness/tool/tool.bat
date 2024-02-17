@echo off
setlocal EnableExtensions DisableDelayedExpansion
:: protect cwd
pushd

:: script is at proj_root/
cd /d %~dp0\..
c:\miatech\python3\Scripts\poetry.exe run python tool\tool.py %*
if NOT %errorlevel% == 0 (
	goto :fail
)
popd
goto :EOF

:fail
popd
