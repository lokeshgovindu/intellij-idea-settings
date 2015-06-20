import os
import sys

# GDAL/OGR
import gdal
import osgeo.ogr


def main():
    filePath = r'C:\Data\Shapefiles\tl_2009_us_state\tl_2009_us_state.shp'
    shapefile = osgeo.ogr.Open(filePath)
    numLayers = shapefile.GetLayerCount()
    print('NumLayers = [%d]' % numLayers)
    layer = shapefile.GetLayer(0)
    numFeatures = layer.GetFeatureCount()
    print('NumFeatures = [%d]' % numFeatures)
    for featureNum in xrange(numFeatures):
        feature = layer.GetFeature(featureNum)
        featureName = feature.GetField('NAME')
        print('Feature %d has name %s' % (featureNum, featureName))
        # for key, value in feature.items().items():
        #     print(key, value)
        geometry = feature.GetGeometryRef()
        geometryName = geometry.GetGeometryName()
        print('GeometryName = [%s]' % geometryName)
        print('-' * 79)

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
