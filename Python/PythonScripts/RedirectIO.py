import os, sys


class RedirectStdStreams(object):
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush()
        self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush();
        self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr


if __name__ == '__main__':
    # devnull = open(os.devnull, 'w')
    redirectedfile = r'E:/LGTEMP/redirectio.txt'
    devnull = open(redirectedfile, 'w')
    print('Fubar')

    with RedirectStdStreams(stdout=devnull, stderr=devnull):
        for i in xrange(1, 1000, 1):
            print(i)
        print("You'll never see me")

    print("I'm back!")

    print(file(redirectedfile).readlines())
