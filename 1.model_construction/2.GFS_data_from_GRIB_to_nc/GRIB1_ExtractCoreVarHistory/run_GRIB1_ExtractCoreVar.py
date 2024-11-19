#!/usr/bin/python3
import os
import numpy as np

year     = 2008
year     = str(year)
pathin   = "../"+year+"/"+year+"grib/"
pathout  = "../"+year+"/"+year+"nc/"
os.system("rm -rf "+pathout)
os.system("mkdir "+pathout)
filenames = os.listdir(pathin)
filenames.sort()

filename1 = [x for x in filenames if x.find('f000')!=-1]
for i in filename1:
    os.system("ncl extract1.ncl "+"'"+"fin1="+'"'+pathin+i+'"'+"' "+"'"+"fout1="+'"'+pathout+i[:-4]+'nc"'+"'")

for cc in range(3,181,6):
    cc = str(cc).zfill(3)
    filename2 = [x for x in filenames if x.find('f'+cc)!=-1]
    for j in filename2:
        os.system("ncl extract2.ncl "+"'"+"fin2="+'"'+pathin+j+'"'+"' "+"'"+"fout2="+'"'+pathout+j[:-4]+'nc"'+"'")

for cc in range(6,181,6):
    cc = str(cc).zfill(3)
    filename3 = [x for x in filenames if x.find('f'+cc)!=-1]
    for k in filename3:
        os.system("ncl extract3.ncl "+"'"+"fin3="+'"'+pathin+k+'"'+"' "+"'"+"fout3="+'"'+pathout+k[:-4]+'nc"'+"'")

# shit coding, ahh#
print('done')
