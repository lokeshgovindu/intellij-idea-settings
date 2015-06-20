"""
This script looks for the methods available in .def and
and not defined in the source (.obj) files and print on stdout
"""
import sys
import os.path
import re
import dircache
from dircache import listdir
from ntpath import isfile, join
from subprocess import Popen, call
import _winreg as winreg

# =============================================================================

RegOpenKeyEx = winreg.OpenKeyEx
RegEnumKey = winreg.EnumKey
RegEnumValue = winreg.EnumValue
RegError = winreg.error
VS_BASE = r"Software\Microsoft\VisualStudio\%0.1f"

HKEYS = (winreg.HKEY_USERS, winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CLASSES_ROOT)

class Reg:
     """Helper class to read values from the registry
     """
 
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

def doit():
	batchFilePath = 'D:/Build/Generation_3/GetLatestSources_Preview.bat'
	#os.system( batchFilePath )
	call( batchFilePath )
	return None

def Test_1( defFilePath, interDirPath ):
	for f in listdir( interDirPath ):
		filePath = join( interDirPath, f )
		if ( '.obj' == os.path.splitext( filePath )[1] ):
			print filePath
	return None

def find_vcvarsall(version):
	"""Find the vcvarsall.bat file

	At first it tries to find the productdir of VS 2008 in the registry. If
	that fails it falls back to the VS90COMNTOOLS env var.
	"""
	vsbase = VS_BASE % version
	try:
		productdir = Reg.get_value(r"%s\Setup\VC" % vsbase,
								   "productdir")
	except KeyError:
		logger.debug("Unable to find productdir in registry")
		productdir = None

	if not productdir or not os.path.isdir(productdir):
		toolskey = "VS%0.f0COMNTOOLS" % version
		toolsdir = os.environ.get(toolskey, None)

		if toolsdir and os.path.isdir(toolsdir):
			productdir = os.path.join(toolsdir, os.pardir, os.pardir, "VC")
			productdir = os.path.abspath(productdir)
			if not os.path.isdir(productdir):
				logger.debug("%s is not a valid directory", productdir)
				return None
		else:
			logger.debug("env var %s is not set or invalid", toolskey)
	if not productdir:
		logger.debug("no productdir found")
		return None
	vcvarsall = os.path.join(productdir, "vcvarsall.bat")
	if os.path.isfile(vcvarsall):
		return vcvarsall
	logger.debug("unable to find vcvarsall.bat")
	return None

if __name__ == '__main__':
	print 'Task_2'

	defFilePath  = "E:/Build/Gen_3_64Bit/sources_rdo/elib/elib.def"
	interDirPath = "E:/Build/Gen_3_64Bit/arch/Win32Debug/obj/elib"

	print 'defFilePath = ' + defFilePath
	print 'interDirPath = ' + interDirPath

	#Test_1( defFilePath, interDirPath )
	#doit()
	os.system( '\"' + find_vcvarsall( 10 ) + '\"')
	os.system(  )
