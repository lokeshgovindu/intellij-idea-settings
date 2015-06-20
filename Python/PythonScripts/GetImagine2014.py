import sys
import os
import subprocess
import argparse
import time


__ATLTRUCKIMAGINE__ = 'ftp://atltruck/IDK/IMAGINE/14.0'
__TARGETDIRECTORY__ = r'\\in-disrv01\ConquerorsTeamSpace\Products\IMAGINE\14.0'
__recepients__ = 'lgovindu@intergraph.com'
# __recepients__ = 'schallag@intergraph.com;lgovindu@intergraph.com;svvankad@intergraph.com;gpeddoll@intergraph.com;nrkolli@intergraph.com;mkshivak@intergraph.com;pkvalipi@intergraph.com;ssamayam@intergraph.com;lpkota@intergraph.com;vpperepa@intergraph.com;iharidas@intergraph.com'


def GetDateTime():
    """Returns the date time as a string in the format of YYYY-MM-DD HH:MM:SS'"""
    dt = time.strftime("%Y-%m-%d %H:%M:%S")
    return dt

def PrintInfo(info):
    print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), info))
    return None

#===============================================================================
# RunNcFTPCommand
#===============================================================================
def RunNcFTPCommand(command, targetDirectory=''):
    """This method just executes the given command using NcFTPGet.
And returns the NcFTP exitCode."""
    # Get CurrentWorkingDirectory
    cwd = os.getcwd()
    if targetDirectory != None and os.path.isdir(targetDirectory):
        PrintInfo('Change CurrentWorkingDirectory to \"%s\"' % targetDirectory)
        # Change CWD to the specified target directory
        os.chdir(targetDirectory)

    # Run NcFTPGet command
    PrintInfo('Executing Command = \"%s\"' % command)
    exitCode = os.system(command)
    PrintInfo('ExitCode = %d' % exitCode)

    # Change CWD
    os.chdir(cwd)
    return exitCode

#===============================================================================
# GetFile
#===============================================================================
def GetFile(ftpUserName, ftpPassword, ftpPathName, targetDirectory=''):
    """Get the file using NcFTP"""
    cwd = os.getcwd()
    if targetDirectory != None and os.path.isdir(targetDirectory):
        PrintInfo('Change CurrentWorkingDirectory to \"%s\"' % targetDirectory)
        os.chdir(targetDirectory)

    # NcFTPGet executable
    command = 'ncftpget.exe'

    # If username and password specified
    if ftpUserName and ftpPassword:
        command += ' -u ' + ftpUserName + ' -p ' + ftpPassword

    # add ftp file path
    command += ' ' + ftpPathName

    #     command = 'ncftpget.exe -u {0} -p {1} {2} > stdout'.format( ftpUserName, ftpPassword, ftpPathName )
    PrintInfo('Executing Command = \"%s\"' % command)
    exitCode = 0
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = popen.communicate()
    if popen.wait() != 0: exitCode = popen.returncode
    PrintInfo('ExitCode = %d' % exitCode)
    # raise Exception(str(stderr))

    os.chdir(cwd)

    return exitCode


#===============================================================================
# GetDirectory
#===============================================================================
def GetDirectory(ftpUserName, ftpPassword, ftpPathName, targetDirectory=''):
    """Get the file using NcFTP"""
    cwd = os.getcwd()
    if targetDirectory != None and os.path.isdir(targetDirectory):
        PrintInfo('Change CurrentWorkingDirectory to \"%s\"' % targetDirectory)
        os.chdir(targetDirectory)

    # NcFTPGet executable
    command = 'ncftpget.exe'

    # If username and password specified
    if ftpUserName and ftpPassword:
        command += ' -u ' + ftpUserName + ' -p ' + ftpPassword

    # add ftp file path
    command += ' -R ' + ftpPathName + ' -r ' + '99'

    #     command = 'ncftpget.exe -u {0} -p {1} {2} > stdout'.format( ftpUserName, ftpPassword, ftpPathName )
    PrintInfo('Executing Command = \"%s\"' % command)
    exitCode = 0
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = popen.communicate()
    if popen.wait() != 0: exitCode = popen.returncode
    PrintInfo('ExitCode = %d' % exitCode)
    # raise Exception(str(stderr))

    os.chdir(cwd)

    return exitCode


