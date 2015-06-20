'''
Visual Studio 2010 VC++ Project File Utils
'''

from dircache import listdir
from ntpath import join
import _winreg as winreg
import math
import os
import re
import subprocess
import sys
import xml.dom.minidom

#===============================================================================

HKEYS = ( winreg.HKEY_USERS, winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CLASSES_ROOT )

RegOpenKeyEx = winreg.OpenKeyEx
RegEnumKey = winreg.EnumKey
RegEnumValue = winreg.EnumValue
RegError = winreg.error

REParseCondition = re.compile(r"^[^=]*==[^']*'([^\|]*)\|([^']*)'[ ]*$")
REParseCondition_ConfigurationNameGroup = 1
REParseCondition_PlatformNameGroup = 2

VS_BASE = r"Software\Microsoft\VisualStudio\%0.1f"

REProjectPath = re.compile('^Project.* = ' + # Project GUID
                           '\".*\"' + ", " + # Project Name
                           '\".*.vcxproj.*\"' + ", " + # Project Path
                           '.*' + '$', # Rem
                           re.IGNORECASE)


class Reg:
    """Helper class to read values from the registry"""

    def get_value( cls, path, key ):
        for base in HKEYS:
            d = cls.read_values(base, path)
            if d and key in d:
                return d[key]
        raise KeyError(key)

    get_value = classmethod(get_value)

    def read_keys( cls, base, key ):
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

    def read_values( cls, base, key ):
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

    def convert_mbcs( s ):
        dec = getattr(s, "decode", None)
        if dec is not None:
            try:
                s = dec("mbcs")
            except UnicodeError:
                pass
        return s

    convert_mbcs = staticmethod(convert_mbcs)

def addCygwinToPath():
    if os.system("nm"):
        try:
            cygwinInstallDir = Reg.get_value(r"SOFTWARE\Cygwin\setup", "rootdir")
            cygwinBinPath = os.path.join(cygwinInstallDir, 'bin')
        except KeyError:
            return False

        print 'cygwinBinPath = %s' % cygwinBinPath
        os.environ['path'] = os.environ['path'] + ';' + cygwinBinPath
    return True

def getMSBuildProjType( msbuildProj ):
    # Somewhat crude way of differentiating an MSBuild CSProj from a VCProj
    for config in msbuildProj.getElementsByTagName("PropertyGroup"):
        anNodes = config.getElementsByTagName("AssemblyName")
        if ( anNodes == None or anNodes.length == 0 ):
            continue

        return "CSProj"

    return "VCXProj"

def getMSBuildProjConfigs( msbuildProj ):
    configs = []
    for config in msbuildProj.getElementsByTagName("PropertyGroup"):
        conditionValue = config.getAttribute("Condition")
        if ( conditionValue == "" ):
            continue
        mtch = REParseCondition.match(conditionValue)

        # This seems odd...let it go for now
        if ( mtch == None ):
            continue

        configs.append(mtch.group(REParseCondition_ConfigurationNameGroup) \
                       + "|" + mtch.group(REParseCondition_PlatformNameGroup))

    return configs

def getVCProjConfigs( vcProj ):
    configs = []
    for config in vcProj.getElementsByTagName("Configuration"):
        configs.append(config.getAttribute("Name"))

    print configs
    return configs

def getProjTypeProjAndCurrentConfigs( projFileDom ):
    vsProjs = projFileDom.getElementsByTagName("VisualStudioProject")
    if ( vsProjs ):
        projType = "VCProj"
        configs = getVCProjConfigs(vsProjs[0])
    else:
        vsProjs = projFileDom.getElementsByTagName("Project")
        if ( vsProjs ):
            projType = getMSBuildProjType(vsProjs[0])
            configs = getMSBuildProjConfigs(vsProjs[0])
        else:
            return None

    return ( projType, vsProjs[0], configs )

