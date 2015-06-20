import CommonUtils
import os
import sys
import subprocess

def PrintNumbers(n):
    for i in xrange(n):
        CommonUtils.PrintInfo(i)
    return 0

def main():
    # PrintNumbers(10)

    # ncftpgetCmd = 'ncftpget.exe -u ftpuser -p kroNos!2013! "ftp://atltruck/Products/IMAGINE/15.0/IMAGINE_2014-10-31_1213_b108/IMAGINE x64.iso"'
    # ncftpgetCmdArgs = ['ncftpget.exe', '-u', 'ftpuser', '-p', 'kroNos!2013!', 'ftp://atltruck/Products/IMAGINE/15.0/IMAGINE_2014-10-31_1213_b108/IMAGINE x64.iso']
    # print(ncftpgetCmdArgs)
    # subprocess.call(ncftpgetCmdArgs, shell=True)


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
