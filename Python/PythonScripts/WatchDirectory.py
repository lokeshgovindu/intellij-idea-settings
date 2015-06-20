"""
LoGo's FileSystemWatcher used to sync/monitor FileSystem

*** Read available features listed below before using this script. ****

Required Software
-----------------

- Python Version 2.7.2


Available features
==================

Sync Directory
--------------

Use this option to sync target directory with source directory.

1. #N builds are  already there in source directory, all these builds will automatically be sync'ed
   when you run the script with sync mode.

2. Source directory maintains #n builds but you want to sync and keeps only last #m (< n) builds, then you have
   to use '--sync-last-n-builds' parameter to control the number of builds to sync.


File System Watcher
-------------------

Use this (watch) option to monitor for the new files/directories, it doesn't sync target with source directory.
I mean, if there are #n number of builds already available in source directory and not available in target
directory, these items will not be identified as new items.


TODO Items
----------

1. If target directory structure is not similar with source directory structure.
   Ex: ZIP files are available in source directory and you want to pull ZIP and extract it to target directory.

2. Sub-Folders feature.

"""

from __future__ import print_function
from CommonUtils import *
import os
import sys
import time
import argparse
import glob
import thread


def DirectoryPath(directoryPath):
    if directoryPath and os.path.isdir(directoryPath):
        return directoryPath
    raise "Invalid Directory Path!"


def GetFilesAndDirectories(pattern):
    paths = []
    for filePath in glob.glob(pattern): paths.append(filePath)
    return paths


def GetAddedAndDeletedItems(oldItems, newItems):
    addedItems = []
    deletedItems = []
    for item in newItems:
        if not oldItems.count(item):
            addedItems.append(item)
    for item in oldItems:
        if not newItems.count(item):
            deletedItems.append(item)
    return addedItems, deletedItems


class LoGoFileSystemWatcher:
    def __init__(self,
                 sourceDirectory,
                 targetDirectory,
                 pattern,
                 syncLastNBuilds=7,
                 subFolders=False,
                 interval=600,
                 externalScript=None,
                 externalScriptArgs=None,
                 extScriptWaitTime=600):
        """
        :param sourceDirectory: Source Directory Path
        :param targetDirectory: Target Directory Path
        :param pattern: File pattern
        :param subFolders: Search file pattern in sub-folders
        :param interval: Look for changes for every _interval_ time
        :param externalScript: Script file to be executed on change
        :param externalScriptArgs: These args will be passed to as args to external _externalScript_
        :param extScriptWaitTime: Wait for _extScriptWaitTime_ time and invoke _externalScript_
        """
        self.sourceDirectory    = sourceDirectory
        self.targetDirectory    = targetDirectory
        self.pattern            = pattern
        self.syncLastNBuilds    = syncLastNBuilds
        self.subFolders         = subFolders
        self.interval           = interval
        self.externalScript     = externalScript
        self.externalScriptArgs = externalScriptArgs
        self.extScriptWaitTime  = extScriptWaitTime

    def Sleep(self, waitTime):
        for i in xrange(waitTime, 0, -1):
            print('Wait %d seconds!' % i, end='\r')
            time.sleep(1)
        print('Sleep over!', end='\r')
        print(' ' * 80, end='\r')

    def StartSyncing(self):
        """
        Monitor for the that are not available in source.
        """
        PrintInfo('Watching started...')
        PrintInfo('')

        # -----------------------------------------------------------------------------
        # List of items that are already downloaded or currently downloading
        # -----------------------------------------------------------------------------
        downloadedItems = []

        while True:
            # -----------------------------------------------------------------------------
            # Get new items list
            # -----------------------------------------------------------------------------
            newItems, availableItems =\
                GetNewItemsList(source=self.sourceDirectory,
                                target=self.targetDirectory,
                                pattern=self.pattern,
                                considerLastNBuilds=self.syncLastNBuilds)

            newItems, deleted = GetAddedAndDeletedItems(downloadedItems, newItems)
            
            # Print(availableItems, 'availableItems')
            # Print(newItems, 'newItems')

            # -----------------------------------------------------------------------------
            # New items are available
            # -----------------------------------------------------------------------------
            if newItems and self.externalScript:
                # Print new items on stdout (console)
                PrintIterable(newItems, title='New Items', indent='', printFunc=PrintInfo)

                # -----------------------------------------------------------------------------
                # Don't start fetching them immediately (file is being copied), wait for
                # sometime then file will be available for reading and start pulling.
                # -----------------------------------------------------------------------------
                self.Sleep(self.extScriptWaitTime)

                # -----------------------------------------------------------------------------
                # Invoke externalScript if specified.
                # -----------------------------------------------------------------------------
                for filePath in newItems:
                    if filePath not in downloadedItems:
                        if IsPythonFile(self.externalScript):
                            if self.externalScriptArgs:
                                command = 'python {0} --file \"{1}\" %s'.format(self.externalScript, filePath, self.externalScriptArgs)
                            else:
                                command = 'python {0} --file \"{1}\"'.format(self.externalScript, filePath)
                        elif IsBatchFile(self.externalScript):
                            if self.externalScriptArgs:
                                command = '{0} \"{1}\" %s'.format(self.externalScript, filePath, self.externalScriptArgs)
                            else:
                                command = '{0} \"{1}\"'.format(self.externalScript, filePath)
                        else:
                            command = self.externalScript

                        PrintInfo('Executing ExternalScriptCmd : [%s]' % command)
                        thread.start_new_thread(RunSystemCommand, (command,))
                        downloadedItems.append(filePath)
            else:
                # Sleep interval seconds of time
                self.Sleep(self.interval)

        PrintInfo('End Watching!')


    def StartWatching(self):
        """
        Watches for the new files/folders only.
        """
        PrintInfo('Watching started...')
        PrintInfo('')

        # Get the initial items
        files = GetFilesAndDirectories(self.pattern)

        while True:
            # Sleep interval seconds of time
            self.Sleep(self.interval)

            newFiles = self.GetFilesAndDirectories()
            added, deleted = GetAddedAndDeletedItems(files, newFiles)

            # Print added and delete items
            if added: PrintIterable(added, 'Added Files/Folders')

            # Do not print deleted file, here I am not updating the deleted files
            # if deleted: Print(deleted, 'Deleted Files/Folders')

            if self.externalScript:
                for filePath in added:
                    files.append(filePath)
                    command = 'python {0} --file \"{1}\"'.format(self.externalScript, filePath)
                    self.Sleep(self.extScriptWaitTime)
                    PrintInfo('Executing Command: %s' % command)
                    thread.start_new_thread(RunSystemCommand, (command,))

                    # Do not update entire list, just add the newly created ISO files
                    # files = newFiles

        PrintInfo('End Watching!')


