'''
Created on Feb 23, 2016

@author: Administrator
'''

import matplotlib.pyplot as plt
import numpy as np
from images2gif import writeGif
from PIL import Image
import os
import pysal
import scipy.stats as st
import Basemap as bm
    
def sig4_map1(xCoord, yCoord, sList, tvalue):
    value1 = -abs(tvalue)
    value2 = 0
    value3 = abs(tvalue)
    
    symbolSize=5
    
    s = np.asarray(sList)
    
    group1 = np.ma.masked_where(s > value1, s)
    group2 = np.ma.masked_where(np.logical_or(s< value1, s> value2), s)
    group3 = np.ma.masked_where(np.logical_or(s< value2, s> value3), s)
    group4 = np.ma.masked_where(s < value3, s)
    
    
    oneGroup1 = []
    oneGroup2 = []
    oneGroup3 = []
    oneGroup4 = []
    
    for grp1 in group1:
        if grp1 !='--':
            oneGroup1.append(symbolSize)
        else:
            oneGroup1.append(0)
    
    for grp2 in group2:
        if grp2 !='--':
            oneGroup2.append(symbolSize)
        else:
            oneGroup2.append(0)
    
    for grp3 in group3:
        if grp3 !='--':
            oneGroup3.append(symbolSize)
        else:
            oneGroup3.append(0)
    
    for grp4 in group4:
        if grp4 !='--':
            oneGroup4.append(symbolSize)
        else:
            oneGroup4.append(0)
    
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1,1,1)
    
    
    ax.scatter(xCoord,yCoord, s= oneGroup1, c='#123FA5', edgecolor='none', label =' ~ '+ str(value1))
    ax.scatter(xCoord,yCoord, s= oneGroup2, c='#9AE602', edgecolor='none', label = str(value1)+' ~ '+str(value2))
    ax.scatter(xCoord,yCoord, s= oneGroup3, c='#F6CC02', edgecolor='none', label = str(value2)+' ~ '+str(value3))
    ax.scatter(xCoord,yCoord, s= oneGroup4, c='#F60202', edgecolor='none', label = str(value3)+' ~ ')
    
    # http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
    ax.legend(loc='upper left', ncol=2, fontsize=9, bbox_to_anchor=(-0.15, 0.1), title='t-value', markerscale=3.0, fancybox = True, scatterpoints = 1)
    
    return fig, ax

