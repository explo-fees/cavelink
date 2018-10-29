# encoding: utf-8

# Goal
# 1. Get Cavelink data
# 2. Display data, console output

###############################################################################
# Imports
import os
import sys
sys.path.append(os.getcwd()+'/../')
import cavelink

###############################################################################
# Configuration

SLUMP_MOTIERS_URL = 'http://www.cavelink.com/cl/da.php?s=106&g=1&w=101&l=20'
MOTIERS_SLUMP_DESC = 'Water Level in Motiers'

###############################################################################
# Functions



###############################################################################
# Program

motiers_Water_Level = cavelink.Sensor(URL=SLUMP_MOTIERS_URL, rows=3)

# Insert each dict line into database
print(MOTIERS_SLUMP_DESC)

for key, value in motiers_Water_Level.getData().items():
   print(key, value)
