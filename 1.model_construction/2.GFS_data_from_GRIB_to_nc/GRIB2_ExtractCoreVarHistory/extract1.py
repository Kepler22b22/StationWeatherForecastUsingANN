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
agument = sys.argv
filenamein = str(agument[1])
filenameout= str(agument[2])
fin  = pygrib.open(filenamein)
# LIST ALL VARIABLES
#for var in fin: print(var)

##### GET VARIABLES AND AREA #####
var  = fin.select(name='Geopotential Height',typeOfLevel='isobaricInhPa',level=200)[0]
var1_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Geopotential Height',typeOfLevel='isobaricInhPa',level=500)[0]
var2_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Geopotential Height',typeOfLevel='isobaricInhPa',level=700)[0]
var3_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Geopotential Height',typeOfLevel='isobaricInhPa',level=850)[0]
var4_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)

var  = fin.select(name='Temperature',typeOfLevel='isobaricInhPa',level=200)[0]
var5_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Temperature',typeOfLevel='isobaricInhPa',level=500)[0]
var6_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Temperature',typeOfLevel='isobaricInhPa',level=700)[0]
var7_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Temperature',typeOfLevel='isobaricInhPa',level=850)[0]
var8_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)

var  = fin.select(name='Relative humidity',typeOfLevel='isobaricInhPa',level=200)[0]
var9_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Relative humidity',typeOfLevel='isobaricInhPa',level=500)[0]
var10_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Relative humidity',typeOfLevel='isobaricInhPa',level=700)[0]
var11_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Relative humidity',typeOfLevel='isobaricInhPa',level=850)[0]
var12_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)

var  = fin.select(name='Vertical velocity',typeOfLevel='isobaricInhPa',level=200)[0]
var13_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Vertical velocity',typeOfLevel='isobaricInhPa',level=500)[0]
var14_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Vertical velocity',typeOfLevel='isobaricInhPa',level=700)[0]
var15_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Vertical velocity',typeOfLevel='isobaricInhPa',level=850)[0]
var16_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)

var  = fin.select(name='U component of wind',typeOfLevel='isobaricInhPa',level=200)[0]
var17_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='U component of wind',typeOfLevel='isobaricInhPa',level=500)[0]
var18_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='U component of wind',typeOfLevel='isobaricInhPa',level=700)[0]
var19_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='U component of wind',typeOfLevel='isobaricInhPa',level=850)[0]
var20_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)

var  = fin.select(name='V component of wind',typeOfLevel='isobaricInhPa',level=200)[0]
var21_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='V component of wind',typeOfLevel='isobaricInhPa',level=500)[0]
var22_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='V component of wind',typeOfLevel='isobaricInhPa',level=700)[0]
var23_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='V component of wind',typeOfLevel='isobaricInhPa',level=850)[0]
var24_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)

var  = fin.select(name='Absolute vorticity',typeOfLevel='isobaricInhPa',level=200)[0]
var25_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Absolute vorticity',typeOfLevel='isobaricInhPa',level=500)[0]
var26_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Absolute vorticity',typeOfLevel='isobaricInhPa',level=700)[0]
var27_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Absolute vorticity',typeOfLevel='isobaricInhPa',level=850)[0]
var28_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)


var  = fin.select(name='Temperature',typeOfLevel='surface',level=0)[0]
var29_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Surface pressure',typeOfLevel='surface',level=0)[0]
var30_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='2 metre temperature',typeOfLevel='heightAboveGround',level=2)[0]
var31_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Specific humidity',typeOfLevel='heightAboveGround',level=2)[0]
var32_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
#var  = fin.select(name='2 metre dewpoint temperature',typeOfLevel='heightAboveGround',level=2)[0]
#var33_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='2 metre relative humidity',typeOfLevel='heightAboveGround',level=2)[0]
var34_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='10 metre U wind component',typeOfLevel='heightAboveGround',level=10)[0]
var37_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='10 metre V wind component',typeOfLevel='heightAboveGround',level=10)[0]
var38_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Geopotential Height',typeOfLevel='unknown',level=0)[0]
var43_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
#var  = fin.select(name='Total Cloud Cover',typeOfLevel='atmosphere')[0]
#var44_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)

