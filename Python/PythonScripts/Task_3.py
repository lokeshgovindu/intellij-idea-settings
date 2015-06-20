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

REProjectPath = re.compile(	'^Project.* = ' + 				# Project GUID
							'\".*\"' + ", " + 				# Project Name
							'\".*.vcxproj.*\"' + ", " + 	# Project Path
							'.*' + '$',						# Rem
							re.IGNORECASE )

REParseCondition = re.compile(r"^[^=]*==[^']*'([^\|]*)\|([^']*)'[ ]*$")
REParseCondition_ConfigurationNameGroup = 1
REParseCondition_PlatformNameGroup = 2

RegOpenKeyEx	= winreg.OpenKeyEx
RegEnumKey		= winreg.EnumKey
RegEnumValue	= winreg.EnumValue
RegError		= winreg.error

HKEYS			= ( winreg.HKEY_USERS, winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CLASSES_ROOT )

Generation_3 = '<INVALID PATH>'

VCConfiguration	= "Release"
VCPlatform		= "Win32"

#===============================================================================
# 
#===============================================================================
class Reg:
	"""Helper class to read values from the registry"""
	
	def get_value( cls,	path, key ):
		for base in HKEYS:
			d = cls.read_values( base, path )
			if d and key in d:
				return d[key]
		raise KeyError( key )
	get_value = classmethod( get_value )

	def read_keys( cls, base, key ):
		"""Return list of registry keys."""
		try:
			handle = RegOpenKeyEx( base, key )
		except RegError:
			return None
		L = []
		i = 0
		while True:
			try:
				k = RegEnumKey( handle, i )
			except RegError:
				break
			L.append( k )
			i += 1
		return L
	read_keys = classmethod( read_keys )

	def	read_values( cls, base, key ):
		"""Return dict of registry keys and values.
 
		All names are converted to lowercase.
		"""
		try:
			handle = RegOpenKeyEx( base, key )
		except RegError:
			return None
		d = {}
		i = 0
		while True:
			try:
				name, value, type = RegEnumValue( handle, i )
			except RegError:
				break
			name = name.lower()
			d[ cls.convert_mbcs( name ) ] = cls.convert_mbcs( value )
			i += 1
		return d
	read_values = classmethod( read_values )

	def convert_mbcs( s ):
		dec = getattr( s, "decode", None )
		if dec is not None:
			try:
				s = dec( "mbcs" )
			except UnicodeError:
				pass
		return s
	convert_mbcs = staticmethod( convert_mbcs )

#===============================================================================
# 
#===============================================================================
def functionsNotInModule( defFilePath, interDirPath ):

	writeNewDef = True

	if not os.path.exists( defFilePath ):
		return defFilePath + ": File Not Found!"

	if not os.path.exists( interDirPath ):
		return interDirPath + ": Intermediate Direcotry Path Not found!"
	
	if ( writeNewDef ):
		part1, part2 = os.path.splitext( defFilePath )
		newDefFilePath = part1 + "New" + part2
		newDefFile = file( newDefFilePath, 'w' )
		
	
	functionsInDefFile = []
	skipLines = True	# Skip lines until we get EXPORTS
	for line in file( defFilePath ):
		if skipLines:
			if ( writeNewDef ):
				newDefFile.write( line )
			line = line.strip()				
			if line.lower() == 'exports':
				skipLines = False
			continue
		line = line.strip()
		if ( line != "" ):
			functionsInDefFile.append( line )


#	print "#functions in def file : %i" % len( functionsInDefFile )

#	fpObjs = open( 'D:/LGTEMP/functionsInObjs.txt', 'w' )

	for f in listdir( interDirPath ):
		filePath = join( interDirPath, f )
		if ( '.obj' == os.path.splitext( filePath )[1] ):
			print "Processing file : " + filePath
#			print "==============================================================================="

#			fpObjs.write( "Exported functions in : " + filePath + "\n" )
#			fpObjs.write( "===============================================================================\n" )
			popen = subprocess.Popen( 'nm -g -C %s' % ( filePath ),
									  stdout = subprocess.PIPE,
									  stderr = subprocess.PIPE )

			stdout, stderr = popen.communicate()
			if popen.wait() != 0 :
				raise Exception( str( stderr ) )

			for line in stdout.split( '\n' ):
				l = line.split()
				if len(l) == 3 and l[1] == 'T':
