from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

f = drive.CreateFile()
f.SetContentFile('GoogleDriveAPITest.py') # Read local file
f.Upload() # Upload it

"""
import os
import sys

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def main():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return 0


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    print(info.center(79, '-'))
    exitCode = main()
    print('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    print(info.center(79, '-'))
    sys.exit(exitCode)
"""