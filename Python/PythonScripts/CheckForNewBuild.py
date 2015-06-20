import os
import sys
import argparse
import CommonUtils
PrintInfo = CommonUtils.PrintInfo


def main():
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@',
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-s', '--source', '--source-directory', type=CommonUtils.ValidDirectory, dest='source_directory', required=True,
                        help='Source Directory')
    parser.add_argument('-t', '--target', '--target-directory', type=CommonUtils.ValidDirectory, dest='target_directory', required=True,
                        help='Target Directory')
    parser.add_argument('-p', '--pattern', dest='pattern', type=str, required=True,
                        help='Pattern that you are looking for.\n'
                             'Examples:\n'
                             '"*" : All files and directories\n'
                             '"*/*.iso" : All .iso files in the top level directories.')

    options = parser.parse_args()
    PrintInfo('Options : %s' % options)
    PrintInfo('')

    source = options.source_directory
    target = options.target_directory
    pattern = options.pattern.strip()

    itemsList = CommonUtils.GetNewItemsList(source, target, pattern)
    CommonUtils.PrintIterable(itemsList, title='NewItems', indent='\t')

    return 0 if itemsList else -1


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    PrintInfo(info.center(80, '-'))
    exitCode = main()
    PrintInfo('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    PrintInfo(info.center(80, '-'))
    sys.exit(exitCode)