## automatically setting the range of estimates
def value6_map1(xCoord, yCoord, sList):
    
    symbolSize=5
    
    s = np.asarray(sList)
    
    maxValue = np.amax(s)
    minValue = np.amin(s)
    
    if abs(maxValue) >= abs(minValue):
        absRange = abs(maxValue)
    else:
        absRange = abs(minValue)
    
    value1 = -(absRange/3*2)
    value2 = -(absRange/3)
    value3 = 0
    value4 = absRange/3
    value5 = absRange/3*2
    
    group1 = np.ma.masked_where(s > value1, s)
    group2 = np.ma.masked_where(np.logical_or(s< value1, s> value2), s)
    group3 = np.ma.masked_where(np.logical_or(s< value2, s> value3), s)
    group4 = np.ma.masked_where(np.logical_or(s< value3, s> value4), s)
    group5 = np.ma.masked_where(np.logical_or(s< value4, s> value5), s)
    group6 = np.ma.masked_where(s < value5, s)
    
    
    
    oneGroup1 = []
    oneGroup2 = []
    oneGroup3 = []
    oneGroup4 = []
    oneGroup5 = []
    oneGroup6 = []
    
    for grp1 in group1:
        if grp1 !='--':
            oneGroup1.append(symbolSize)
        else:
            oneGroup1.append(0)
    
    for grp2 in group2:
        if grp2 !='--':
            oneGroup2.append(symbolSize)
        else:
            oneGroup2.append(0)
    
    for grp3 in group3:
        if grp3 !='--':
            oneGroup3.append(symbolSize)
        else:
            oneGroup3.append(0)
    
    for grp4 in group4:
        if grp4 !='--':
            oneGroup4.append(symbolSize)
        else:
            oneGroup4.append(0)
            
    for grp5 in group5:
        if grp5 !='--':
            oneGroup5.append(symbolSize)
        else:
            oneGroup5.append(0)
            
    for grp6 in group6:
        if grp6 !='--':
            oneGroup6.append(symbolSize)
        else:
            oneGroup6.append(0)
    
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(1,1,1)
    
    
    legendValue1 = str(round(value1,2))
    legendValue2 = str(round(value2,2))
    legendValue3 = str(round(value3,2))
    legendValue4 = str(round(value4,2))
    legendValue5 = str(round(value5,2))
    
    rangeList = bm.addBasemap(bm.basemapRange, bm.basemapPolygonList, bm.basemapLineList, bm.basemapPointList, bm.basemapElements, ax)
    
    ## Setting for ax
    ax.set_xlim(rangeList[0],rangeList[1])
    ax.set_ylim(rangeList[2],rangeList[3])
    
    ax.scatter(0,0, s=0, c='w', label = 'Estimates')
    if oneGroup1.count(0) != len(oneGroup1):
        ax.scatter(xCoord,yCoord, s= oneGroup1, c='#3300CC', edgecolor='none', label = 'less than ' + legendValue1)
    if oneGroup2.count(0) != len(oneGroup2):
        ax.scatter(xCoord,yCoord, s= oneGroup2, c='#3333FF', edgecolor='none', label = legendValue1 + ' - ' + legendValue2)
    if oneGroup3.count(0) != len(oneGroup3):
        ax.scatter(xCoord,yCoord, s= oneGroup3, c='#33CCFF', edgecolor='none', label = legendValue2 + ' - ' + legendValue3)
    
    if oneGroup4.count(0) != len(oneGroup4):
        ax.scatter(xCoord,yCoord, s= oneGroup4, c='#FFCC00', edgecolor='none', label = legendValue3 + ' - ' + legendValue4)
    if oneGroup5.count(0) != len(oneGroup5):
        ax.scatter(xCoord,yCoord, s= oneGroup5, c='#FF6600', edgecolor='none', label = legendValue4 + ' - ' + legendValue5)
    if oneGroup6.count(0) != len(oneGroup6):
        ax.scatter(xCoord,yCoord, s= oneGroup6, c='#FF0000', edgecolor='none', label = 'more than '+legendValue5)
    
    ax.legend(loc=3, ncol=1, fontsize=7, bbox_to_anchor=(-0.15,-0.15), markerscale=3.0, fancybox = True, scatterpoints = 1)
    
    return fig, ax


