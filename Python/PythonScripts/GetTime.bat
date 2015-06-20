@ECHO OFF

REM ===================================================================================================================
REM Syntax    : :GetTime <VarTime> <Seperator>
REM Arguments :
REM   %1 [O]  : <VarTime> Variable for storing time
REM   %2 [I]  : <Seperator> Seperator between the HH and MM
REM ===================================================================================================================

:GetTime
IF "%1" EQU "" (
	> CON ECHO No arguments passed.
	> CON ECHO This function always returns time in 24-format
	> CON ECHO Syntax    : :GetTime ^<VarTime^> ^<Seperator^>
	> CON ECHO Arguments :
	> CON ECHO   %%1 [O]  : ^<VarTime^>    Variable for storing time
	> CON ECHO   %%2 [I]  : ^<Seperator^>  Seperator between the HH and MM
	> CON ECHO.
	EXIT /B
)
SETLOCAL ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION
SET HH=%TIME:~0,2%
SET MM=%TIME:~3,2%
IF /I "%HH:~0,1%" EQU " " SET HH=0%HH:~1,1%
ENDLOCAL & SET %~1=%HH%%2%MM%
EXIT /B REM GetTime_END

REM ===================================================================================================================
