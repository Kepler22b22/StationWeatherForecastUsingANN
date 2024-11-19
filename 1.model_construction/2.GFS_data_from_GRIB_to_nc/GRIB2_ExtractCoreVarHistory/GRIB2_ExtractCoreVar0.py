#!/usr/bin/python3
import os
import numpy as np
import sys

agument  = sys.argv
year     = str(agument[1])
pathin   = "../data/"+year+"/"+year+"grib/"
pathout  = "../data/"+year+"/"+year+"nc/"
#os.system("rm -rf "+pathout)
#os.system("mkdir "+pathout)
filenames = os.listdir(pathin)
filenames.sort()
filename1 = [x for x in filenames if x.find('_000.grb2')!=-1]

for i in filename1:
    os.system("./extract1.py "+pathin+i+' '+pathout+i[:-4]+'nc')

print('done')
