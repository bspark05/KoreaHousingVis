'''
Created on Mar 15, 2016

@author: Administrator
'''
import shapefile
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.lines as mlines
from matplotlib.collections import PatchCollection
import numpy as np

## Basemap List
# polygon (path, facecolor, edgecolor, linewidths(double))
basemapPolygonList = [
                        ["shapefiles/Submarket", "None", "k", .1],
                        ["shapefiles/HanRiverSmo", "#BDDFE9", "None", .1]
                        ]

# point (path, color, size(double), shape, edgecolor, label)
basemapPointList = [
                    ["shapefiles/SubwayStation", "k", 6, "x", "k", "Subway stations" ]
                    ]

# line (paht, color, linewidth, label)
basemapLineList = [
                   ["shapefiles/SubwaySmo", "#7B8082", .5, None]
                   ]

# map elements
basemapElements = ["shapefiles/mapelements2.png"]

basemapRange = ["shapefiles/Submarket"]







# input - path of shapefile (string) / output - list of minX, maxX, minY, and maxY
def findRange(shpFile):
    sf=shapefile.Reader(shpFile)
    
    shapes  = sf.shapes()
    Nshp    = len(shapes)
    
    minX = 99999999999999999
    minY = 99999999999999999
    maxX = -99999999999999999
    maxY = -99999999999999999
    
    for nshp in xrange(Nshp):
        pts     = np.array(shapes[nshp].points)
        
        for xy in pts :
            if minX > xy[0]: # if x value is smaller than minX
                minX = xy[0]
            if minY > xy[1]:
                minY = xy[1]
            if maxX < xy[0]:
                maxX = xy[0]
            if maxY < xy[1]:
                maxY = xy[1]
    
    return [minX, maxX, minY, maxY]


def addShpPolygon(shpFile, shpScheme, ax):
    sf=shapefile.Reader(shpFile)
    
    shapes  = sf.shapes()
    Nshp    = len(shapes)
    
    for nshp in xrange(Nshp):
        ptchs   = []
        pts     = np.array(shapes[nshp].points)
        prt     = shapes[nshp].parts
        par     = list(prt) + [pts.shape[0]]
        for pij in xrange(len(prt)):
            ptchs.append(Polygon(pts[par[pij]:par[pij+1]]))
        ax.add_collection(PatchCollection(ptchs,facecolor=shpScheme[0],edgecolor=shpScheme[1], linewidths=shpScheme[2]))

def addShpPoint(shpFile, shpSchem, ax):
    sf=shapefile.Reader(shpFile)
    
    shapes  = sf.shapes()
    Nshp    = len(shapes)
    
    Xcoord = []
    Ycoord = []
    
    for nshp in xrange(Nshp):
        pts = shapes[nshp].points
        
        Xcoord.append(pts[0][0])
        Ycoord.append(pts[0][1])
    
    ax.scatter(Xcoord, Ycoord, c=shpSchem[0], s=shpSchem[1], marker = shpSchem[2], edgecolors = shpSchem[3], label = shpSchem[4])
    
def addShpLine(shpFile, shpSchem, ax):
    sf=shapefile.Reader(shpFile)
    
    Xcoord = []
    Ycoord = []
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        
        Xcoord.append(x)
        Ycoord.append(y)
        ax.plot(x,y, color = shpSchem[0], linewidth = shpSchem[1], label = shpSchem[2])
    ax.plot(x,y, color = shpSchem[0], linewidth = shpSchem[1], label = 'Subway lines')
    
    
def addBasemap(basemapRange, basemapPolygonList, basemapLineList, basemapPointList, basemapElements, ax):
    rangeList = [-1, -1, -1, -1]
    
    if len(basemapPolygonList) > 0:
        rangeList = findRange(basemapRange[0])
        for basemap in basemapPolygonList:
            addShpPolygon(basemap[0], basemap[1:], ax)
    
    if len(basemapLineList) > 0:
        for basemap in basemapLineList:
            addShpLine(basemap[0], basemap[1:], ax)
            
    if len(basemapPointList) > 0:
        for basemap in basemapPointList:
            addShpPoint(basemap[0], basemap[1:], ax)
            
    im = plt.imread(basemapElements[0])
    ax.imshow(im, zorder = 0, extent=[rangeList[0],rangeList[1],rangeList[2],rangeList[3]])
    
        
    return rangeList 