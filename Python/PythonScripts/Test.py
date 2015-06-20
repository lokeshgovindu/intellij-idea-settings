from __future__ import print_function
# import __future__
import os
import sys
import thread
import time
import logo
import psutil
import urllib
import urllib2

import math
import decimal

import win32ui
import win32gui
import win32con
import win32api

import os
import sys
import glob
import datetime
import thread
import time
import argparse
import re
import string
import parse
import parser
import subprocess

import CommonUtils



def print_time(threadName, delay):
    count = 0
    while count < 9:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


def thread_example():
    print("Function %s called from function %s" % (logo.callee(), logo.caller()))

    # Creating two threads as follows
    try:
        thread.start_new_thread(print_time, ("Thread-1", 2,))
        thread.start_new_thread(print_time, ("Thread-2", 4,))
    except:
        print("Error: unable to start thread")

    time.sleep(5)
    while True:
        time.sleep(1)
        # print("Threads activeCount : %d" % thread._count())
        numberOfThreads = thread._count()
        if numberOfThreads == 0: break


def GetDateTime():
    """Returns the date time as a string in the format of YYYY-MM-DD HH-MM-SS'"""
    dt = time.strftime("%Y-%m-%d %H:%M:%S")
    return dt


def timeexample():
    """
    Time example
    """
    # print('%s' % time.accept2dyear)
    # print(time.gmtime())
    # print(time.asctime())
    # print(time.ctime())
    # print(time.localtime())
    # print(time.mktime(time.localtime()))
    # print(time.ctime(time.mktime(time.localtime())))
    # print(time.strftime('%a'))
    # print(time.strftime('%A'))
    # print(time.strftime('%b'))
    # print(time.strftime('%B'))
    # print(time.strftime('%c'))
    # print(time.strftime('%d'))
    # print(time.strftime('%H'))
    # print(time.strftime('%I'))
    # print(time.strftime('%j'))
    # print(time.strftime('%m'))
    # print(time.strftime('%M'))
    # print(time.strftime('%p'))
    # print(time.strftime('%S'))
    # print(time.strftime('%U'))
    # print(time.strftime('%w'))
    # print(time.strftime('%W'))
    # print(time.strftime('%x'))
    # print(time.strftime('%X'))
    # print(time.strftime('%c'))
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    # print(time.strftime('%y'))
    # print(time.strftime('%Y'))
    # print(time.strftime('%Z'))
    # print(time.strftime('%%'))
    # while True:
    #     time.sleep(1)
    #     print(time.strftime('%Y-%m-%d %H:%M:%S'))


def sorting():
    l = [5, 2, 7, 6, 3, 1, 4]
    print(l)
    l.sort()
    print(l)
    return None


def doit():
    filepath = r'X:\Products\IMAGINE\14.0\IMAGINE_x64_LatestInstall.cmd'
    print(os.path.basename(filepath))
    print(os.path.dirname(filepath))
    print(os.path.split(filepath))
    print(os.path.splitext(filepath))

    filepath = r'X:/Products/IMAGINE/14.0/IMAGINE_x64_LatestInstall.cmd'
    print(os.path.basename(filepath))
    print(os.path.dirname(filepath))
    print(os.path.split(filepath))
    print(os.path.splitext(filepath))

    print('Last access: %s' % os.path.getatime(filepath))
    print('Last access: %s' % time.ctime(os.path.getatime(filepath)))
    print('Last modified: %s' % os.path.getmtime(filepath))
    print('Last modified: %s' % time.ctime(os.path.getmtime(filepath)))

    print('Created: %s' % os.path.getctime(filepath))
    print('Created: %s' % time.ctime(os.path.getctime(filepath)))


def WaitForProcess(processName):
    for proc in psutil.process_iter():
        if hasattr(proc, 'name') and proc.name == processName:
            print(proc)
            proc.wait()


