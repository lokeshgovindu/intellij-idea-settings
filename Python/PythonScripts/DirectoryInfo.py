"""
Display Directory Information.
"""
import os
import sys
import argparse
import datetime
import CommonUtils
PrintInfo = CommonUtils.PrintInfo

def main():
    parser = argparse.ArgumentParser(description='Display Directory Information')
    parser.add_argument('--path', '-p', dest='path', required=True, help='Absolute Directory Path')
    parser.add_argument('--sub-folders', '-s', type=bool, dest='subfolders', default=True, help='Include all subdirectories')
    options = parser.parse_args()

    fp = CommonUtils.FormatPrinter(width=18, printFunc=CommonUtils.PrintInfo)

    started = datetime.datetime.now()
    fp.Print('Started', started)
    PrintInfo('')
    fp.Print('Options', options)
    directoryPath = os.path.abspath(options.path)
    subFolders = options.subfolders
    fp.Print('DirectoryPath', directoryPath)
    fp.Print('Sub-Folders', subFolders)

    if not os.path.exists(directoryPath):
        PrintInfo('')
        PrintInfo('ERROR: DirectoryPath [%s] doesn\'t exist!' % directoryPath)
        return 1

    # -----------------------------------------------------------------------------
    # Get Directory Information
    # -----------------------------------------------------------------------------
    directoryInfo = CommonUtils.GetDirectoryInfo(directoryPath=directoryPath, subDirectories=subFolders)

    # -----------------------------------------------------------------------------
    # Write Directory Information on stdout
    # -----------------------------------------------------------------------------
    fp.Print('Files', directoryInfo[0])
    fp.Print('Folders', directoryInfo[1])
    fp.Print('Size', CommonUtils.FormatSize(directoryInfo[2]))

    ended = datetime.datetime.now()
    elapsed = ended - started
    PrintInfo('')
    fp.Print('Ended', ended)
    fp.Print('Elapsed', elapsed)
    return 0


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    PrintInfo(info.center(80, '-'))
    exitCode = main()
    info = ' ' + fileName + ' ' + 'End' + ' '
    PrintInfo(info.center(80, '-'))
    sys.exit(exitCode)
