import CommonUtils
import os
import sys
import math
import re
import time
import datetime

from vcxprojUtils import getModuleDefFilePath, getSolutionsFromBO
from vcxprojUtils import addCygwinToPath
from vcxprojUtils import query_vsvarsall
from vcxprojUtils import getProjectsFromSLN
import vcxprojUtils


#===============================================================================
# 
#===============================================================================
def test_GetModuleDefFilePath():
#	projectFilePath = "E:\\Build\\Gen_3_64Bit\\sources_rdo\\erasterlib\\erasterlib.vcxproj"
    projectFilePath = 'E:\\Build\\Gen_3_64Bit\\sources_rdo\\codesamples\\codesamples.vcxproj'

    configurations = []
    configurations.append("Release|Win32")
    configurations.append("URelease|x64")

    nconfigs = len(configurations)
    for i in xrange(0, nconfigs, 1):
        moduleDefFilePath = getModuleDefFilePath(projectFilePath, configurations[i])
        print 'Config = %s, moduleDefFilePath = %s' % ( configurations[i], moduleDefFilePath )

    return None

#===============================================================================
# 
#===============================================================================
def test_GetModuleDefFilePath_1( projectFilePath ):
#	projectFilePath = "E:\\Build\\Gen_3_64Bit\\sources_rdo\\erasterlib\\erasterlib.vcxproj"
#	projectFilePath = 'E:\\Build\\Gen_3_64Bit\\sources_rdo\\codesamples\\codesamples.vcxproj'

#	configurations = []
#	configurations.append( "Debug|Win32" )
#	configurations.append( "Release|Win32" )
#	configurations.append( "UDebug|x64" )
#	configurations.append( "URelease|x64" )

#	nconfigs = len( configurations )
#	for i in xrange( 0, nconfigs, 1 ):
#		moduleDefFilePath = getModuleDefFilePath( projectFilePath, configurations[ i ] )
#		print 'Config = %s, moduleDefFilePath = %s' % ( configurations[ i ], moduleDefFilePath )

    defPath1 = getModuleDefFilePath(projectFilePath, 'Release|Win32')
    defPath2 = getModuleDefFilePath(projectFilePath, 'URelease|x64')
    if ( defPath1 != defPath2 and ( defPath1 == None or defPath2 == None ) ):
    #		print "  NotEqual (%s, %s)" % ( defPath1, defPath2 )
    #		print projectFilePath
    #		print '\tRelease|Win32 : %s' % defPath1
    #		print '\t URelease|x64 : %s' % defPath2
        return True

    return False

#===============================================================================
# 
#===============================================================================
def test_GetProjectsFromSolution():
    solutionFilePath = "E:\\Build\\Gen_3_64Bit\\Solutions\\Gen3ERMapperSDK.SLN"
    #	solutionFilePath = "E:\\Build\\Gen_3_64Bit\\Solutions\\IMAGINEFrameworkPluginsERM.SLN"

    for projectFilePath in getProjectsFromSLN(solutionFilePath):
    #		print os.path.splitext(os.path.basename( projectFilePath ))[0]
        print projectFilePath
    #		print 'Processing : %s' % projectFilePath
    #		defFilePath1 = getModuleDefFilePath( projectFilePath, 'Release|Win32' )
    #		defFilePath2 = getModuleDefFilePath( projectFilePath, 'Release|x64' )
    #		if defFilePath1 != defFilePath2:
    #			print projectFilePath
    #		if test_GetModuleDefFilePath_1( projectFilePath ):
    #			print projectFilePath

    return None

#===============================================================================
# 
#===============================================================================
def test_GetSolutionsFromBO():
    boFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ENC'
    for sln in getSolutionsFromBO(boFilePath): print sln
    return None


def test_DisplayProjectsFromBO():
#	boFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ENC-x64'
#	boFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ENC'
    boFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ERMapper'
    for sln in getSolutionsFromBO(boFilePath):
        print 'Solution : %s' % sln
        print '---------------------------------------------------------------'
        i = 1
        projects = getProjectsFromSLN(sln)
        projectNames = []
        duplicates = False
        projCount = math.log10(len(projects)) + 1
        fmt = '%%%dd. %%s' % projCount
        #		print 'fmt = %s'% fmt
        for prj in projects:
        #			print fmt % ( i, prj )
            prjName = os.path.splitext(os.path.basename(prj))[0]
            print fmt % ( i, prjName )
            i += 1
            if ( projectNames.count(prjName) != 0 ): duplicates = True
            projectNames.append(prjName)

        if (  duplicates == True ):
            print ''
            print "=== Multiple projects have same name! ==="
        print ''
    #			if test_GetModuleDefFilePath_1( prj ) == True: print '## %s' % prj

    return None


def test_GetPOMFilesFromBO():
# 	boFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-IMAGINE-A'
#  	boFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-IMAGINE-B'
    boFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-IMAGINE-C'
    # 	boFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ENC'
    # 	boFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ERMapper'
    for sln in getSolutionsFromBO(boFilePath):
        print 'Solution : %s' % sln
        print '---------------------------------------------------------------'
        i = 1
        projects = getProjectsFromSLN(sln)
        projectNames = []
        duplicates = False
        projCount = math.log10(len(projects)) + 1
        fmt = '%%%dd. %%s' % projCount
        #		print 'fmt = %s'% fmt

        for prj in projects:
        #			print fmt % ( i, prj )
            prjDir = os.path.split(prj)[0]
            for file in os.listdir(prjDir):
                fileName = os.path.basename(file).lower()
                if fileName == "pom.xml":
                    print fmt % ( i, prj )
                    i += 1
                # 			prjName = os.path.splitext( os.path.basename( prj ) )[0]
                # 			print fmt % ( i, prjDir )
                # 			i += 1
                # 			if ( projectNames.count( prjName ) != 0 ): duplicates = True
                # 			projectNames.append( prjName )

        if (  duplicates == True ):
            print ''
            print "=== Multiple projects have same name! ==="
        print ''
    #			if test_GetModuleDefFilePath_1( prj ) == True: print '## %s' % prj

    return None


