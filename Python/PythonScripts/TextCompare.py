import os
import sys

def TextCompare(source, target):
    sourcefp = open(source, 'r')
    targetfp = open(target, 'r')
    lineNum = 0
    filesAreEqual = True
    while sourcefp:
        lineNum += 1
        sourceLine = sourcefp.readline().rstrip('\n')
        targetLine = targetfp.readline().rstrip('\n')
        if not sourceLine or not targetLine:
            break

        if sourceLine != targetLine:
            print('Line : %s' % lineNum)
            col = 0
            lineLen = len(sourceLine)
            for i in xrange(lineLen):
                if sourceLine[i] != targetLine[i]:
                    print('Col : %s' % i)
                    print(sourceLine[i:])
                    print(targetLine[i:])
                    filesAreEqual = False
                    break

            print('SourceLine: [%s]' % sourceLine)
            print('TargetLine: [%s]' % targetLine)
            break
    print('Number of lines processed : %s' % lineNum)
    sourcefp.close()
    targetfp.close()
    return filesAreEqual

def main():
    source = r'F:\Data\Del\63_7385_nodata.ecw.EcwMask.txt'
    target = r'F:\Data\Del\63_7385_iv0.ecw.EcwMask.txt'
    print(os.path.getsize(source))
    # target = r'F:\Data\Del\63_7385.ecw.EcwMask.txt'
    equal = TextCompare(source, target)
    if equal:
        print('Files are equal.')
    else:
        print('Files are NOT equal.')
    return 0 if equal == True else 1


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    print(info.center(80, '-'))
    exitCode = main()
    print('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    print(info.center(80, '-'))
    sys.exit(exitCode)
