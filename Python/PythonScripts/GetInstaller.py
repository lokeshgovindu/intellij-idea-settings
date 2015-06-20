import sys
import os
import argparse
import datetime
import SendMail
import CommonUtils
import parse

PrintInfo               = CommonUtils.PrintInfo
RunSystemCommand        = CommonUtils.RunSystemCommand

__PRODUCTNAME__         = 'DesktopIDKs'
__PRODUCTVERSION__      = 'Mainline'
# __MFT__                 = 'DesktopIDKs'
# __MLABEL__              = '{0}_{1}'.format(__PRODUCTNAME__, __PRODUCTVERSION__)

__TARGETDIRECTORY__     = r'\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\Products\IDKs\{1}\{0}'.format(__PRODUCTNAME__, __PRODUCTVERSION__)
__TARGETBACKUP__        = r'\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\Products\IDKs\{1}\{0}_Backup'.format(__PRODUCTNAME__, __PRODUCTVERSION__)
__RECEPIENTS__          = 'schallag@intergraph.com;lgovindu@intergraph.com;svvankad@intergraph.com;gpeddoll@intergraph.com;ssamayam@intergraph.com'

# These are for my testing
__TARGETDIRECTORY__     = r'E:\TEMP\IDKs\{1}\{0}'.format(__PRODUCTNAME__, __PRODUCTVERSION__)
__TARGETBACKUP__        = r'E:\TEMP\IDKs\{1}\{0}_Backup'.format(__PRODUCTNAME__, __PRODUCTVERSION__)
__RECEPIENTS__          = 'lgovindu@intergraph.com'

__KEEP_LAST_N_BUILDS__  = 15


def Write_Product_LatestInstall_CmdFile(isoFilePath, productName):
    fileName = os.path.basename(isoFilePath)
    parentDirPath = os.path.dirname(os.path.dirname(isoFilePath))
    config = CommonUtils.GetConfig(fileName)
    if config:
        cmdFilePath = os.path.join(parentDirPath, '%s_%s_LatestInstall.cmd' % (productName, config))
    else:
        cmdFilePath = os.path.join(parentDirPath, '%s_LatestInstall.cmd' % productName)
    PrintInfo('CMD File : [%s]' % cmdFilePath)
    fp = open(cmdFilePath, 'w')
    fp.write('\"%s\"' % isoFilePath)
    fp.close()