def test_DisplayProjectsFromBOInWikiFormat():
#	boFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ENC-x64'
#	boFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ENC'
    boFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ERMapper'

    for sln in getSolutionsFromBO(boFilePath):
        solutionName = os.path.splitext(os.path.basename(sln))[0]
        print '\---------------------------------------------------------------------------------------------------------------\-'
        print ''
        print 'h4. %s.SLN' % solutionName
        print ''
        print '|| Primary Trailer | | ||'
        print '|| Checked In CI | | ||'
        print ''
        print '|| Projects Dependency Graph | !%s_DepGraph.png|thumbnail,border=1,width=100! ||' % solutionName
        print ''
        print '{table-plus}'
        print '|| Projects || Leader || Status || UnitTest to Unicode || Status || Trailer || Status || Linking Status || UnitTest Built x64 || Status ||'
        i = 1
        projects = getProjectsFromSLN(sln)
        projectNames = []
        duplicates = False
        projCount = math.log10(len(projects)) + 1
        #		fmt = '%%%dd. %%s' % projCount
        #		print 'fmt = %s'% fmt
        for prj in projects:
        #			print fmt % ( i, prj )
            prjName = os.path.splitext(os.path.basename(prj))[0]
            #			print fmt % ( i, prjName )
            print '| %s | | | | | | | | | |' % prjName
            i += 1
            if ( projectNames.count(prjName) != 0 ): duplicates = True
            projectNames.append(prjName)
        print '{table-plus}'
        if (  duplicates == True ):
            print ''
            print "=== Multiple projects have same name! ==="
        print ''
    #			if test_GetModuleDefFilePath_1( prj ) == True: print '## %s' % prj

    return None


def test_3():
    projectFilePath = 'E:\\Build\\Gen_3_64Bit\\sources_gio\\binglib\\binglib.vcxproj'
    print vcxprojUtils.getUnitTestSolution(projectFilePath)
    return None


def GetAllUnitTestSolutions():
    boFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ERMapper'
    for sln in getSolutionsFromBO(boFilePath):
        print 'SLN : %s' % sln
        print '----------------------------------------------------------------'
        for prj in getProjectsFromSLN(sln):
            unitTestSLN = vcxprojUtils.getUnitTestSolution(prj)
            if ( unitTestSLN != None ):
                print unitTestSLN
    return None


def test_BuildSolution_Gen3ERMapperSDK():
#	solutionFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\Gen3PhotogrammetryToolkitPlugins.SLN'
#	solutionFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\Gen3ERMapperSDK.SLN'
#	solutionFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\Gen3CRSToolkit.SLN'
#	solutionFilePath = 'E:\\Build\\Gen_3_64Bit\\lg_Solutions\\BuildERDASProducts\\BuildERDASProducts.SLN'

# UnitTets
#	solutionFilePath = 'E:\\Build\\Gen_3_64Bit\\sources_erm\\LIB\\ERMapperLib_NG\\UnitTest\\ERMapperLib_NGUnitTest.SLN'
#	solutionFilePath = 'E:\\Build\\Gen_3_64Bit\\sources_erm\\LIB\\ERMCRS\\UnitTest\\ermcrsUnitTest.SLN'

#	configs = [ 'UDebug|x64', 'URelease|x64' ]
    configs = ['Debug|Win32', 'Release|Win32', 'UDebug|x64', 'URelease|x64']
    slns = [
        'E:\\Build\\Gen_3_64Bit\\Solutions\\Gen3ERMapperSDK.SLN',
        'E:\\Build\\Gen_3_64Bit\\sources_erm\\LIB\\ERMCRS\\UnitTest\\ermcrsUnitTest.SLN',
        'E:\\Build\\Gen_3_64Bit\\sources_erm\\LIB\\ERMapperLib_NG\\UnitTest\\ERMapperLib_NGUnitTest.SLN'
    ]

    #	buildConfig = 'Debug|Win32'
    #	buildAction = 'Build'
    #	vcxprojUtils.BuildProject( solutionFilePath, 'ERMapper', 'Release|Win32', 'Rebuild' )
    #	vcxprojUtils.BuildProject( solutionFilePath, 'ERMapper', 'Debug|Win32', 'Rebuild' )

    for sln in slns:
        for config in configs:
            print "==========================================================="
            print "Building SLN = %s, Config = %s" % (sln, config)
            vcxprojUtils.BuildSolution(sln, config, 'Rebuild')
            print ""

        #	for line in file( 'UnitTestSLNs.txt' ):
        #		line = line.strip()
        #		vcxprojUtils.BuildSolution( line )

        #	for config in configs:
        #		print "==============================================================="
        #		print "Building SLN = %s, Config = %s" % ( solutionFilePath, config )
        #		vcxprojUtils.BuildSolution( solutionFilePath, config, "Rebuild" )

    return None


def test_BuildSolution_IMAGINEFrameworkPluginsERM():
#	solutionFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\IMAGINEFrameworkPluginsERM.SLN'
#	vcxprojUtils.BuildProject( solutionFilePath, 'vr_algorithm', 'Debug|Win32', 'Build')
#	vcxprojUtils.BuildProject( solutionFilePath, 'vr_algorithm', 'UDebug|x64', 'Build')
#	return None

# UnitTets
#	solutionFilePath = 'E:\\Build\\Gen_3_64Bit\\sources_erm\\LIB\\ERMapperLib_NG\\UnitTest\\ERMapperLib_NGUnitTest.SLN'
#	solutionFilePath = 'E:\\Build\\Gen_3_64Bit\\sources_erm\\LIB\\ERMCRS\\UnitTest\\ermcrsUnitTest.SLN'

