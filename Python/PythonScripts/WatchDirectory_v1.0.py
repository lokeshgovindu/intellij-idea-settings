from __future__ import print_function
import os
import sys
import time
import watchdog.events
import argparse
import glob
import datetime
import math
import thread
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def DebugInfo(info):
    print('[%s] %s' % (time.strftime("%Y-%m-%d %H:%M:%S"), info))
    return None

class my_handler(FileSystemEventHandler):
    def __init__(self, scriptfile='', scriptargfile=''):
        FileSystemEventHandler.__init__(self)
        self.scriptfile = scriptfile
        self.scriptargfile = scriptargfile

    def on_created(self, event):
        self.print_event(event)
        if type(event) is watchdog.events.DirCreatedEvent:
            # do something, call the script
            if self.scriptfile and self.scriptargfile:
                os.system("%s @%s".format(self.scriptfile, self.scriptargfile))
            pass
        return None

    def on_deleted(self, event):
        self.print_event(event)
        return None

    def print_event(self, event):
        print('\n--------------------------------------------------------------------------------')
        print('       event : %s' % event)
        print('        type : %s' % type(event))
        print('  event_type : %s' % event.event_type)
        print('is_directory : %s' % event.is_directory)
        print('    src_path : %s' % event.src_path)
        return None


def WatchDirUsingWatchDog(dirpath, recursive=False, externalscript=''):
    event_handler = my_handler(externalscript)
    observer = Observer()
    observer.schedule(event_handler, dirpath, recursive=False)
    observer.start()
    print('Watching started...')
    print('    Directory : %s' % dirpath)
    print('    Recursive : %s' % recursive)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    except:
        print("exception occurred!")
        print("exc_info: %s" % sys.exc_info)
        print("exc_type: %s" % sys.exc_type)

    observer.join()
    return None


def DirectoryPath(directoryPath):
    if directoryPath and os.path.isdir(directoryPath):
        return directoryPath
    raise "Invalid Directory Path!"


def main_watchdog():
    """Watch directory using watchdog package"""
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog="This script supports fromfile_prefix_chars (\'@\').\
                                      \nArguments that start with any of the specified characters\
                                      \nwill be treated as files, and will be replaced\
                                      \nby the arguments they contain.")

    parser.add_argument('-d', '--dirpath', type=DirectoryPath,
                        action='store', metavar='DIRECTORYPATH', dest='dirpath', required=True,
                        help='DirectoryPath (required)')
    parser.add_argument('-r', '--recursive', action='store_true', dest='recursive',
                        help='Watch sub-directories (recursive)')
    parser.add_argument('--script', '--extscript', type=file,
                        metavar='EXTERNALSCRIPT', dest='externalscript',
                        help='Run the ExternalScript on any change to the Directory/File')
    parser.add_argument('--scriptargsfile', type=file,
                        metavar='SCRIPTARGSFILE', dest='scriptargsfile',
                        help='file path that contains args to external script.')

    opts = parser.parse_args()

    WatchDirUsingWatchDog(opts.dirpath, opts.recursive, opts.externalscript)
    return None


class LoGoFileSystemWatcher:
    def __init__(self, pattern, interval=600, externalScript=None, extScriptWaitTime=600):
        self.pattern = pattern
        self.interval = interval
        self.externalScript = externalScript
        self.extScriptWaitTime = extScriptWaitTime

    def GetFilesAndDirectories(self):
        paths = []
        for filePath in glob.glob(self.pattern): paths.append(filePath)
        return paths

    def Sleep(self, waitTime):
        for i in xrange(waitTime, 0, -1):
            print('Wait %d seconds!' % i, end='\r')
            time.sleep(1)
        print('Sleep over!', end='\r')
        print(' ' * 80, end='\r')

    def startWatching(self):
        print('Watching started...')
        print('    Pattern : %s' % self.pattern)

        # Get the initial items
        files = self.GetFilesAndDirectories()

        while True:
            # Sleep interval seconds of time
            self.Sleep(self.interval)

            DebugInfo('Check for changes')
            newFiles = self.GetFilesAndDirectories()
            added, deleted = GetAddedAndDeletedItems(files, newFiles)

            # Print added and delete items
            if added: Print(added, 'Added Files/Folders')

            # Do not print deleted file, here I am not updating the deleted files
            # if deleted: Print(deleted, 'Deleted Files/Folders')

            if self.externalScript:
                for filePath in added:
                    files.append(filePath)
                    directoryName = os.path.basename(filePath)
                    command = '{0} --file \"{1}\"'.format(self.externalScript, filePath)
                    self.Sleep(self.extScriptWaitTime)
                    DebugInfo('Executing Command: %s' % command)
                    # os.system(command)
                    thread.start_new_thread(os.system, (command,))

            files = newFiles

        print(datetime.datetime.now())
        pass


def ValidFilePath(filePath):
    if filePath and os.path.isfile(filePath):
        return filePath
    raise "Invalid File Path!"

def main_normal():
    """
    This function monitors everything based on your search pattern
    """

    parser = argparse.ArgumentParser(fromfile_prefix_chars='@',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog="This script supports fromfile_prefix_chars (\'@\').\
                                     \nArguments that start with any of the specified characters\
                                     \nwill be treated as files, and will be replaced\
                                     \nby the arguments they contain.")

    parser.add_argument('-p', '--pattern', type=str,
                        action='store', metavar='PATTERN', dest='pattern', required=True,
                        help='DirectoryPath you can use wildcard chars (required)')
    parser.add_argument('-i', '--interval', type=int,
                        dest='interval', required=True, default=600,
                        help='Check for changes for every interval seconds of time. (default: 600 seconds)')
    parser.add_argument('--script', '--externalScript', type=str,
                        metavar='EXTERNALSCRIPT', dest='externalScript',
                        help='Run the ExternalScript on any change to the Directory/File')
    parser.add_argument('--scriptWaitTime', type=int, dest='scriptWaitTime', default=600,
                        help='Wait for <WaitTime> seconds before executing externalScript. (default: 600 seconds)')

    opts = parser.parse_args()
    DebugInfo('Options : %s' % opts)
    watcher = LoGoFileSystemWatcher(pattern=opts.pattern,
                                    interval=opts.interval,
                                    externalScript=opts.externalScript)
    watcher.startWatching()

    return None


def WatchDirectory_Test1():
    path = r'E:\LGTEMP'
    # path = r'\\In-disrv01\ConquerorsTeamSpace\Products\IMAGINE\14.0'
    # WatchDirUsingWatchDog(path)
    return None


def PrintInfo(info):
    print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), info))


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


class PrintItems:
    def __init__(self, numberOfItems):
        self.numberOfItems = numberOfItems
        self.fmt = ('%%%dd. %%s' % (int)(math.log10(self.numberOfItems) + 1))
        self.counter = 1

    def Print(self, str):
        print(self.fmt % (self.counter, str))
        self.counter += 1


def Print(iterable, headerInfo=None):
    if headerInfo:
        length = len(headerInfo)
        print(headerInfo)
        print('=' * length)
    if not iterable:
        print('Empty!')
        return None
    fmt = ('%%%dd. %%s' % len(str(len(iterable))))
    n = len(iterable)
    for i in xrange(0, n, 1):
        print(fmt % (i + 1, iterable[i]))
    return None

if __name__ == "__main__":
    # Print(os.listdir(r'E:\LGTEMP'), 'List of files/folders available')
    # Print([1, 2, 3])
    main_normal()
    # WatchDirectory_Test1()
    # main()
    print("\n=== END ===")
    sys.exit(0)
