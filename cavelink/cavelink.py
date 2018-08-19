# coding=utf-8

# Published 2016
# Author : sebastien at pittet dot org
# Public domain source code, under MIT License

"""
This API provides access to Cave-Link data. It has some interest for cavers.
Following libraries are required :
    $ pip install python-dateutil requests
"""

from dateutil.parser import *
from collections import OrderedDict
import time
import re  # to use regular expression in python
import requests
import sys

# ########################## Common definitions #########################
# Some examples of URL
_CL_NIVEAU_S2_COVA = "http://www.cavelink.com/cl/da.php?s=115&g=1&w=103&l=10"
_CL_NIVEAU_LANCELEAU = "http://www.cavelink.com/cl/da.php?s=142&g=20&w=100&l=10"
_CL_TEMP_SIPHON = "http://www.cavelink.com/cl/da.php?s=106&g=1&w=0&l=10"
_CL_V_FEES_SUR1 = "http://www.cavelink.com/cl/da.php?s=142&g=0&w=0&l=10"
_CL_TEMP_FEES_SUR1 = "http://www.cavelink.com/cl/da.php?s=142&g=10&w=1&l=10"

# Default definitions
default_CL = _CL_NIVEAU_LANCELEAU
default_rows = '10'

#########################################################################


class Cavelink:

    """
    Parse the webpage used to export the data and
    provides values back.
    """

    def __init__(self, URL=default_CL, rows=default_rows):
        # Replace number of rows, if provided
        URL = re.sub('(?<=l=)\d{1,}', str(rows), URL)

        try:
            webpage = requests.get(URL)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        # Get the HTML page
        htmlContent = webpage.text

        self.rawData = htmlContent.replace(",", "")  # remove separator (,)
        self.data = htmlContent.split("<br>")

        for line in self.data:

            match = re.search('(?<=Stn=)\d{1,}', line)
            if match:
                self.station = match.group(0)

            match = re.search('(?<=Grp=)\d{1,}', line)
            if match:
                self.group = match.group(0)

            match = re.search('(?<=Nr=)\d{1,}', line)
            if match:
                self.number = match.group(0)

            match = re.search('(?<=Einheit : )\S{1,}', line)
            if match:
                self.unit = match.group(0).upper()  # uppercase (C | M | ?)

    def station(self):
        return self.station

    def group(self):
        return self.group

    def number(self):
        return self.number

    def unit(self):
        return self.unit

    def getData(self):
        DictValues = {}

        for line in self.data:
            if IsNotNull(line):
                epochDatetime = findDate(line[0:16])
                if epochDatetime > 0:
                    # a date was found on this line
                    # insert value in dict with epoch as key
                    DictValues[epochDatetime] = float(line[17:])
        # order the dict by key (epoch)
        return OrderedDict(sorted(DictValues.items()))

# ###################### SOME USEFUL TOOLS ###############################


def IsNotNull(value):
    return value is not None and len(value) > 0


def toEpoch(value):
    return int(time.mktime(time.strptime(value, "%Y-%m-%d %H:%M:%S")))


def findDate(inputValue):
    try:
        DateTimeString = str(parse(inputValue, ignoretz=True, dayfirst=True))
    except Exception:
        # if not found, epoch = 0
        DateTimeString = "1970-01-01 00:00:00"

    # Convert to epoch date time and return the value
    return toEpoch(DateTimeString)


def toHumanTime(epoch):
    return time.strftime("%d.%m.%Y %H:%M", time.localtime(float(epoch)))

######################################################################


# auto-test when executed directly

if __name__ == "__main__":

    from sys import exit, stdout

    # If launched interactively, display OK message
    if stdout.isatty():
        # Get last value measured/transmitted (by asking only 1 last row)
        SlumpTemperature = Cavelink(URL=_CL_NIVEAU_LANCELEAU, rows=10)
        Data = SlumpTemperature.getData()

        print('################################################')
        print('Station ID is: %s' % SlumpTemperature.station)
        print('Group ID is: %s' % SlumpTemperature.group)
        print('Number is: %s' % SlumpTemperature.number)
        print('Unit for this data set is: %s\n---' % SlumpTemperature.unit)

        for key, value in Data.items():
            LastDataValue = value
            LastDataTime = toHumanTime(str(key))
            print('%s : %s %s' % (LastDataTime,
                                  LastDataValue,
                                  SlumpTemperature.unit))

        print('################################################')

    exit(0)