#	configs = [ 'Debug|Win32', 'Release|Win32' ]
#	configs = [ 'UDebug|x64', 'URelease|x64' ]
#	configs = [ 'Debug|Win32', 'Release|Win32', 'UDebug|x64', 'URelease|x64' ]
    configs = ['Debug|Win32', 'UDebug|x64', 'Release|Win32', 'URelease|x64']
    slns = [
        'E:\\Build\\Gen_3_64Bit\\Solutions\\IMAGINEFrameworkPluginsERM.SLN',
        'E:\\Build\\Gen_3_64Bit\\sources_gio\\rf_ers\\UnitTest\\rf_ersUnitTest.SLN',
        'E:\\Build\\Gen_3_64Bit\\sources_gio\\rf_alg\\UnitTest\\rf_algUnitTest.SLN'
    ]

    #	for sln in slns:
    #		for config in configs:
    #			print "==========================================================="
    #			print "Cleaning SLN = %s, Config = %s" % (sln, config)
    #			vcxprojUtils.BuildSolution( sln, config, 'Clean' )
    #			print ""

    for sln in slns:
        for config in configs:
            print "==========================================================="
            print "Building SLN = %s, Config = %s" % (sln, config)
            vcxprojUtils.BuildSolution(sln, config, 'Build')
            print ""

        #	for line in file( 'UnitTestSLNs.txt' ):
        #		line = line.strip()
        #		vcxprojUtils.BuildSolution( line )

        #	for config in configs:
        #		print "==============================================================="
        #		print "Building SLN = %s, Config = %s" % ( solutionFilePath, config )
        #		vcxprojUtils.BuildSolution( solutionFilePath, config, "Rebuild" )

    return None


def test_Build_buildOrder():
    solutionFilePath = 'E:\\Build\\Gen_3_64Bit\\lg_Solutions\\BuildERDASProducts\\BuildERDASProducts.SLN'

    #	configs = [ 'UDebug|x64', 'URelease|x64' ]
    #	configs = [ 'Debug|Win32', 'Release|Win32', 'UDebug|x64', 'URelease|x64' ]
    #	configs = [ 'UDebug|x64' ]
    #	configs = [ 'Debug|Win32', 'UDebug|x64' ]
    configs = ['Debug|Win32', 'UDebug|x64', 'Release|Win32', 'URelease|x64']
    unitTestSLNs = [
        'E:\\Build\\Gen_3_64Bit\\sources_erm\\LIB\\ERMapperLib_NG\\UnitTest\\ERMapperLib_NGUnitTest.SLN',
        'E:\\Build\\Gen_3_64Bit\\sources_erm\\LIB\\ERMCRS\\UnitTest\\ermcrsUnitTest.SLN',
        'E:\\Build\\Gen_3_64Bit\\sources_gio\\rf_alg\\UnitTest\\rf_algUnitTest.SLN',
        'E:\\Build\\Gen_3_64Bit\\sources_gio\\rf_ers\\UnitTest\\rf_ersUnitTest.SLN',
    ]

    #	buildConfig = 'Debug|Win32'
    #	buildAction = 'Build'
    #	vcxprojUtils.BuildProject( solutionFilePath, 'ERMapper', 'Release|Win32', 'Rebuild' )
    #	vcxprojUtils.BuildProject( solutionFilePath, 'ERMapper', 'Debug|Win32', 'Rebuild' )

    #
    # Clean All UnitTest Solutions first
    #
    print "[Clean] Started at %s" % datetime.datetime.now()
    for config in configs:
        vcxprojUtils.BuildProject(solutionFilePath, 'ERMapper', config, "Clean")
        for sln in unitTestSLNs:
            vcxprojUtils.BuildSolution(sln, config, 'Clean')
    print "[Clean] Ended at %s" % datetime.datetime.now()

    print "[Build] Started at %s" % datetime.datetime.now()
    for config in configs:
        print "==============================================================="
        print "Building SLN = %s, Config = %s" % ( solutionFilePath, config )
        vcxprojUtils.BuildProject(solutionFilePath, 'ERMapper', config, "Build")
        for sln in unitTestSLNs:
            print "==============================================================="
            print "Building UnitTest SLN = %s, Config = %s" % ( sln, config )
            vcxprojUtils.BuildSolution(sln, config, 'Build')
        #		vcxprojUtils.BuildSolution( solutionFilePath, config, "Build" )
    print "[Build] Ended at %s" % datetime.datetime.now()

    return None


def test_4():
    solutionFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\Gen3PhotogrammetryToolkitPlugins.sln'
    ct = 0
    for prj in vcxprojUtils.getProjectsFromSLN(solutionFilePath):
        print '----------------------------------------------------------------'
        print 'ProjectFile : %s' % prj
        unitTestSLNPath = vcxprojUtils.getUnitTestSolution(prj)
        if ( unitTestSLNPath != None ):
            ct += 1
            print '%d. %s' % ( ct, unitTestSLNPath )
        #		ct += 1
        #		print '%2d. %s' % ( ct, prj )
    return None


def test_5():
    solutionFilePath = 'E:\\Build\\Gen_3_64Bit\\Solutions\\Gen3PhotogrammetryToolkitPlugins.sln'
    for prj in vcxprojUtils.getProjectsFromSLN(solutionFilePath):
        for line in file(prj):
            line = line.strip()
            if ( line.find('irsiflib.lib') != -1 ):
                print prj
                break
    return None