## Manually setting the range of estimates
def value6_map2(xCoord, yCoord, sList, rangeValue):
    
    symbolSize=5
    
    s = np.asarray(sList)
    
    absRange = rangeValue
    
    value1 = -(absRange/3*2)
    value2 = -(absRange/3)
    value3 = 0
    value4 = absRange/3
    value5 = absRange/3*2
    
    group1 = np.ma.masked_where(s > value1, s)
    group2 = np.ma.masked_where(np.logical_or(s< value1, s> value2), s)
    group3 = np.ma.masked_where(np.logical_or(s< value2, s> value3), s)
    group4 = np.ma.masked_where(np.logical_or(s< value3, s> value4), s)
    group5 = np.ma.masked_where(np.logical_or(s< value4, s> value5), s)
    group6 = np.ma.masked_where(s < value5, s)
    
    
    oneGroup1 = []
    oneGroup2 = []
    oneGroup3 = []
    oneGroup4 = []
    oneGroup5 = []
    oneGroup6 = []
    
    for grp1 in group1:
        if grp1 !='--':
            oneGroup1.append(symbolSize)
        else:
            oneGroup1.append(0)
    
    for grp2 in group2:
        if grp2 !='--':
            oneGroup2.append(symbolSize)
        else:
            oneGroup2.append(0)
    
    for grp3 in group3:
        if grp3 !='--':
            oneGroup3.append(symbolSize)
        else:
            oneGroup3.append(0)
    
    for grp4 in group4:
        if grp4 !='--':
            oneGroup4.append(symbolSize)
        else:
            oneGroup4.append(0)
            
    for grp5 in group5:
        if grp5 !='--':
            oneGroup5.append(symbolSize)
        else:
            oneGroup5.append(0)
            
    for grp6 in group6:
        if grp6 !='--':
            oneGroup6.append(symbolSize)
        else:
            oneGroup6.append(0)
    
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1,1,1)
    
    
    legendValue1 = str(round(value1,2))
    legendValue2 = str(round(value2,2))
    legendValue3 = str(round(value3,2))
    legendValue4 = str(round(value4,2))
    legendValue5 = str(round(value5,2))
    
    
    
    ax.scatter(xCoord,yCoord, s= oneGroup1, c='#3300CC', edgecolor='none', label = '~' + legendValue1)
    ax.scatter(xCoord,yCoord, s= oneGroup2, c='#3333FF', edgecolor='none', label = legendValue1 + '~' + legendValue2)
    ax.scatter(xCoord,yCoord, s= oneGroup3, c='#33CCFF', edgecolor='none', label = legendValue2 + '~' + legendValue3)
    
    ax.scatter(xCoord,yCoord, s= oneGroup4, c='#FFCC00', edgecolor='none', label = legendValue3 + '~' + legendValue4)
    ax.scatter(xCoord,yCoord, s= oneGroup5, c='#FF6600', edgecolor='none', label = legendValue4 + '~' + legendValue5)
    ax.scatter(xCoord,yCoord, s= oneGroup6, c='#FF0000', edgecolor='none', label = legendValue5 + '~')
    
    ax.legend(loc='upper left', ncol=2, fontsize=9, bbox_to_anchor=(-0.15, 0.12), title='estimates', markerscale=3.0, fancybox = True, scatterpoints = 1)
    
    return fig, ax

def map2(xCoord, yCoord, estValues, tValues, correctedT, rangeValue):
    
        
    #correctedT : double determined by year variable
    #rangeValue : 
    
    valueList = []

    for ind, value in enumerate(xCoord):
