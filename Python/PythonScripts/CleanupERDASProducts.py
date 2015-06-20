import os
import sys
import re
import stat
import shutil
import argparse
import time
import textwrap

# DesktopIDKs_2013-07-28_1102_b813
reERDASProduct = re.compile(r'^(\w+)_(\d{4}-\d{2}-\d{2})_(\d{4})_b(\d+)$')


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


def remove_readonly(fn, path, excInfo):
    if fn is os.rmdir:
        os.chmod(path, stat.S_IWRITE)
        os.rmdir(path)
    elif fn is os.remove:
        os.chmod(path, stat.S_IWRITE)
        os.remove(path)


class CleanupERDASProducts:
    def __init__(self, directoryPath, keepLastNBuilds=30):
        self.directoryPath = directoryPath
        self.keepLastNBuilds = keepLastNBuilds


def RemoveProducts(directoryPath=None, keepLastNBuilds=30):
    products = []
    productsToRemove = []

    # Get the available products which matches regular expression 'reERDASProduct'
    for directoryName in os.listdir(directoryPath):
        matchObj = reERDASProduct.match(directoryName)
        if matchObj:
            products.append(directoryName)

    totalNumOfProducts = len(products)
    print('TotalNumOfProducts = [%d]' % totalNumOfProducts)

    numOfBuildsToRemove = totalNumOfProducts - keepLastNBuilds
    print('NumOfBuildsToRemove = [%d]' % numOfBuildsToRemove)

    if numOfBuildsToRemove > 0:
        productsToRemove = products[:numOfBuildsToRemove]
        print('productsToRemove = [%s]' % productsToRemove)

    exitCode = 0

    if productsToRemove:
        print('Removing products...')
        for productName in productsToRemove:
            delDirectoryPath = os.path.join(directoryPath, productName)
            print('Removing [%s] ...' % delDirectoryPath)
            # shutil.rmtree(delDirectoryPath, onerror=remove_readonly)
            exitCode = RunSystemCommand('rmdir /S /Q {}'.format(delDirectoryPath)) and exitCode

    return exitCode


def main():
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description='Clean ERDAS Products',
                                     epilog=textwrap.dedent('''\
                                        And Defaults:
                                            --display=True'''
                                        )
                                    )

    parser.add_argument('--directory', dest='directory', required=True,
                        help='Path of the ERDAS Products Installers directory')
    parser.add_argument('--keep-last-n-builds', '--keep', dest='keeplastnbuilds', type=int, required=True,
                        help='Keep the last N builds.')

    options = parser.parse_args()
    print('Options : %s' % options)
    RemoveProducts(options.directory, options.keeplastnbuilds)
    return 0


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    print(info.center(80, '-'))
    status = 0
    status = main()
    info = ' ' + fileName + ' ' + 'End' + ' '
    print(info.center(80, '-'))
    sys.exit(status)
