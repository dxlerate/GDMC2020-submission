#   drakeliang@utexas.edu

import time # for timing
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
from random import *
from numpy import *
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *

import utilityFunctions as utilityFunctions

inputs = (
	("BasicTest", "label"),
	("Creator: Drake Liang", "label"),
    ("drakeliang@utexas.edu", "label"),
	)

def perform(level, box, options):
    surfaceLevel = getSurfaceLevel(level, box)
    cols_count = box.maxz - box.minz
    rows_count = box.maxx - box.minx
    for x in xrange(rows_count):
        for z in xrange(cols_count):
            utilityFunctions.setBlock(level, (41, 0), x + box.minx, surfaceLevel[x][z]+1, z + box.minz)

def getSurfaceLevel(level, box):
    # Returns list of surface y values
    NONSURFACEBLOCKS = [0, 6, 17, 18, 30, 31, 32, 37, 38, 39, 40, 50, 51, 59, 63, 64, 78, 81, 83, 85, 86, 91, 99, 100, 103, 104, 105, 106, 111, 127, 141, 142, 161, 162, 175]
    cols_count = box.maxz - box.minz
    rows_count = box.maxx - box.minx
    surfaceLevel = [[0 for x in range(cols_count)] for x in range(rows_count)] 
    for x in xrange(rows_count):
        for z in xrange(cols_count):
            for y in xrange(box.maxy, 0, -1):
                tempBlock = level.blockAt(x + box.minx, y, z + box.minz)
                if tempBlock not in NONSURFACEBLOCKS:
                    surfaceLevel[x][z] = y
                    break;
    return surfaceLevel


# Replaces ground surface with tnt
# NONSURFACEBLOCKS = [0, 6, 17, 18, 30, 31, 32, 37, 38, 39, 40, 50, 51, 59, 63, 64, 78, 81, 83, 85, 86, 91, 99, 100, 103, 104, 105, 106, 111, 127, 141, 142, 161, 162, 175]
# for x in xrange(box.minx, box.maxx):
#     for z in xrange(box.minz, box.maxz):
#         for y in xrange(box.maxy, 0, -1):
#             tempBlock = level.blockAt(x, y, z)
#             if tempBlock not in NONSURFACEBLOCKS:
#                 utilityFunctions.setBlock(level, (46, 0), x, y+1, z)
#                 break;
