#!/opt/anaconda3/bin/python

"""
进行GFS的数据下载
屈永霖。2020年05月20日
"""
import sys
import bs4
from urllib.request import urlopen
from urllib.request import urlretrieve

def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print( '%.2f%%' % per)
    
if __name__ == '__main__':    
    
    agument = sys.argv
    ide = str(agument[1])
    link =  'https://www1.ncdc.noaa.gov/pub/has/model/HAS'+ide+'/'

    print("==================================================")
    print("download from:",link)
    print("==================================================")
    html       =  urlopen(link)
    source     =  html.read().decode("utf-8")
    bs4obj     =  bs4.BeautifulSoup(source,"lxml")
    tags       =  bs4obj.findAll('a')

    for tag in tags[5:35]:
        print("======================================")
        print('downloading: '+tag.text+',please wait')
        urlretrieve(link+tag.text, tag.text, Schedule)
        print('downloading: '+tag.text+' finished')
        print("======================================")
    print('done')
    



