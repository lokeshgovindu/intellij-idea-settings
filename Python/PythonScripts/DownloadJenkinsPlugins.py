import os
import sys
import urllib


def DownloadFile():
    urlPaths = [
        "http://updates.jenkins-ci.org/download/plugins/antisamy-markup-formatter/1.3/antisamy-markup-formatter.hpi",
        "http://updates.jenkins-ci.org/download/plugins/git-client/1.12.0/git-client.hpi",
        "http://updates.jenkins-ci.org/download/plugins/git/2.3.1/git.hpi",
        "http://updates.jenkins-ci.org/download/plugins/jobConfigHistory/2.10/jobConfigHistory.hpi",
        "http://updates.jenkins-ci.org/download/plugins/external-monitor-job/1.4/external-monitor-job.hpi",
        "http://updates.jenkins-ci.org/download/plugins/translation/1.12/translation.hpi",
        "http://updates.jenkins-ci.org/download/plugins/perforce/1.3.29/perforce.hpi",
        "http://updates.jenkins-ci.org/download/plugins/ldap/1.11/ldap.hpi",
        "http://updates.jenkins-ci.org/download/plugins/junit/1.2/junit.hpi",
        "http://updates.jenkins-ci.org/download/plugins/cvs/2.12/cvs.hpi",
        "http://updates.jenkins-ci.org/download/plugins/script-security/1.10/script-security.hpi",
        "http://updates.jenkins-ci.org/download/plugins/email-ext/2.39/email-ext.hpi",
        "http://updates.jenkins-ci.org/download/plugins/ivytrigger/0.33/ivytrigger.hpi",
        "http://updates.jenkins-ci.org/download/plugins/matrix-auth/1.2/matrix-auth.hpi",
        "http://updates.jenkins-ci.org/download/plugins/mailer/1.12/mailer.hpi",
        "http://updates.jenkins-ci.org/download/plugins/build-flow-plugin/0.17/build-flow-plugin.hpi",
        "http://updates.jenkins-ci.org/download/plugins/active-directory/1.39/active-directory.hpi",
        "http://updates.jenkins-ci.org/download/plugins/mapdb-api/1.0.6.0/mapdb-api.hpi",
        "http://updates.jenkins-ci.org/download/plugins/subversion/2.4.5/subversion.hpi",
        "http://updates.jenkins-ci.org/download/plugins/pam-auth/1.2/pam-auth.hpi",
        "http://updates.jenkins-ci.org/download/plugins/maven-plugin/2.8/maven-plugin.hpi",
        "http://updates.jenkins-ci.org/download/plugins/javadoc/1.3/javadoc.hpi",
        "http://updates.jenkins-ci.org/download/plugins/git-client/1.12.0/git-client.hpi",
    ]

    outDir = r'D:\Softwares\Jenkins\Plugins'
    prevDir = os.curdir
    os.chdir(outDir)
    for urlPath in urlPaths:
        vs = urlPath.split('/')
        fileName, fileExt = os.path.splitext(vs[-1])
        fileNameWithVersion = fileName + '_' + vs[-2] + fileExt
        outFilePath = os.path.join(outDir, fileNameWithVersion)
        print('Downloading [%s] to [%s]' % (fileNameWithVersion, outFilePath))
        urllib.urlretrieve(urlPath, fileNameWithVersion)
        urllib.urlcleanup()

    os.chdir(prevDir)
    return 0


def main():
    DownloadFile()
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
