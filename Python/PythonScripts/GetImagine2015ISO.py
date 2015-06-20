import sys
import os
import subprocess
import argparse
import time
import datetime
import CommonUtils
PrintInfo = CommonUtils.PrintInfo

__PRODUCTNAME__     = 'IMAGINE'
__PRODUCTVERSION__  = '15.0'
__MFT__             = 'ERDAS IMAGINE'
__MLABEL__          = 'IMAGINE 2015'

# These are for my testing
__TARGETDIRECTORY__ = r'E:\TEMP'
__RECEPIENTS__      = 'lgovindu@intergraph.com'

# __TARGETDIRECTORY__ = r'\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\Products\{}\{}'.format(__PRODUCTNAME__, __PRODUCTVERSION__)
# __RECEPIENTS__      = 'smajety@intergraph.com;schallag@intergraph.com;lgovindu@intergraph.com;svvankad@intergraph.com;gpeddoll@intergraph.com;nrkolli@intergraph.com;mkshivak@intergraph.com;pkvalipi@intergraph.com;ssamayam@intergraph.com;lpkota@intergraph.com;vpperepa@intergraph.com'

__KEEP_LAST_N_BUILDS__ = 45


def PrintInfo(info):
    print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), info))
    sys.stdout.flush()
    return None


def GetDoubleQuotedString(string):
    """
    Returns the double quoted string.
    :param string: String to be double quoted.
    :rtype : str
    """
    return '"' + string + '"'


def RunSystemCommand(cmd):
    """
    Execute the given command.
    :param cmd: Command to execute.
    :param alwaysRun: You can ignore this param.
    :rtype : int
    """
    exitCode = os.system(GetDoubleQuotedString(cmd))
    return exitCode


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


def GetConfig(fileName):
    return ('x86' if fileName.find('x86') != -1 else ('x64' if fileName.find('x64') != -1 else ''))


# ------------------------------------------------------------------------------
# RunNcFTPCommand
# ------------------------------------------------------------------------------
def RunNcFTPCommand(command, targetDirectory=''):
    """This method just executes the given command using NcFTPGet.
And returns the NcFTP exitCode."""
    # Get CurrentWorkingDirectory
    cwd = os.getcwd()
    if targetDirectory and os.path.isdir(targetDirectory):
        PrintInfo('Change CurrentWorkingDirectory to [%s]' % targetDirectory)
        # Change CWD to the specified target directory
        os.chdir(targetDirectory)

    # Run NcFTPGet command
    PrintInfo('Executing Command = [%s]' % command)
    exitCode = RunSystemCommand(command)
    PrintInfo('ExitCode = %d' % exitCode)

    # Change CWD
    os.chdir(cwd)
    return exitCode


# ------------------------------------------------------------------------------
# GetFile
# ------------------------------------------------------------------------------
def GetFile(ftpUserName, ftpPassword, ftpPathName, targetDirectory=''):
    """Get the file using NcFTP"""
    cwd = os.getcwd()
    if targetDirectory and os.path.isdir(targetDirectory):
        PrintInfo('Change CurrentWorkingDirectory to [%s]' % targetDirectory)
        os.chdir(targetDirectory)

    # NcFTPGet executable
    command = 'ncftpget.exe'

    # If username and password specified
    if ftpUserName and ftpPassword:
        command += ' -u ' + ftpUserName + ' -p ' + ftpPassword

    # add ftp file path
    command += ' ' + '\"' + ftpPathName + '\"'

    PrintInfo('Executing Command = [%s]' % command)
    exitCode = 0
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = popen.communicate()
    if popen.wait() != 0: exitCode = popen.returncode
    PrintInfo('ExitCode = %d' % exitCode)
    # raise Exception(str(stderr))

    os.chdir(cwd)

    return exitCode


# ------------------------------------------------------------------------------
# GetDirectory
# ------------------------------------------------------------------------------
def GetDirectory(ftpUserName, ftpPassword, ftpPathName, targetDirectory=''):
    """Get the file using NcFTP"""
    cwd = os.getcwd()
    if targetDirectory and os.path.isdir(targetDirectory):
        PrintInfo('Change CurrentWorkingDirectory to [%s]' % targetDirectory)
        os.chdir(targetDirectory)

    # NcFTPGet executable
    command = 'ncftpget.exe'

    # If username and password specified
    if ftpUserName and ftpPassword:
        command += ' -u ' + ftpUserName + ' -p ' + ftpPassword

    # add ftp file path
    command += ' -R ' + ftpPathName + ' -r ' + '99'

    # command = 'ncftpget.exe -u {0} -p {1} {2} > stdout'.format( ftpUserName, ftpPassword, ftpPathName )
    PrintInfo('Executing Command = [%s]' % command)
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
    ftpPathName = 'ftp://atltruck/IDK/IMAGINE/15.0/IMAGINE_2013-05-08_0717_b306/64/ERDASIMAGINE.msi'
    targetDirectory = r'D:\LGTEMP'

    GetFile(ftpUserName, ftpPassword, ftpPathName, targetDirectory)

    return None