def RunUnitTestsSLNs():
    unitTestsSLNs = []
    unitTestsSLNs.append('E:\\Build\\Gen_3_64Bit\\sources_rdo\\gm_framecamera\\UnitTest\\gm_frameCameraUnitTest.sln')
    unitTestsSLNs.append('E:\\Build\\Gen_3_64Bit\\sources_rdo\\gm_orthosar\\UnitTest\\gm_orthosarUnitTest.sln')
    unitTestsSLNs.append('E:\\Build\\Gen_3_64Bit\\sources_gio\\tf_shape\\UnitTest\\tf_shapeUnitTest.sln')
    unitTestsSLNs.append('E:\\Build\\Gen_3_64Bit\\sources_gio\\tf_sstin\\UnitTest\\tf_sstinUnitTest.sln')
    unitTestsSLNs.append('E:\\Build\\Gen_3_64Bit\\sources_gio\\tf_raster\\UnitTest\\tf_rasterUnitTest.sln')
    unitTestsSLNs.append('E:\\Build\\Gen_3_64Bit\\sources_gio\\tf_ascii\\UnitTest\\tf_asciiUnitTest.sln')
    unitTestsSLNs.append('E:\\Build\\Gen_3_64Bit\\sources_gio\\tf_evec\\UnitTest\\tf_evecUnitTest.sln')
    unitTestsSLNs.append('E:\\Build\\Gen_3_64Bit\\sources_gio\\tf_annotation\\UnitTest\\tf_annotationUnitTest.sln')
    unitTestsSLNs.append('E:\\Build\\Gen_3_64Bit\\sources_rdo\\gm_iso\\UnitTest\\gm_isoUnitTest.sln')
    unitTestsSLNs.append('E:\\Build\\Gen_3_64Bit\\sources_gio\\tf_binary\\UnitTest\\tf_binaryUnitTest.sln')
    unitTestsSLNs.append('E:\\Build\\Gen_3_64Bit\\sources_gio\\tf_tmtin\\UnitTest\\tf_tmtinUnitTest.sln')
    unitTestsSLNs.append('E:\\Build\\Gen_3_64Bit\\sources_gio\\tf_cad\\UnitTest\\tf_cadUnitTest.sln')

    buildAction = 'Rebuild';

    buildConfig = 'URelease|x64'
    #	buildConfig = 'Release|Win32'

    for sln in unitTestsSLNs:
        print 'Executing SLN : %s' % sln
        print '-----------------------------------------------------------------'
        vcxprojUtils.BuildSolution(sln, buildConfig, buildAction)
        print '=== Finished, SLN : %s ===' % sln
        print ''

    return None

#===============================================================================
# 
#===============================================================================
REAdditionalDependencies = re.compile('^.*<AdditionalDependencies>.*' +
                                      '.*' +
                                      '</AdditionalDependencies>.*$',
                                      re.IGNORECASE)


def isProjectLinkedWith( projectFilePath, libName ):
    '''
    find the specified libName (Import Library)
    in the project
    '''
    if ( not os.path.exists(projectFilePath) ): return None

    try:
        bOk = 'False'
        for line in file(projectFilePath):
            if REAdditionalDependencies.match(line) != None:
                if str(line).find(libName) != -1:
                    bOk = 'True'
                    break
        if bOk == 'True':
        #			print projectFilePath
            return True

    except:
        return False

    return False

#===============================================================================
# 
#===============================================================================
def test_6():
    boFiles = []
    #	boFiles.append( 'E:\\Build\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-BLD' )
    #	boFiles.append( 'E:\\Build\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-BLD-x64' )
    boFiles.append('E:\\Build\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ENC')
    boFiles.append('E:\\Build\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ENC-x64')
    #	boFiles.append( 'E:\\Build\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-ERMapper' )
    #	boFiles.append( 'E:\\Build\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-IMAGINE-A' )
    #	boFiles.append( 'E:\\Build\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-IMAGINE-B' )
    #	boFiles.append( 'E:\\Build\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-IMAGINE-C' )
    #	boFiles.append( 'E:\\Build\Gen_3_64Bit\\Solutions\\buildOrder_Desktop-LPS' )

    i = 1
    for bo in boFiles:
        for sln in getSolutionsFromBO(bo):
        #			print 'Solution : %s' % sln
        #			print '---------------------------------------------------------------'
            projects = getProjectsFromSLN(sln)
            projCount = math.log10(len(projects)) + 1
            fmt = '%%%dd. %%s' % projCount
            #		print 'fmt = %s'% fmt
            for prj in projects:
            #			print fmt % ( i, prj )
            #			i += 1
                if ( isProjectLinkedWith(prj, 'ephoezlib.lib')):
                    print fmt % ( i, prj )
                    i += 1

                #			print ''
    #			if test_GetModuleDefFilePath_1( prj ) == True: print '## %s' % prj

    return None

#===============================================================================
# 
#===============================================================================
def test_7():
    print '\---------------------------------------------------------------------------------------------------------------\-'
    print ''
    print 'h4. %s' % 'SolutionName.SLN'
    print ''
    print '|| Primary Trailer | | ||'
    print '|| Checked In CI | | ||'
    print ''
    print '|| Projects Dependency Graph | !SolutionName_DepGraph.png|thumbnail,border=1,width=100! ||'
    print ''
    print '{table-plus}'
    print '|| Projects || Leader || Status || UnitTest to Unicode || Status || Trailer || Status || Linking Status || UnitTest Built x64 || Status ||'
    print '| %s | | | | | | | | | |' % 'ProjectName'
    print '{table-plus}'
    return None


def BuildVCXProjects(solutionPath,
                     projectNames,
                     buildAction='Build',
                     configs=['Debug|Win32', 'Release|Win32', 'UDebug|x64', 'URelease|x64'],
                     displayElapsedTime=False):
    if displayElapsedTime:
        sc = CommonUtils.ScopedTimer(True)

    for cfg in configs:
        for proj in projectNames:
            projectName = proj
            if projectName.lower() == 'ecommon' and (cfg == 'UDebug|x64' or cfg == 'URelease|x64'):
                continue
            if projectName.lower() == 'erasterlib' and (cfg == 'UDebug|x64' or cfg == 'URelease|x64'):
                continue

            # print projectName, cfg
            exitCode = vcxprojUtils.BuildProject(solutionPath, projectName, cfg, buildAction)

            if exitCode != 0:
                return exitCode

    unitTestProjects = []
    for unittest in unitTestProjects:
        for config in configs:
            exitCode = vcxprojUtils.BuildProject(solutionPath, unittest, config, buildAction)
            if exitCode != 0:
                return exitCode

    return 0


def GetDoubleQuotedString(string):
    """
    Returns the double quoted string.
    :param string: String to be double quoted.
    :rtype : str
    """
    return '"' + string + '"'


def RunSystemCommand(cmd):
    """
    Execute the given command.
    :param cmd: Command to execute.
    :param alwaysRun: You can ignore this param.
    :rtype : int
    """
    exitCode = os.system(GetDoubleQuotedString(cmd))
    return exitCode