def main():
    parser = argparse.ArgumentParser(
        description="Get ERDAS Installers",
        fromfile_prefix_chars='@',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
This script supports fromfile_prefix_chars (\'@\').
Arguments that start with any of the specified characters will be treated as
files, and will be replaced by the arguments they contain.


--file / --file-path
--------------------
Path file/folder you want to download.
Ex: '\\atltruck\Products\IDKs\Mainline\DesktopIDKs\DesktopIDKs_2014-11-22_0346_b2638'
    '\\atltruck\Products\IMAGINE\15.0\IMAGINE_2014-11-18_1717_b212\IMAGINE x64.iso'
    '\\atltruck\Products\IMAGINE\15.0\Updates\IMAGINE_2014-11-16_0822_b207_from_b200\IMAGINE x86 Patch.iso'
    '\\atltruck\AT\15\Candidates\IMAGINE\RC7\ISOs\IMAGINE-RC7.iso'
Based on the file path, you need to specify the respective correct values for --file-path-format, --source-directory,
and --target-directory.


--file-path-format
------------------
File path format to parse and get {productname}, {version} & {build} fields.
If file path is '\\atltruck\Products\IDKs\Mainline\DesktopIDKs\DesktopIDKs_2014-11-22_0346_b2638' then
you need to use '\\atltruck\Products\IDKs\{version}\{productname}\{build}'. Parse module can parse the string
using specified format pattern. And you wil get the following:

  productname : DesktopIDKs
      version : Mainline
        build : DesktopIDKs_2014-11-22_0346_b2638


--source-directory
------------------
Source directory path, where you are looking for builds/installers/anything.
Ex: \\atltruck\Products\IDKs\Mainline\DesktopIDKs


--target-directory
------------------
Target directory path of builds/installers that you are copying to.
Ex: \\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\Products\IDKs\Mainline\DesktopIDKs
Please do NOT forget, we are maintaining the same folder structure of source in target directory.
"""
    )

    parser.add_argument('-u', '--username', type=str, dest='username', default='ftpuser',
                        help='FTP UserName (required)')
    parser.add_argument('-p', '--password', type=str, dest='password', default='kroNos!2013!',
                        help='FTP Password (required)')
    parser.add_argument('-f', '--file', '--file-path', type=str, dest='filePath', required=True,
                        help='ERDAS installer/any file/folder path')
    parser.add_argument('--file-path-format', type=str, dest='filePathFormat', required=True,
                        help='File path format to parse and get {productname}, {version} & {build} fields.')
    parser.add_argument('--source-directory', type=str, dest='sourceDirectory', required=True,
                        help='Source directory path of builds/installers.')
    parser.add_argument('--target-directory', type=str, dest='targetDirectory', required=True,
                        help='Target directory path of builds/installers.')

    opts = parser.parse_args()
    PrintInfo(opts)

    cwd = os.getcwd()

    uncPath = opts.filePath
    uncPathFormat = opts.filePathFormat

    fileName = os.path.basename(uncPath)
    config = CommonUtils.GetConfig(fileName)
    PrintInfo('Config = [%s]' % config)

    print(uncPath, uncPathFormat)
    productname, version, build = CommonUtils.GetProductNameVersionBuild(uncPathFormat, uncPath)
    # build = os.path.basename(uncPath)
    PrintInfo('ProductName = [%s]' % productname)
    PrintInfo('Version = [%s]' % version)
    PrintInfo('Build = [%s]' % build)
    return 0


    ftpPath = CommonUtils.ConvertToFTP(uncPath)
    PrintInfo('ftpPath = [%s]' % ftpPath)

    targetDirectory = os.path.join(cwd, build + config)
    if not os.path.exists(targetDirectory): os.mkdir(targetDirectory)
    PrintInfo('targetDirectory = [%s]' % targetDirectory)

    PrintInfo('CWD = [%s]' % os.getcwd())
    targetShareDir = os.path.join(__TARGETDIRECTORY__, build)
    PrintInfo('targetShareDir = [%s]' % targetShareDir)

    started = datetime.datetime.now()
    PrintInfo('Started : [%s]' % started)

    sourceDirectory = uncPath
    PrintInfo('SourceDirectory = [%s]' % sourceDirectory)
    PrintInfo('TargetDirectory = [%s]' % targetDirectory)

    # ------------------------------------------------------------------------------
    # Get file using NcFTPGet
    # ------------------------------------------------------------------------------
    while True:
        exitCode = CommonUtils.GetDirectory(opts.username, opts.password, ftpPath, targetDirectory)
        PrintInfo('ExitCode = %d' % exitCode)
        if exitCode == 0:
            break

    ended = datetime.datetime.now()
    PrintInfo('Ended : [%s]' % ended)

    timeTaken = (ended - started)
    PrintInfo("timeTaken = [%s]" % timeTaken)

    # ------------------------------------------------------------------------------
    # Copy the Installer to TargetDirectory
    # ------------------------------------------------------------------------------
    if not os.path.exists(targetShareDir):
        PrintInfo('Creating target directory: [%s]' % targetShareDir)
        RunSystemCommand('mkdir {}'.format(targetShareDir))
    PrintInfo('Copying [%s] installer, [%s] -> [%s]' % (productname, fileName, targetShareDir))
    tSrcDir = os.path.join(targetDirectory, fileName)
    tDstDir = targetShareDir
    CommonUtils.CopyDirectoryUsingRobocopy(tSrcDir, tDstDir)

    # ------------------------------------------------------------------------------
    # Write/Update Product LatestInstall Command
    # ------------------------------------------------------------------------------
    targetIsoPath = os.path.join(targetShareDir, fileName)
    Write_Product_LatestInstall_CmdFile(targetIsoPath, productname)

    # ------------------------------------------------------------------------------
    # Send mail
    # ------------------------------------------------------------------------------
    PrintInfo('Sending Mail ...')
    htmlText = CommonUtils.GetHtmlMailText(source=uncPath, target=targetShareDir, elapsed=timeTaken)
    SendMail.SendHtmlMail(
        fromMailText=productname,
        to=__RECEPIENTS__.split(';'),
        subject=build + ' ' + config,
        msgText=htmlText,
        label='{0}_{1}'.format(productname, version)
    )

    # ------------------------------------------------------------------------------
    # Remove temp files/directories
    # ------------------------------------------------------------------------------
    os.chdir(cwd)
    PrintInfo('Removing targetDirectory: [%s]' % targetDirectory)
    RunSystemCommand('rmdir /S /Q {}'.format(targetDirectory))

    # ------------------------------------------------------------------------------
    # Backup IDKIncludedBGs.txt files for DesktopIDKs
    # ------------------------------------------------------------------------------
    PrintInfo('Backup IDKIncludedBGs.txt files')
    backupIDKIncludedBGsCmd = 'robocopy \"{0}\" \"{1}\" IDKIncludedBGs.txt /S /E /NP /NS /NC /NDL /NJH /NJS'.format(__TARGETDIRECTORY__, __TARGETBACKUP__)
    PrintInfo('Executing backupIDKIncludedBGsCmd = [%s]' % backupIDKIncludedBGsCmd)
    RunSystemCommand(backupIDKIncludedBGsCmd)
    
    # ------------------------------------------------------------------------------
    # Clean up products folder
    # ------------------------------------------------------------------------------
    cleanupCmd = 'python CleanupERDASProducts.py --directory \"{}\" --keep {}'.format(__TARGETDIRECTORY__, __KEEP_LAST_N_BUILDS__)
    PrintInfo('Cleanup directory [%s]' % __TARGETDIRECTORY__)
    RunSystemCommand(cleanupCmd)

    return 0


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    PrintInfo(info.center(79, '-'))
    exitCode = main()
    PrintInfo('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    PrintInfo(info.center(79, '-'))
    sys.exit(exitCode)
