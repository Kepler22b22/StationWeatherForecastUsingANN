#!/usr/bin/python3
## Note: ONLY /usr/bin/python3 has pygrib package installed correctly

import pygrib
import numpy as np
import netCDF4 as nc
import sys

### DEFINE LAT LON AREA ###
latbegin = 41
latend   = 41
num_lat  = latend-latbegin+1
lonbegin = 115
lonend   = 115
num_lon  = lonend-lonbegin+1

### OPEN GRIB FILE###
agument = sys.argv
filenamein = str(agument[1])
filenameout= str(agument[2])
fin  = pygrib.open(filenamein)
# LIST ALL VARIABLES
#for var in fin: print(var)

##### GET VARIABLES AND AREA #####

var  = fin.select(name='Surface pressure',typeOfLevel='surface',level=0)[0]
var30_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='2 metre temperature',typeOfLevel='heightAboveGround',level=2)[0]
var31_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='2 metre relative humidity',typeOfLevel='heightAboveGround',level=2)[0]
var34_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='10 metre U wind component',typeOfLevel='heightAboveGround',level=10)[0]
var37_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='10 metre V wind component',typeOfLevel='heightAboveGround',level=10)[0]
var38_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)


var  = fin.select(name='Total Cloud Cover',paramId=228164)[3]
#[3]here,means the forth tcc in grib2,which is the whole atmosphere tcc,the fore three are low-middle-high tcc.
var44_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Total Precipitation',typeOfLevel='surface',level=0)[0]
var45_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Downward short-wave radiation flux',typeOfLevel='surface',level=0)[0]
var46_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Downward long-wave radiation flux',typeOfLevel='surface',level=0)[0]
var47_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Upward short-wave radiation flux',typeOfLevel='surface',level=0)[0]
var48_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Upward long-wave radiation flux',typeOfLevel='surface',level=0)[0]
var49_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)

fin.close()

##### CREATE NC FILE ##### 
fout = nc.Dataset(filenameout,"w",format="NETCDF4")
## define dimesions
longi  = fout.createDimension('longitude',size=num_lon)
lati   = fout.createDimension('latitude',size=num_lat)

## define variables for storing data
lon   = fout.createVariable('lon_3','f4',dimensions='longitude')
lat   = fout.createVariable('lat_3','f4',dimensions='latitude')

p_sfc   = fout.createVariable('p_sfc',  'f4',dimensions=['latitude','longitude'])
t2m     = fout.createVariable('t2m',    'f4',dimensions=['latitude','longitude'])
rh2m    = fout.createVariable('rh2m',   'f4',dimensions=['latitude','longitude'])
u10m    = fout.createVariable('u10m',   'f4',dimensions=['latitude','longitude'])
v10m    = fout.createVariable('v10m',   'f4',dimensions=['latitude','longitude'])
tcc_ave3        = fout.createVariable('tcc_ave3','f4',dimensions=['latitude','longitude'])
prep_sfc_ave3   = fout.createVariable('prep_sfc_ave3',  'f4',dimensions=['latitude','longitude'])
dswave_ave3   = fout.createVariable('dswave_ave3',  'f4',dimensions=['latitude','longitude'])
dlwave_ave3   = fout.createVariable('dlwave_ave3',  'f4',dimensions=['latitude','longitude'])
uswave_ave3   = fout.createVariable('uswave_ave3',  'f4',dimensions=['latitude','longitude'])
ulwave_ave3   = fout.createVariable('ulwave_ave3',  'f4',dimensions=['latitude','longitude'])

## add data to variables                
lon[:] = np.linspace(lonbegin,lonend,lonend-lonbegin+1)
lat[:] = np.linspace(latend,latbegin,latend-latbegin+1) #attention! Don't reverse the sequence

p_sfc[:]   = var30_area
t2m[:]     = var31_area
rh2m[:]    = var34_area
u10m[:]    = var37_area
v10m[:]    = var38_area
tcc_ave3[:]         = var44_area
prep_sfc_ave3[:]    = var45_area
dswave_ave3[:]      = var46_area
dlwave_ave3[:]      = var47_area
uswave_ave3[:]      = var48_area
ulwave_ave3[:]      = var49_area

## add attributes
#global attributes
fout.description = "GFS GRIB2 Chinese area and variables extract, Xinyu Wen, Yonglin Qu, 06-25-2020"
#variable attribute
lon.description  = 'longitude,west is negative'
lon.units        = 'degrees_east'
lon.long_name    = 'longitude'
lat.description  = 'latitude,south is negative'
lat.units        = 'degrees_north'
lat.long_name    = 'latitude'

p_sfc.description    = 'Pressure at surface'
p_sfc.long_name      = 'Pressure'          
#p_sfc.units          = 'Pa'                    
t2m.description      = 'Temperature at 2 metre'
t2m.long_name        = 'Temperature'          
t2m.units            = 'K'                    
rh2m.description     = 'Relative humidity at 2 metre'
rh2m.long_name       = 'Relative humidity'          
rh2m.units           = '%'                    
u10m.description     = 'u-component of wind at 10 metre'
u10m.long_name       = 'u-component of wind'          
u10m.units           = 'm/s'                    
v10m.description     = 'v-component of wind at 10 metre'
v10m.long_name       = 'v-component of wind'          
v10m.units           = 'm/s'                    
tcc_ave3.description = 'Total Cloud Cover'
tcc_ave3.long_name   = 'Total Cloud Cover'          
tcc_ave3.units       = '%'                    

prep_sfc_ave3.description  = 'Total precipitation at surface'
prep_sfc_ave3.long_name    = 'Total precipitation'          
prep_sfc_ave3.units        = 'kg/m^2'                    
dswave_ave3.description    = 'Downward short wave flux' 
dswave_ave3.long_name      = 'Downward short wave flux'
dswave_ave3.units          = 'W/m^2'                   
dlwave_ave3.description    = 'Downward long wave flux'
dlwave_ave3.long_name      = 'Downward long wave flux'
dlwave_ave3.units          = 'W/m^2'                   
uswave_ave3.description    = 'Upward short wave flux'
uswave_ave3.long_name      = 'Upward short wave flux'
uswave_ave3.units          = 'W/m^2'                   
ulwave_ave3.description    = 'Upward long wave flux'
ulwave_ave3.long_name      = 'Upward long wave flux'
ulwave_ave3.units          = 'W/m^2'                   

fout.close()
print(filenamein[:-4]+' is done')