def ValidFilePath(filePath):
    if filePath and os.path.isfile(filePath):
        return filePath
    raise "Invalid File Path!"


def ValidDirectoryPath(directoryPath):
    if directoryPath and os.path.isdir(directoryPath):
        return os.path.normpath(os.path.abspath(directoryPath))
    raise BaseException('Invalid directory path : [%s]' % directoryPath)


def main():
    """
    This function monitors for newly added files in destination directory based on your search pattern,
    but it doesn't sync your source directory with destination directory.
    """
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog="This script supports fromfile_prefix_chars (\'@\').\
                                     \nArguments that start with any of the specified characters\
                                     \nwill be treated as files, and will be replaced\
                                     \nby the arguments they contain.")

    parser.add_argument('--source', '--source-directory', dest='source', type=ValidDirectoryPath,
                        required=True, help='Source Directory Path.')
    parser.add_argument('--target', '--target-directory', dest='target', type=ValidDirectoryPath,
                        required=True, help='Target Directory Path.')
    parser.add_argument('--pattern', type=str, dest='pattern', required=True,
                        help='File/Folder pattern, you can use wildcard chars (required)')
    parser.add_argument('--recursive', '--sub-folders', dest='subFolders', default=False,
                        help='Search for _file-pattern_ in sub-folders too.')
    parser.add_argument('--sync-last-n-builds', type=int, dest='syncLastNBuilds', default=7,
                        help='Sync last #n number of builds only. (default: 7 builds)')
    parser.add_argument('--interval', type=int, dest='interval', default=600,
                        help='Check for changes for every interval seconds of time. (default: 600 seconds)')
    parser.add_argument('--script', '--externalScript', type=str, dest='externalScript',
                        help='Run the ExternalScript on any change to the Directory/File')
    parser.add_argument('--script-args', type=str, dest='scriptArgs',
                        help='Additional arguments to script.')
    parser.add_argument('--scriptWaitTime', type=int, dest='scriptWaitTime', default=600,
                        help='Wait for <WaitTime> seconds before executing externalScript. (default: 600 seconds)')

    opts = parser.parse_args()
    PrintInfo('Options : %s' % opts)

    # ------------------------------------------------------------------------------
    # Inputs
    # ------------------------------------------------------------------------------
    sourceDirectory     = opts.source
    targetDirectory     = opts.target
    pattern             = opts.pattern
    subFolders          = opts.subFolders
    syncLastNBuilds     = opts.syncLastNBuilds
    interval            = opts.interval
    externalScript      = opts.externalScript
    externalScriptArgs  = opts.scriptArgs
    scriptWaitTime      = opts.scriptWaitTime

    PrintInfo('')
    PrintInfo('Inputs:')
    PrintInfo('-------')
    PrintInfo('SourceDirectory    = [%s]' % sourceDirectory)
    PrintInfo('TargetDirectory    = [%s]' % targetDirectory)
    PrintInfo('Pattern            = [%s]' % pattern)
    PrintInfo('syncLastNBuilds    = [%s]' % syncLastNBuilds)
    PrintInfo('Interval           = [%s]' % interval)
    PrintInfo('ExternalScript     = [%s]' % externalScript)
    PrintInfo('ExternalScriptArgs = [%s]' % externalScriptArgs)
    PrintInfo('ScriptWaitTime     = [%s]' % scriptWaitTime)
    PrintInfo('')

    watcher = LoGoFileSystemWatcher(sourceDirectory=sourceDirectory,
                                    targetDirectory=targetDirectory,
                                    pattern=pattern,
                                    syncLastNBuilds=syncLastNBuilds,
                                    subFolders=subFolders,
                                    interval=interval,
                                    externalScript=externalScript,
                                    externalScriptArgs=externalScriptArgs,
                                    extScriptWaitTime=scriptWaitTime)

    # watcher.StartWatching()
    watcher.StartSyncing()
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
