@ECHO OFF
SETLOCAL ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION

SET FilePath=%~f0
SET DirectoryPath=%~dp0

ECHO FilePath         = [%FilePath%]
ECHO DirectoryPath    = [%DirectoryPath%]

PUSHD %DirectoryPath%
ECHO CurrentDirectory = [%CD%]

CALL Python27.bat UpdateJenkins.py

POPD

ENDLOCAL
EXIT /B 0