#         print value
#         print type(yCoord[ind])
        tempArray = [float(value[0]), float(yCoord[ind]), float(estValues[ind]), float(tValues[ind])]
        valueList.append(tempArray)
    


    newValueList = []
    index = 0 
    for value in valueList:
        if abs(value[3]) > abs(correctedT):
            newValueList.append(value)
            index+=1
    
    newxCoord = []
    newyCoord = []
    newEstValues = []
    newTValues = []
    
    for newValue in newValueList:
        newxCoord.append(newValue[0])
        newyCoord.append(newValue[1])
        newEstValues.append(newValue[2])
        newTValues.append(newValue[3])
    
    symbolSize=15
      
    sEst = np.asarray(newEstValues)
    
    absRange = rangeValue
    
    value1 = -(absRange/3*2)
    value2 = -(absRange/3)
    value3 = 0
    value4 = absRange/3
    value5 = absRange/3*2
      
    group1Est = np.ma.masked_where(sEst > value1, sEst)
    group2Est = np.ma.masked_where(np.logical_or(sEst< value1, sEst> value2), sEst)
    group3Est = np.ma.masked_where(np.logical_or(sEst< value2, sEst> value3), sEst)
    group4Est = np.ma.masked_where(np.logical_or(sEst< value3, sEst> value4), sEst)
    group5Est = np.ma.masked_where(np.logical_or(sEst< value4, sEst> value5), sEst)
    group6Est = np.ma.masked_where(sEst < value5, sEst)
      
      
    oneGroup1Est = []
    oneGroup2Est = []
    oneGroup3Est = []
    oneGroup4Est = []
    oneGroup5Est = []
    oneGroup6Est = []
      
    for grp1 in group1Est:
        if grp1 !='--':
            oneGroup1Est.append(symbolSize)
        else:
            oneGroup1Est.append(0)
      
    for grp2 in group2Est:
        if grp2 !='--':
            oneGroup2Est.append(symbolSize)
        else:
            oneGroup2Est.append(0)
      
    for grp3 in group3Est:
        if grp3 !='--':
            oneGroup3Est.append(symbolSize)
        else:
            oneGroup3Est.append(0)
      
    for grp4 in group4Est:
        if grp4 !='--':
            oneGroup4Est.append(symbolSize)
        else:
            oneGroup4Est.append(0)
              
    for grp5 in group5Est:
        if grp5 !='--':
            oneGroup5Est.append(symbolSize)
        else:
            oneGroup5Est.append(0)
              
    for grp6 in group6Est:
        if grp6 !='--':
            oneGroup6Est.append(symbolSize)
        else:
            oneGroup6Est.append(0)
      
      
    legendValue1 = str(round(value1,2))
    legendValue2 = str(round(value2,2))
    legendValue3 = str(round(value3,2))
    legendValue4 = str(round(value4,2))
    legendValue5 = str(round(value5,2))
              
              
    fig = plt.figure(figsize=(9, 7.5))
    ax = fig.add_subplot(1,1,1)
    
    rangeList = bm.addBasemap(bm.basemapRange, bm.basemapPolygonList, bm.basemapLineList, bm.basemapPointList, bm.basemapElements, ax)
    
    ## Setting for ax
    ax.set_xlim(rangeList[0],rangeList[1])
    ax.set_ylim(rangeList[2],rangeList[3])
  
    
    ax.scatter(0,0, s=0, c='w', label = 'Estimates')
    if oneGroup1Est.count(0) != len(oneGroup1Est):
        ax.scatter(newxCoord,newyCoord, s= oneGroup1Est, c='#3300CC', edgecolor='none', label = 'less than ' + legendValue1)
    if oneGroup2Est.count(0) != len(oneGroup2Est):
        ax.scatter(newxCoord,newyCoord, s= oneGroup2Est, c='#3333FF', edgecolor='none', label = legendValue1 + ' - ' + legendValue2)
    if oneGroup3Est.count(0) != len(oneGroup3Est):
        ax.scatter(newxCoord,newyCoord, s= oneGroup3Est, c='#33CCFF', edgecolor='none', label = legendValue2 + ' - ' + legendValue3)
    
    if oneGroup4Est.count(0) != len(oneGroup4Est):
        ax.scatter(newxCoord,newyCoord, s= oneGroup4Est, c='#FFCC00', edgecolor='none', label = legendValue3 + ' - ' + legendValue4)
    if oneGroup5Est.count(0) != len(oneGroup5Est):
        ax.scatter(newxCoord,newyCoord, s= oneGroup5Est, c='#FF6600', edgecolor='none', label = legendValue4 + ' - ' + legendValue5)
    if oneGroup6Est.count(0) != len(oneGroup6Est):
        ax.scatter(newxCoord,newyCoord, s= oneGroup6Est, c='#FF0000', edgecolor='none', label = 'more than '+legendValue5)
        
      
#     ax.legend(loc=3, ncol=1, fontsize=9, bbox_to_anchor=(0.,-0.1), markerscale=3.0, fancybox = True, scatterpoints = 1)
      
    return fig, ax    

