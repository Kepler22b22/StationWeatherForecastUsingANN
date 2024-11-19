#!/opt/anaconda3/bin/python3

import sys
from urllib.request import urlretrieve
#from urllib import urlretrieve

if __name__ == '__main__':    
    
    agument = sys.argv
    year  = str(agument[1])
    month = str(agument[2])
    day   = str(agument[3])
    hour  = str(agument[4]).zfill(3)
    link  =  'http://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs.'+year+month+day+'/00/'
    filename = 'gfs.t00z.pgrb2.1p00.f'+hour
    filepath = link+'gfs.t00z.pgrb2.1p00.f'+hour
    urlretrieve(filepath,filename)

