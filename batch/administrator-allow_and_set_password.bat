@echo off

:: # =============================================================
:: # Author: http://sefikail.cz
:: # License: http://creativecommons.org/licenses/by/3.0/
:: # Source code: https://github.com/sefikail/scriptus
:: # Version: Version: 15.07.2016
:: # =============================================================

REM Administrative privileges
:: ---------------
NET SESSION >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
	goto :isadmin
) ELSE (
	echo Script must be run with administrative privileges!
	pause
	exit /B 1
)

:isadmin


REM Script content:
:: ---------------

:: 1) Allow administrator
net user administrator /active:yes

:: 2) Set password
net user administrator RandomPassword