def legendOnly(xCoord, yCoord, attrListEst, rangeValue):
    symbolSize=5
    
    s = np.asarray(attrListEst)
    
    absRange = rangeValue
    
    value1 = -(absRange/3*2)
    value2 = -(absRange/3)
    value3 = 0
    value4 = absRange/3
    value5 = absRange/3*2
    
    group1 = np.ma.masked_where(s > value1, s)
    group2 = np.ma.masked_where(np.logical_or(s< value1, s> value2), s)
    group3 = np.ma.masked_where(np.logical_or(s< value2, s> value3), s)
    group4 = np.ma.masked_where(np.logical_or(s< value3, s> value4), s)
    group5 = np.ma.masked_where(np.logical_or(s< value4, s> value5), s)
    group6 = np.ma.masked_where(s < value5, s)
    
    
    oneGroup1 = []
    oneGroup2 = []
    oneGroup3 = []
    oneGroup4 = []
    oneGroup5 = []
    oneGroup6 = []
    
    for grp1 in group1:
        if grp1 !='--':
            oneGroup1.append(symbolSize)
        else:
            oneGroup1.append(0)
    
    for grp2 in group2:
        if grp2 !='--':
            oneGroup2.append(symbolSize)
        else:
            oneGroup2.append(0)
    
    for grp3 in group3:
        if grp3 !='--':
            oneGroup3.append(symbolSize)
        else:
            oneGroup3.append(0)
    
    for grp4 in group4:
        if grp4 !='--':
            oneGroup4.append(symbolSize)
        else:
            oneGroup4.append(0)
            
    for grp5 in group5:
        if grp5 !='--':
            oneGroup5.append(symbolSize)
        else:
            oneGroup5.append(0)
            
    for grp6 in group6:
        if grp6 !='--':
            oneGroup6.append(symbolSize)
        else:
            oneGroup6.append(0)
    
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1,1,1)
    
    
    legendValue1 = str(round(value1,2))
    legendValue2 = str(round(value2,2))
    legendValue3 = str(round(value3,2))
    legendValue4 = str(round(value4,2))
    legendValue5 = str(round(value5,2))
    
    ## Setting for ax
    ax.set_xlim(1,2)
    ax.set_ylim(10,11)
    
    rangeList = bm.addBasemap(bm.basemapRange, bm.basemapPolygonList, bm.basemapLineList, bm.basemapPointList, bm.basemapElements, ax)
    
    ax.scatter(0,0, s=0, c='w', label = 'Estimates')
    if oneGroup1.count(0) != len(oneGroup1):
        ax.scatter(xCoord,yCoord, s= oneGroup1, c='#3300CC', edgecolor='none', label = 'less than ' + legendValue1)
    if oneGroup2.count(0) != len(oneGroup2):
        ax.scatter(xCoord,yCoord, s= oneGroup2, c='#3333FF', edgecolor='none', label = legendValue1 + ' - ' + legendValue2)
    if oneGroup3.count(0) != len(oneGroup3):
        ax.scatter(xCoord,yCoord, s= oneGroup3, c='#33CCFF', edgecolor='none', label = legendValue2 + ' - ' + legendValue3)
    
    if oneGroup4.count(0) != len(oneGroup4):
        ax.scatter(xCoord,yCoord, s= oneGroup4, c='#FFCC00', edgecolor='none', label = legendValue3 + ' - ' + legendValue4)
    if oneGroup5.count(0) != len(oneGroup5):
        ax.scatter(xCoord,yCoord, s= oneGroup5, c='#FF6600', edgecolor='none', label = legendValue4 + ' - ' + legendValue5)
    if oneGroup6.count(0) != len(oneGroup6):
        ax.scatter(xCoord,yCoord, s= oneGroup6, c='#FF0000', edgecolor='none', label = 'more than '+legendValue5)
    
    ax.legend(loc=3, ncol=1, fontsize=20, bbox_to_anchor=(0,0), markerscale=10.0, fancybox = True, scatterpoints = 1)
    
    return fig, ax

