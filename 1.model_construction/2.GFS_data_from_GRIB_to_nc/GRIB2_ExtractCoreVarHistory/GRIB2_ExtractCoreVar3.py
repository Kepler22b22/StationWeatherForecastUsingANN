#!/usr/bin/python3
import os
import sys

#这个文件，只处理奇数时次的
agument  = sys.argv
year     = str(agument[1])
hour     = str(agument[2])
pathin   = "../data/"+year+"/"+year+"grib/"
pathout  = "../data/"+year+"/"+year+"nc/"
filenames = os.listdir(pathin)
filenames.sort()
hour = hour.zfill(3)
filename2 = [x for x in filenames if x.find(hour+'.grb2')!=-1]
for j in filename2:
    os.system("./extract2.py "+pathin+j+' '+pathout+j[:-4]+'nc')
print('done')
