#   drakeliang@utexas.edu

import time # for timing
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
from random import *
from numpy import *
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *

import utilityFunctions as utilityFunctions

inputs = (
	("AAAAAAAAAAA", "label"),
	("Creator: Drake Liang", "label"),
	)

def perform(level, box, options):
    z_len = box.maxz - box.minz
    x_len = box.maxx - box.minx
    surfaceLevel = [[0 for x in range(z_len)] for x in range(x_len)]
    biomes = [[0 for x in range(z_len)] for x in range(x_len)] 
    for x in xrange(x_len):
        for z in xrange(z_len):
            world_x = x + box.minx
            world_z = z + box.minz
            surfaceLevel[x][z] = getSurfaceLevel(level, box, world_x, world_z)
            biomes[x][z] = level.getChunk((world_x)//16, (world_z)//16).Biomes[(world_z) % 16,(world_x) % 16]
            utilityFunctions.setBlock(level, (biomes[x][z], 0), world_x, surfaceLevel[x][z]+1, world_z)

def getSurfaceLevel(level, box, world_x, world_z):
    # Returns y value of serface at coordinate
    NONSURFACEBLOCKS = [0, 6, 17, 18, 30, 31, 32, 37, 38, 39, 40, 50, 51, 59, 63, 64, 78, 81, 83, 85, 86, 91, 99, 100, 103, 104, 105, 106, 111, 127, 141, 142, 161, 162, 175]
    for y in xrange(box.maxy, 0, -1):
        tempBlock = level.blockAt(world_x, y, world_z)
        if tempBlock not in NONSURFACEBLOCKS:
            return y

def printNestedList(target):
    for xs in target:
        print(" ".join(map(str, xs)))

# -------------------------
# UNUSED:
# Replaces ground surface with tnt
# for x in xrange(box.minx, box.maxx):
#     for z in xrange(box.minz, box.maxz):
#         for y in xrange(box.maxy, 0, -1):
#             tempBlock = level.blockAt(x, y, z)
#             if tempBlock not in NONSURFACEBLOCKS:
#                 utilityFunctions.setBlock(level, (46, 0), x, y+1, z)
#                 break;