def getProjectNameFromVCProjFileDom( projFileDom, projectFilePath ):
    projectName = None
    for projName in projFileDom.getElementsByTagName("ProjectName"):
        projectName = projName.childNodes[0].data

    if ( projectName == None ):
    #		print "ProjectName is not available in .vcxproj file"
        projectName = os.path.splitext(os.path.basename(projectFilePath))[0]

    return projectName

def getModuleDefFilePath_1( projFileDom, projectFilePath, configuration='Release|Win32' ):
    projectDirPath = os.path.dirname(projectFilePath)
    for itemDefGroup in projFileDom.getElementsByTagName("ItemDefinitionGroup"):
        conditionValue = itemDefGroup.getAttribute("Condition")
        if ( conditionValue == "" ):
            continue
        mtch = REParseCondition.match(conditionValue)

        # This seems odd...let it go for now
        if ( mtch == None ):
            continue

        configName = mtch.group(REParseCondition_ConfigurationNameGroup) \
                     + "|" + mtch.group(REParseCondition_PlatformNameGroup)

        if ( configName != configuration ): continue

        link = itemDefGroup.getElementsByTagName('ModuleDefinitionFile')

        moduleDefFile = link[0].childNodes[0].data

        if ( not os.path.isabs(moduleDefFile) ):
            moduleDefAbsPath = os.path.join(projectDirPath, moduleDefFile)
            if ( not os.path.exists(moduleDefAbsPath) ):
                return None

    return os.path.abspath(moduleDefAbsPath)

def getModuleDefFilePath( projectFilePath, configuration='Release|Win32' ):
    if not os.path.exists(projectFilePath):
        return projectFilePath + ': File Not Found!'

    projectDirPath = os.path.dirname(projectFilePath)
    moduleDefAbsPath = None

    try:
        projFileDom = xml.dom.minidom.parse(projectFilePath)

        for itemDefGroup in projFileDom.getElementsByTagName("ItemDefinitionGroup"):
            conditionValue = itemDefGroup.getAttribute("Condition")
            if ( conditionValue == "" ):
                continue
            mtch = REParseCondition.match(conditionValue)

            # This seems odd...let it go for now
            if ( mtch == None ): continue

            configName = mtch.group(REParseCondition_ConfigurationNameGroup) \
                         + "|" + mtch.group(REParseCondition_PlatformNameGroup)

            if ( configName != configuration ): continue

            link = itemDefGroup.getElementsByTagName('ModuleDefinitionFile')

            moduleDefFile = link[0].childNodes[0].data

            if ( not os.path.isabs(moduleDefFile) ):
                moduleDefAbsPath = os.path.join(projectDirPath, moduleDefFile)
                if ( not os.path.exists(moduleDefAbsPath) ):
                    projFileDom.unlink()
                    return None

        projFileDom.unlink()

    except:
    #		return 'Exception : ' + projectFilePath
        return None

    if moduleDefAbsPath == None: return None
    return os.path.abspath(moduleDefAbsPath)

def getProjectIntDir( projFileDom, projectFilePath ):
    projectFileDirPath = re.sub(r'\\', r'/', os.path.dirname(projectFilePath))

    for IntDir in projFileDom.getElementsByTagName('IntDir'):
    #		print propertyGroup
        conditionValue = IntDir.getAttribute("Condition")
        if ( conditionValue == "" ):
            continue
        mtch = REParseCondition.match(conditionValue)

        # This seems odd...let it go for now
        if ( mtch == None ):
            continue

        configName = mtch.group(REParseCondition_ConfigurationNameGroup) \
                     + "|" + mtch.group(REParseCondition_PlatformNameGroup)

        if ( "Release|Win32" != configName ):
            continue

        IntDirPath = IntDir.childNodes[0].data

        if ( IntDirPath.find("$(Platform)$(Configuration)") >= 0 ):
            IntDirPath = IntDirPath.replace("$(Platform)$(Configuration)", "Win32Release")

        if ( IntDirPath.find("$(ProjectName") >= 0 ):
            projectName = getProjectNameFromVCProjFileDom(projFileDom, projectFilePath)
            IntDirPath = IntDirPath.replace("$(ProjectName)", projectName)

        if ( not os.path.isabs(IntDirPath) ):
            IntDirAbsPath = os.path.join(projectFileDirPath, IntDirPath)
            if ( not os.path.exists(IntDirAbsPath) ):
                return IntDirAbsPath + ": Directory Not Found!"

    return os.path.abspath(IntDirAbsPath)

