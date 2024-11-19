# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:50:58 2020

@author: qyl
"""

import numpy as np
import datetime
import xml.etree.ElementTree as ET
import math

def pretty_xml(element, indent, newline, level=0):  # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
    if element:  # 判断element是否有子元素    
        if (element.text is None) or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
            # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
            # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element)  # 将element转成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个    
            subelement.tail = newline + indent * level
        pretty_xml(subelement, indent, newline, level=level + 1)  # 对子元素进行递归操作
        
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
    
    rh = predict[2]
    rh[rh>100] = 100
    rh[rh<0]   = 0
    predict[2] = rh
    predict[1] = predict[1] * 133.322
    predict[3],predict[4] =  uv_transto_wdws(predict[3],predict[4])#u,v变成风向风速
    
    #创建根节点
    root = ET.Element("MetStationData")
    
    #创建子节点，并添加数据
    stationID        = ET.SubElement(root,"stationID")
    stationID.text   = "54401"

    longitude        = ET.SubElement(root,"longitude")
    longitude.text   = "114.88"

    latitude         = ET.SubElement(root,"latitude")
    latitude.text    = "40.78"

    altitude         = ET.SubElement(root,"altitude")
    altitude.text    = "724.2"
    
    #创建子节点，并添加数据

    for i in range(60):
        
        forecastData  = ET.SubElement(root,'forecastData ID="'+str(i+1)+'"')
        
        date          = ET.SubElement(forecastData,"date")
        forecastHour  = current_date + datetime.timedelta(hours=3*(i+1))
        forecastHour  = datetime.datetime.strftime(forecastHour,'%Y%m%d%H%M%S')
        date.text     = forecastHour
        
        V_2T          = ET.SubElement(forecastData,"V_2T")
        V_2T.text     = str(round(predict[0,i],2))
        
        V_P           = ET.SubElement(forecastData,"V_P")
        V_P.text      = str(round(predict[1,i],2))

        V_2RH         = ET.SubElement(forecastData,"V_2RH")
        V_2RH.text    = str(round(predict[2,i],2))
        
        V_10WS        = ET.SubElement(forecastData,"V_10WS")
        V_10WS.text   = str(round(predict[3,i],2))
        
        V_10WD        = ET.SubElement(forecastData,"V_10WD")
        V_10WD.text   = str(round(predict[4,i],2))
        
        
    pretty_xml(root, '\t', '\n')  # 执行美化方法(数据加入缩进)
    current_time = datetime.datetime.strftime(current_time,'%Y%m%d%H%M%S') #产品生成时间
    current_date = datetime.datetime.strftime(current_date,'%Y%m%d%H%M')   #产品起报时间
    outputfilename = 'Z_SEVP_C_PKU_'+current_time+'_P_WF_BDDQ_54401_'+current_date+'.xml'
    tree = ET.ElementTree(root)
    tree.write(outputfilename,encoding="utf-8",xml_declaration=True)