#					print l
#					fpObjs.write( '\t' + line + '\n' )
					if functionsInDefFile.count( l[2] ) != 0:
#						print '\tRemoved fun : %s' % l[2]
						functionsInDefFile.remove( l[2] )
						if ( writeNewDef ):
							newDefFile.write( l[2] + '\n' )

#			fpObjs.write ( '\n' )

#	fpObjs.close()
	if ( writeNewDef ):
		newDefFile.close()

	print ''
	print "#functions in def file and not defined in module : %i" % len( functionsInDefFile )
	print "==============================================================================="
	#print functionsInDefFile
	count = len( functionsInDefFile )
	digitsCount = math.log10( count ) + 1
	fmt = '%%%dd. %%s' % digitsCount
	for i in xrange( 0, count ):
		#print "%i. %s" % ( i + 1, functionsInDefFile[i] )
		print fmt % ( i + 1, functionsInDefFile[i] )

	return None

#===============================================================================
# 
#===============================================================================
def getVCProjConfigs( vcProj ):
	configs = []
	for config in vcProj.getElementsByTagName("Configuration"):
		configs.append( config.getAttribute( "Name" ) )

	print configs
	return configs

#===============================================================================
# 
#===============================================================================
def getMSBuildProjType( msbuildProj ):
	# Somewhat crude way of differentiating an MSBuild CSProj from a VCProj
	for config in msbuildProj.getElementsByTagName("PropertyGroup"):
		anNodes = config.getElementsByTagName("AssemblyName")
		if ( anNodes == None or anNodes.length == 0 ):
			continue
		
		return "CSProj"

	return "VCXProj"

#===============================================================================
# getMSBuildProjConfigs
#===============================================================================
def getMSBuildProjConfigs( msbuildProj ):
	configs = []
	for config in msbuildProj.getElementsByTagName("PropertyGroup"):
		conditionValue = config.getAttribute( "Condition" )
		if ( conditionValue == "" ):
			continue
		mtch = REParseCondition.match(conditionValue)

		# This seems odd...let it go for now
		if ( mtch == None ):
			continue

		configs.append( mtch.group( REParseCondition_ConfigurationNameGroup ) \
			+ "|" + mtch.group( REParseCondition_PlatformNameGroup ) )

	return configs

#===============================================================================
# getProjTypeProjAndCurrentConfigs
#===============================================================================
def getProjTypeProjAndCurrentConfigs( projFileDom ):
	vsProjs = projFileDom.getElementsByTagName("VisualStudioProject")
	if ( vsProjs ):
		projType = "VCProj"
		configs = getVCProjConfigs( vsProjs[0] )
	else:
		vsProjs = projFileDom.getElementsByTagName("Project")
		if ( vsProjs ):
			projType = getMSBuildProjType( vsProjs[0] )
			configs = getMSBuildProjConfigs( vsProjs[0] )
		else:
			return None

	return ( projType, vsProjs[0], configs )

#===============================================================================
# 
#===============================================================================
def getModuleDefFilePath( projFileDom, projectDirPath ):
	for itemDefGroup in projFileDom.getElementsByTagName( "ItemDefinitionGroup" ):
		conditionValue = itemDefGroup.getAttribute( "Condition" )
		if ( conditionValue == "" ):
			continue
		mtch = REParseCondition.match(conditionValue)

		# This seems odd...let it go for now
		if ( mtch == None ):
			continue

		configName = mtch.group( REParseCondition_ConfigurationNameGroup ) \
			+ "|" + mtch.group( REParseCondition_PlatformNameGroup )
		
		if ( "Release|Win32" != configName ):
			continue
		
		link = itemDefGroup.getElementsByTagName( 'ModuleDefinitionFile' )
		
		moduleDefFile = link[0].childNodes[0].data
		
		if ( not os.path.isabs( moduleDefFile ) ):
			moduleDefAbsPath = os.path.join( projectDirPath, moduleDefFile )
			if ( not os.path.exists( moduleDefAbsPath ) ):
