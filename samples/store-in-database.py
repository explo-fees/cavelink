# encoding: utf-8

# Goal
# 1. Get Cavelink data
# 2. Store it in a database (SQLite)

###############################################################################
# Imports
import os
import sys
sys.path.append(os.getcwd()+'/../')
import lcavelink
import sqlite3

###############################################################################
# Configuration

DATABASE = os.path.join(os.getcwd(), 'cavelink.db')
DB_SCHEMA = os.path.join(os.getcwd(), 'schema.sql')
SLUMP_MOTIERS_URL = 'http://www.cavelink.com/cl/da.php?s=106&g=1&w=101&l=20'
MOTIERS_SLUMP_DESC = 'Water Level in Motiers'

###############################################################################
# Functions

def initialize_db():
    if os.path.isfile(DATABASE):
        print('Error in initialize_db: Cannot initialize database. File already exists.')
    else:
        # Create database connection
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.executescript(open(DB_SCHEMA, 'r').read())


###############################################################################
# Program

motiers_Water_Level = lcavelink.Cavelink(URL=SLUMP_MOTIERS_URL, rows=100)

create_sensor_query = 'INSERT OR IGNORE INTO SENSORS (Unit, Description) VALUES ("%s", "%s")' % (motiers_Water_Level.unit, MOTIERS_SLUMP_DESC)

# Initialize database if database doesn't exist.
initialize_db()

# Insert data in database
conn = sqlite3.connect(DATABASE)
conn.execute(create_sensor_query)

# Insert each dict line into database
for key, value in motiers_Water_Level.getData().iteritems():
    sql_insert = 'INSERT OR IGNORE INTO DATA (Epoch, Value, Sensor)\
                  SELECT %s, %s, sensors.id \
                  FROM sensors \
                  WHERE Description="Water Level in Motiers"' % (key, value)
    conn.execute(sql_insert)

conn.commit()
conn.close()
