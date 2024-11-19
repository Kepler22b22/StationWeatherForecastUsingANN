# -*- coding: utf-8 -*-
"""
This code is : GFS data translate from nc to npy.

The raw nc format GFS data are downloaded from website:
https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs
"""

import netCDF4 as nc
import numpy   as np
import os

#------------------------------------------------------
def variable_read(year,hour,var,path,lat,lon):
    filepath   = path+year+'/'+year+'nc/'
    filenames  = os.listdir(filepath)
    filenames.sort()
    filenames1 = [x for x in filenames if x.find(hour+'.nc')!=-1]

    variable_total = np.empty([len(filenames1),len(var)+1])
    i=0
    for filename in filenames1:    
        nc_obj     = nc.Dataset(filepath+filename)
        date       = filename[6:14]#6:14 is date in the filenames
        variable   = []                 
        for s in var:

            #55,70 is the latitude and lontitude eages of China. The other eages are ignored.
            #e.g. peking is (40,116), in (55-40,116-70),the count number is(15,46)
            variable_temp     = (nc_obj.variables[s][55-lat,lon-70])   
            variable.append(variable_temp)
        variable.append(date)
        variable = np.array(variable)
        variable_total[i,:] = variable
        i=i+1

    return variable_total

def variable_save(years,hour,var,path,citysite,lat,lon):
    
    year = years[0]
    variable_total     = variable_read(year,hour,var,path,lat,lon)    
    for year in years[1:]:
        variable_temp  = variable_read(year,hour,var,path,lat,lon)
        variable_total = np.r_[variable_total,variable_temp]
        
    if not os.path.exists('../data'):
        os.mkdir('../data')
    if not os.path.exists('../model/input_npys'):
        os.mkdir('../model/input_npys')
        
    np.save('../data/input_npys/'+citysite+'npy/'+citysite+'save_x_'+hour,variable_total)
    
#------------------------------------------------------
if  __name__ == "__main__":

    path           = '../data/'
    
    years          = ['2005','2006','2007','2008','2009',
                      '2010','2011','2012','2013','2014',
                      '2015','2016','2017','2018','2019','2020']

    #GFS data variable names are different in odd and even times, so we make
    #hours1 = 3,9,15...177
    #hours2 = 6,12,18...180
    hours1         = np.arange(3,181,6)
    hours2         = np.arange(6,181,6)
        
    variablenames1 = ['t2m',  'p_sfc', 'rh2m',  'u10m','v10m',
                      'tcc_ave3'     , 'prep_sfc_ave3',
                      'dswave_ave3'  , 'dlwave_ave3'  ,
                      'uswave_ave3'  , 'ulwave_ave3'  ]
    variablenames2 = ['t2m',  'p_sfc', 'rh2m',  'u10m','v10m',
                      'tcc_ave6'     , 'prep_sfc_ave6',
                      'dswave_ave6'  , 'dlwave_ave6'  ,
                      'uswave_ave6'  , 'ulwave_ave6'  ]

    '''
    city_lat_lons = [[50953,46,127],[57494,31,114],[56778,25,103],[56187,31,104],
                     [52866,37,102],[57083,35,114],[53463,41,112],
                     [59287,23,113],[51463,44,88],[58362,31,121],[55591,30,91],
                     [54857,36,120],[54662,39,121],[59758,20,110],[58847,26,119],[54511,40,116]]
    '''
    city_lat_lons =  [[54401,41,115]]               

    for n in city_lat_lons:
        citysite = str(n[0])
        citylat  = int(n[1])
        citylon  = int(n[2])
        print(citysite+' GFS input reading begin...')
        if not os.path.exists('../data/input_npys/'+citysite+'npy'):
            os.mkdir('../data/input_npys/'+citysite+'npy')
        for hour in hours1:
            hour = str(hour).zfill(3)    
            variable_save(years,hour,variablenames1,path,citysite,citylat,citylon)
            print(hour+' is done')
        for hour in hours2:
            hour = str(hour).zfill(3)    
            variable_save(years,hour,variablenames2,path,citysite,citylat,citylon)
            print(hour+' is done')

        print(citysite+' GFS input reading finished')





