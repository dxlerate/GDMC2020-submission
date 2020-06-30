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
    # Replaces grass with tnt
    # for x, y, z in box.positions:
        
    #     # the below lines would need to be nested in one of the above two so that x, y and z are defined
    #     if level.blockAt(x, y, z) == 2: # will check if the block id that is at (x, y, z) is equal to 2. If true it will run the lines below
    #         level.setBlockAt(x, y, z, 46) # This will set the block at (x, y, z) to 46
        
    #     level.blockDataAt(x, y, z) # takes the value of the block data at (x, y, z)
    #     level.setBlockDataAt(x, y, z, 0) # Will set the block data at (x, y, z) to 0
                    
    #     # tell MCedit that the selection box has been modified
    #     level.markDirtyBox(box)

    # Replaces ground surface with tnt
    NONSURFACEBLOCKS = [0, 6, 17, 18, 30, 31, 32, 37, 38, 39, 40, 50, 51, 59, 63, 64, 78, 81, 83, 85, 86, 91, 99, 100, 103, 104, 105, 106, 111, 127, 141, 142, 161, 162, 175]
    for x in xrange(box.minx, box.maxx):
        for z in xrange(box.minz, box.maxz):
            for y in xrange(box.maxy, 0, -1):
                tempBlock = level.blockAt(x, y, z)
                if tempBlock not in NONSURFACEBLOCKS:
                    utilityFunctions.setBlock(level, (46, 0), x, y+1, z)
                    break;

