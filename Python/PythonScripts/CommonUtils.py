import os
import sys
import time
import glob
import math
import subprocess
import datetime
import parse


def Print(info):
    """
    Print the _info_ on stdout with present time as prefix.
    @param info: Info you want to write on stdout
    @return: None
    """
    print(info)
    sys.stdout.flush()
    return None


def PrintInfo(info):
    """
    Print the _info_ on stdout with present time as prefix.
    @param info: Info you want to write on stdout
    @return: None
    """
    print('[%s] %s' % (time.strftime("%Y-%m-%d %H:%M:%S"), info))
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
    :rtype : int
    """
    exitCode = os.system(GetDoubleQuotedString(cmd))
    return exitCode


def GetNewItemsList(source, target, pattern, considerLastNBuilds=-1):
    """
    Returns the list of items that are available in source folder and not available in target folder.
    Return empty lists if either source or target directory is not available. I feel this is correct behaviour
        for now, because if target directory is not available and source is available, all items in the source
        would be recognized as new items and script will get executed for these items, this is not correct.

    @param source: Source Directory Path
    @param target: Target Directory Path
    @param pattern: Pattern of files/folders that you are looking for.
    @param considerLastNBuilds: GetNewItemsList considers only last #considerLastNBuilds only (ignore the old builds).
            If considerLastNBuilds is -1 means consider all builds.
    @return: List of items that are available in source and not available in target.

    Example:
    --------

        Source = [\\atltruck\Products\IMAGINE\15.0]
        Target = [\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\Products\IMAGINE\15.0]
        Pattern = [*\*.iso]

          New Items:
          --------------------------------------------------------------------------------
          1. \\atltruck\Products\IMAGINE\15.0\IMAGINE_2014-10-22_0633_b50\IMAGINE x64.iso
          2. \\atltruck\Products\IMAGINE\15.0\IMAGINE_2014-10-22_0633_b50\IMAGINE x86.iso
          --------------------------------------------------------------------------------

    """
    if not os.path.exists(source) or not os.path.exists(target):
        PrintInfo('ERROR: Source [%s] or target [%s] is not available!' % (source, target))
        return [], []

    sourceWithBS = source + '\\'
    targetWithBS = target + '\\'

    sourcePattern = os.path.join(source, pattern)
    # PrintInfo('SourcePattern = [%s]' % sourcePattern)

    targetPattern = os.path.join(target, pattern)
    # PrintInfo('TargetPattern = [%s]' % targetPattern)

    sourcePaths = [filePath.replace(sourceWithBS, '') for filePath in glob.glob(sourcePattern)]
    # PrintInfo('sourcePaths = [%s]' % sourcePaths)

    if considerLastNBuilds > 0:
        totalNumOfBuilds = len(sourcePaths)
        numOfBuildsToRemove = totalNumOfBuilds - considerLastNBuilds
        if numOfBuildsToRemove > 0:
            sourcePaths = sourcePaths[numOfBuildsToRemove:]

    targetPaths = [filePath.replace(targetWithBS, '') for filePath in glob.glob(targetPattern)]
    # PrintInfo('targetPaths = [%s]' % targetPaths)

    newItems = [os.path.join(source, fileSource) for fileSource in sourcePaths if not fileSource in targetPaths]
    # PrintInfo('New Items : [%s]' % newItems)

    availableItems = [os.path.join(source, fileSource) for fileSource in sourcePaths if fileSource in targetPaths]
    # PrintInfo('Available Items : [%s]' % availableItems)

    return newItems, availableItems


def PrintIterable(iterable, title='Elements', indent='', printFunc=Print):
    """

    @param iterable: List of items to print on stdout.
    @param title: Title for the items.
    @param indent: Print items with given indent.

    Example: Here, title is 'Company Names', indent is 2

    |
    |  Company Names:
    |  --------------------------------------------------------------------------------
    |  1. Intergraph Consulting Pvt Ltd
    |  2. Hexagon Geospatial
    |  --------------------------------------------------------------------------------
    |

    """
    printFunc('')
    printFunc('%s%s:' % (indent, title))
    printFunc('%s%s' % (indent, '-' * 79))
    if iterable:
        itemsCount = len(iterable)
        fmt = '%s%%%dd. %%s' % (indent, math.log10(itemsCount) + 1)
        for i in xrange(itemsCount):
            printFunc(fmt % (i + 1, iterable[i]))
    else:
        printFunc('%s--- empty ---' % indent)
    printFunc('%s%s' % (indent, '-' * 79))
    printFunc('')


def ValidDirectory(directoryPath):
    directoryPath = directoryPath.strip()
    if not directoryPath or not os.path.isdir(directoryPath):
        info = (r'Directory path [%s] does not exist!' % directoryPath)
        raise BaseException(info)
    return directoryPath


def GetConfig(fileName):
    return ('x86' if fileName.find('x86') != -1 else ('x64' if fileName.find('x64') != -1 else ''))


def IsFTP(ftpPath): return ftpPath.startswith('ftp://')


def IsUNC(uncPath): return uncPath.startswith('\\')


def ConvertToFTP(path):
    if IsFTP(path): return path
    if IsUNC(path): return 'ftp:' + path.replace('\\', '/')
    info = r'Path [{}] is not in UNC/FTP format!'.format(path)
    raise BaseException(info)


def ConvertToUNC(path):
    if IsUNC(path): return path
    if IsFTP(path): return path[4:].replace('/', '\\')
    return None


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
    # PrintInfo('ExitCode = %d' % exitCode)
    # raise Exception(str(stderr))

    os.chdir(cwd)
    return exitCode


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
    # PrintInfo('ExitCode = %d' % exitCode)
    # raise Exception(str(stderr))

    os.chdir(cwd)
    return exitCode


def CopyFileUsingRobocopy(sourceDirectory, targetDirectory, fileName):
    options = '/NP /NJH /NJS'
    command = 'robocopy.exe \"{}\" \"{}\" \"{}\" {}'.format(sourceDirectory, targetDirectory, fileName, options)
    PrintInfo('Executing Command : [%s]' % command)
    exitCode = RunSystemCommand(command)
    return exitCode


def CopyDirectoryUsingRobocopy(sourceDirectory, targetDirectory):
    options = '/MIR /NP /NJH /NJS'
    command = 'robocopy.exe \"{}\" \"{}\" {}'.format(sourceDirectory, targetDirectory, options)
    PrintInfo('Executing Command : [%s]' % command)
    exitCode = RunSystemCommand(command)
    return exitCode


def GetDirectorySize(directoryPath, subDirectories=True):
    """
    Returns size of directory in Bytes.
    @rtype: int
    @param directoryPath: Directory Path
    @param subdirectories: Calculate for all subdirectories.
    @return: Size in Bytes.
    """
    ret = 0
    if subDirectories:
        for dirPath, dirNames, fileNames in os.walk(directoryPath):
            for f in fileNames:
                ret += os.path.getsize(os.path.join(dirPath, f))
    else:
        for fileName in os.listdir(directoryPath):
            filePath = os.path.join(directoryPath, fileName)
            if os.path.isfile(filePath):
                ret += os.path.getsize(filePath)
        return ret
    return ret


def GetDirectoryInfo(directoryPath, subDirectories=True):
    """
    Returns (#files, #folders, size in bytes) of directory.
    @rtype: int
    @param directoryPath: Directory Path
    @param subdirectories: Calculate for all subdirectories.
    @return: (#files, #folders, sizeInBytes).
    """
    files, folders, size = 0, 0, 0
    if subDirectories:
        for dirPath, dirNames, fileNames in os.walk(directoryPath):
            folders += len(dirNames)
            for f in fileNames:
                size += os.path.getsize(os.path.join(dirPath, f))
                files += 1
    else:
        for fileName in os.listdir(directoryPath):
            filePath = os.path.join(directoryPath, fileName)
            if os.path.isfile(filePath):
                size += os.path.getsize(filePath)
                files += 1
    return files, folders, size


def FormatSize(sizeInBytes):
    """
    Format the size.
    Ex:
        207374507   : 197.77 MB
        5455693352  : 5.08 GB
        111107237   : 105.96 MB
        10          : 10 Bytes
        1024        : 1024 Bytes
        1048576     : 1024 KB
        3145728     : 3 MB
    @rtype : str
    @param sizeInBytes: Size in Bytes.
    @return: Formatted string.
    """
    l = [(1 << 40, 'TB'), (1 << 30, 'GB'), (1 << 20, 'MB'), (1 << 10, 'KB'), (1, 'Bytes')]
    for (k, v) in l:
        if sizeInBytes > k:
            if sizeInBytes % k == 0:
                return '{0} {1}'.format(sizeInBytes / k, v)
            else:
                return '{0:.2f} {1}'.format(float(sizeInBytes) / k, v)
    return '0 Bytes'


def IsPythonFile(fileName):
    return '.py' == os.path.splitext(fileName)[1]


def IsBatchFile(fileName):
    return '.bat' == os.path.splitext(fileName)[1]


def GetProductNameVersionBuild(format, filePath):
    dictObj = parse.parse(format, filePath)
    return dictObj['productname'], dictObj['version'], dictObj['build']


def GetHtmlTable(table):
    ret = '<table>\n'
    for tr in table:
        ret += '<tr style=\'mso-yfti-irow:0;mso-yfti-firstrow:yes;height:15.75pt\'>'
        for i, td in enumerate(tr):
            if i == 0:
                ret += '<td width=99 style=\'width:74.0pt;border:solid windowtext 1.0pt;background:#D9D9D9;padding:0cm 5.4pt 0cm 5.4pt;height:15.75pt\'><b>{0}</b></td>'.format(td)
            else:
                ret += '<td width=789 style=\'width:592.0pt;border:solid windowtext 1.0pt;border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.75pt\'>{0}</td>'.format(td)
        ret += '</tr>\n'
    ret += '</table>\n'
    return ret


def GetHtmlMailText(source, target, elapsed):
    table = list()
    table.append(['Source', GetDoubleQuotedString(source)])
    table.append(['Target', GetDoubleQuotedString(target)])
    directorInfo = GetDirectoryInfo(target, True)
    if os.path.isdir(target):
        size = '{0} ({1} bytes)'.format(FormatSize(directorInfo[2]), '{0:,}'.format(directorInfo[2]))
        contains = '{0} Files, {1} Folders'.format(directorInfo[0], directorInfo[1])
        table.append(['Size', size])
        table.append(['Contains', contains])
    else:
        size = os.path.getsize(target)
        size = '{0} ({1} bytes)'.format(FormatSize(size), '{0:,}'.format(size))
        table.append(['Size', size])

    table.append(['Elapsed', elapsed])

    htmlTable = GetHtmlTable(table)

    html = '<html>\n'
    html += '<style>\n'
    html += 'table, th, td {\n'
    html += 'border: 1px solid black;\n'
    html += 'border-collapse: collapse;\n'
    html += 'font-family: Calibri;\n'
    html += 'font-size: 11.0pt\n'
    html += '}\n'
    html += '</style>\n'
    html += '<body style="font-family:Calibri;font-size:11.0pt;">'
    html += htmlTable
    html += '</body>\n'
    html += '</html>\n'

    return html


def CallMain(mainfunc):
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    print(info.center(79, '-'))
    sc = ScopedTimer(displayExtraInfo=True)
    exitCode = mainfunc()
    del sc
    print('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    print(info.center(79, '-'))
    sys.exit(exitCode)


class ScopedTimer:
    def __init__(self, displayExtraInfo=False):
        self.started = datetime.datetime.now()
        self.displayExtraInfo = displayExtraInfo
        if self.displayExtraInfo:
            print('Started : %s' % self.started)

    def __del__(self):
        ended = datetime.datetime.now()
        if self.displayExtraInfo:
            # print('Started : %s' % self.started)
            print('Ended   : %s' % ended)
        elapsed = ended - self.started
        print('Elapsed : %s' % elapsed)


class FormatPrinter:
    def __init__(self, width, sep=':', printFunc=Print):
        """
        @param width: Width for the key (LHS width).
        @param sep: Separator between key & value.
        @param printFunc: Alternative print function.
        """
        self.width = width
        self.fmt = '%{0}s {1} %s'.format(self.width, sep)
        self.printFunc = printFunc

    def Print(self, key, value):
        """
        Print the Key (LHS), Value (RHS) in the following format.

             DirectoryPath : E:\Labs
               Sub-Folders : True
                     Files : 90596
                   Folders : 12113
                      Size : 6.18 GB

        @param key: Key
        @param value: Value
        """
        self.printFunc(self.fmt % (key, value))
