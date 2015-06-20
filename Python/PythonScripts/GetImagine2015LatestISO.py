import sys
import os
import argparse
import datetime
import CommonUtils
PrintInfo = CommonUtils.PrintInfo

__PRODUCTNAME__     = 'IMAGINE'
__PRODUCTVERSION__  = '15.0'
__MFT__             = 'ERDAS IMAGINE'
__MLABEL__          = 'IMAGINE 2015'

# These are for my testing
__RECEPIENTS__      = 'lgovindu@intergraph.com'
# __RECEPIENTS__      = 'smajety@intergraph.com;schallag@intergraph.com;lgovindu@intergraph.com;svvankad@intergraph.com;gpeddoll@intergraph.com;nrkolli@intergraph.com;mkshivak@intergraph.com;pkvalipi@intergraph.com;ssamayam@intergraph.com;lpkota@intergraph.com;vpperepa@intergraph.com'

__KEEP_LAST_N_BUILDS__ = 45


def main():
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-un', '--username', type=str,
                        action='store', metavar='USERNAME', dest='username', default='ftpuser',
                        help='FTP UserName (required)')
    parser.add_argument('-pw', '--password', type=str,
                        action='store', metavar='PASSWORD', dest='password', default='kroNos!2013!',
                        help='FTP Password (required)')
    parser.add_argument('-s', '--source', '--source-directory', type=CommonUtils.ValidDirectory, dest='source_directory', required=True,
                        help='Source Directory')
    parser.add_argument('-t', '--target', '--target-directory', type=CommonUtils.ValidDirectory, dest='target_directory', required=True,
                        help='Target Directory')
    parser.add_argument('-p', '--pattern', dest='pattern', type=str, required=True,
                        help='Pattern that you are looking for.\n'
                             'Examples:\n'
                             '"*" : All files and directories\n'
                             '"*/*.iso" : All .iso files in the top level directories.')

    opts = parser.parse_args()
    PrintInfo(opts)

    sourceDirectory = opts.source_directory
    targetDirectory = opts.target_directory
    pattern = opts.pattern
    cwd = os.getcwd()

    itemsList = CommonUtils.GetNewItemsList(sourceDirectory, targetDirectory, pattern)
    CommonUtils.PrintIterable(itemsList, title='NewItems', indent='\t')

    # Simply exit if there are no new items.
    if not itemsList:
        return 0

    # Some new items are available.
    # Fetch the least latest item, by default list is already sorted by its name.
    uncPath = itemsList[0]

    fileName = os.path.basename(uncPath)
    config = CommonUtils.GetConfig(fileName)
    build = os.path.basename(os.path.dirname(uncPath))

    ftpPath = CommonUtils.ConvertToFTP(uncPath)
    localTargetDirectory = os.path.join(cwd, build + config)
    if not os.path.exists(localTargetDirectory): os.mkdir(localTargetDirectory)
    PrintInfo('LocalTargetDirectory  = [%s]' % localTargetDirectory)
    # os.chdir(targetDirectory)

    PrintInfo('CWD = [%s]' % os.getcwd())
    targetShareDir = os.path.join(targetDirectory, build)

    started = datetime.datetime.now()
    PrintInfo('Started : [%s]' % started)

    # ------------------------------------------------------------------------------
    # Get file using NcFTPGet
    # ------------------------------------------------------------------------------
    while True:
        exitCode = CommonUtils.GetFile(opts.username, opts.password, ftpPath, localTargetDirectory)
        PrintInfo('ExitCode = %d' % exitCode)
        if exitCode == 0: break

    ended = datetime.datetime.now()
    PrintInfo('Ended : [%s]' % ended)

    timeTaken = ( ended - started )
    PrintInfo("timeTaken = [%s]" % timeTaken)

    # ------------------------------------------------------------------------------
    # Copy the ISO image to TargetDirectory
    # ------------------------------------------------------------------------------
    if not os.path.exists(targetShareDir):
        PrintInfo('Creating target directory: [%s]' % targetShareDir)
        CommonUtils.RunSystemCommand('mkdir {}'.format(targetShareDir))
    PrintInfo('Copying [%s] installer from [%s] -> [%s]' % (__PRODUCTNAME__, fileName, targetShareDir))
    # shutil.copy(fileName, targetShareDir)
    CommonUtils.CopyFileUsingRobocopy(localTargetDirectory, targetShareDir, fileName)

    # ------------------------------------------------------------------------------
    # Write/Update Product LatestInstall Command
    # ------------------------------------------------------------------------------
    targetIsoPath = os.path.join(targetShareDir, fileName)
    Write_Product_LatestInstall_CmdFile(targetIsoPath)

    # ------------------------------------------------------------------------------
    # send mail
    # ------------------------------------------------------------------------------
    body = 'Available at {}, TimeTaken : {}'.format(targetShareDir, timeTaken)
    sendMailCmd = 'python SendMail.py --mft "{}" -r {} --sub "{} {}" --text "{}" --label "{}"'.format(
        __MFT__, __RECEPIENTS__, build, config, body, __MLABEL__
    )
    PrintInfo('SendMail Command : [%s]' % sendMailCmd)
    CommonUtils.RunSystemCommand(sendMailCmd)

    # ------------------------------------------------------------------------------
    # Remove temp files/directories
    # ------------------------------------------------------------------------------
    os.chdir(cwd)
    PrintInfo('Removing targetDirectory: [%s]' % localTargetDirectory)
    removeCmd = 'rmdir /S /Q {}'.format(CommonUtils.GetDoubleQuotedString(localTargetDirectory))
    PrintInfo('Executing RemoveCmd = [%s]' % removeCmd)
    CommonUtils.RunSystemCommand(removeCmd)

    # ------------------------------------------------------------------------------
    # Clean up products folder
    # ------------------------------------------------------------------------------
    cleanupCmd = 'python CleanupERDASProducts.py --directory \"{}\" --keep {}'.format(targetDirectory, __KEEP_LAST_N_BUILDS__)
    PrintInfo('Cleanup directory [%s]' % targetDirectory)
    CommonUtils.RunSystemCommand(cleanupCmd)

    return 0


def Write_Product_LatestInstall_CmdFile(isoFilePath):
    fileName = os.path.basename(isoFilePath)
    parentDirPath = os.path.dirname(os.path.dirname(isoFilePath))
    config = CommonUtils.GetConfig(fileName)
    if config:
        cmdFilePath = os.path.join(parentDirPath, '%s_%s_LatestInstall.cmd' % (__PRODUCTNAME__, config))
    else:
        cmdFilePath = os.path.join(parentDirPath, '%s_LatestInstall.cmd' % __PRODUCTNAME__)
    PrintInfo('CMD File : [%s]' % cmdFilePath)
    fp = open(cmdFilePath, 'w')
    fp.write('\"%s\"' % isoFilePath)
    fp.close()
    

if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    PrintInfo(info.center(80, '-'))
    exitCode = main()
    PrintInfo('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    PrintInfo(info.center(80, '-'))
    sys.exit(exitCode)
    