#var  = fin.select(name='Maximum temperature',typeOfLevel='heightAboveGround',level=2)[0]
#var35_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
#var  = fin.select(name='Minimum temperature',typeOfLevel='heightAboveGround',level=2)[0]
#var36_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Convective available potential energy',typeOfLevel='surface',level=0)[0]
var39_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Convective inhibition',typeOfLevel='surface',level=0)[0]
var40_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Convective available potential energy',typeOfLevel='pressureFromGroundLayer',level=18000-0)[0]
var41_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)
var  = fin.select(name='Convective inhibition',typeOfLevel='pressureFromGroundLayer',level=18000-0)[0]
var42_area,lats,lons = var.data(lat1=latbegin,lat2=latend,lon1=lonbegin,lon2=lonend)

fin.close()

##### CREATE NC FILE ##### 
fout = nc.Dataset(filenameout,"w",format="NETCDF4")
## define dimesions
longi  = fout.createDimension('longitude',size=num_lon)
lati   = fout.createDimension('latitude',size=num_lat)

## define variables for storing data
lon   = fout.createVariable('lon_3','f4',dimensions='longitude')
lat   = fout.createVariable('lat_3','f4',dimensions='latitude')

gh200   = fout.createVariable('gh200',  'f4',dimensions=['latitude','longitude'])
gh500   = fout.createVariable('gh500',  'f4',dimensions=['latitude','longitude'])
gh700   = fout.createVariable('gh700',  'f4',dimensions=['latitude','longitude'])
gh850   = fout.createVariable('gh850',  'f4',dimensions=['latitude','longitude'])

t200    = fout.createVariable('t200',   'f4',dimensions=['latitude','longitude'])
t500    = fout.createVariable('t500',   'f4',dimensions=['latitude','longitude'])
t700    = fout.createVariable('t700',   'f4',dimensions=['latitude','longitude'])
t850    = fout.createVariable('t850',   'f4',dimensions=['latitude','longitude'])

rh200   = fout.createVariable('rh200',  'f4',dimensions=['latitude','longitude'])
rh500   = fout.createVariable('rh500',  'f4',dimensions=['latitude','longitude'])
rh700   = fout.createVariable('rh700',  'f4',dimensions=['latitude','longitude'])
rh850   = fout.createVariable('rh850',  'f4',dimensions=['latitude','longitude'])

w200    = fout.createVariable('w200',   'f4',dimensions=['latitude','longitude'])
w500    = fout.createVariable('w500',   'f4',dimensions=['latitude','longitude'])
w700    = fout.createVariable('w700',   'f4',dimensions=['latitude','longitude'])
w850    = fout.createVariable('w850',   'f4',dimensions=['latitude','longitude'])

u200    = fout.createVariable('u200',   'f4',dimensions=['latitude','longitude'])
u500    = fout.createVariable('u500',   'f4',dimensions=['latitude','longitude'])
u700    = fout.createVariable('u700',   'f4',dimensions=['latitude','longitude'])
u850    = fout.createVariable('u850',   'f4',dimensions=['latitude','longitude'])

v200    = fout.createVariable('v200',   'f4',dimensions=['latitude','longitude'])
v500    = fout.createVariable('v500',   'f4',dimensions=['latitude','longitude'])
v700    = fout.createVariable('v700',   'f4',dimensions=['latitude','longitude'])
v850    = fout.createVariable('v850',   'f4',dimensions=['latitude','longitude'])

absv200 = fout.createVariable('absv200','f4',dimensions=['latitude','longitude'])
absv500 = fout.createVariable('absv500','f4',dimensions=['latitude','longitude'])
absv700 = fout.createVariable('absv700','f4',dimensions=['latitude','longitude'])
absv850 = fout.createVariable('absv850','f4',dimensions=['latitude','longitude'])

t_sfc   = fout.createVariable('t_sfc',  'f4',dimensions=['latitude','longitude'])
p_sfc   = fout.createVariable('p_sfc',  'f4',dimensions=['latitude','longitude'])
t2m     = fout.createVariable('t2m',    'f4',dimensions=['latitude','longitude'])
sh2m    = fout.createVariable('sh2m',   'f4',dimensions=['latitude','longitude'])
#dew2m   = fout.createVariable('dew2m',  'f4',dimensions=['latitude','longitude'])
rh2m    = fout.createVariable('rh2m',   'f4',dimensions=['latitude','longitude'])
#tmax    = fout.createVariable('tmax',   'f4',dimensions=['latitude','longitude'])
#tmin    = fout.createVariable('tmin',   'f4',dimensions=['latitude','longitude'])
u10m    = fout.createVariable('u10m',   'f4',dimensions=['latitude','longitude'])
v10m    = fout.createVariable('v10m',   'f4',dimensions=['latitude','longitude'])
#tcc     = fout.createVariable('tcc',    'f4',dimensions=['latitude','longitude'])
hgt_sfc = fout.createVariable('hgt_sfc','f4',dimensions=['latitude','longitude'])                                        
cape_sfc= fout.createVariable('cape_sfc','f4',dimensions=['latitude','longitude'])
cape_180= fout.createVariable('cape_180','f4',dimensions=['latitude','longitude'])
cin_sfc = fout.createVariable('cin_sfc','f4',dimensions=['latitude','longitude'])
cin_180 = fout.createVariable('cin_180','f4',dimensions=['latitude','longitude'])

