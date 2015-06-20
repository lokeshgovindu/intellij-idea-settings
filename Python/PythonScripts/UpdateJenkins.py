import os
import sys
import time
import glob


def RunSystemCommand(cmd):
    """
    Execute the given command.
    :param cmd: Command to execute.
    :param alwaysRun: You can ignore this param.
    :rtype : int
    """
    exitCode = os.system('"' + cmd + '"')
    return exitCode


def GetLatestJenkinsWarFile(jenkinsInstallersDirPath):
    if not os.path.exists(jenkinsInstallersDirPath):
        raise BaseException('Jenkins Installers directory path [%s] doesn\'t exist!' % jenkinsInstallersDirPath)

    jenkinsWarFiles = glob.glob1(jenkinsInstallersDirPath, "*.war")
    if jenkinsWarFiles:
        fileNameWithExt = glob.glob1(jenkinsInstallersDirPath, "*.war")[-1]
        jenkinsNewWarFilePath = os.path.join(jenkinsInstallersDirPath, fileNameWithExt)
        return jenkinsNewWarFilePath

    return ''


def main():
    jenkinsInstallersDirPath = r'\\IN-CONQUERORS7\Softwares\Jenkins'
    print('JenkinsInstallersDirPath = [%s]' % jenkinsInstallersDirPath)
    jenkinsNewWarFilePath = GetLatestJenkinsWarFile(jenkinsInstallersDirPath)
    print('jenkinsNewWarFilePath = [%s]' %(jenkinsNewWarFilePath,))
    if not jenkinsNewWarFilePath or not os.path.exists(jenkinsNewWarFilePath):
        print('[ERROR] Latest jenkins war file is not available in [%s]!' % jenkinsInstallersDirPath)
        return 1

    # Stop the jenkins service
    stopServiceCmd = 'PsService stop jenkins'
    print('Executing stopServiceCmd = [%s]' % (stopServiceCmd,))
    RunSystemCommand(stopServiceCmd)
    time.sleep(3)

    ProgramFiles_x86 = os.getenv('ProgramFiles(x86)')
    if not ProgramFiles_x86:
        ProgramFiles_x86 = os.getenv('ProgramFiles')

    jenkinsTargetDirectory = os.path.join(ProgramFiles_x86, r'Jenkins')
    jenkinsTargetWarFilePath = os.path.join(ProgramFiles_x86, r'Jenkins\jenkins.war')
    print('')

    # Delete existing jenkins_old.war file
    if os.path.exists(jenkinsTargetWarFilePath):
        print('Jenkins.war file [%s] exist!' % (jenkinsTargetWarFilePath,))
        jenkinsOldWarFilePath = os.path.join(ProgramFiles_x86, r'Jenkins\jenkins_old.war')
        if os.path.exists(jenkinsOldWarFilePath):
            deleteCmd = 'DEL /F /Q \"{}\"'.format(jenkinsOldWarFilePath)
            print('Executing DeleteCmd = [%s]' % (deleteCmd,))
            exitCode = RunSystemCommand(deleteCmd)
            print('ExitCode = [%s]' % (exitCode))
            print('')

        # Rename the existing jenkins.war file
        cwd = os.getcwd()
        os.chdir(jenkinsTargetDirectory)
        print('Rename file [%s] -> [%s]' % (jenkinsTargetWarFilePath, jenkinsOldWarFilePath))
        renameCmd = 'RENAME \"{}\" \"{}\"'.format('jenkins.war', 'jenkins_old.war')
        print('Executing RenameCmd = [%s]' % (renameCmd,))
        exitCode = RunSystemCommand(renameCmd)
        os.chdir(cwd)
        print('ExitCode = [%s]' % (exitCode,))
        print('')

    # Copy the new jenkins.war file to the jenkins directory
    copyCmd = 'COPY /V /Y \"{}\" \"{}\"'.format(jenkinsNewWarFilePath, jenkinsTargetWarFilePath)
    print('Executing CopyCmd = [%s]' % (copyCmd,))
    exitCode = RunSystemCommand(copyCmd)
    print('ExitCode = [%s]' % (exitCode,))
    print('')

    # Start the jenkins service
    startServiceCmd = 'PsService start jenkins'
    print('Executing startServiceCmd = [%s]' % (startServiceCmd,))
    RunSystemCommand(startServiceCmd)
    time.sleep(3)
    return 0


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    print(info.center(80, '-'))
    exitCode = main()
    print('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    print(info.center(80, '-'))
    sys.exit(exitCode)