def DownloadFile():
    urlPaths = ['http://updates.jenkins-ci.org/download/plugins/extra-columns/1.14/extra-columns.hpi',
                'http://updates.jenkins-ci.org/download/plugins/urltrigger/0.37/urltrigger.hpi',
                'http://updates.jenkins-ci.org/download/plugins/credentials/1.13/credentials.hpi',
                'http://updates.jenkins-ci.org/download/plugins/cloudbees-plugin-gateway/5.0/cloudbees-plugin-gateway.hpi',
                'http://updates.jenkins-ci.org/download/plugins/parameterized-trigger/2.25/parameterized-trigger.hpi',
                'http://updates.jenkins-ci.org/download/plugins/msbuild/1.22/msbuild.hpi',
                'http://updates.jenkins-ci.org/download/plugins/groovy-postbuild/1.9/groovy-postbuild.hpi',
                'http://updates.jenkins-ci.org/download/plugins/greenballs/1.14/greenballs.hpi',
                'http://updates.jenkins-ci.org/download/plugins/ssh-credentials/1.6.1/ssh-credentials.hpi',
                'http://updates.jenkins-ci.org/download/plugins/mapdb-api/1.0.1.0/mapdb-api.hpi',
                'http://updates.jenkins-ci.org/download/plugins/scm-api/0.2/scm-api.hpi',
                'http://updates.jenkins-ci.org/download/plugins/subversion/2.4/subversion.hpi',
                'http://updates.jenkins-ci.org/download/plugins/performance/1.10/performance.hpi',
                'http://updates.jenkins-ci.org/download/plugins/token-macro/1.10/token-macro.hpi',
                'http://updates.jenkins-ci.org/download/plugins/git-client/1.9.1/git-client.hpi',
                'http://updates.jenkins-ci.org/download/plugins/git/2.2.1/git.hpi',
                'http://updates.jenkins-ci.org/download/plugins/git-server/1.3/git-server.hpi',
                'http://updates.jenkins-ci.org/download/plugins/scriptler/2.7/scriptler.hpi',
                'http://updates.jenkins-ci.org/download/plugins/git/2.2.1/git.hpi',
                'http://updates.jenkins-ci.org/download/plugins/coverity/1.3.1/coverity.hpi',
                'http://updates.jenkins-ci.org/download/plugins/jobConfigHistory/2.6/jobConfigHistory.hpi',
                'http://updates.jenkins-ci.org/download/plugins/fstrigger/0.39/fstrigger.hpi',
                'http://updates.jenkins-ci.org/download/plugins/translation/1.11/translation.hpi',
                'http://updates.jenkins-ci.org/download/plugins/perforce/1.3.27/perforce.hpi',
                'http://updates.jenkins-ci.org/download/plugins/email-ext/2.38/email-ext.hpi',
                'http://updates.jenkins-ci.org/download/plugins/matrix-auth/1.2/matrix-auth.hpi',
                'http://updates.jenkins-ci.org/download/plugins/build-flow-plugin/0.12/build-flow-plugin.hpi',
                'http://updates.jenkins-ci.org/download/plugins/ssh-slaves/1.6/ssh-slaves.hpi',
                'http://updates.jenkins-ci.org/download/plugins/active-directory/1.37/active-directory.hpi',
                'http://updates.jenkins-ci.org/download/plugins/buildresult-trigger/0.17/buildresult-trigger.hpi',
                'http://updates.jenkins-ci.org/download/plugins/nested-view/1.14/nested-view.hpi',
                'http://updates.jenkins-ci.org/download/plugins/ssh-credentials/1.6.1/ssh-credentials.hpi',
                'http://updates.jenkins-ci.org/download/plugins/maven-plugin/2.3/maven-plugin.hpi',
                'http://updates.jenkins-ci.org/download/plugins/timestamper/1.5.11/timestamper.hpi',
                'http://updates.jenkins-ci.org/download/plugins/credentials/1.13/credentials.hpi',
                'http://updates.jenkins-ci.org/download/plugins/git-server/1.3/git-server.hpi',
                'http://updates.jenkins-ci.org/download/plugins/git-client/1.9.1/git-client.hpi']

    outDir = r'C:\Softwares\Jenkins\Plugins'
    prevDir = os.curdir
    os.chdir(outDir)
    for urlPath in urlPaths:
        vs = urlPath.split('/')
        fileName, fileExt = os.path.splitext(vs[-1])
        fileNameWithVersion = fileName + '_' + vs[-2] + fileExt
        outFilePath = os.path.join(outDir, fileNameWithVersion)
        PrintInfo('Downloading [%s] to [%s]' % (fileNameWithVersion, outFilePath))
        urllib.urlretrieve(urlPath, fileNameWithVersion)
        urllib.urlcleanup()

    os.chdir(prevDir)

    return 0


def IconTest():
    ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
    ico_y = win32api.GetSystemMetrics(win32con.SM_CYICON)

    index = 0
    large, small = win32gui.ExtractIconEx(r'E:\Build\Generation_3\root\bin\Win32Release\ermapper.exe', index)
    win32gui.DestroyIcon(small[index])
    print('large = [%s]' % (large,))

    hdc = win32ui.CreateDCFromHandle( win32gui.GetDC(0) )
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap( hdc, ico_x, ico_x )
    hdc = hdc.CreateCompatibleDC()

    hdc.SelectObject( hbmp )
    hdc.DrawIcon((0,0), large[0])

    hbmp.SaveBitmapFile( hdc, r'F:\ConquerorsTeamSpace\DesktopScreens\ER Mapper\ermapper_icon.bmp')
    return 0


