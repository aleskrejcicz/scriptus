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

setlocal

goto comment_multiline
  10.0* => Windows 10
  10.0* => Windows Server 2016 Technical Preview
  6.3*  => Windows 8.1
  6.3*  => Windows Server 2012 R2
  6.2   => Windows 8
  6.2   => Windows Server 2012
  6.1   => Windows 7
  6.1   => Windows Server 2008 R2
  6.0   => Windows Server 2008
  6.0   => Windows Vista
  5.2   => Windows Server 2003 R2
  5.2   => Windows Server 2003
  5.2   => Windows XP 64-Bit Edition
  5.1   => Windows XP
  5.0   => Windows 2000

/RL level
  A value that sets the run level for the task. Valid values are LIMITED and HIGHEST. The default is LIMITED.
  Windows XP and Windows Server 2003:  This option is not available.
:comment_multiline


set version=
for /f "usebackq tokens=1,2 delims==|" %%I in (`wmic os get version /format:list`) do 2>NUL set "%%I=%%J"

if  "%version%" == "" (
    for /f "tokens=2*" %%i in ('reg.exe query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v "CurrentVersion"') do set version=%%j
)

set first2str=%version:~0,2%
set version_prefix=%first2str:.=%

set runlevel=
if /i %version_prefix% GEQ 6 (
	set runlevel=/RL HIGHEST
)

schtasks /Create /TN "wpkg-start" /TR "\\server\wpkg-start.bat" /SC DAILY /ST 01:33:33 /RU "SYSTEM" %runlevel%

endlocal

pause
