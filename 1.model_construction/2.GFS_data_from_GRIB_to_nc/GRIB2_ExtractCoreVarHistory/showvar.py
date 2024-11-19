#!/usr/bin/python3

import pygrib
import numpy as np
import netCDF4 as nc
import sys

### DEFINE LAT LON AREA ###
latbegin = 15
latend   = 55
num_lat  = latend-latbegin+1
lonbegin = 70
lonend   = 140
num_lon  = lonend-lonbegin+1

### OPEN GRIB FILE###
filenamein = "gfs_3_20200301_0000_009.grb2"
fin  = pygrib.open(filenamein)
# LIST ALL VARIABLES
i=0
for var in fin: 
    i = i+1
    if i==483 or i==482 or i==481 or i==480 or i==479:
    #if i==246:
        '''
        print(var)
        for i in range(len(var.keys())):
            print(var.keys()[i]+':')
            print(var.var.keys([i]))
        a = var.keys()[0]
        print(a)
        print(var.a)
        '''
        print(var)
        #print(var.typeOfLevel)
        #print(var.level)
        #print(var.name)
        #print(var.shortName)
        print(var.paramId)
'''
for var in fin:
    print(var)
'''