def Run_ExportECW_Tests(root, platform, configuration, tests):
    print('Root = [%s]' % root)
    print('Config = [%s%s]' % (platform, configuration))
    workingDirectory = r'%s\bin\%s%s' % (root, platform, configuration)
    tests = [
        # ----------------------------- ECW v3 ------------------------------

        # 'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_v3.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile',
        # 'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_v3_iv.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -ignorevalues 0',
        # 'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_v3_iv.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -ignorevalues 0:100',
        # 'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_v3_aoi.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/2-4_ellipse.aoi',
        #
        # 'exportecw.exe -inputfilename f:/data/2-4_NoData.img -outputfilename f:/data/del/2-4_NoData_v3.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile',
        # 'exportecw.exe -inputfilename f:/data/2-4_NoData.img -outputfilename f:/data/del/2-4_NoData_v3_aoi.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/2-4_ellipse.aoi',

        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_v3.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_v3_aoi.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/opacitylayerbug/cn28643_customer.aoi',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_v3_oim.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -orienttomap',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_v3_oim_iv.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -orienttomap -ignorevalues 0',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_v3_oim_aoi.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -orienttomap -vecfile f:/data/opacitylayerbug/cn28643_customer.aoi',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_v3_oim_aoi_1.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -orienttomap -vecfile f:/data/opacitylayerbug/cn28643_customer_oim.aoi',
        # 'exportecw.exe -inputfilename f:/data/tony data/strip1_1.img -outputfilename f:/data/del/strip1_1_aoi_rect.ecw -photointerp Grayscale -compratio 10 -ecwversion 3 -reportfile -vecfile f:/data/tony data/strip1_1_rect.aoi',
        # 'exportecw.exe -inputfilename f:/data/tony data/strip1_1.img -outputfilename f:/data/del/strip1_1_otm_aoi_rect.ecw -photointerp Grayscale -compratio 10 -ecwversion 3 -reportfile -orienttomap -vecfile f:/data/tony data/strip1_1_otm_rect.aoi',
        # 'exportecw.exe -inputfilename f:/data/jira/im-10823/calibrated_img/calibrated.img -outputfilename f:/data/del/calibrated_v3_aoi.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -vecfile f:/data/jira/im-10823/calibrated_img/calibrated.aoi -reportfile',
        # 'exportecw.exe -inputfilename f:/data/jira/im-10823/calibrated_img/calibrated.img -outputfilename f:/data/del/calibrated_v3_otm_aoi_rect.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -orienttomap -vecfile f:/data/jira/im-10823/calibrated_img/calibrated.aoi -reportfile',

        # ----------------------------- ECW v2 ------------------------------

        # 'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_v2.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 2 -reportfile',
        # 'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_v2_iv.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 2 -reportfile -ignorevalues 0',
        # 'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_v2_aoi.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 2 -reportfile -vecfile f:/data/2-4_ellipse.aoi',
        #
        # 'exportecw.exe -inputfilename f:/data/2-4_NoData.img -outputfilename f:/data/del/2-4_NoData_v2.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 2 -reportfile',
        # 'exportecw.exe -inputfilename f:/data/2-4_NoData.img -outputfilename f:/data/del/2-4_NoData_v2_aoi.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 2 -reportfile -vecfile f:/data/2-4_ellipse.aoi',
        #
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_v2.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 2 -reportfile',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_v2_oim.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 2 -reportfile -orienttomap',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_v2_oim_iv.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 2 -reportfile -orienttomap -ignorevalues 0',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_v2_oim_aoi.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 2 -reportfile -orienttomap -vecfile f:/data/opacitylayerbug/cn28643_customer.aoi',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_v3_oim_aoi_1.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -orienttomap -vecfile f:/data/opacitylayerbug/cn28643_customer_oim.aoi',

        # ----------- others ----------------

        # 'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_rect.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/2-4_rect.aoi',
        # 'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_rect.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/2-4_fullimage.aoi',
        # 'exportecw.exe -inputfilename f:/data/306_image_mosaic.img -outputfilename f:/data/del/306_image_mosaic_v3.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile',
        # 'exportecw.exe -inputfilename f:/data/306_image_mosaic.img -outputfilename f:/data/del/306_image_mosaic_v3_iv.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -ignorevalues 0',
        # 'exportecw.exe -inputfilename f:/data/306_image_mosaic.img -outputfilename f:/data/del/306_image_mosaic_v3_sun.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/306_image_mosaic_sun.aoi',
        # 'exportecw.exe -inputfilename f:/data/306_image_mosaic.img -outputfilename f:/data/del/306_image_mosaic_v2_sun.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 2 -reportfile -vecfile f:/data/306_image_mosaic_sun.aoi',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_aoi_rect.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/opacitylayerbug/cn28643_customer.aoi',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_aoi_small_rect.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/opacitylayerbug/cn28643_customer_small_rect.aoi',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_test.img -outputfilename f:/data/del/cn28643_test_v3_iv.ecw -bands 1 2 3 -blocksize 315 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -ignorevalues 0',

        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_test.img -outputfilename f:/data/del/cn28643_test_t8.ecw -bands 1 2 3 -blocksize 315 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/opacitylayerbug/cn28643_customer_small_rect.aoi',
        # 'ReadECWMask.exe -in "f:/data/del/cn28643_test_t8.ecw"',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_test.img -outputfilename f:/data/del/cn28643_test_t1.ecw -bands 1 2 3 -blocksize 315 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/opacitylayerbug/cn28643_customer_small_rect.aoi -nthreads 1',
        # 'ReadECWMask.exe -in "f:/data/del/cn28643_test_t1.ecw"',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_test.img -outputfilename f:/data/del/cn28643_test_otm_t1.ecw -bands 1 2 3 -blocksize 315 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/opacitylayerbug/cn28643_customer_small_rect.aoi -orienttomap -nthreads 1',
        # 'ReadECWMask.exe -in "f:/data/del/cn28643_test_otm_t1.ecw"',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_test.img -outputfilename f:/data/del/cn28643_test_otm_t8.ecw -bands 1 2 3 -blocksize 315 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/opacitylayerbug/cn28643_customer_small_rect.aoi -orienttomap -nthreads 8',
        # 'ReadECWMask.exe -in "f:/data/del/cn28643_test_otm_t8.ecw"',

        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_t8.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/opacitylayerbug/cn28643_customer_small_rect.aoi',
        # 'ReadECWMask.exe -in "F:\Data\Del\cn28643_customer_t8.ecw" -b 0 0 1200 1200',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_t1.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/opacitylayerbug/cn28643_customer_small_rect.aoi -nthreads 1',
        # 'ReadECWMask.exe -in "F:\Data\Del\cn28643_customer_t1.ecw" -b 0 0 1200 1200',
        # 'exportecw.exe -inputfilename f:/data/opacitylayerbug/cn28643_customer.tif -outputfilename f:/data/del/cn28643_customer_oim_smrect.ecw -bands 1 2 3 -blocksize 256 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -orienttomap -vecfile f:/data/opacitylayerbug/cn28643_customer_small_rect.aoi',
        # 'ReadECWMask.exe -in "f:/data/del/cn28643_customer_oim_smrect.ecw" -b 0 0 1200 1200',
        # 'exportecw.exe -inputfilename f:/data/___example_data/dc_ikonos_3band_dd_st.img -outputfilename f:/data/del/dc_ikonos_3band_dd_st_aoi_shapes.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/___example_data/dc_ikonos_3band_dd_st_shapes.aoi',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\Tiff\1000x1000hongkong.tif" -outputfilename "F:\Data\Del\1000x1000_honkong_aoi_img_v2.ecw" -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 2 -orienttomap -vecfile "\\ingrnet.com\in\SGI\geospatial\gs1\erdas\batchtestdata\export\input_data\tiff\honkangdata.aoi"',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\img\1000x1000hongkong.img" -outputfilename "F:\Data\Del\1000x1000hongkong_img_v2.ecw" -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 2 -orienttomap',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\jp2\1000x1000hongkong.jp2" -outputfilename "F:\Data\Del\1000x1000_honkong_aoi_jp2_v2.ecw" -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 2 -orienttomap -vecfile "\\ingrnet.com\in\SGI\geospatial\gs1\erdas\batchtestdata\export\input_data\tiff\honkangdata.aoi"',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\jp2\1000x1000hongkong.jp2" -outputfilename "F:\Data\Del\1000x1000hongkong_jp2_v2.ecw" -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 2 -orienttomap',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\Tiff\1000x1000hongkong.tif" -outputfilename "F:\Data\Del\1000x1000_honkong_aoi_v2.ecw" -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 2 -orienttomap -vecfile "\\ingrnet.com\in\SGI\geospatial\gs1\erdas\batchtestdata\export\input_data\tiff\honkangdata.aoi"',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\Tiff\1000x1000hongkong.tif" -outputfilename "F:\Data\Del\1000x1000hongkong_v2.ecw" -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 2 -orienttomap',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\Tiff\1000x1000hongkong.tif" -outputfilename "F:\Data\Del\1000x1000_honkong_aoi_img_v3.ecw" -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -orienttomap -vecfile "\\ingrnet.com\in\SGI\geospatial\gs1\erdas\batchtestdata\export\input_data\tiff\honkangdata.aoi"',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\img\1000x1000hongkong.img" -outputfilename "F:\Data\Del\1000x1000hongkong_img_v3.ecw" -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -orienttomap',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\jp2\1000x1000hongkong.jp2" -outputfilename "F:\Data\Del\1000x1000_honkong_aoi_jp2_v3.ecw" -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -orienttomap -vecfile "\\ingrnet.com\in\SGI\geospatial\gs1\erdas\batchtestdata\export\input_data\tiff\honkangdata.aoi"',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\jp2\1000x1000hongkong.jp2" -outputfilename "F:\Data\Del\1000x1000hongkong_jp2_v3.ecw" -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -orienttomap',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\Tiff\1000x1000hongkong.tif" -outputfilename "F:\Data\Del\1000x1000_honkong_aoi_v3.ecw" -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -orienttomap -vecfile "\\ingrnet.com\in\SGI\geospatial\gs1\erdas\batchtestdata\export\input_data\tiff\honkangdata.aoi"',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\Tiff\1000x1000hongkong.tif" -outputfilename "F:\Data\Del\1000x1000hongkong_v3.ecw" -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -orienttomap',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\IMG\dc_ikonos_3band_dd_st.img" -outputfilename "F:\Data\Del\ExportEcw_8bit-v3-rgb-maskaoi_x64.ecw" -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -vecfile \\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\IMG\dc_ikonos_3band_dd_st_shapes.aoi',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\IMG\dc_ikonos_3band_dd_st.img" -outputfilename "F:\Data\Del\ExportEcw_8bit-v3-rgb-maskiv0_x64.ecw" -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -ignorevalues 0',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\IMG\dc_ikonos_3band_dd_st.img" -outputfilename "F:\Data\Del\ExportEcw_8bit-v3-rgb-maskiv100-150_x64.ecw" -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -ignorevalues 101:150',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\IMG\dc_ikonos_3band_dd_st.img" -outputfilename "F:\Data\Del\ExportEcw_v2-rgb-maskiv0_x64.ecw" -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 2 -ignorevalues 0',
        # r'exportecw -inputfilename "\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\BatchTestData\EXPORT\INPUT_DATA\IMG\dc_ikonos_3band_dd_st.img" -outputfilename "F:\Data\Del\ExportEcw_v2-rgb-maskiv100-150_x64.ecw" -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 2 -ignorevalues 101:150',

        # --- Subset tests ---
        # r'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_ellipse.ecw -bands 1 2 3 -upperleft 1085282.000 2059610.000 -lowerright 1093986.000 2054234.000 -coordinatetype MAP -photointerp RGB -compratio 20 -ecwversion 3 -reportfile',
        # r'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_rect_bboxcompute.ecw -bands 1 2 3 -upperleft 1085661.066 2060896.766 -lowerright 1093640.392 2052750.308 -coordinatetype MAP -photointerp RGB -compratio 20 -ecwversion 3 -reportfile',
        # r'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_rect_withexpectedbbox.ecw -bands 1 2 3 -upperleft 1085658.000 2060898.000 -lowerright 1093642.000 2052754.000 -coordinatetype MAP -photointerp RGB -compratio 20 -ecwversion 3 -reportfile',
        # r'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_rect1.ecw -bands 1 2 3 -upperleft 1085589.102 2061089.207 -lowerright 1093694.058 2052562.793 -coordinatetype MAP -photointerp RGB -compratio 20 -ecwversion 3 -reportfile',
        # r'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_rect2.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/2-4_rect.aoi',
        # r'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_rect.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/2-4_rect.aoi',
        # r'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_star.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/2-4_star.aoi',
        # r'exportecw.exe -inputfilename f:/data/2-4.img -outputfilename f:/data/del/2-4_ellipse.ecw -bands 1 2 3 -photointerp RGB -compratio 20 -ecwversion 3 -reportfile -vecfile f:/data/2-4_ellipse.aoi',
        # r'exportecw.exe -inputfilename f:/data/63_7385/63_7385.tif -outputfilename f:/data/del/63_7385_otm.ecw -upperleft 1000 1000 -lowerright 4000 4000 -coordinatetype FILE -blocksize 256 -photointerp Grayscale -compratio 10 -ecwversion 3 -reportfile -orienttomap',
        # r'exportecw.exe -inputfilename f:/data/63_7385/63_7385.tif -outputfilename f:/data/del/63_7385_otm.ecw -upperleft 1000 1000 -lowerright 4000 4000 -coordinatetype FILE -blocksize 256 -photointerp Grayscale -compratio 10 -ecwversion 3 -reportfile -orienttomap',
        # r'ECWEncoderGDS -in "f:/data/2-4.img" -out "f:/data/del/2-4_ecwencodergds.ecw"',

        # ----------------------------- ExportECW performance test with VMCx dataset -----------------------------------
        r'exportecw.exe -inputfilename f:/data/img-rle-external-rrd/306_image_mosaic.img -outputfilename f:/data/del/306_image_mosaic.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -pixelsize 0.5 -resample "Nearest Neighbor" -noDataColor Black -reportfile -nthreads 8 -encodeCache 100',
        # r'exportecw.exe -inputfilename f:/data/img-rle-external-rrd/306_imgs.vmcx -outputfilename f:/data/del/306_imgs.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -pixelsize 0.5 -resample "Nearest Neighbor" -noDataColor Black -reportfile -nthreads 8 -encodeCache 100',
        # r'exportecw.exe -inputfilename f:/data/img-rle-external-rrd/singlemosaicimg_1.vmcx -outputfilename f:/data/del/singlemosaicimg_1.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -pixelsize 0.5 -resample "Nearest Neighbor" -noDataColor Black -reportfile -nthreads 8 -encodeCache 100',
        # r'exportecw.exe -inputfilename f:/data/img-rle-external-rrd/twentyoverlap/306_images.vmcx -outputfilename f:/data/del/306_images.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -pixelsize 0.5 -resample "Nearest Neighbor" -noDataColor Black -reportfile -nthreads 8 -encodeCache 100',
    ]
    print('workingDirectory = [%s]' % workingDirectory)
    prevCD = os.getcwd()
    os.chdir(workingDirectory)

    for test in tests:
        print('Executing test = [%s]' % test)
        startTime = datetime.datetime.now()
        print('StartTime = [%s]' % startTime)
        exitCode = RunSystemCommand(test)
        finishTime = datetime.datetime.now()
        print('FinishTime = [%s]' % finishTime)
        print('Time taken = [%s]' % (finishTime - startTime))
        if exitCode:
            print('exitCode = [%d]' % exitCode)

    os.chdir(prevCD)
    return 0

