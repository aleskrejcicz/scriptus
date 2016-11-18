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

:: 1) Add registry keys
REG ADD "HKLM\SOFTWARE\Policies\Microsoft\Windows\Gwx" /v DisableGWX /d 1 /f
REG ADD "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" /v DisableOSUpgrade /d 1 /f
REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\OSUpgrade" /v AllowOSUpgrade /d 0 /f
REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\OSUpgrade" /v ReservationsAllowed /d 0 /f

:: 2) Uninstall and kill GWX
TASKKILL /IM GWX.exe /T /F
start /wait wusa /uninstall /kb:3035583 /quiet /norestart
