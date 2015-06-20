@ECHO OFF
SETLOCAL ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION

SET FilePath=%~f0
SET DirectoryPath=%~dp0

REM ECHO FilePath         = [%FilePath%]
REM ECHO DirectoryPath    = [%DirectoryPath%]

PUSHD %DirectoryPath%
REM ECHO CurrentDirectory = [%CD%]

@IF NOT DEFINED Python27 SET Python27=%SystemDrive%\Python27\python.exe

@%Python27% .\DirectoryInfo.py %*

POPD

ENDLOCAL
EXIT /B 0