#				print moduleDefAbsPath + ": File Not Found!"
				return None
		
	return os.path.abspath( moduleDefAbsPath )

#===============================================================================
# 
#===============================================================================
def getProjectIntDir( projFileDom, projectFilePath ):
	
	projectFileDirPath = re.sub( r'\\', r'/', os.path.dirname( projectFilePath ) )

	for IntDir in projFileDom.getElementsByTagName( 'IntDir' ):
#		print propertyGroup
		conditionValue = IntDir.getAttribute( "Condition" )
		if ( conditionValue == "" ):
			continue
		mtch = REParseCondition.match(conditionValue)

		# This seems odd...let it go for now
		if ( mtch == None ):
			continue

		configName = mtch.group( REParseCondition_ConfigurationNameGroup ) \
			+ "|" + mtch.group( REParseCondition_PlatformNameGroup )
		
		if ( "Release|Win32" != configName ):
			continue
		
		IntDirPath = IntDir.childNodes[0].data
		
		if ( IntDirPath.find( "$(Platform)$(Configuration)" ) >= 0 ):
			IntDirPath = IntDirPath.replace( "$(Platform)$(Configuration)", "Win32Release" )
			
		if ( IntDirPath.find( "$(ProjectName") >= 0 ):
			projectName = getProjectNameFromVCProjFileDom( projFileDom, projectFilePath )			
			IntDirPath = IntDirPath.replace( "$(ProjectName)", projectName )
			
		if ( not os.path.isabs( IntDirPath ) ):
			IntDirAbsPath = os.path.join( projectFileDirPath, IntDirPath )
			if ( not os.path.exists( IntDirAbsPath ) ):
				return IntDirAbsPath + ": Directory Not Found!"
		
	return os.path.abspath( IntDirAbsPath )

#===============================================================================
# 
#===============================================================================
def ParseVCXProj( projectFilePath ):
	if ( not os.path.exists( projectFilePath ) ):
		return projectFilePath + ": Project File Missing!"			
	
	projectFileDirPath = re.sub( r'\\', r'/', os.path.dirname( projectFilePath ) )
	
	try:
		projFileDom = xml.dom.minidom.parse( projectFilePath )
		
		projTypeProjAndCurrentConfigs = getProjTypeProjAndCurrentConfigs( projFileDom )
#		print projTypeProjAndCurrentConfigs
		
		if ( projTypeProjAndCurrentConfigs == None ):
			return projectFilePath + ": Cannot Upgrade non-VisualStudioProject"

		moduleDefPath = getModuleDefFilePath( projFileDom, projectFileDirPath )
		intDirPath = getProjectIntDir( projFileDom, projectFilePath )
		
		print "==================================================================="
		print "  ProjectFile : " + projectFilePath
		print "ModuleDefFile : " + repr( moduleDefPath )
		print "       IntDir : " + repr( intDirPath )
		if ( moduleDefPath != None and intDirPath != None ):
			functionsNotInModule( moduleDefPath, intDirPath)
		
	except:
		return "Exception: " + projectFilePath

	return None

#===============================================================================
# 
#===============================================================================
def parseSolutionForProjects( solutionFilePath ):
	"""
	Parse solution (.sln) file for projects (.vcxproj)
	"""
	if ( not os.path.exists( solutionFilePath ) ):
		return solutionFilePath + ": Solution File Missing!"

#	if ( not os.path.exists( solutionFilePath ) ):
#		solutionAbsPath = Generation_3 + '\\Solutions\\' + solutionFilePath
#		if ( not os.path.exists( solutionAbsPath ) ):
#			return solutionFilePath + ": Solution File Missing!"

	solutionsDirPath = os.path.dirname( solutionFilePath )

	try:
		for line in file( solutionFilePath ):
			if REProjectPath.match( line ) != None:
				items = re.split( '\"', line )
				project = items[5]
				projectFilePath = os.path.join( solutionsDirPath, project )
				projectFilePath = os.path.abspath( projectFilePath )
				ParseVCXProj( projectFilePath )

	except:
		return solutionFilePath + ": Solution File Error:" + str(sys.exc_info()[0]) + str(sys.exc_info()[1])

#===============================================================================
# 
#===============================================================================
def getProjectNameFromVCProjFile( projectFilePath ):
	if ( not os.path.exists( projectFilePath ) ):
