# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:40:22 2021

@author: qyl
"""

import numpy as np
import datetime
#import xml.etree.ElementTree as ET
import math
from xml.dom.minidom import Document

def uv2wsd(x, y):
    ws = np.sqrt(x ** 2 + y ** 2)
    wd = np.arctan2(y, x)
    wd = wd * 180 / np.pi
    wd =90-wd
    ind = np.where(wd>=360)
    wd[ind]=wd[ind]-360
    return (ws, wd)
        
def uv_transto_wdws(u,v):
    num = u.size
    ws = np.zeros([num])
    wd = np.zeros([num])
    for i in range(num):
    
        ws[i] = (u[i]*u[i] + v[i]*v[i]) ** 0.5
    
        if   (u[i] > 0)  & (v[i] > 0):
            wd[i] = 270 - math.atan(v[i] / u[i]) * 180 / math.pi
        elif (u[i] < 0)  & (v[i] > 0):
            wd[i] = 90  - math.atan(v[i] / u[i]) * 180 / math.pi
        elif (u[i] < 0)  & (v[i] < 0):
            wd[i] = 90  - math.atan(v[i] / u[i]) * 180 / math.pi
        elif (u[i] > 0)  & (v[i] < 0):
            wd[i] = 270 - math.atan(v[i] / u[i]) * 180 / math.pi
        elif (u[i] == 0) & (v[i] > 0):
            wd[i] = 180
        elif (u[i] == 0) & (v[i] < 0):
            wd[i] = 0
        elif (u[i] > 0)  & (v[i] == 0):
            wd[i] = 270
        elif (u[i] < 0)  & (v[i] == 0):
            wd[i] = 90
        elif (u[i] == 0) & (v[i] == 0):
            wd[i] = 0
    return wd,ws

if __name__ == '__main__':

    current_time = datetime.datetime.today() - datetime.timedelta(hours=8)
    current_date = datetime.datetime.strftime(current_time,'%Y-%m-%d')#时间转化成字符串
    current_date = datetime.datetime.strptime(current_date,'%Y-%m-%d')#字符串转化成时间
    year         = str(current_time.year).zfill(4)
    month        = str(current_time.month).zfill(2)
    day          = str(current_time.day).zfill(2)
    predict = np.load('54401_'+year+month+day+'ANNpredict.npy') #读取数据
    #以下，为使湿度预报中超过100的，等于100，并使得风向风速转化过来。
    rh = predict[2]
    rh[rh>100] = 100
    rh[rh<0]   = 0
    predict[2] = rh
    #predict[1] = predict[1] * 133.322
    predict[3],predict[4] =  uv_transto_wdws(predict[3],predict[4])#u,v变成风向风速
#-------------------------------------------------------------------------
    #在内存中创建一个空的文档
    doc = Document() 
    #创建一个根节点MetStationData对象
    MetStationData = doc.createElement("MetStationData")
    #创建子节点    
    stationID      = doc.createElement("stationID")
    longitude      = doc.createElement("longitude")
    latitude       = doc.createElement("latitude")
    altitude       = doc.createElement("altitude")

    #将根节点添加到文档对象中
    doc.appendChild(MetStationData)
    #将子节点添加到根节点中
    MetStationData.appendChild(stationID)
    MetStationData.appendChild(longitude)
    MetStationData.appendChild(latitude)
    MetStationData.appendChild(altitude)
    #子节点内容写入
    stationID_text = doc.createTextNode('54401')
    stationID.appendChild(stationID_text)
    longitude_text  = doc.createTextNode('114.88')
    longitude.appendChild(longitude_text) 
    latitude_text = doc.createTextNode('40.78')
    latitude.appendChild(latitude_text) 
    altitude_text = doc.createTextNode('724.2')
    altitude.appendChild(altitude_text) 
    
    for i in range(60):
        
        #创建forecastData子节点
        forecastData   = doc.createElement("forecastData")
        
        #将forecastData子节点放在根节点下
        MetStationData.appendChild(forecastData)
        
        #为forecastData子节点设置属性，也就是ID号
        forecastData.setAttribute('ID',str(i+1))
        
        #创建子子节点，时间和预报变量
        date           = doc.createElement("date")
        V_2T           = doc.createElement("V_2T")
        V_2P           = doc.createElement("V_2P")
        V_2RH          = doc.createElement("V_2RH")
        V_2WD          = doc.createElement("V_2WD")
        V_2WS          = doc.createElement("V_2WS")   
        
        #将子子节点添加到子节点forecastData中
        forecastData.appendChild(date)
        forecastData.appendChild(V_2T)
        forecastData.appendChild(V_2P)
        forecastData.appendChild(V_2RH)
        forecastData.appendChild(V_2WD)
        forecastData.appendChild(V_2WS)
        
        #子子节点内容写入
        forecastHour  = current_date + datetime.timedelta(hours=3*(i+1))
        forecastHour  = datetime.datetime.strftime(forecastHour,'%Y%m%d%H%M')        
        date_text     = doc.createTextNode(forecastHour)
        date.appendChild(date_text)
        
        V_2T_text  = doc.createTextNode(str(round(predict[0,i],2)))
        V_2T.appendChild(V_2T_text)
        
        V_2P_text  = doc.createTextNode(str(round(predict[1,i],2)))
        V_2P.appendChild(V_2P_text)  
        
        V_2RH_text = doc.createTextNode(str(round(predict[2,i],2)))
        V_2RH.appendChild(V_2RH_text)  
        
        V_2WD_text = doc.createTextNode(str(round(predict[3,i],2)))
        V_2WD.appendChild(V_2WD_text)  
        
        V_2WS_text = doc.createTextNode(str(round(predict[4,i],2)))
        V_2WS.appendChild(V_2WS_text)       
        
    #文件保存    
    current_time = datetime.datetime.strftime(current_time,'%Y%m%d%H%M%S') #产品生成时间
    current_date = datetime.datetime.strftime(current_date,'%Y%m%d%H%M')   #产品起报时间
    outputfilename = 'Z_SEVP_C_PKU_'+current_time+'_P_WF_BDDQ_54401_'+current_date+'.xml'
    fp = open(outputfilename, 'w')
    #以下,indent是每个tag前填充的字符，如：'  '，则表示每个tag前有两个空格,'\t'就会空格空的更大一些
    #addindent是每个子结点的缩近字符
    #newl是每个tag后填充的字符，如：’\n’，则表示每个tag后面有一个回车
    doc.writexml(fp, indent='', addindent='  ', newl='\n', encoding="utf-8")
    fp.close()


