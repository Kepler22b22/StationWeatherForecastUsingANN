#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:52:42 2020

@author: quyonglin

read OBS data

"""
import numpy as np
import pandas as pd
import math
import gc

class readOBSdata:
    def __init__(self,filename):
        self.array = pd.read_excel(filename,header=6,usecols=[0,1,2,5,6,7])
        self.array.columns = ['date','T','P','rh','wd','ws']
        self.array.index   = pd.to_datetime(self.array['date'],format='%d.%m.%Y %H:%M')
        
    def showvariables(self):
        print(self.array.columns)
    def showarray(self):
        print(self.array)
    def readvariable(self,variable):
        return self.array[variable]

def wdws_transto_uv(wd,ws):
    num = wd.size
    u = np.zeros([num])
    v = np.zeros([num])
    for i in range(num):
        if wd[i] == '从北方吹来的风':
            alpha = 0
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东北偏北方向吹来的风':
            alpha = 22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东北方吹来的风':
            alpha = 45
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东北偏东方向吹来的风':
            alpha = 45+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东方吹来的风':
            alpha = 90
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东南偏东方向吹来的风':
            alpha = 90+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东南方吹来的风':
            alpha = 135
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东南偏南方向吹来的风':
            alpha = 135+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从南方吹来的风':
            alpha = 180
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西南偏南方向吹来的风':
            alpha = 180+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西南方吹来的风':
            alpha = 225
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西南偏西方向吹来的风':
            alpha = 225+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西方吹来的风':
            alpha = 270
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西北偏西方向吹来的风':
            alpha = 270+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西北方吹来的风':
            alpha = 315
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西北偏北方向吹来的风':
            alpha = 315+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        else:
            u[i]  = 0
            v[i]  = 0
        u = pd.Series(u)
        u.index = wd.index
        v = pd.Series(v)
        v.index = wd.index
    return u,v

if __name__ == '__main__' :
    
    #citysites = {'54401'}


    citysites = {'50953','59287','57494','54511','58362',
                 '56778','56187','52866','55591','57083',
                 '54857','54662','53463','59758','58847',
                 '51463',}

    '''
    北京	    54511
    哈尔滨	50953
    广州	    59287
    武汉	    57494
    昆明	    56778
    成都(温江)56187
    西宁	    52866
    拉萨	    55591
    郑州	    57083
    青岛	    54857
    大连	    54662
    呼和浩特	53463
    海口	    59758
    福州	    58847	
    上海	    58362,上海宝山站，数据有问题(已修复)    
    乌鲁木齐	51463
    
    西安(泾河)	57131西安这个站，数据从2016年开始的
    '''


    for citysite in citysites:
        print(citysite+' is reading...')
        filename1 = '../data/OBS/'+citysite+'.01.02.2005.31.12.2012.1.0.0.cn.utf8.00000000.xls'
        filename2 = '../data/OBS/'+citysite+'.01.01.2013.31.10.2020.1.0.0.cn.utf8.00000000.xls'
        citydata1 = readOBSdata(filename1)
        citydata2 = readOBSdata(filename2)       
        T_1   = citydata1.readvariable('T')
        T_2   = citydata2.readvariable('T')
        P_1   = citydata1.readvariable('P')
        P_2   = citydata2.readvariable('P')
        rh_1  = citydata1.readvariable('rh')
        rh_2  = citydata2.readvariable('rh')
        wd_1  = citydata1.readvariable('wd')
        wd_2  = citydata2.readvariable('wd')
        ws_1  = citydata1.readvariable('ws')
        ws_2  = citydata2.readvariable('ws')
        
        
        T     = pd.concat([T_1,T_2]).sort_index()
        P     = pd.concat([P_1,P_2]).sort_index() 
        rh    = pd.concat([rh_1,rh_2]).sort_index() 
        wd    = pd.concat([wd_1,wd_2]).sort_index() 
        ws    = pd.concat([ws_1,ws_2]).sort_index() 
        u,v   = wdws_transto_uv(wd,ws)
        
        total  = pd.concat([T,P,rh,u,v,wd,ws],axis=1)
        total.columns = ['T','P','rh','u','v','wd','ws']
        total.to_excel('../data/OBS/'+citysite+'obs_rp5ru.xlsx')
        print(citysite+' save finished')
        
        del filename1,filename2,citydata1,citydata2
        del T_1,T_2,P_1,P_2,rh_1,rh_2,wd_1,wd_2,ws_1,ws_2
        del T,P,rh,wd,ws,u,v
        gc.collect()
    print('all done')



