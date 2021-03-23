# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:24:21 2020

@author: user
"""

import random as rd
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

#%%

file = pd.read_csv("77WEEKDAY.csv")

data = pd.read_csv("77D.csv")
data.head()

file['people'] = 0
file['normalize'] = 0.0000

for i in range(len(file['on_time'])):
    for j in range(len(data['on_time'])):
        if file['on_time'][i] == data['on_time'][j]:            
            file['normalize'][i] = data['normalize'][j].copy()
            file['people'][i] = data['people'][j].copy()
            break


#%%



#%%
#基於每個時段的需求量，分配每個時段(5:00~5:59  ... 21:00~21:10) 要發幾班車
his = []

for number in range(30,70):
    
    shift = number
    
    p=[]
    trans = []
    for j in range(17):
        total = 0
        for i in range(60):
            total += file['people'][j * 60 + i]
            
        if j == 16:
            for i in range(11):            
                total += file['people'][(j+1) * 60 + i]
        p.append(total)
    all_people = sum(p)
    
    for i in range(len(p)):
        trans.append(int(round(p[i] / all_people * shift)))
    
      
    
    min_fitness = 9999
    min_chrom = []
    min_list = []
    generation = 0
    generation_size = 100
    chrom_size = 100
    
    P0 = initialize()
    
    while generation < generation_size:
        P1 = reproduce(P0)
        P0 = P1.copy()
    
        generation += 1
        
    his.append(min_fitness)
#print("The min value is {} at {}".format(min_fitness , min_chrom))

#%%
plt.plot(np.arange(30,70),his)

#%%  查看染色體收斂程度
l = []
for i in range(chrom_size):
    l.append(score(P0[i]))
r = Counter(l)
r

#%%  看班次時間(指標)
f = []
for i in range(1031):
    if min_chrom[i] == 1:
        f.append(i)
f

#%% 看班次時間(實際時間)
d1 = time_converse(f)
d1

#%%  匯出資料

f = pd.DataFrame(f, columns=['time'])
f.to_excel('92W_shift.xlsx')


#%%
#initialize
def initialize():

    chrom = np.zeros((chrom_size,1031),dtype = 'int')
    for i in range(chrom_size):
        for j in range(17):
            r_list = []        
            if j == 16:
                for num in range(trans[j]):
                    r = rd.randint(0,13)
                    while r in r_list:
                        r = rd.randint(0,13)
                    r_list.append(r)
                    chrom[i][j * 60 + r * 5] = 1
            else:
                for num in range(trans[j]):   #選出要放1的位置           
                    r = rd.randint(0,11)            
                    while r in r_list:
                        r = rd.randint(0,11)
                    r_list.append(r)
                    chrom[i][j * 60 + r * 5] = 1

    return chrom  
            
#evaluation

def score(l):                  #input: l =發車陣列[0,1,1,1,0,0,0,1]   a = 乘客需求(array)
                                 #output: time = 乘客總等候時間(fitness value)
    b = list(np.zeros(len(l)))
    l = l.copy()
    c = np.array(file['normalize'])
    #c = a
    
    i = len(l) - 1              #乘客無車可搭，懲罰係數 = 10
    while l[i] == 0:
        c[i] = c[i] * 10
        i -= 1
    

    if l[-1] == 0:              #若末班車無發車，調整迴圈用 
        b[-1] = 1     
        l[-1] = 1
    for i in range(len(l)):     #計算乘客等待時間

        if l[i] == 0:
            j = i
            times = 1
            while l[j+1] == 0:
                times += 1
                j += 1

            b[i] = times
           
    
    
    
    time = sum(b*c)
    
    return time

def selection_1(P0):
    chrom = P0.copy()
    selection_index = []    #放染色體位置
    selection = []          #放染色體的適應值
    k = 5
    while len(selection_index) < k:
        r_value = rd.randint(0,chrom_size - 1)     #隨機取K個位置

        while r_value in selection_index:
            r_value = rd.randint(0,chrom_size - 1)

        selection_index.append(r_value)

    for i in range(len(selection_index)):          #轉換成適應值
        selection.append( 1 / score(chrom[selection_index[i]]))
    
    total = sum(selection)
    selection = []
    for i in range(len(selection_index)):
        selection.append((1 / score(chrom[selection_index[i]]) / total))
      
    p = np.random.choice(selection_index , p = np.array(selection).ravel())
        
    return p

    
#selection : tournament selection : 先隨機取K個染色體，從中選出最好的染色體，但有一定機率選出第二好的染色體，當作其中一個parent

def selection(P0):
    chrom = P0.copy()
    selection_index = []    #放染色體位置
    selection = []          #放染色體的適應值
    k = 5
    while len(selection_index) < k:
        r_value = rd.randint(0,chrom_size - 1)     #隨機取K個位置

        while r_value in selection_index:
            r_value = rd.randint(0,chrom_size - 1)

        selection_index.append(r_value)

    for i in range(len(selection_index)):          #轉換成適應值
        selection.append(score(chrom[selection_index[i]]))

    r = rd.random()

    if r >= 0.9:                                     #有10%的機率會選擇第二小的染色體
        selection_index.remove(selection_index[np.argmin(selection)])
        selection.remove(min(selection))
        p = selection_index[np.argmin(selection)]   #p = 親代染色體位置

    else:
        p = selection_index[np.argmin(selection)]

    return p         #回傳染色體位置




def reproduce(P0):
    global min_fitness
    global min_list
    global min_chrom
    
    chrom = P0.copy()
    offspring = np.zeros((1,1031),dtype = 'int') 
    chrom_number = 0
    
    while chrom_number < chrom_size:
        p1 = selection_1(chrom)
        p2 = selection_1(chrom)

        while p1 == p2:
            p2 = selection_1(chrom)


        #crossover  雙點交配

        r1 = rd.randint(0,16)     #取兩個亂數，做為切割點
        r2 = rd.randint(1,17)

        while r1 == r2:
            r2 = rd.randint(1,17)

        if r1 > r2:              #r1必須小於r2
            temp = r2
            r2 = r1
            r1 = temp


        if r2 == 17:
            number = (r2 - r1) * 60 + 11

        else:
            number = (r2 - r1) * 60

        p1_chrom = chrom[p1].copy()    
        p2_chrom = chrom[p2].copy()
        p1_neighbor = chrom[p1].copy()
        p2_neighbor = chrom[p2].copy()
        for i in range(number):       #neighborhood 製造
            p2_neighbor[r1 * 60 + i] = chrom[p1][r1 * 60 + i]          
            p1_neighbor[r1 * 60 + i] = chrom[p2][r1 * 60 + i]

        if score(p1_chrom) >= score(p1_neighbor):   #選較好的染色體當作offspring
            o1_chrom = p1_neighbor.copy()
        else:
            o1_chrom = p1_chrom.copy()

        if score(p2_chrom) >= score(p2_neighbor):
            o2_chrom = p2_neighbor.copy()
        else:
            o2_chrom = p2_chrom.copy()

        #mutation

        r = rd.random()

        if r > 0.9:
            o1_neighbor = o1_chrom.copy()
            r1 = rd.randint(0,16)

            if r1 == 16:
                for i in range(71):
                    o1_neighbor[r1 * 60 + i] = 0
                
                for num in range(trans[r1]):
                    r_list = []
                    r = rd.randint(0,13)
                    while r in r_list:
                        r = rd.randint(0,13)
                    r_list.append(r)
                    o1_neighbor[r1 * 60 + r * 5] = 1
            else:
                for i in range(60):
                    o1_neighbor[r1 * 60 + i] = 0
                
                for num in range(trans[r1]):   #選出要放1的位置     
                    r_list = []
                    r = rd.randint(0,11)            
                    while r in r_list:
                        r = rd.randint(0,11)
                    r_list.append(r)
                    o1_neighbor[r1 * 60 + r * 5] = 1    

            if score(o1_chrom) >= score(o1_neighbor):
                o1_chrom = o1_neighbor.copy()

        r = rd.random()

        if r > 0.9:
            o2_neighbor = o2_chrom.copy()
            r2 = rd.randint(0,16)

            if r2 == 16:
                for i in range(71):
                    o2_neighbor[r2 * 60 + i] = 0
                for num in range(trans[r2]):
                    r_list = []
                    r = rd.randint(0,13)
                    while r in r_list:
                        r = rd.randint(0,13)
                    r_list.append(r)
                    o2_neighbor[r2 * 60 + r * 5] = 1
            else:
                for i in range(60):
                    o2_neighbor[r2 * 60 + i] = 0
                    
                for num in range(trans[r2]):   #選出要放1的位置     
                    r_list = []
                    r = rd.randint(0,11)            
                    while r in r_list:
                        r = rd.randint(0,11)
                    r_list.append(r)
                    o2_neighbor[r2 * 60 + r * 5] = 1    

            if score(o2_chrom) >= score(o2_neighbor):
                o2_chrom = o2_neighbor.copy()

        offspring = np.row_stack((offspring , o1_chrom))       
        offspring = np.row_stack((offspring , o2_chrom))    
        chrom_number += 2
    
    offspring = np.delete(offspring,0,0)
    for i in range(chrom_size):
        if score(offspring[i]) <= min_fitness:
            min_chrom = offspring[i].copy()
            min_fitness = score(offspring[i])
    min_list.append(min_fitness)
    return offspring

def transit_distribution(l):    #檢測發車分配是否有錯誤的情況
    k = []
    for j in range(17):
        n = 0
        if j == 16:
            for i in range(71):
                n += l[i + j * 60]
                
        else:
            
            for i in range(60):
                n += l[i + j * 60]
                
        k.append(n)
    return k

def time_converse(l):
    t = []
    for i in range(len(l)):
        h = l[i] // 60 + 5
        m = l[i] % 60
        s = str(h) + ":" + str(m).zfill(2)
        
        t.append(s)
        
    return t