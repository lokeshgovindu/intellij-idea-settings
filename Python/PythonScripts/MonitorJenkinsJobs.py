import os
import sys
import time
import datetime
import CommonUtils
import re
import subprocess
import argparse

PrintInfo = CommonUtils.Print

rePsListLine = re.compile('^(?P<name>.+[^\s])\s+(?P<pid>\d+)\s+(?P<priority>\d+)\s+(?P<threads>\d+)\s+(?P<handles>\d+)\s+(?P<privatevm>\d+)\s+(?P<cputime>.+[^\s])\s+(?P<elapsedtime>.+)$')
reTimeDelta = re.compile('^(?P<hours>\d+):(?P<minutes>\d\d):(?P<seconds>\d\d)\.(?P<milliseconds>\d+)$')

# Name                Pid Pri Thd  Hnd   Priv        CPU Time    Elapsed Time
# Idle                  0   0   2    0      0  1037:44:02.640     0:00:00.000
# System                4   8 163 2164    160     8:01:37.531   567:12:16.700
# smss                380  11   3   33    476     0:00:00.062   567:12:15.075
# csrss               536  13  10  923   4004     0:02:59.484   567:10:46.872
# csrss               584  13   7   75   1688     0:00:01.984   567:10:16.637
# imgcompare         4448   8   1  348 108872     0:00:26.500     0:07:25.935
# Test Cpp 2013      6980   8   1   39   1092     0:00:00.031     0:00:06.665

def KillProcess(computer, processName):
    PsKillCmd = r'PsKill -t \\%s "%s"' % (computer, processName)
    PrintInfo('PsKillCmd = [%s]' % PsKillCmd)
    exitCode = CommonUtils.RunSystemCommand(PsKillCmd)
    return exitCode

def KillProcesses(processNames, computer=None, maxTimeOut=10800):
    maxTimeOut = datetime.timedelta(seconds=maxTimeOut)

    # -----------------------------------------------------------------------------
    # Create PsListCmd
    # -----------------------------------------------------------------------------
    PsListCmd = 'PsList'
    if computer != None:
        PsListCmd += ' ' + '\\\\' + computer
    PrintInfo('PsListCmd = [%s]' % PsListCmd)

    # -----------------------------------------------------------------------------
    # Execute PsListCmd on the _computer_ and traverse the generated output by PsList.
    # If any process has been executing over _maxTimeOut_ seconds then kill that
    #   process using PsKill.
    # -----------------------------------------------------------------------------
    result = subprocess.Popen(PsListCmd.split(), shell=False, stdout=subprocess.PIPE)

    for line in result.stdout:
        line = line.strip()
        psListObj = rePsListLine.match(line)
        if psListObj:
            timeDeltaObj = reTimeDelta.match(psListObj.groupdict()['elapsedtime'])
            if timeDeltaObj:
                delta = datetime.timedelta(hours=int(timeDeltaObj.groupdict()['hours']),
                                           minutes=int(timeDeltaObj.groupdict()['minutes']),
                                           seconds=int(timeDeltaObj.groupdict()['seconds']),
                                           milliseconds=int(timeDeltaObj.groupdict()['milliseconds']))
                processName = psListObj.groupdict()['name']
                if processName in processNames and delta > maxTimeOut:
                    # PrintInfo('line = [%s]' % line)
                    # PrintInfo('hours = %s' % timeDeltaObj.groupdict()['hours'])
                    # PrintInfo('minutes = %s' % timeDeltaObj.groupdict()['minutes'])
                    # PrintInfo('seconds = %s' % timeDeltaObj.groupdict()['seconds'])
                    # PrintInfo('milliseconds = %s' % timeDeltaObj.groupdict()['milliseconds'])
                    # PrintInfo('delta = %s' % delta)
                    PrintInfo('ComputerName = [%s], ProcessName = [%s], ElapsedTime = [%s]' % (computer, processName, delta))
                    KillProcess(computer, processName)

    return 0


def main():
    parser = argparse.ArgumentParser(
        prog='MonitorJenkinsJobs',
        description='This script will kill the specified jobs if they are running more than the maxtimeout'
    )
    # parser.add_argument('--computers', metavar='COMPUTER', dest='computers', nargs='*', required=False,
    #                     help='List of ComputerNames separated by space.')
    # parser.add_argument('--processes', metavar='PROCESSNAME', dest='processes', nargs='+', required=True,
    #                     help='List of ProcessNames separated by space.')
    parser.add_argument('--computers', dest='computers', type=str, required=False,
                        help='List of ComputerNames separated by comma.')
    parser.add_argument('--processes', dest='processes', type=str, required=True,
                        help='List of ProcessNames separated by comma.')
    parser.add_argument('--timeout', dest='timeout', type=int, default=10800,
                        help='Maximum timeout in seconds. (default: 10800 (3 hours))')

    options = parser.parse_args()

    print('options = [%s]' % options)
    # computers = options.computers
    # processes = options.processes
    computers = options.computers.split(',')
    processes = options.processes.split(',')
    timeout   = options.timeout

    for computer in computers:
        KillProcesses(processNames=processes, computer=computer, maxTimeOut=timeout)

    return 0


def main_test():
    computers = [
        'IN-ERDDEVVM02',
        'IN-ERDDEVVM04',
        'IN-ERDDEVVM05',
        'IN-ERDDEVVM06',
        'IN-ERDDEVVM07',
        'IN-ERDDEVVM08',
        'IN-ERDDEVVM11',
        'IN-ERDDEVVM12',
        'IN-ERDDEVVM13',
        'IN-ERDDEVVM14',
        'IN-ERDDEVVM15',
        'IN-ERDDEVVM16',
    ]

    processNames = [
        'batchprocess',
        'ecw_compress',
        'export_raster_trans',
        'import_raster_trans'
    ]

    timeOut = 10800

    for computer in computers:
        KillProcesses(processNames=processNames, computer=computer, maxTimeOut=timeOut)

    return 0


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    PrintInfo(info.center(79, '-'))
    exitCode = main()
    # exitCode = main_test()
    PrintInfo('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    PrintInfo(info.center(79, '-'))
    sys.exit(exitCode)