def BuildECWJP2IMAGINE():
    sln = r'E:\Build\Generation_3\lg_Solutions\ECWJP2_IMAGINE.sln'
    projs = ['ecwjp2_sdk', 'eecwjp2', 'eecwjp2UnitTest', 'rf_ecw', 'rf_ecwUnitTest', 'rf_jp2', 'rf_jp2UnitTest', 'ej2k',
             'ecwopacity', 'exportecw', 'exportjp2']
    projs = ['ecwjp2_sdk', 'eecwjp2', 'rf_ecw', 'rf_jp2', 'ej2k', 'ecwopacity', 'exportecw', 'exportjp2']

    exitCode = 0
    exitCode = exitCode or BuildVCXProjects(solutionPath=sln, projectNames=projs, buildAction='build', configs=['Release|Win32'])
    exitCode = exitCode or BuildVCXProjects(solutionPath=sln, projectNames=projs, buildAction='build', configs=['URelease|x64'])
    exitCode = exitCode or BuildVCXProjects(solutionPath=sln, projectNames=projs, buildAction='build', configs=['Debug|Win32'])
    exitCode = exitCode or BuildVCXProjects(solutionPath=sln, projectNames=projs, buildAction='build', configs=['UDebug|x64'])
    # vcxprojUtils.BuildSolution(sln, 'Release|Win32')
    # vcxprojUtils.BuildSolution(sln, 'Debug|Win32')
    # vcxprojUtils.BuildSolution(sln, 'URelease|x64')
    # vcxprojUtils.BuildSolution(sln, 'UDebug|x64')
    return exitCode