## add data to variables                
lon[:] = np.linspace(lonbegin,lonend,lonend-lonbegin+1)
lat[:] = np.linspace(latend,latbegin,latend-latbegin+1) #attention! Don't reverse the sequence

gh200[:]   = var1_area
gh500[:]   = var2_area
gh700[:]   = var3_area
gh850[:]   = var4_area

t200[:]    = var5_area
t500[:]    = var6_area
t700[:]    = var7_area
t850[:]    = var8_area

rh200[:]   = var9_area
rh500[:]   = var10_area
rh700[:]   = var11_area
rh850[:]   = var12_area

w200[:]    = var13_area
w500[:]    = var14_area
w700[:]    = var15_area
w850[:]    = var16_area

u200[:]    = var17_area
u500[:]    = var18_area
u700[:]    = var19_area
u850[:]    = var20_area

v200[:]    = var21_area
v500[:]    = var22_area
v700[:]    = var23_area
v850[:]    = var24_area

absv200[:] = var25_area
absv500[:] = var26_area
absv700[:] = var27_area 
absv850[:] = var28_area

t_sfc[:]   = var29_area
p_sfc[:]   = var30_area
t2m[:]     = var31_area
sh2m[:]    = var32_area
#dew2m[:]   = var33_area
rh2m[:]    = var34_area
#tmax[:]    = var35_area
#tmin[:]    = var36_area
u10m[:]    = var37_area
v10m[:]    = var38_area
#tcc[:]     = var44_area
hgt_sfc[:]    = var43_area
cape_sfc[:]   = var39_area
cin_sfc[:]    = var40_area
cape_180[:]   = var41_area
cin_180[:]    = var42_area

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

gh200.description    = 'Geopotential Height at 200hPa'
gh200.long_name      = 'Geopotential Height'
gh200.units          = 'gpm'
gh500.description    = 'Geopotential Height at 500hPa'
gh500.long_name      = 'Geopotential Height'
gh500.units          = 'gpm'
gh700.description    = 'Geopotential Height at 700hPa'
gh700.long_name      = 'Geopotential Height'
gh700.units          = 'gpm'
gh850.description    = 'Geopotential Height at 850hPa'
gh850.long_name      = 'Geopotential Height'
gh850.units          = 'gpm'

t200.description     = 'Temperature at 200hPa'
t200.long_name       = 'Temperature'          
t200.units           = 'K'                    
t500.description     = 'Temperature at 500hPa'
t500.long_name       = 'Temperature'          
t500.units           = 'K'                    
t700.description     = 'Temperature at 700hPa'
t700.long_name       = 'Temperature'          
t700.units           = 'K'                    
t850.description     = 'Temperature at 850hPa'
t850.long_name       = 'Temperature'          
t850.units           = 'K'                    

rh200.description    = 'Relative humidity at 200hPa'
rh200.long_name      = 'Relative humidity'          
rh200.units          = '%'                    
rh500.description    = 'Relative humidity at 500hPa'
rh500.long_name      = 'Relative humidity'          
rh500.units          = '%'                    
rh700.description    = 'Relative humidity at 700hPa'
rh700.long_name      = 'Relative humidity'          
rh700.units          = '%'                    
rh850.description    = 'Relative humidity at 850hPa'
rh850.long_name      = 'Relative humidity'          
rh850.units          = '%'                    

w200.description     = 'vertical velocity at 200hPa'
w200.long_name       = 'Pressure vertical velocity'          
w200.units           = 'Pa/s'                    
w500.description     = 'vertical velocity at 500hPa'
w500.long_name       = 'Pressure vertical velocity'          
w500.units           = 'Pa/s'                    
w700.description     = 'vertical velocity at 700hPa'
w700.long_name       = 'Pressure vertical velocity'          
w700.units           = 'Pa/s'                    
w850.description     = 'vertical velocity at 850hPa'
w850.long_name       = 'Pressure vertical velocity'          
w850.units           = 'Pa/s'                    

