import os
import sys
import _winreg as winreg
import subprocess

HKEYS = ( winreg.HKEY_USERS, winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CLASSES_ROOT )
RegOpenKeyEx = winreg.OpenKeyEx
RegEnumKey = winreg.EnumKey
RegEnumValue = winreg.EnumValue
RegError = winreg.error

VS_BASE = r"Software\Microsoft\VisualStudio\%0.1f"


class Reg:
    """Helper class to read values from the registry"""

    def get_value(cls, path, key):
        for base in HKEYS:
            d = cls.read_values(base, path)
            if d and key in d:
                return d[key]
        raise KeyError(key)

    get_value = classmethod(get_value)

    def read_keys(cls, base, key):
        """Return list of registry keys."""
        try:
            handle = RegOpenKeyEx(base, key)
        except RegError:
            return None
        L = []
        i = 0
        while True:
            try:
                k = RegEnumKey(handle, i)
            except RegError:
                break
            L.append(k)
            i += 1
        return L

    read_keys = classmethod(read_keys)

    def read_values(cls, base, key):
        """Return dict of registry keys and values.

        All names are converted to lowercase.
        """
        try:
            handle = RegOpenKeyEx(base, key)
        except RegError:
            return None
        d = {}
        i = 0
        while True:
            try:
                name, value, type = RegEnumValue(handle, i)
            except RegError:
                break
            name = name.lower()
            d[cls.convert_mbcs(name)] = cls.convert_mbcs(value)
            i += 1
        return d

    read_values = classmethod(read_values)

    def convert_mbcs(s):
        dec = getattr(s, "decode", None)
        if dec is not None:
            try:
                s = dec("mbcs")
            except UnicodeError:
                pass
        return s

    convert_mbcs = staticmethod(convert_mbcs)


def removeDuplicates(variable):
    """Remove duplicate values of an environment variable."""
    oldList = variable.split(os.pathsep)
    newList = []
    for i in oldList:
        if i not in newList:
            newList.append(i)
    newVariable = os.pathsep.join(newList)
    return newVariable


def find_vcvarsall(version=10):
    """
    Find the vcvarsall.bat file
    At first it tries to find the productdir of VS 20XX in the registry. If
    that fails it falls back to the VSXXXCOMNTOOLS env var.
    """
    vsbase = VS_BASE % version
    try:
        productdir = Reg.get_value(r"%s\Setup\VC" % vsbase, "productdir")
    except KeyError:
        productdir = None

    if not productdir or not os.path.isdir(productdir):
        toolskey = "VS%0.f0COMNTOOLS" % version
        toolsdir = os.environ.get(toolskey, None)

        if toolsdir and os.path.isdir(toolsdir):
            productdir = os.path.join(toolsdir, os.pardir, os.pardir, "VC")
            productdir = os.path.abspath(productdir)
            if not os.path.isdir(productdir):
                return None
        else:
            print "env var %s is not set or invalid" % toolskey

    if not productdir:
        print "no productdir found"
        return None

    vcvarsall = os.path.join(productdir, "vcvarsall.bat")

    if os.path.isfile(vcvarsall):
        return vcvarsall

    print "unable to find vcvarsall.bat"

    return None


def query_vcvarsall(version, arch="x86"):
    """Launch vcvarsall.bat and read the settings from its environment"""
    vcvarsall = find_vcvarsall(version)
    interesting = set(( "include", "lib", "libpath", "path" ))
    result = {}

    if vcvarsall is None:
        # raise PackagingPlatformError("Unable to find vcvarsall.bat")
        raise Exception("Unable to find vcvarsall.bat")
    print('Calling [%s] ...' % vcvarsall)
    popen = subprocess.Popen('"%s" %s & set' % (vcvarsall, arch), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = popen.communicate()
    if popen.wait() != 0:
        # raise PackagingPlatformError(stderr.decode("mbcs"))
        raise Exception(stderr.decode("mbcs"))

    stdout = stdout.decode("mbcs")
    for line in stdout.split("\n"):
        line = Reg.convert_mbcs(line)
        if '=' not in line:
            continue
        line = line.strip()
        key, value = line.split('=', 1)
        key = key.lower()
        if key in interesting:
            if value.endswith(os.pathsep):
                value = value[:-1]
            result[key] = removeDuplicates(value)

    if len(result) != len(interesting):
        raise ValueError(str(list(result)))

    return result


def main():
    vc_env = query_vcvarsall(12)
    os.environ['path'] = vc_env['path']
    os.system('cs')
    return 0


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    print(info.center(79, '-'))
    exitCode = main()
    print('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    print(info.center(79, '-'))
    sys.exit(exitCode)