def functionsNotInModule( defFilePath, interDirPath, functions ):
    writeNewDef = True

    if not os.path.exists(defFilePath):
        return defFilePath + ": File Not Found!"

    if not os.path.exists(interDirPath):
        return interDirPath + ": Intermediate Direcotry Path Not found!"

    if ( writeNewDef ):
        part1, part2 = os.path.splitext(defFilePath)
        newDefFilePath = part1 + "New" + part2
        newDefFile = file(newDefFilePath, 'w')

    functionsInDefFile = []
    skipLines = True    # Skip lines until we get EXPORTS
    for line in file(defFilePath):
        if skipLines:
            if ( writeNewDef ):
                newDefFile.write(line)
            line = line.strip()
            if line.lower() == 'exports':
                skipLines = False
            continue
        line = line.strip()
        if ( line != "" ):
            functionsInDefFile.append(line)


            #	print "#functions in def file : %i" % len( functionsInDefFile )

            #	fpObjs = open( 'D:/LGTEMP/functionsInObjs.txt', 'w' )

    objectFiles = []
    for f in listdir(interDirPath):
        filePath = join(interDirPath, f)
        if ( ".obj" == os.path.splitext(filePath)[1] ):
            objectFiles.append(filePath)

    objectFilesCount = len(objectFiles)
    digitsCount = math.log10(objectFilesCount) + 1
    fmt = "Processing ( %%%dd / %d ) : %%s" % ( digitsCount, objectFilesCount )

    for i in xrange(0, objectFilesCount, 1):
        filePath = objectFiles[i]
        print fmt % ( i + 1, filePath )
        #		print "==============================================================================="

        #		fpObjs.write( "Exported functions in : " + filePath + "\n" )
        #		fpObjs.write( "===============================================================================\n" )
        popen = subprocess.Popen('nm -g -C %s' % ( filePath ),
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)

        stdout, stderr = popen.communicate()
        if popen.wait() != 0:
            raise Exception(str(stderr))

        for line in stdout.split('\n'):
            l = line.split()
            if len(l) == 3 and l[1] == 'T':
            #				print l
            #				fpObjs.write( '\t' + line + '\n' )
                if functionsInDefFile.count(l[2]) != 0:
                #					print '\tRemoved fun : %s' % l[2]
                    functionsInDefFile.remove(l[2])
                    if ( writeNewDef ):
                        newDefFile.write(l[2] + '\n')

                        #		fpObjs.write ( '\n' )

                        #	fpObjs.close()
    if ( writeNewDef ):
        newDefFile.close()

    #	print ''
    #	print "#functions in def file and not defined in module : %i" % len( functionsInDefFile )
    #	print "==============================================================================="
    #	count = len( functionsInDefFile )
    #	digitsCount = math.log10( count ) + 1
    #	fmt = '%%%dd. %%s' % digitsCount
    #	for i in xrange( 0, count ):
    #		print fmt % ( i + 1, functionsInDefFile[i] )

    for f in functionsInDefFile:
        functions.append(f)

    return None

def methodsInDefFile( defFilePath, methodsInDefFile ):
    if not os.path.exists(defFilePath):
        return defFilePath + ": File Not Found!"

    skipLines = True    # Skip lines until we get EXPORTS
    for line in file(defFilePath):
        if skipLines:
            line = line.strip()
            if line.lower() == 'exports':
                skipLines = False
            continue
        line = line.strip()
        if ( line != "" ):
            methodsInDefFile.append(line)

    return None