mp = {}

def P(k, n):
    if k > n:   return 0
    if k == n:  return 1

    pr = (k, n)
    if mp.has_key(pr): return mp[pr]
    res = P(k + 1, n) + P(k, n - k);
    mp[pr] = res % 1000000
    return mp[pr]


def nCr(n, r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n - r)

def Cn(n):
    # return nCr(2 * n, n) - nCr(2 * n, n + 1)
    return nCr(2 * n, n) / (n + 1)

def ProjectEulerTest():
    # for r in xrange(1, 100, 1):
    #     print('r = %3d, ncr = %d' % (r, nCr(100, r)))
    # print(nCr(99, 49))
    n1, n2, i = 5, 17, 1
    sum = 66 # Sum of perimeters of first two triangles.

    while True:
        print(n1, n2, i)
        n = 4 * n2 - n1 + 2 * i
        perimeter = 3 * n + i
        if perimeter >= 10**9:
            break
        sum += perimeter
        n1, n2, i = n2, n, -i

    print(sum)
    return 0

def doit():
    l = [1, 2, 3]
    print(1 in l)
    print(4 in l)

def walk_example():
    timer = CommonUtils.ScopedTimer()
    directoryPath = r'F:\TEMP'
    numberOfFiles = 0
    for dirPath, dirNames, fileNames in os.walk(directoryPath):
        print(dirPath)
        print(fileNames)
        numberOfFiles += 1
    print( "Number of files : %d" % numberOfFiles )
    return None


def glob_example():
    # dirPath = r"E:\LGTEMP"
    # dirPath = r'\\In-disrv01\ConquerorsTeamSpace\Products\IMAGINE\14.0'
    # os.chdir(dirPath)
    # pattern  = r'\\In-disrv01\ConquerorsTeamSpace\Products\IMAGINE\14.0\*\*.iso'

    started = datetime.datetime.now()
    print(started)
    pattern = r'\\atltruck\IDK\IMAGINE\14.0\*\*.iso'
    for file in glob.glob(pattern): print(file)
    ended = datetime.datetime.now()
    print(ended)
    print(ended - started)
    return None


def doit_1():
    dirPath = r"E:\LGTEMP"
    dirPath = os.getenv("LGTEMP", dirPath)
    print( "Directory Path : %s" % dirPath )
    # print( os.listdir( dirPath ) )
    glob.glob()
    return None


def PrintNumbers(start, end, waitTime):
    for i in xrange(start, end + 1, 1):
        CommonUtils.PrintInfo(i)
        time.sleep(waitTime)
    return None

def ValidDirectoryPath(directoryPath):
    if directoryPath and os.path.isdir(directoryPath):
        return os.path.normpath(os.path.abspath(directoryPath))
    raise BaseException('Invalid directory path : [%s]' % directoryPath)


def GetFilesAndDirectories(pattern):
    paths = []
    for filePath in glob.glob(pattern): paths.append(filePath)
    return paths

def CountNumbers(N):
    for i in xrange(N):
        print(i + 1)
        time.sleep(1)

def thread_example():
    print('Thread Example')
    N = 30
    waitTime = 3
    # CountNumbers(30)
    threadId = thread.start_new_thread(CountNumbers, (N,))
    print('ThreadID = %s' % threadId)
    print('Wait for %s seconds...' % waitTime)
    time.sleep(waitTime)
    pass


def PsListTest():
    pass


def VSTest():
    vs120comntools = os.environ['VS120COMNTOOLS']
    vsvars32 = os.path.join(vs120comntools, 'vsvars32.bat')
    # os.system('"' + vsvars32 + '"')
    args = []
    print(os.environ)
    args.append('type')
    args.append(vsvars32)
    returncode = subprocess.call(args, shell=True)
    print('returncode = %d' % returncode)
    print(os.environ)
    os.system('cl')
    pass

import osgeo

