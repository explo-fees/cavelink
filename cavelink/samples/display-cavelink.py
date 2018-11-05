# encoding: utf-8

# Goal
# 1. Get Cavelink data
# 2. Display data, console output

###############################################################################
# Imports
import os
import sys
sys.path.append(os.getcwd()+'/../')
from cavelink import cavelink
import json

###############################################################################
# Configuration

SLUMP_MOTIERS_URL = 'http://www.cavelink.com/cl/da.php?s=106&g=1&w=101&l=20'
MOTIERS_SLUMP_DESC = 'Water Level in Motiers'

###############################################################################
# Functions

###############################################################################
# Program

motiers = cavelink.Sensor(URL=SLUMP_MOTIERS_URL,
                          rows=3)

# Display data
print(MOTIERS_SLUMP_DESC)

water_level = motiers.getJSON(datefmt='human')
water_level_json = json.loads(water_level)

# parse measures
for timestamp in water_level_json['measures']:
    print('%s -> %s %s' % (timestamp,
                           water_level_json['measures'][timestamp],
                           water_level_json['sensor']['unit']))
