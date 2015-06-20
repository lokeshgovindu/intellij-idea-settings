import os
import sys


def RunSystemCommand(cmd):
    """
    Execute the given command.
    :param cmd: Command to execute.
    :rtype : int
    """
    exitCode = os.system('"' + cmd + '"')
    return exitCode


class Robocopy:
    ExitStatus = {
        0x00: 'No files were copied. No failure was encountered. No files were mismatched. The files already exist in the destination directory; therefore, the copy operation was skipped.',
        0x01: 'All files were copied successfully.',
        0x02: 'There are some additional files in the destination directory that are not present in the source directory. No files were copied.',
        0x03: 'Some files were copied. Additional files were present. No failure was encountered.',
        0x05: 'Some files were copied. Some files were mismatched. No failure was encountered.',
        0x06: 'Additional files and mismatched files exist. No files were copied and no failures were encountered. This means that the files already exist in the destination directory.',
        0x07: 'Files were copied, a file mismatch was present, and additional files were present.',
        0x08: 'Several files did not copy.',
        0x10: 'The system cannot find the path specified.'
    }

    @staticmethod
    def Copy(sourceDirectory, targetDirectory, options='/S /E /NP /NJH /NJS'):
        """
        Copy directory using ROBOCOPY (Robust File Copy for Windows)
        :rtype : int
        :param sourceDirectory: Source Directory
        :param targetDirectory: Target Directory
        :param options: Robocopy Options
        :return: ExitCode of Robocopy Command
        """
        if not os.path.isdir(sourceDirectory):
            return -1

        command = 'robocopy.exe \"{}\" \"{}\" {}'.format(sourceDirectory, targetDirectory, options)
        print('Executing Command : [%s]' % command)
        exitCode = RunSystemCommand(command)

        return exitCode

    @staticmethod
    def CopyFolderStructure(sourceDirectory, targetDirectory):
        """
        Create directory tree and zero-length files only.
        @param sourceDirectory: Source Directory Path.
        @param targetDirectory: Target Directory Path.
        @return: ExitCode of robocopy process.
        """
        options='/MIR /CREATE /NP /NJH /NJS'
        return Robocopy.Copy(sourceDirectory, targetDirectory, options)


def CopyDirectory(sourceDirectory, targetDirectory):
    if not os.path.isdir(sourceDirectory):
        return -1

    options = '/S /E /NP /NJH'
    command = 'robocopy.exe \"{}\" \"{}\" {}'.format(sourceDirectory, targetDirectory, options)
    print('Executing Command : %s' % command)
    exitCode = RunSystemCommand(command)

    return exitCode


def main():
    sourceDirectory = r'\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\Products\IDKs\13.0\DesktopIDKs\DesktopIDKs_2013-04-09_1032_b660'
    targetDirectory = r'E:\TEMP\DesktopIDKs_2013-04-09_1032_b660'

    # exitCode = CopyDirectory(sourceDirectory, targetDirectory)
    # exitCode = Robocopy.Copy(sourceDirectory, targetDirectory)
    exitCode = Robocopy.CopyFolderStructure(sourceDirectory, targetDirectory)
    print('ExitCode = [%d]' % exitCode)
    print('Robocopy ExitCode = [%d] & Status = [%s]' % (exitCode, Robocopy.ExitStatus[exitCode]))
    return exitCode


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    print(info.center(80, '-'))
    exitCode = main()
    print('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    print(info.center(80, '-'))
    sys.exit(exitCode)