def BuildECWJP2ERMapper():
    sln = r'E:\Build\Generation_3\lg_Solutions\ECWJP2_ERMapper.sln'
    projs = ['ERMapperLib_NG', 'ecw', 'ecw_compress', 'ecw_compress_gui', 'ecw_opacity_builder',
             'ecw_report', 'erswarp']

    exitCode = 0
    exitCode = exitCode or BuildVCXProjects(solutionPath=sln, projectNames=projs, buildAction='build', configs=['Release|Win32'])
    exitCode = exitCode or BuildVCXProjects(solutionPath=sln, projectNames=projs, buildAction='build', configs=['Debug|Win32'])
    # vcxprojUtils.BuildSolution(sln, 'Release|Win32')
    # vcxprojUtils.BuildSolution(sln, 'Debug|Win32')
    # vcxprojUtils.BuildSolution(sln, 'URelease|x64')
    # vcxprojUtils.BuildSolution(sln, 'UDebug|x64')
    return exitCode


def BuildUnitTestSolutions():
    solutions = [
        # r'E:\Build\Generation_3\sources_rdo\erasterlib\UnitTest\erasterlibUnitTest.sln',
        r'E:\Build\Generation_3\sources_rdo\eecwjp2\UnitTest\eecwjp2UnitTest.sln',
        r'E:\Build\Generation_3\sources_rdo\rf_ecw\UnitTest\rf_ecwUnitTest.sln'
    ]

    for sln in solutions:
        exitCode = 0
        exitCode = exitCode or vcxprojUtils.BuildSolution(sln, 'Release|Win32')
        exitCode = exitCode or vcxprojUtils.BuildSolution(sln, 'Debug|Win32')
        exitCode = exitCode or vcxprojUtils.BuildSolution(sln, 'URelease|x64')
        exitCode = exitCode or vcxprojUtils.BuildSolution(sln, 'UDebug|x64')
        if exitCode != 0:
            print('ERROR: Failed to build failed on sln [%s]' % sln)