def Test_GetFile():
    ftpUserName = 'ftpuser'
    ftpPassword = 'kroNos!2013!'
    ftpPathName = 'ftp://atltruck/IDK/IMAGINE/14.0/IMAGINE_2013-05-08_0717_b306/64/ERDASIMAGINE.msi'
    targetDirectory = r'D:\LGTEMP'

    GetFile(ftpUserName, ftpPassword, ftpPathName, targetDirectory)

    return None


def Test_GetDirectory():
    ftpUserName = 'ftpuser'
    ftpPassword = 'kroNos!2013!'
    ftpPathName = 'ftp://atltruck/IDK/IMAGINE/14.0/IMAGINE_2013-06-16_0810_b537/'

    targetDirectory = r'E:\DownloadsUsingRiverbed\IMAGINE_2013-06-16_0810_b537'

    GetDirectory(ftpUserName, ftpPassword, ftpPathName, targetDirectory)

    return None


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u', '--username', type=str,
                        action='store', metavar='USERNAME', dest='username', default='ftpuser',
                        help='FTP UserName (required)')
    parser.add_argument('-p', '--password', type=str,
                        action='store', metavar='PASSWORD', dest='password', default='kroNos!2013!',
                        help='FTP Password (required)')
    parser.add_argument('-b', '--build', type=str, action='store', dest='build', required=True,
                        help='IMAGINE 2014 Build')

    opts = parser.parse_args()
    PrintInfo(opts)

    build = opts.build
    cwd = os.getcwd()
    PrintInfo('[%s] CWD = %s' % (sys.argv[0], cwd))
    targetDirectory = os.path.join(cwd, build)
    PrintInfo('[%s] Build = %s' % (sys.argv[0], build))
    PrintInfo('[%s] targetDirectory  = %s' % (sys.argv[0], targetDirectory))
    if not os.path.exists(targetDirectory):
        os.mkdir(targetDirectory)
    os.chdir(targetDirectory)
    ftpBuildPath = __ATLTRUCKIMAGINE__ + '/' + build
    targetShareDir = os.path.join(__TARGETDIRECTORY__, build)
    for config in ['x64', 'x86']:
##        imagineZip = 'IMAGINE_' + config + '.zip'
        imagineiso = 'IMAGINE_' + config + '.zip'
        ftpPath = ftpBuildPath + '/' + imagineiso

        # Get file using ncftpget
        exitCode = 0
        while True:
            exitCode = GetFile(opts.username, opts.password, ftpPath)
            PrintInfo('[main] ExitCode = %d' % exitCode)
            if exitCode == 0: break

        # Unzip to share
        zipFilePath = os.path.join(targetDirectory, imagineZip)
        tempDir = os.path.join(targetShareDir, config)
        # if not os.path.isdir(tempDir) or not os.path.exists(tempDir): os.mkdir(tempDir)
        os.system('mkdir {}'.format(tempDir))
        command = 'wzunzip.exe -d {} {} > nul'.format(zipFilePath, tempDir)
        PrintInfo('[main] Executing Command : %s' % command)
        os.system(command)   # execute command

        # send mail
        sendMailCmd = 'SendMail.py --mft "ERDAS IMAGINE" -r {} --sub "{} {}" --text "Available at {}" --label "{}"'.format(
            __recepients__, build, config, tempDir, 'IMAGINE 2014'
        )
        PrintInfo('SendMail Command : %s' % sendMailCmd)
        os.system(sendMailCmd)

    os.chdir(cwd)
    return None


def Test_RunNcFTPCommand():
#     command = 'ncftpget.exe -u ftpuser -p kroNos!2013! -b ftp://atltruck/IDK/IMAGINE/14.0/IMAGINE_2013-05-08_0717_b306/64/ERDASIMAGINE.msi'
    command = 'ncftpget.exe -u ftpuser -p kroNos!2013! ftp://atltruck/IDK/IMAGINE/14.0/IMAGINE_2013-05-08_0717_b306/64/IMAGINE.zip'
    exitCode = RunNcFTPCommand(command)
    PrintInfo('NcFTPGet ExitCode = %d' % exitCode)
    return exitCode


if __name__ == '__main__':
    Test_GetDirectory()
#     Test_GetFile()
#     Test_RunNcFTPCommand()
##    main()
    PrintInfo("\n[%s] === END ===" % sys.argv[0])
    sys.exit(0)