def ParseVCXProj( projectFilePath ):
    if ( not os.path.exists(projectFilePath) ):
        return projectFilePath + ": Project File Missing!"

    projectFileDirPath = re.sub(r'\\', r'/', os.path.dirname(projectFilePath))

    try:
        projFileDom = xml.dom.minidom.parse(projectFilePath)

        projTypeProjAndCurrentConfigs = getProjTypeProjAndCurrentConfigs(projFileDom)

        if ( projTypeProjAndCurrentConfigs == None ):
            return projectFilePath + ": Cannot Upgrade non-VisualStudioProject"

        moduleDefPath = getModuleDefFilePath_1(projFileDom, projectFilePath)
        intDirPath = getProjectIntDir(projFileDom, projectFilePath)

        print "==================================================================="
        print "  ProjectFile : " + projectFilePath
        print "ModuleDefFile : " + repr(moduleDefPath)
        print "       IntDir : " + repr(intDirPath)
        print ""
        if ( moduleDefPath != None and intDirPath != None ):
            # functions: Functions exported using def file but not defined
            #	in module
            functions = []
            functionsNotInModule(moduleDefPath, intDirPath, functions)
            #			print "#Functions : %d" % len( functions )

        projFileDom.unlink()

    except:
        return "Exception: " + projectFilePath

    return None

def getUndefinedFuncs( projectFilePath, functions ):
    if ( not os.path.exists(projectFilePath) ):
        return projectFilePath + ": Project File Missing!"

    try:
        projFileDom = xml.dom.minidom.parse(projectFilePath)

        projTypeProjAndCurrentConfigs = getProjTypeProjAndCurrentConfigs(projFileDom)

        if ( projTypeProjAndCurrentConfigs == None ):
            return projectFilePath + ": Cannot Upgrade non-VisualStudioProject"

        moduleDefPath = getModuleDefFilePath_1(projFileDom, projectFilePath)
        intDirPath = getProjectIntDir(projFileDom, projectFilePath)

        print "==================================================================="
        print "  ProjectFile : " + projectFilePath
        print "ModuleDefFile : " + repr(moduleDefPath)
        print "       IntDir : " + repr(intDirPath)
        print ""
        if ( moduleDefPath != None and intDirPath != None ):
            # functions: Functions exported using def file but not defined
            #	in module
            functionsNotInModule(moduleDefPath, intDirPath, functions)
            #			print "#Functions : %d" % len( functions )

        projFileDom.unlink()

    except:
        return "Exception: " + projectFilePath

    return None