u200.description     = 'u-component of wind at 200hPa'
u200.long_name       = 'u-component of wind'          
u200.units           = 'm/s'                    
u500.description     = 'u-component of wind at 500hPa'
u500.long_name       = 'u-component of wind'          
u500.units           = 'm/s'                    
u700.description     = 'u-component of wind at 700hPa'
u700.long_name       = 'u-component of wind'          
u700.units           = 'm/s'                    
u850.description     = 'u-component of wind at 850hPa'
u850.long_name       = 'u-component of wind'          
u850.units           = 'm/s'                    

v200.description     = 'v-component of wind at 200hPa'
v200.long_name       = 'v-component of wind'          
v200.units           = 'm/s'                    
v500.description     = 'v-component of wind at 500hPa'
v500.long_name       = 'v-component of wind'          
v500.units           = 'm/s'                    
v700.description     = 'v-component of wind at 700hPa'
v700.long_name       = 'v-component of wind'          
v700.units           = 'm/s'                    
v850.description     = 'v-component of wind at 850hPa'
v850.long_name       = 'v-component of wind'          
v850.units           = 'm/s'                    

absv200.description  = 'Absolute vorticity at 200hPa'
absv200.long_name    = 'Absolute vorticity'          
absv200.units        = '/s'                    
absv500.description  = 'Absolute vorticity at 500hPa'
absv500.long_name    = 'Absolute vorticity'          
absv500.units        = '/s'                    
absv700.description  = 'Absolute vorticity at 700hPa'
absv700.long_name    = 'Absolute vorticity'          
absv700.units        = '/s'                    
absv850.description  = 'Absolute vorticity at 850hPa'
absv850.long_name    = 'Absolute vorticity'          
absv850.units        = '/s'                    


t_sfc.description    = 'Temperature at surface'
t_sfc.long_name      = 'Temperature'          
t_sfc.units          = 'K'                    
p_sfc.description    = 'Pressure at surface'
p_sfc.long_name      = 'Pressure'          
#p_sfc.units          = 'Pa'                    
t2m.description      = 'Temperature at 2 metre'
t2m.long_name        = 'Temperature'          
t2m.units            = 'K'                    
sh2m.description     = 'Specific humidity at 2 metre'
sh2m.long_name       = 'Specific humidity'          
sh2m.units           = 'kg/kg'                    
#dew2m.description    = 'Dewpoint Temperature at 2 metre'
#dew2m.long_name      = 'Dewpoint Temperature'          
#dew2m.units          = 'K'                    
rh2m.description     = 'Relative humidity at 2 metre'
rh2m.long_name       = 'Relative humidity'          
rh2m.units           = '%'                    
#tmax.description     = 'Maximun temperature at 2 metre'
#tmax.long_name       = 'Maximum temperature'          
#tmax.units           = 'K'                    
#tmin.description     = 'Minimun temperature at 2 metre'
#tmin.long_name       = 'Minimum temperature'          
#tmin.units           = 'K'                    
u10m.description     = 'u-component of wind at 10 metre'
u10m.long_name       = 'u-component of wind'          
u10m.units           = 'm/s'                    
v10m.description     = 'v-component of wind at 10 metre'
v10m.long_name       = 'v-component of wind'          
v10m.units           = 'm/s'                    
#tcc.description      = 'Total Cloud Cover'
#tcc.long_name        = 'Total Cloud Cover'          
#tcc.units            = '%'                    
hgt_sfc.description  = 'Geopotential height at surface'
hgt_sfc.long_name    = 'Geopotential height'          
hgt_sfc.units        = 'gpm'                    
cape_sfc.description = 'Convective available. potential energy at surface'
cape_sfc.long_name   = 'Convective available. potential energy'          
cape_sfc.units       = 'J/kg'                    
cape_180.description = 'Convective available. potential energy at 180'
cape_180.long_name   = 'Convective available. potential energy'          
cape_180.units       = 'J/kg'                    
cin_sfc.description  = 'Convective inhibition at surface'
cin_sfc.long_name    = 'Convective inhibition'          
cin_sfc.units        = 'J/kg'                    
cin_180.description  = 'Convective inhibition at 180'
cin_180.long_name    = 'Convective inhibition'          
cin_180.units        = 'J/kg'                    

fout.close()
print(filenamein[:-4]+' is done')