def Test_GetDirectory():
    ftpUserName = 'ftpuser'
    ftpPassword = 'kroNos!2013!'
    ftpPathName = 'ftp://atltruck/IDK/IMAGINE/15.0/IMAGINE_2013-06-16_0810_b537/'

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
                        help='IMAGINE 2015 Build ISO file path')

    opts = parser.parse_args()
    PrintInfo(opts)

    cwd = os.getcwd()

    uncPath = opts.filePath

    fileName = os.path.basename(uncPath)
    config = GetConfig(fileName)
    build = os.path.basename(os.path.dirname(uncPath))

    ftpPath = ConvertToFTP(uncPath)
    targetDirectory = os.path.join(cwd, build + config)
    if not os.path.exists(targetDirectory): os.mkdir(targetDirectory)
    PrintInfo('targetDirectory  = [%s]' % targetDirectory)
    # os.chdir(targetDirectory)

    PrintInfo('CWD = [%s]' % os.getcwd())
    targetShareDir = os.path.join(__TARGETDIRECTORY__, build)

    started = datetime.datetime.now()
    PrintInfo('Started : [%s]' % started)

    # ------------------------------------------------------------------------------
    # Get file using NcFTPGet
    # ------------------------------------------------------------------------------
    while True:
        exitCode = GetFile(opts.username, opts.password, ftpPath, targetDirectory)
        PrintInfo('ExitCode = %d' % exitCode)
        if exitCode == 0: break

    ended = datetime.datetime.now()
    PrintInfo('Ended : [%s]' % ended)

    timeTaken = ( ended - started )
    PrintInfo("timeTaken = [%s]" % timeTaken)

    # ------------------------------------------------------------------------------
    # Copy the ISO image to TargetDirectory
    # ------------------------------------------------------------------------------
    if not os.path.exists(targetShareDir):
        PrintInfo('Creating target directory: [%s]' % targetShareDir)
        RunSystemCommand('mkdir {}'.format(targetShareDir))
    PrintInfo('Copying IMAGINE ISO [%s] -> [%s]' % (fileName, targetShareDir))
    # shutil.copy(fileName, targetShareDir)
    CopyFileUsingRobocopy(targetDirectory, targetShareDir, fileName)

    # ------------------------------------------------------------------------------
    # Write/Update IMAGINE LatestInstall Command
    # ------------------------------------------------------------------------------
    targetIsoPath = os.path.join(targetShareDir, fileName)
    Write_IMAGINE_LatestInstall_CmdFile(targetIsoPath)

    # ------------------------------------------------------------------------------
    # send mail
    # ------------------------------------------------------------------------------
    body = 'Available at {}, TimeTaken : {}'.format(targetShareDir, timeTaken)
    sendMailCmd = 'python SendMail.py --mft "{}" -r {} --sub "{} {}" --text "{}" --label "{}"'.format(
        __MFT__, __RECEPIENTS__, build, config, body, __MLABEL__
    )
    PrintInfo('SendMail Command : [%s]' % sendMailCmd)
    RunSystemCommand(sendMailCmd)

    # ------------------------------------------------------------------------------
    # Remove temp files/directories
    # ------------------------------------------------------------------------------
    os.chdir(cwd)
    PrintInfo('Removing targetDirectory: [%s]' % targetDirectory)
    RunSystemCommand('rmdir /S /Q {}'.format(targetDirectory))

    # ------------------------------------------------------------------------------
    # Clean up products folder
    # ------------------------------------------------------------------------------
    cleanupCmd = 'python CleanupERDASProducts.py --directory \"{}\" --keep {}'.format(__TARGETDIRECTORY__, __KEEP_LAST_N_BUILDS__)
    PrintInfo('Cleanup directory [%s]' % __TARGETDIRECTORY__)
    RunSystemCommand(cleanupCmd)    

    return 0


def Write_IMAGINE_LatestInstall_CmdFile(isoFilePath):
    fileName = os.path.basename(isoFilePath)
    parentDirPath = os.path.dirname(os.path.dirname(isoFilePath))
    config = GetConfig(fileName)
    if config:
        cmdFilePath = os.path.join(parentDirPath, '%s_%s_LatestInstall.cmd' % (__PRODUCTNAME__, config))
    else:
        cmdFilePath = os.path.join(parentDirPath, '%s_LatestInstall.cmd' % __PRODUCTNAME__)
    PrintInfo('CMD File : [%s]' % cmdFilePath)
    fp = open(cmdFilePath, 'w')
    fp.write('\"%s\"' % isoFilePath)
    fp.close()
    

def CopyFileUsingRobocopy(sourceDirectory, targetDirectory, fileName):
    options = '/NP /NJH /NJS'
    command = 'robocopy.exe \"{}\" \"{}\" \"{}\" {}'.format(sourceDirectory, targetDirectory, fileName, options)
    PrintInfo('Executing Command : [%s]' % command)
    exitCode = RunSystemCommand(command)
    return exitCode


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    PrintInfo(info.center(80, '-'))
    exitCode = main()
    PrintInfo('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    PrintInfo(info.center(80, '-'))
    sys.exit(exitCode)
    