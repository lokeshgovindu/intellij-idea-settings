import os
import sys
import argparse

class DirectoryCompare:
    def __init__(self, directoryPath1, directoryPath2, recursive=True):
        self.directoryPath1 = directoryPath1
        self.directoryPath2 = directoryPath2
        self.recursive = recursive
        pass

    def Start(self):
        self.fs1 = open('compare1.txt', 'w+t')
        self.fs2 = open('compare2.txt', 'w+t')
        ret = self.DirComp(self.directoryPath1, self.directoryPath2, self.recursive)
        self.fs1.close()
        self.fs2.close()
        return ret

    def DirComp(self, dir1, dir2, recursive):
        directoriesSet1 = set()
        directoriesSet2 = set()
        filesSet1 = set()
        filesSet2 = set()

        # Get the files and directories in directory1
        for fileName in os.listdir(dir1):
            filePath = os.path.join(dir1, fileName)
            if os.path.isdir(filePath):
                directoriesSet1.add(fileName)
            else:
                filesSet1.add(fileName)

        # Get the files and directories in directory2
        for fileName in os.listdir(dir2):
            filePath = os.path.join(dir2, fileName)
            if os.path.isdir(filePath):
                directoriesSet2.add(fileName)
            else:
                filesSet2.add(fileName)

        if filesSet1 != filesSet2:
            # print('Files are not equal in [%s], [%s], and they are [%s]' % (dir1, dir2, filesSet1 ^ filesSet2))
            filesIn1 = filesSet1.difference(filesSet2)
            if filesIn1:
                # self.fs1.write('%s\n' % filesIn1)
                for fileName in filesIn1:
                    self.fs1.write('[F] %s\n' % os.path.join(dir1, fileName))

            filesIn2 = filesSet2.difference(filesSet1)
            if filesIn2:
                # self.fs2.write('%s\n' % filesIn2)
                for fileName in filesIn2:
                    self.fs2.write('[F] %s\n' % os.path.join(dir2, fileName))

        if directoriesSet1 != directoriesSet2:
            # print('Directories are not equal in [%s], [%s] and they are [%s]' % (dir1, dir2, directoriesSet1 ^ directoriesSet2))
            dirsIn1 = directoriesSet1.difference(directoriesSet2)
            if dirsIn1:
                # self.fs1.write('%s\n' % dirsIn1)
                for directoryName in dirsIn1:
                    self.fs1.write('[D] %s\n' % os.path.join(dir1, directoryName))
            dirsIn2 = directoriesSet2.difference(directoriesSet1)
            if dirsIn2:
                # self.fs2.write('%s\n' % dirsIn2)
                for directoryName in dirsIn2:
                    self.fs1.write('[D] %s\n' % os.path.join(dir2, directoryName))

        self.fs1.flush()
        self.fs2.flush()

        for directoryName in directoriesSet1.intersection(directoriesSet2):
            path1 = os.path.join(dir1, directoryName)
            path2 = os.path.join(dir2, directoryName)
            self.DirComp(path1, path2, recursive)

        return True


def main():
    parser = argparse.ArgumentParser(description='Compare directories')
    parser.add_argument('--dir1', type=str, dest='dir1', required=True, help='First Directory Path')
    parser.add_argument('--dir2', type=str, dest='dir2', required=True, help='Second Directory Path')
    parser.add_argument('--recursive', type=bool, dest='recursive', default=True, help='Include sub-directories. (default: True)')
    options = parser.parse_args()
    print(' Begin '.center(80, '-'))
    print('Options = [%s]' % options)
    dir1 = options.dir1
    dir2 = options.dir2
    dirComp = DirectoryCompare(dir1, dir2, True)
    ret = dirComp.Start()
    print(' End '.center(80, '-'))
    return 0


if __name__ == '__main__':
    exitCode = main()
    sys.exit(exitCode)
    # print(os.listdir(r'E:\Build\IM_2014\root_14.00.0100.00395'))
