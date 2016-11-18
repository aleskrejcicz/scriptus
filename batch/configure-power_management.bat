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

REM B: Nastaveni pro pocitace pripojene na kabel

:: Vypnuti monitoru
powercfg -change -monitor-timeout-ac 15

:: Rezim spanku
powercfg -change -standby-timeout-ac 0

:: Rezim hibernace
powercfg -change -hibernate-timeout-ac 0

:: Zakazat uspavani disku
powercfg -change -disk-timeout-ac 0

REM E: Nastaveni pro pocitace pripojene na kabel

pause