def main():
    sc = CommonUtils.ScopedTimer(displayExtraInfo=True)
    # Add Cygwin's bin (nm is required to be in path) path
    # if addCygwinToPath() == False:
    #     print "Cygwin's is not installed"
    vc_env = query_vsvarsall(12)
    # for key in vc_env:
    #     print('%s = %s' % (key, vc_env[key]))
    print('Path = %s' % os.environ["Path"])
    os.environ['path'] = vc_env["path"]
    print('Path = %s' % os.environ["Path"])

    sln = r'E:\Build\Generation_3\lg_Solutions\Test.sln'
    projs = ['rf_png', 'rf_jfif', 'rf_tiff']

    buildAction = 'build'
    exitCode = 0
    # exitCode = exitCode or BuildVCXProjects(solutionPath=sln, projectNames=projs, buildAction=buildAction, configs=['Release|Win32'])
    # exitCode = exitCode or BuildVCXProjects(solutionPath=sln, projectNames=projs, buildAction=buildAction, configs=['URelease|x64'])
    # exitCode = exitCode or BuildVCXProjects(solutionPath=sln, projectNames=projs, buildAction=buildAction, configs=['Debug|Win32'])
    # exitCode = exitCode or BuildVCXProjects(solutionPath=sln, projectNames=projs, buildAction=buildAction, configs=['UDebug|x64'])

    # exitCode = BuildVCXProjects('Build', ['Debug|Win32', 'Release|Win32'])
    # print('exitCode of BuildVCXProjects = [%d]' % exitCode)
    # RunSystemCommand('robocopy E:\\Build\\Generation_3\\root\\usr\\lib\\Win32Release\\RasterFormats \"C:\\Program Files\\Hexagon\\ERDAS IMAGINE 2015\\usr\\lib\\Win32Release\\rasterformats\" srp.dll /NJH /NJS /NP')
    # RunSystemCommand('robocopy E:\\Build\\Generation_3\\root\\usr\\lib\\x64URelease\\RasterFormats \"C:\\Program Files\\Hexagon\\ERDAS IMAGINE 2015\\usr\\lib\\x64URelease\\rasterformats\" srp.dll /NJH /NJS /NP')

    # if exitCode != 0:
    #     exitCode = BuildVCXProjects('Rebuild', platform=platform, configuration=configuration)
    #     print('exitCode of BuildVCXProjects = [%d]' % exitCode)

    # ------------------------------------------------------------------------------
    # Run tests
    # ------------------------------------------------------------------------------

    # workingDirectory = r'E:\Build\IM_2014\root\bin\Win32Release'
    # workingDirectory = r'E:\Build\IM_2014\root\bin\%s%s' % (platform, configuration)
    # workingDirectory = r'E:\Build\IM_2014\root\bin\Win32Debug'

    tests = [
        # r'exportecw.exe -inputfilename f:/data/img-rle-external-rrd/306_image_mosaic.img -outputfilename f:/data/del/306_image_mosaic.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -pixelsize 0.5 -resample "Nearest Neighbor" -noDataColor Black -reportfile -nthreads 8 -encodeCache 100',
        r'exportecw.exe -inputfilename f:/data/img-rle-external-rrd/306_imgs.vmcx -outputfilename f:/data/del/306_imgs.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -pixelsize 0.5 -resample "Nearest Neighbor" -noDataColor Black -reportfile -nthreads 8 -encodeCache 100',
        # r'exportecw.exe -inputfilename f:/data/img-rle-external-rrd/singlemosaicimg_1.vmcx -outputfilename f:/data/del/singlemosaicimg_1.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -pixelsize 0.5 -resample "Nearest Neighbor" -noDataColor Black -reportfile -nthreads 8 -encodeCache 100',
        # r'exportecw.exe -inputfilename f:/data/img-rle-external-rrd/twentyoverlap/306_images.vmcx -outputfilename f:/data/del/306_images.ecw -bands 1 2 3 -blocksize 512 -photointerp RGB -compratio 20 -ecwversion 3 -pixelsize 0.5 -resample "Nearest Neighbor" -noDataColor Black -reportfile -nthreads 8 -encodeCache 100',
    ]
    # root = r'C:\Program Files\Intergraph\ERDAS IMAGINE 2015'
    # Run_ExportECW_Tests(root, 'x64', "URelease", tests)

    # root = r'E:\Build\Generation_3\root'
    # Run_ExportECW_Tests(root, 'x64', "URelease", tests)
    # test_GetPOMFilesFromBO()
    return exitCode


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    print(info.center(79, '-'))
    exitCode = main()
    print('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    print(info.center(79, '-'))
    sys.exit(exitCode)