if __name__ == '__main__':

    index = 0
    while index < 9:
        filename1 = "SaleApartment"
        filename2 = "03_GWR.dbf"
        filename2_lag = "03LAG_GWR.dbf"
        filename2 = filename2_lag
         
        executeImage = 0    # 0: do not execute / 1: execute only t-value part / 2: execute only estimate part / 2.5: execute only estimate part (fixed range) / 3: execute estimate part significant / 4: execute only legend
        executeGIF = 3      # 0: do not execute / 1: execute only t-value part / 2: execute only estimate part / 2.5: execute only estimate part (fixed range) / 3: execute estimate part significant
             
        year = 2006+index
        year_lag = 2007+index
        year = year_lag
         
        noVar = 12 # number of variables including intercept
        noVar_lag = 13
        noVar = noVar_lag
          
        alpha = 0.05
         
         
         
        # 2006        2007        2008        2009       2010        2011        2012       2013        2014        2015
        # 566.8244    485.6843    629.6769    428.059    491.9345    557.4785    359.712    304.6463    297.4755    389.2181
        effectParaDict = {'2006' : 566.8244, '2007': 485.6843, '2008': 629.6769, '2009': 428.059, '2010': 491.9345, '2011': 557.4785, '2012': 359.712, '2013': 304.6463, '2014': 668.8347, '2015': 762.3142}
        effectParaDict_lag = {'2007': 380.4266, '2008': 466.3113, '2009': 276.951, '2010': 228.1931, '2011': 453.0001, '2012': 266.8246, '2013': 325.0223, '2014': 317.4129, '2015': 260.5769}
        effectParaDict = effectParaDict_lag
        
        effectPara = effectParaDict[str(year)]
         
        pValue = alpha/(effectPara/noVar)
        tValue = round(abs(st.norm.ppf(pValue/2)),2)
          
        range1=noVar # no of estimate parameters
        range2=5+(noVar)*2 # 5 - other parameters in GWR result
           
        ## open dbf
        data = pysal.open(filename1+str(year)+filename2)
           
        ## importing name of fields
        coordListName = data.header[-2:] # x, y coordinate
           
        estListName = data.header[:range1] # estimates
        tvalListName = data.header[range2:-2] # t-value
           
        valueListName = estListName+tvalListName # estimate[:noVar]+t-value[noVar:]
         
               
        if executeImage > 0 :
                   
            valueList = []
            ## importing values of estimates and t-value
            for row in data :
                values = row[:range1]+row[range2:-2] + row[-2:]
                valueList.append(values)
               
               
            if (executeImage//1) < 2.0:    
                   
                ### Creating t-value maps
                       
                    ## importing values of each field from valueList
                    for indx, name in enumerate(valueListName[noVar:]): # switching field among t-values
                                 
                        xCoordList = []
                        yCoordList = []
                        attrListT = []
                                 
                        for row in valueList: # do not change valueList[] because [] is nth row
                            xCoordList.append(row[-2:-1])    # importing x (the second from the last)
                            yCoordList.append(row[-1])      # importing y (the last)
                            attrListT.append(float(row[indx+noVar]))   #importing t-values of a field            
                                  
                             
                        fig, ax = sig4_map1(xCoordList, yCoordList, attrListT, tValue)
                                      
                        ax.set_xlabel(coordListName[0])
                        ax.set_ylabel(coordListName[1])
                        ax.axis('off')
                                   
                        #change path 
                        ax.set_title(name+"_"+str(year))
                        fig.savefig("t_values/"+filename1+str(year)+"_"+name+".png")
                         
                        print("save a t-value map successfully")
                         
                         
            if executeImage != 1:
                 
        
                ### Creating estimate maps
                      
                ## importing values of each field from valueList
                for indx, name in enumerate(valueListName[:noVar]): # switching field among estimates
                          
                    xCoordList = []
                    yCoordList = []
                    attrListEst = []
                    attrListT = []
                               
                    for row in valueList: # do not change valueList[] because [] is nth row
                        xCoordList.append(row[-2:-1])    # importing x (the second from the last)
                        yCoordList.append(row[-1])      # importing y (the last)
                        attrListEst.append(float(row[indx]))   #importing estimates of a field      
                        attrListT.append(float(row[indx+noVar]))   #importing t-values of a field      
                      
                    def getRangeValue(filename1, filename2, indx):
                            repValueList =[]
                            i = 0
#                             while i<10:
                            while i<9:
                                ## open dbf
#                                 data = pysal.open(filename1+str(i+2006)+filename2) # starting year - 2006
                                data = pysal.open(filename1+str(i+2007)+filename2) # starting year - 2007
                                
                                 
                                valueList = []
                                for row in data:
                                    value = row[indx]
                                    valueList.append(value)
                                    valueArray = np.asarray(valueList)
                                    maxValue = np.amax(valueArray)
                                    minValue = np.amin(valueArray)
                                     
                                    if abs(maxValue) > abs(minValue):
                                        repValue = abs(maxValue)
                                    else:
                                        repValue = abs(minValue)
                                 
                                repValueList.append(repValue)
                                i+=1
                                 
                            repValueArray = np.asarray(repValueList)
                            finalRangeValue = np.mean(repValueArray)
                             
                            return round(finalRangeValue,2)
                    rangeValue = getRangeValue(filename1, filename2, indx)
    #                 print('rangeValue='+str(rangeValue))
                     
                          
                    if executeImage == 2.5:
                         
                        fig, ax = value6_map2(xCoordList, yCoordList, attrListEst, rangeValue)
                         
                        ax.set_xlabel(coordListName[0])
                        ax.set_ylabel(coordListName[1])
                        ax.axis('off')
                                      
                        #change path 
                        ax.set_title(name+"_"+str(year))
                        fig.savefig("est_values1/"+filename1+str(year)+"_"+name+".png")
                        print("save an estimates map successfully")
                         
                    elif executeImage==3 :
                         
                        fig, ax = map2(xCoordList, yCoordList, attrListEst, attrListT, tValue, rangeValue)
                         
                         
                        ax.set_xlabel(coordListName[0])
                        ax.set_ylabel(coordListName[1])
                        ax.axis('off')
                                      
                         
    #                     ax.set_title(name+"_"+str(year))
                         
                        fontdict = {'fontsize': 30,
                                    'fontweight' : 'bold',
                                    'verticalalignment': 'baseline',
                                    'horizontalalignment': 'center'}
                         
                        ax.set_title(str(year), fontdict = fontdict)
                         
                        #change path 
                        fig.savefig("est_values3/"+filename1+str(year)+"_"+name+".png")
                        print("save an map of estimates significant successfully")
                         
                    elif executeImage == 4:
                        xCoordList = [0,0,0,0,0,0]
                        yCoordList = [0,1,2,3,4,5]
                        attrListEst = [-rangeValue, -(1.5/3)*rangeValue, -(0.5/3)*rangeValue, (0.5/3)*rangeValue, (1.5/3)*rangeValue, rangeValue]
                         
                        fig ,ax = legendOnly(xCoordList, yCoordList, attrListEst, rangeValue)
                         
                        ax.axis('off')
                         
                        #change path 
                        fig.savefig("legend/"+filename1+str(year)+"_"+name+".png")
                        print("save a legend successfully")
                                   
                    else:
                         
                        fig, ax = value6_map1(xCoordList, yCoordList, attrListEst)
                         
    #                     shpFile = 'shapefiles/Submarket'
    #                     addShpPolygon(shpFile, ax)
    #                     shpFile = 'shapefiles/HanRiverSmo'
    #                     addShpPolygon(shpFile, ax)
                                    
                        ax.set_xlabel(coordListName[0])
                        ax.set_ylabel(coordListName[1])
                        ax.axis('off')
                                      
                        #change path 
                        ax.set_title(name+"_"+str(year))
                        fig.savefig("est_values/"+filename1+str(year)+"_"+name+".png")
                        print("save an estimates map successfully")
      
      
        if executeGIF > 0 :
              
            ### GIF generator
                
#             filepath1 = 'E:/Programming/Eclipse/KoreaHousingVis/'
            filepath1 = 'D:/Programming/Project/git/KoreaHousingVis/'
            filepath2_t = 't_values/'
            filepath2_est = 'est_values/'
            filepath21_est = 'est_values1/'
            filepath22_est = 'est_values2/'
            filepath23_est = 'est_values3/'
            filepath3_t = 'gif_t_values/'
            filepath3_est = 'gif_est_values/'
            filepath31_est = 'gif_est_values1/'
            filepath32_est = 'gif_est_values2/'
            filepath33_est = 'gif_est_values3/'
              
              
            if executeGIF == 1:
                ### Creating t-value gif file 
                fileDir = os.path.join(os.path.dirname(__file__), filepath2_t)
                   
                # iteration of t-value columns 
                for fieldname in valueListName[noVar:]:  
                    os.chdir(filepath1+filepath2_t)
                    os.getcwd()
                         
                    images = []    
                    i=0
                    while i<10: # no of years
                        
                        filename3 = filename1+str(i+2006) # starting year = 2006
                        i+=1    
                        filename = filename3+'_'+fieldname+'.png'
                             
                        images.append(Image.open(filename))
                     
                          
                    os.chdir(filepath1+filepath3_t)
                    os.getcwd()
                          
                    gifname = filename1+'_'+fieldname+'.gif'
                          
                    writeGif(gifname, images, duration=1)
                    print(gifname)        
                  
              
            if executeGIF == 2:
                ### Creating estimates gif file 
                fileDir = os.path.join(os.path.dirname(__file__), filepath2_est)
              
              
                #change fieldnameList 
                for fieldname in valueListName[:noVar]:
                    os.chdir(filepath1+filepath2_est)
                    os.getcwd()
                         
                    images = []    
                    i=0
                    while i<10: # no of years
                        filename3 = filename1+str(i+2006) # starting year = 2006
                        i+=1    
                        filename = filename3+'_'+fieldname+'.png'
                             
                        images.append(Image.open(filename))
                     
                          
                    os.chdir(filepath1+filepath3_est)
                    os.getcwd()
                          
                    gifname = filename1+'_'+fieldname+'.gif'
                          
                    writeGif(gifname, images, duration=1)
                    print(gifname)
                     
            if executeGIF == 2.5:
                ### Creating estimates gif file 
                fileDir = os.path.join(os.path.dirname(__file__), filepath21_est)
              
              
                #change fieldnameList 
                for fieldname in valueListName[:noVar]:
                    os.chdir(filepath1+filepath21_est)
                    os.getcwd()
                         
                    images = []    
                    i=0
                    while i<10: # no of years
                        filename3 = filename1+str(i+2006) # starting year = 2006
                        i+=1    
                        filename = filename3+'_'+fieldname+'.png'
                             
                        images.append(Image.open(filename))
                     
                          
                    os.chdir(filepath1+filepath31_est)
                    os.getcwd()
                          
                    gifname = filename1+'_'+fieldname+'.gif'
                          
                    writeGif(gifname, images, duration=1)
                    print(gifname)    
                     
            if executeGIF == 3:
                ### Creating estimates gif file 
                fileDir = os.path.join(os.path.dirname(__file__), filepath23_est)
              
              
                #change fieldnameList 
                for fieldname in valueListName[:noVar]:
                    os.chdir(filepath1+filepath23_est)
                    os.getcwd()
                         
                    images = []    
                    i=0
                    while i<9: # no of years
                        filename3 = filename1+str(i+2007) # starting year = 2007
                        i+=1    
                        filename = filename3+'_'+fieldname+'.png'
                             
                        images.append(Image.open(filename))
                     
                          
                    os.chdir(filepath1+filepath33_est)
                    os.getcwd()
                          
                    gifname = filename1+'_'+fieldname+'.gif'
                          
                    writeGif(gifname, images, duration=1)
                    print(gifname)    
        index+=1