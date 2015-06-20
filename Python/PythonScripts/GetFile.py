import sys
import os
import subprocess
import argparse
import time
import datetime

def GetDoubleQuotedString(string):
    """
    Returns the double quoted string.
    :param string: String to be double quoted.
    :rtype : str
    """
    return '"' + string + '"'

def GetDateTime():
    """Returns the date time as a string in the format of YYYY-MM-DD HH:MM:SS'"""
    dt = time.strftime("%Y-%m-%d %H:%M:%S")
    return dt


def PrintInfo(info):
    print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), info))
    return None


def IsFTP(ftpPath): return ftpPath.startswith('ftp://')


def IsUNC(uncPath): return uncPath.startswith('\\')


def ConvertToFTP(path):
    if IsFTP(path): return path
    if IsUNC(path): return 'ftp:' + path.replace('\\', '/')
    return None


def ConvertToUNC(path):
    if IsUNC(path): return path
    if IsFTP(path): return path[4:].replace('/', '\\')
    return None

def RunSystemCommand(cmd):
    """
    Execute the given command.
    :param cmd: Command to execute.
    :param alwaysRun: You can ignore this param.
    :rtype : int
    """
    exitCode = os.system(cmd)
    return exitCode
        

def RunNcFTPCommand(command, targetDirectory=''):
    """This method just executes the given command using NcFTPGet.
And returns the NcFTP exitCode."""
    # Get CurrentWorkingDirectory
    cwd = os.getcwd()
    if targetDirectory and os.path.isdir(targetDirectory):
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


def GetFile(ftpUserName, ftpPassword, ftpPathName, targetDirectory=''):
    """Get the file using NcFTP"""
    cwd = os.getcwd()
    if targetDirectory and os.path.isdir(targetDirectory):
        PrintInfo('Change CurrentWorkingDirectory to \"%s\"' % targetDirectory)
        os.chdir(targetDirectory)

    # NcFTPGet executable
    command = 'ncftpget.exe'

    # If username and password specified
    if ftpUserName and ftpPassword:
        command += ' -u ' + ftpUserName + ' -p ' + ftpPassword

    # add ftp file path
    command += ' ' + '\"' + ftpPathName + '\"'

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
    if targetDirectory and os.path.isdir(targetDirectory):
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
    parser.add_argument('-f', '--file', '--filePath', '--isoFilePath', type=str,
                        action='store', dest='filePath', required=True,
                        help='IMAGINE 2014 Build ISO file path')

    parser.add_argument('--target-directory', type=str, dest='target_directory', required=True, help='Target directory')

    parser.add_argument('--mail-from-text', type='str', dest='mail_from_text', default='Intergraph Consulting',
                        help='Mail from text. e.g [Team HR] in (Team HR <hrd2@india.ingr.com>)')
    parser.add_argument('--mail-label', type=str, dest='mail_label', default='None', help='Mail label')
    parser.add_argument('--mail-recipients', type=str, dest='mail_recipients', default='lgovindu@intergraph.com',
                        help='email-ids separated by semi-colon(;)')

    opts = parser.parse_args()
    PrintInfo(opts)

    cwd = os.getcwd()

    uncPath = opts.filePath
    targetDirectory = opts.target_directory
    mailLabel = opts.mail_label
    mailRecipients = opts.mail_recipients
        
    if not os.path.exists(targetDirectory):
        print('Target directory [%s] doesn\'t exists!')
        return -1

    fileName = os.path.basename(uncPath)
    config = 'x86'
    build = os.path.basename(os.path.dirname(os.path.dirname(uncPath)))

    ftpPath = ConvertToFTP(uncPath)
    targetDirectoryLocal = os.path.join(cwd, build + config + time.strftime("%Y-%m-%d_%H%M%S"))
    if not os.path.exists(targetDirectoryLocal): os.mkdir(targetDirectoryLocal)
    PrintInfo('targetDirectoryLocal  = %s' % targetDirectoryLocal)
    # os.chdir(targetDirectoryLocal)

    PrintInfo('CWD = %s' % os.getcwd())
    targetShareDir = os.path.join(targetDirectory, build)

    started = datetime.datetime.now()
    PrintInfo('Started : %s' % started)

    # Get file using NcFTPGet
    while True:
        exitCode = GetFile(opts.username, opts.password, ftpPath, targetDirectoryLocal)
        PrintInfo('ExitCode = %d' % exitCode)
        if exitCode == 0: break

    ended = datetime.datetime.now()
    PrintInfo('Ended : %s' % ended)

    timeTaken = ( ended - started )
    PrintInfo("timeTaken = %s" % timeTaken)

    # Copy the ISO image to TargetDirectory
    if not os.path.exists(targetShareDir):
        PrintInfo('Creating target directory: %s' % targetShareDir)
        os.system('mkdir {}'.format(targetShareDir))
    PrintInfo('Copying Server ISO %s -> %s' % (fileName, targetShareDir))
    # shutil.copy(fileName, targetShareDir)
    CopyFileUsingRobocopy(targetDirectoryLocal, targetShareDir, fileName)

    # Write/Update IMAGINE LatestInstall Commad
    targetIsoPath = os.path.join(targetShareDir, fileName)
    Write_IMAGINE_LatestInstall_CmdFile(targetIsoPath)

    # send mail
    body = 'Available at {}, TimeTaken : {}'.format(targetIsoPath, timeTaken)
    sendMailCmd = 'python SendMail.py --mft "Server" -r {} --sub "{} {}" --text "{}" --label "{}"'.format(
        mailRecipients, build, config, body, mailLabel
    )
    PrintInfo('SendMail Command : [%s]' % sendMailCmd)
    RunSystemCommand(GetDoubleQuotedString(sendMailCmd))

    os.chdir(cwd)
    # Remove temp files/directories
    PrintInfo('Removing targetDirectoryLocal: %s' % targetDirectoryLocal)
    RunSystemCommand(GetDoubleQuotedString('rmdir /S /Q {}'.format(targetDirectoryLocal)))
    return None


def Write_IMAGINE_LatestInstall_CmdFile(isoFilePath):
    fileName = os.path.basename(isoFilePath)
    parentDirPath = os.path.dirname(os.path.dirname(isoFilePath))
    config = 'x86'
    cmdFilePath = os.path.join(parentDirPath, 'Server_%s_LatestInstall.cmd' % config)
    PrintInfo('CMD File : %s' % cmdFilePath)
    fp = open(cmdFilePath, 'w')
    fp.write('\"%s\"' % isoFilePath)
    fp.close()


def CopyFileUsingRobocopy(sourceDirectory, targetDirectory, fileName):
    options = '/NP /NJH /NJS'
    command = 'robocopy.exe \"{}\" \"{}\" \"{}\" {}'.format(sourceDirectory, targetDirectory, fileName, options)
    PrintInfo('Executing Command : %s' % command)
    os.system(command)
    return None


if __name__ == '__main__':
    # Test_GetDirectory()
    # Test_GetFile()
    PrintInfo( "=================================== Started ====================================" )
    main()
    PrintInfo("\n[%s] === END ===" % sys.argv[0])
    PrintInfo( "==================================== Ended =====================================" )
    sys.exit(0)