def main():
    timer = CommonUtils.ScopedTimer(displayExtraInfo=True)

    # VSTest()
    # sys.path.append(r'C:\OSGeo4W\apps\gdal-17\pymod')

    # r'\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\Products\IDKs\15.0\DesktopIDKs\DesktopIDKs_2014-11-18_2256_b212'
    # desktopIDKsPath       = r'\\atltruck\Products\IDKs\15.0\DesktopIDKs\DesktopIDKs_2014-11-18_2256_b212'
    # desktopIDKsPath       = r'\\atltruck\Products\IDKs\Mainline\DesktopIDKs\DesktopIDKs_2014-11-22_0346_b2638'
    # desktopIDKsPathFormat = r'\\atltruck\Products\IDKs\{version}\{productname}\{build}'
    #
    # print(CommonUtils.GetProductNameVersionBuild(desktopIDKsPathFormat, desktopIDKsPath))
    # productname, version, build = CommonUtils.GetProductNameVersionBuild(desktopIDKsPathFormat, desktopIDKsPath)
    # targetDirectory = r'\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\Products\IDKs\{version}\{productname}'.format(productname=productname, version=version)
    # print('targetDirectory = [%s]' % targetDirectory)
    #
    # imagineISOPath       = r'\\atltruck\Products\IMAGINE\15.0\IMAGINE_2014-11-18_1717_b212\IMAGINE x64.iso'
    # imagineISOPathFormat = r'\\atltruck\Products\{productname}\{version}\{build}\IMAGINE x64.iso'
    # print(CommonUtils.GetProductNameVersionBuild(imagineISOPathFormat, imagineISOPath))
    #
    # imagineISOPatchPath       = r'\\atltruck\Products\IMAGINE\15.0\Updates\IMAGINE_2014-11-16_0822_b207_from_b200\IMAGINE x86 Patch.iso'
    # imagineISOPatchPathFormat = r'\\atltruck\Products\{productname}\{version}\Updates\{build}\{filenamewithext}'
    # print(CommonUtils.GetProductNameVersionBuild(imagineISOPatchPathFormat, imagineISOPatchPath))
    #
    # imagineRCISOPath       = r'\\atltruck\AT\15\Candidates\IMAGINE\RC7\ISOs\IMAGINE-RC7.iso'
    # imagineRCISOPathFormat = r'\\atltruck\AT\{version}\Candidates\{productname}\{build}\ISOs\IMAGINE-RC7.iso'
    # print(CommonUtils.GetProductNameVersionBuild(imagineRCISOPathFormat, imagineRCISOPath))

    # Parse module test
    # name = 'Lokesh Govindu'
    # age = 30
    # # print(parse.parse('My name is {name}.', 'My name is Lokesh Govindu.'))
    # print('I am {name} and I have {age} years of old.'.format(name=name, age=age))
    # print('vars() = [%s]' % vars())
    # print('My name is %(name)s.' % vars())

    # walk_example()
    # thread_example()
    # print('After calling thread_example...')
    # lg = lgclass()
    # with lgclass() as lgobj:
    #     print('test')
    # print(GetDirectoryInfo(r'E:\Build\IM_2015\root'))
    # print(GetDirectoryInfo(r'F:\Data\JIRA'))
    # print(CommonUtils.GetDirectoryInfo(r'F:\Data\JP2-Test'))
    # numFiles, directorySize = GetDirectoryInfo(r'F:\Data\JIRA')
    # print('#Files = %s, Size = %s' % (numFiles, directorySize))
    # print('Formatted DirectorySize = [%s]' % FormatSize(directorySize))
    # print(GetDirectorySize(r'F:\Data\ERS', False))
    # print(FormatSize(GetDirectorySize(r'F:\Data\ERS', False)))
    # print(FormatSize(GetDirectorySize(r'F:\Data\ERS')))
    # print(FormatSize(GetDirectorySize(r'F:\Data\Test')))
    # print(FormatSize(GetDirectorySize(r'F:\Data\TIF')))
    # print(FormatSize(10))
    # print(FormatSize(1 << 10))
    # print(FormatSize(1 << 20))
    # print(FormatSize(3 * 1 << 20))

    # source = r'\\atltruck\Products\IMAGINE\15.0'
    # target = r'\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\Products\IMAGINE\15.0'
    # pattern = r'*\*.iso'
    # filePaths = GetNewItemsList(source, target, pattern)
    # Print(filePaths, title='New Items')
    return 0


def main_argparse():
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@',
                                     description='Argument parser test!')
    parser.add_argument('--name', dest='name', type=str, help='Your Name')
    parser.add_argument('--age', dest='age', type=int, help='Your Age')
    parser.add_argument('--hometown', dest='hometown', type=str, help='Home town')
    options = parser.parse_args()
    print('Options = [%s]' % options)
    return 0


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    print(info.center(79, '-'))
    exitCode = main()
    # exitCode = main_argparse()
    info = ' ' + fileName + ' ' + 'End' + ' '
    print(info.center(79, '-'))
    sys.exit(exitCode)
