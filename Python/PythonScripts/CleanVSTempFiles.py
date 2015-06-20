import os
import sys
import fnmatch
import re
import glob
import argparse


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


def DeleteFiles(directory, extensions, subdirectories):
    """
    Deletes one or more files using MS DOS DEL Command.
    :rtype : int
    :param directory: Directory to be cleaned.
    :param extensions: List of extensions of files to be deleted.
    :param subdirectories: Delete files from all subdirectories.
    :return: 0 for success.
    """
    if not os.path.exists(directory) or not extensions:
        return
    cwd = os.getcwd()
    os.chdir(directory)
    print('Current working directory : [%s]' % os.getcwd())

    names = ''
    for ext in extensions:
        names = '*.' + ext if not names else names + ' ' + '*.' + ext
    print('names = [%s]' % names)

    cmd = ''
    if subdirectories:
        cmd = 'DEL /F /S /Q ' + names
    else:
        cmd = 'DEL /F /Q ' + names
    print('cmd = [%s]' % cmd)
    exitCode = RunSystemCommand(cmd)
    os.chdir(cwd)
    return exitCode


def DeleteFilesNew(directory, extensions, subdirectories=True):
    """
    Deletes one or more files using MS DOS DEL Command.
    :rtype : int
    :param directory: Directory to be cleaned.
    :param extensions: List of extensions of files to be deleted.
    :param subdirectories: Delete files from all subdirectories.
    :return: 0 for success.
    """
    if not os.path.exists(directory) or not extensions:
        return

    exclude = ''
    for ext in extensions:
        exclude = '^.*\.' + ext + '$' if not exclude else exclude + '|' + '^.*\.' + ext + '$'

    count = 0
    for root, dir, files in os.walk(directory):
        for item in files:
            if re.match(exclude, item):
                filePath = os.path.join(root, item)
                print('\t' + filePath)
                # os.remove(filePath)
                DeleteFile(filePath)
                count += 1
    print('Delete files count = [%d]' % count)
    return 0


def DeleteFile(filePath, force=True):
    cmd = ''
    if force:
        cmd = 'DEL /F \"%s\"' % filePath
    else:
        cmd = 'DEL \"%s\"' % filePath
    exitCode = RunSystemCommand(cmd)
    return exitCode


def ValidDirectory(directory):
    if not os.path.isdir(directory):
        raise BaseException('Invalid directory : [%s].' % directory)
    return directory


def main():
    parser = argparse.ArgumentParser(description='Delete VisualStudio temporary files')
    parser.add_argument('--dir', '--directory', type=ValidDirectory, dest='directory', required=True,
                        help='Directory path to clean!')
    options = parser.parse_args()
    print('options = [%s]' % options)

    directory = options.directory

    # directory = r'E:\Labs\C++'
    extensions = [
        'aps', 'bsc', 'exp', 'idb', 'ilk', 'log', 'ncb', 'sdf', 'obj', 'pch', 'pdb', 'plg', 'res', 'sbr',
        'tmp', 'trg', 'htm', 'dep', 'manifest', 'ipch', 'tlog', 'lastbuildstate', 'vcxproj.user', 'vsp'
    ]
    # exitCode = DeleteFiles(directory, extensions, True)
    exitCode = DeleteFilesNew(directory, extensions, True)
    # return exitCode

    return 0

if __name__ == '__main__':
    exitCode = 0
    print(' Begin '.center(80, '-'))
    exitCode = main()
    print('ExitCode = [%d]' % exitCode)
    print(' End '.center(80, '-'))
    sys.exit(exitCode)