def getExportedMethods( projectTargetFilePath, functions ):
    """
    This functions will find out the functions defined and exported
    in the module (exported using __declspec(dllexport)
    """
    #	projectTargetFilePath = "E:\\Build\\Gen_3_64Bit\\root\\bin\\Win32Release\\ePrj.dll"
    #	projectTargetFilePath = "E:\\Build\\Gen_3_64Bit\\root\\bin\\Win32Release\\eCommonU.dll"

    if not os.path.exists(projectTargetFilePath):
        return projectTargetFilePath + ": File Not Found!"

    popen = subprocess.Popen('dumpbin /exports %s' % ( projectTargetFilePath ),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

    stdout, stderr = popen.communicate()
    if popen.wait() != 0:
        raise Exception(str(stderr))

    skipLines = True
    for line in stdout.split('\n'):
        line = line.strip()

        if len(line) == 0: continue;

        if skipLines:
            if line.startswith("ordinal"):
                skipLines = False
            continue

        split_list = line.split()

        if len(split_list) < 4: break;
        functions.append(split_list[3])

    return None

def find_vcvarsall( version=10):
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

def query_vsvarsall( version, arch="x86" ):
    """Launch vcvarsall.bat and read the settings from its environment"""
    vcvarsall = find_vcvarsall(version)
    interesting = set(( "include", "lib", "libpath", "path" ))
    result = {}

    if vcvarsall is None:
        # raise PackagingPlatformError("Unable to find vcvarsall.bat")
        raise Exception("Unable to find vcvarsall.bat")
    print "calling 'vcvarsall.bat %s' (version=%s)" % ( arch, version )
    popen = subprocess.Popen('"%s" %s & set' % ( vcvarsall, arch ),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

    stdout, stderr = popen.communicate()
    if popen.wait() != 0:
        #raise PackagingPlatformError(stderr.decode("mbcs"))
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

def removeDuplicates( variable ):
    """Remove duplicate values of an environment variable."""
    oldList = variable.split(os.pathsep)
    newList = []
    for i in oldList:
        if i not in newList:
            newList.append(i)
    newVariable = os.pathsep.join(newList)
    return newVariable

def doit_1( projectFilePath1, projectFilePath2 ):
    '''
    This function list the functions exported from module_1
    but defined in module_2
    '''
    # Get all functions exported in module_1 file and store them in list_1
    #	and remove the functions from list_1 which are defined in module_1
    #
    # Traverse through all the .obj files in IntDir of module_2 and
    #	get the exported functions and search for these exported functions
    #	in list_1, if exist print on stdout

    print "Project_1 : %s" % projectFilePath1
    print "Project_2 : %s" % projectFilePath2

    functionsInProj1 = []
    #	getUndefinedFuncs( projectFilePath1, functionsInProj1 )

    defFilePath = "E:/Build/Gen_3_64Bit/sources_rdo/erasterlib/erasterlibA.def"
    #	defFilePath = "E:/Build/Gen_3_64Bit/sources_rdo/erasterlib/erasterlibu.def"

    methodsInDefFile(defFilePath, functionsInProj1)

    #	print "#Items in functionsInProj1 : %d" % len( functionsInProj1 )
    #	for fun in functionsInProj1: print fun

    methodsExportedInProj2 = []
    #	project2TargetFilePath = "E:\\Build\\Gen_3_64Bit\\root\\bin\\Win32Release\\ePrjU.dll"
    #	project2TargetFilePath = "E:\\Build\\Gen_3_64Bit\\root\\bin\\Win32Release\\ePrj.dll"
    project2TargetFilePath = "E:\\Build\\Gen_3_64Bit\\root\\bin\\Win32Release\\eCommon.dll"
    #	project2TargetFilePath = "E:\\Build\\Gen_3_64Bit\\root\\bin\\Win32Release\\eCommonU.dll"

    getExportedMethods(project2TargetFilePath, methodsExportedInProj2)

    #	print "#Items in methodsExportedInProj2 : %d" % len( methodsExportedInProj2 )
    #	for method in methodsExportedInProj2: print method

    # Traverse each method in methodsExportedInProj2, if any method found
    #	in functionsInProj1 then display this method on stdout
    #	ct = 0
    #	for method in methodsExportedInProj2:
    #		if functionsInProj1.count( method ) != 0:
    #			ct += 1
    #			print "%d. %s" % ( ct, method )

    ct = 0
    for method in functionsInProj1:
    #		tmp = methodsExportedInProj2.count( method )
    #		print "%d. %s" % ( tmp, method )
    #		if tmp != 0: ct += 1
    #	print "ct = %d" % ct
        if methodsExportedInProj2.count(method) == 0:
            ct += 1
            print "%d. %s" % ( ct, method )

            #	ParseVCXProj( projectFilePath2 )
    return None

def test_1():
    projectFilePath = "E:\\Build\\Gen_3_64Bit\\sources_rdo\\erasterlib\\erasterlib.vcxproj"
    #	projectFilePath2 = "E:\\Build\\Gen_3_64Bit\\sources_rdo\\ePrj\\ePrj.vcxproj"
    #	projectFilePath1 = "E:\\Build\\Gen_3_64Bit\\sources_rdo\\erasterlib\\erasterlib.vcxproj"
    #	projectFilePath2 = "E:\\Build\\Gen_3_64Bit\\sources_rdo\\ePrj\\ePrj.vcxproj"

    #	projectFilePath1 = "E:\\Build\\Gen_3_64Bit\\sources_rdo\\erasterlib\\erasterlibu.vcxproj"
    #	projectFilePath2 = "E:\\Build\\Gen_3_64Bit\\sources_rdo\\eCommon\\eCommonU.vcxproj"

    #	doit_1( projectFilePath1, projectFilePath2 )

    try:
        projFileDom = xml.dom.minidom.parse(projectFilePath)

        projModuleDefFilePath = getModuleDefFilePath_1(projFileDom, projectFilePath)
        print "ModuleDefFilePath = %s" % repr(projModuleDefFilePath)
        projFileDom.unlink()
    except:
        return "Exception : " + projectFilePath

    return None

def getProjectsFromSLN( solutionFilePath ):
    """
    Prase solution (.sln) file for projects (.vcxproj)
    """
    if ( not os.path.exists(solutionFilePath) ):
        return solutionFilePath + ": File Not Found!"

    solutionDirPath = os.path.dirname(solutionFilePath)

    ret = []

    try:
        for line in file(solutionFilePath):
            if REProjectPath.match(line) != None:
                items = re.split('\"', line)
                project = items[5]
                #print 'Project =', project
                projectFilePath = os.path.join(solutionDirPath, project)
                projectFilePath = os.path.abspath(projectFilePath)
                ret.append(projectFilePath)

    except:
        return solutionFilePath + ": Solution File Error:" + str(sys.exc_info()[0]) + str(sys.exc_info()[1])

    return ret

def getSolutionsFromBO( boFilePath ):
    '''
    Returns all the solution files in list
    '''
    ret = []
    if not os.path.exists(boFilePath): return ret
    boDirPath = os.path.dirname(boFilePath)
    for sln in file(boFilePath):
        sln = sln.strip()
        sln = os.path.join(boDirPath, sln)
        ret.append(sln)
    return ret

def getUnitTestSolution( projectFilePath ):
    if not os.path.exists(projectFilePath): return None

    projectDirPath = os.path.dirname(projectFilePath)
    unitTestDirPath = os.path.join(projectDirPath, 'UnitTest')

    if not os.path.exists(unitTestDirPath): return None

    for filename in listdir(unitTestDirPath):
        if ( '.sln' == os.path.splitext(filename)[1] ):
            return os.path.join(unitTestDirPath, filename)

    print '[getUnitTestSolution] UnitTest folder is available, but there is no .SLN file!'
    print '[getUnitTestSolution] ProjectFile : %s' % projectFilePath

    return None

def BuildSolution( solutionFilePath, buildConfig='Release|Win32', buildAction='Build' ):
    if not os.path.exists(solutionFilePath): return -1
    expr = 'devenv %s /%s \"%s\"' % ( solutionFilePath, buildAction, buildConfig )
    print('Executing expr = [%s]' % expr)
    exitCode = os.system(expr)
    return exitCode


class BuildProjectResult:
    def __init__(self, slnPath):
        pass


def BuildProject( solutionFilePath, projectName, buildConfig='Release|Win32', buildAction='Build' ):
    if not os.path.exists(solutionFilePath): return None

    #	devenv E:\Build\Gen_3_64Bit\Solutions\Gen3ERMapperSDK.sln /Build "Debug|Win32" /Project ERMErdasInit /ProjectConfig "Debug|Win32"
    expr = 'devenv %s /%s \"%s\" /Project %s /ProjectConfig \"%s\"' % (
        solutionFilePath, buildAction, buildConfig, projectName, buildConfig )
    print('Executing expr = %s' % expr)
    exitCode = os.system(expr)
    print("")

    return exitCode