#		return projectFilePath + ": File Not Found!"
		return None
	
	projFileDom = xml.dom.minidom.parse( projectFilePath )
	
	projectName = None
	for projName in projFileDom.getElementsByTagName( "ProjectName"):
		projectName = projName.childNodes[0].data
		
	if ( projectName == None ):
#		print "ProjectName is not available in .vcxproj file"
		projectName = os.path.splitext( os.path.basename( projectFilePath ) )[0]
	
	projFileDom.unlink()
		
	return projectName

#===============================================================================
# 
#===============================================================================
def getProjectNameFromVCProjFileDom( projFileDom, projectFilePath ):
	projectName = None
	for projName in projFileDom.getElementsByTagName( "ProjectName"):
		projectName = projName.childNodes[0].data
		
	if ( projectName == None ):
#		print "ProjectName is not available in .vcxproj file"
		projectName = os.path.splitext( os.path.basename( projectFilePath ) )[0]
		
	return projectName

#===============================================================================
# 
#===============================================================================
def parseBuildOrder( buildOrderFilePath ):
	"""
	Parse build order file
	"""
	if ( not os.path.exists( buildOrderFilePath ) ):
		return buildOrderFilePath + ": Build Order File Not Found!"

	solutionsDirPath = re.sub( r'\\', r'/', os.path.dirname( buildOrderFilePath ) )

	try:
		for line in file( buildOrderFilePath ):
#			print line
#			strLine = line.strip()
			parseSolutionForProjects( os.path.join( solutionsDirPath, line.strip() ) )
	except:
		return buildOrderFilePath + ': Build Order File Error:' + str(sys.exc_info()[0]) + str(sys.exc_info()[1])

#===============================================================================
# 
#===============================================================================
if __name__ == '__main__':
	if os.system( "nm" ):
		print "nm is not available in path!"
		try:
			cygwinInstallDir = Reg.get_value( r"SOFTWARE\Cygwin\setup", "rootdir" )
			cygwinBinPath = os.path.join( cygwinInstallDir, 'bin' )
		except KeyError:
			print "Unable to find cygwin root dir in registry"
			cygwinBinPath = None
			sys.exit()

	print 'cygwinBinPath = %s' % cygwinBinPath
	os.environ[ 'path' ] = os.environ[ 'path' ] + ';' + cygwinBinPath

#	solutionFilePath = "E:\\Build\\Gen_3_64Bit\\Solutions\\Gen3ERMapperSDK.sln"
#	parseSolutionForProjects( solutionFilePath )
	
#	buildOrderFilePath = "E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ERMapper"
#	parseBuildOrder( buildOrderFilePath )

#	print getProjectNameFromVCProjFile( "LG" )

#	projectFilePath = 'E:\\Build\\Gen_3_64Bit\\sources_rdo\\erasterlib\\erasterlib.vcxproj'
#	ParseVCXProj( projectFilePath )

#	ParseVCXProj( "E:\\Build\\Gen_3_64Bit\\sources_erm\\ERM_RASTER_TRANS\\GDAL\\erm_raster_gdal_ng.vcxproj" )

#	sys.exit()

	if len(sys.argv) <= 1:
		print 'No args passed(workspace path)!'
		sys.exit( -1 )
		
	Generation_3 = sys.argv[1]
	print "Generation_3 folder path : " + Generation_3

	buildOrderFiles = [
#		'buildOrder_Desktop-BLD'		,
		'buildOrder_Desktop-ENC'		,
#		'buildOrder_Desktop-ERMapper'	,
#		'buildOrder_Desktop-IMAGINE-A'	,
#		'buildOrder_Desktop-IMAGINE-B'	,
#		'buildOrder_Desktop-IMAGINE-C'	,
#		'buildOrder_Desktop-LPS'		,
#		'buildOrder_Extensions'			,
		]

	for buildOrderFile in buildOrderFiles:
		filePath = Generation_3 + '\\Solutions\\' + buildOrderFile
		print 'Processing : ' + filePath
		print "==============================================================================="
		parseBuildOrder( filePath )
		print '\n'

	print "=== END ==="		
	sys.exit()
