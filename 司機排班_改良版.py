# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 12:16:02 2021

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:10:02 2020

@author: user
"""

import random as rd
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import matplotlib.dates as mdates
from datetime import datetime
#%%
class algorithm:
    def __init__(self):
        self.crossover_successful = False
        global D77_drive_time,D168E_drive_time,D168W_drive_time,D0North_drive_time,D0South_drive_time,D92_drive_time,DY1_drive_time,DY1_ex_drive_time
        D77_drive_time = [20,20,21,21,21,21,20,20,22,22,23,23,
                  24,24,23,22,23,24,24,24,23,23,24,26,
                  27,26,25,23,23,23,24,23,22,22,21,22,
                  22,22,23,22,22,22,21,21,21,21,21,21,
                  21,21,21,21,21,22,22,21,21,23,25,25,
                 26,26,25,24,23,22,22,23,23,23,24,23,
                 22,21,20,21,22,22,23,23,23,22,22,21,
                 21,21,20,21,21,22,22,22,22,22,22,22,
                 22,22,22,22,22,22,22,22,22,22,22,23,
                 26,25,24,22,23,23,24,23,22,22,21,22,
                 22,22,23,23,24,25,26,27,26,25,23,22,
                 24,26,26,26,26,26,27,27,27,28,26,27,
                 25,25,25,24,25,25,25,24,24,24,23,22,
                 22,22,21,21,21,21,21,21,22,22,22,22,
                 23,22,21,20,18,19,19,20,21,22,22,22,
                 22,22,22,22,22,22,22,21,21,21,20,20,
                 20,20,20,21,21,21,21,21,20,20,20,20,
                 20,20,20]

        D168E_drive_time = [20,20,20,21,20,20,19,20,21,23,22,22,
                           22,22,22,22,22,22,22,23,23,24,23,23,
                           22,22,22,22,22,23,23,22,22,21,21,22,
                           22,22,22,22,21,21,21,21,22,22,22,22,
                           21,21,20,20,21,21,22,22,22,21,23,24,
                           25,24,24,23,23,23,23,22,22,21,22,22,
                           23,22,21,20,21,21,22,22,22,22,22,22,
                           22,23,24,25,24,24,23,24,25,26,26,26,
                           26,25,23,22,22,21,21,22,22,22,22,22,
                           22,22,22,22,23,24,26,27,27,28,26,25,
                           24,23,23,22,24,26,27,27,27,27,26,26,
                           25,25,25,25,26,26,27,28,28,29,28,27,
                           26,26,26,26,25,25,25,25,25,25,26,26,
                           26,26,25,25,25,24,23,23,23,23,24,25,
                           25,26,27,28,28,28,29,28,27,26,25,23,
                           24,24,24,25,25,24,24,23,22,21,22,22,
                           23,23,24,24,24,23,23,23,23,23,23,20,
                           19,19,19]
        
        D168W_drive_time = [19,19,20,20,21,21,21,22,22,22,22,23,
                           23,24,23,23,22,22,22,22,23,23,24,24,
                           24,25,25,26,26,25,24,23,22,21,20,22,
                           22,23,24,24,25,23,24,21,23,25,27,25,
                           25,24,23,22,21,23,24,24,24,23,23,23,
                           22,22,23,24,25,24,24,23,24,24,25,24,
                           23,23,24,24,25,24,24,23,23,23,23,23,
                           23,23,23,23,23,23,23,23,23,22,21,21,
                           22,22,21,20,19,20,21,23,22,22,21,21,
                           21,21,21,22,22,23,25,27,26,26,25,25,
                           26,26,26,26,26,26,26,26,26,26,26,26,
                           25,23,25,27,29,29,28,28,26,25,24,25,
                           26,27,25,24,24,25,26,27,28,28,28,29,
                           28,27,26,24,23,23,22,22,23,23,24,24,
                           23,23,23,22,21,21,21,21,21,21,21,21,
                           21,21,21,21,21,21,21,20,20,20,19,19,
                           19,19,20,20,20,19,19,19,19,19,20,20,
                           20,20,19]
        
        D0North_drive_time = [9,9,9,9,9,10,10,10,10,12,12,13,
                              13,13,14,14,14,13,13,13,13,13,14,14,
                              15,15,15,15,15,15,15,14,14,14,14,14,
                              14,15,14,14,14,15,15,15,15,15,14,14,
                              14,14,14,14,14,14,14,14,15,14,15,15,
                              15,15,15,15,15,15,15,15,15,15,15,15,
                              15,15,15,15,15,15,15,15,15,15,15,16,
                              16,16,16,16,16,15,15,15,14,14,15,15,
                              14,15,15,15,15,15,15,14,14,14,14,15,
                              15,15,15,15,15,15,15,15,15,15,15,15,
                              15,15,15,15,15,15,15,16,16,16,17,17,
                              16,16,15,15,16,17,18,20,20,20,20,20,
                              20,20,20,20,20,19,18,16,16,16,17,17,
                              18,18,18,18,17,17,17,16,16,16,15,15,
                              16,16,16,16,16,15,15,15,15,15,15,15,
                              15,15,15,14,14,14,14,14,14,15,15,15,
                              14,14,15,15,15,15,14,14,14,14,14,13,
                              13,13,13]
        
        D0South_drive_time = [9,9,9,9,9,9,10,10,10,10,11,11,
                              12,13,14,15,16,15,14,13,13,13,14,14,
                              15,15,15,16,16,16,16,16,16,16,15,15,
                              15,15,15,15,15,14,14,14,14,14,14,15,
                              15,15,16,16,16,16,16,16,16,15,14,13,
                              13,12,12,13,13,14,15,15,16,16,16,15,
                              15,15,15,15,14,14,13,13,13,14,14,15,
                              15,16,17,16,15,15,14,14,14,15,15,16,
                              17,17,17,16,16,16,16,15,15,15,15,15,
                              15,15,15,15,15,16,16,16,16,16,17,17,
                              17,16,16,15,15,14,15,15,16,16,17,18,
                              18,18,18,19,19,18,17,16,16,18,18,19,
                              19,19,19,19,18,18,18,17,17,17,17,17,
                              17,17,17,17,17,17,16,16,16,16,16,15,
                              15,15,15,15,15,15,15,15,15,15,15,15,
                              15,15,15,15,15,15,15,15,15,15,15,15,
                              15,15,15,15,15,15,15,15,15,14,14,14,
                              13,13,13]
        
        D92_drive_time = [9,9,9,9,9,9,9,9,10,10,11,11,
                          12,14,14,14,15,15,14,14,14,15,15,15,
                          15,15,15,15,15,15,15,15,15,15,14,14,
                          14,14,14,14,14,14,13,13,14,14,15,15,
                          14,14,15,15,16,17,16,15,13,13,13,14,
                          15,17,17,16,16,16,15,15,14,14,14,15,
                          15,15,15,15,15,15,15,15,14,14,13,13,
                          14,15,16,15,15,14,13,13,13,13,13,13,
                          12,12,12,12,13,13,14,14,13,13,13,14,
                          15,15,15,15,15,15,14,14,14,13,13,15,
                          16,17,17,16,16,16,16,15,16,17,18,16,
                          16,15,16,17,18,17,16,15,16,17,20,17,
                          16,16,16,16,16,17,18,18,19,19,20,18,
                          17,16,16,16,16,17,18,20,16,16,16,15,
                          15,15,15,15,14,14,14,14,15,15,15,15,
                          15,15,15,15,15,15,13,13,12,12,12,12,
                          12,12,12,12,12,12,12,12,12,12,11,11,
                          11,11,11]
        
        DY1_drive_time = [17,17,17,17,17,18,18,18,18,20,20,19,
                         20,20,21,21,21,21,22,22,21,21,21,21,
                         21,22,22,23,23,23,23,23,24,24,23,23,
                         22,22,22,22,22,21,21,21,20,20,20,20,
                         20,20,20,20,20,19,19,19,18,18,18,19,
                         22,22,21,21,21,21,21,20,20,19,20,20,
                         21,20,20,19,19,20,20,19,19,18,18,19,
                         19,19,19,19,19,19,19,19,19,19,19,20,
                         20,21,21,22,20,19,18,20,20,21,20,19,
                         18,19,19,20,20,20,20,20,19,19,19,20,
                         21,21,20,20,20,21,21,21,22,22,23,23,
                         24,24,23,22,22,23,24,23,22,22,21,21,
                         21,21,22,22,21,21,20,21,21,21,22,22,
                         22,19,20,18,18,18,19,19,19,19,19,19,
                         19,19,19,19,20,20,20,20,20,20,21,21,
                         21,20,19,19,19,18,18,18,19,19,19,19,
                         18,18,18,18,18,18,18,18,18,18,17,17,
                         17,17,17]
        
        DY1_ex_drive_time = [17,17,17,17,17,18,18,18,18,20,20,19,
                         20,20,21,21,21,21,22,22,21,21,21,21,
                         21,22,22,23,23,23,23,23,24,24,23,23,
                         22,22,22,22,22,21,21,21,20,20,20,20,
                         20,20,20,20,20,19,19,19,18,18,18,19,
                         22,22,21,21,21,21,21,20,20,19,20,20,
                         21,20,20,19,19,20,20,19,19,18,18,19,
                         19,19,19,19,19,19,19,19,19,19,19,20,
                         20,21,21,22,20,19,18,20,20,21,20,19,
                         18,19,19,20,20,20,20,20,19,19,19,20,
                         21,21,20,20,20,21,21,21,22,22,23,23,
                         24,24,23,22,22,23,24,23,22,22,21,21,
                         21,21,22,22,21,21,20,21,21,21,22,22,
                         22,19,20,18,18,18,19,19,19,19,19,19,
                         19,19,19,19,20,20,20,20,20,20,21,21,
                         21,20,19,19,19,18,18,18,19,19,19,19,
                         18,18,18,18,18,18,18,18,18,18,17,17,
                         17,17,17]
    
            
    def run(self , d , number): #跑演算法的指令，包含選擇染色體、交配、突變，d: 司機的List， number: 迴圈次數
        print("Run Ga or sa")
        i = 0
        while i < number:   
            self.crossover_successful = True
            self.selection_p1()  #選擇第一條染色體
            self.selection_p2()  #選擇第二條染色體
            if self.find_p2 == False:   #若找不到P2，則直接跳出，執行下一個iteration
                continue

            
            self.crossover()
            if self.crossover_successful == True:    #若交配有成功，則進行突變
                self.mutation()
                self.his.append(self.fitness_his(d))  #紀錄每個iteration的目標值(所有司機適應值總和)
                i += 1

                
            
            else:   #若交配沒有成功，則執行下一個iteration
                continue

    def run_TB(self ,d , number):
        print("Run TB")
        i = 0
        while i < number:   
            self.crossover_successful = False
            candidate = []       #染色體候選List
            candidate_num = []   #判斷是否重複選取p2之List
            self.selection_p1()
            for j in range(self.chrom_num):          #選取數個p2染色體         
                self.selection_p2()
                
                if self.find_p2 == False:   #若找不到P2，則直接跳出，執行下一個iteration
                    break
                
                else:
                    if self.p2 in candidate_num: #如果選到的p2有在重複選取p2之List裡面，則重新選擇p2
                        continue
                    
                    else:               #若沒有在重複選取p2之List裡面，則將p2放進染色體候選list裡面
                        a = tabu_candidate(self.p1,self.p2,self.day,self.c,self.m,self.n,self.p1_neighbor,self.p2_neighbor)
                        candidate.append(a)
                        candidate_num.append(self.p2)

            if self.find_p2 == True:                
                candidate.sort(key = lambda x:x.takeValue())   #候選人排序，由小到大
    
                
                for item in candidate:
                    self.p2 = item.p2
                    if self.tabu_list.check(self.p1 , self.p2) == True:  #若p1 p2有在tabu list裡面，則跳過
                        continue
                    
                    else: #若沒有，則確定p2染色體
                        self.tabu_list.add(self.p1 , self.p2)  #將p1 p2 紀錄在tabu list裡
                        self.tabu_list.update()  #更新tabu list
                        if len(np.nonzero(d[self.p1].shift[self.day])[0]) == 1:  #單點交配方案，選擇交配點
                            self.c = item.c
                        else:                        #雙點交配方案，選擇2個交配點
                            self.m = item.m
                            self.n = item.n
                        self.day = item.day
                        break
                    
                else:       #若無任何p2符合，則重新迴圈
                    continue
                    
                self.crossover()   #選好最佳P2後即可進行交配
                self.mutation()
                self.his.append(self.fitness_his(d))
                i += 1
                
    
    def drive_time(self , number , time):  #number: 公車代碼1~8  time:班次時間(period)  return: 當時的駕駛時間
        if number == 1:
            return D77_drive_time[time]   
        elif number == 2:
            return D168E_drive_time[time]
        elif number == 3:
            return D168W_drive_time[time]
        elif number == 4:
            return D0North_drive_time[time]
        elif number == 5:
            return D0South_drive_time[time]
        elif number == 6:
            return D92_drive_time[time]
        elif number == 7:
            return DY1_drive_time[time]
        elif number == 8:
            return DY1_ex_drive_time[time]
    
    def idle_time(self,k1):    #input:某天的班表   output:回傳可交配的點(單點交配用)
        lunch = range(77,91)
        dinner = range(144,168)
        eat_lunch = False
        eat_dinner = False
        l = k1.copy()

        for shift in np.nonzero(l)[0]:
            shift_end = shift + self.drive_time(l[shift] , shift) + 1
            if shift_end >= len(l):
                shift_end = len(l)
            
            l[shift : shift_end] = [1] * (shift_end - shift)
            if (shift + self.drive_time(l[shift] , shift) + 1 in lunch) and (eat_lunch == False):
                l[shift_end : shift_end + 10] = [1] * 10
                eat_lunch = True
                
            if (shift + self.drive_time(l[shift] , shift) + 1 in dinner) and (eat_dinner == False):
                l[shift_end : shift_end + 10] = [1] * 10
                eat_dinner = True
        s1 = set([i for i , e in enumerate(l) if e == 0])
        
        return s1

    def find_break(self, k1,k2):    #input:某天的班表(list, size = 207)   output:回傳可交配的點(雙點交配用)
        lunch = range(77,91)
        dinner = range(144,168)
        eat_lunch = False
        eat_dinner = False
        l1 = k1.copy()
        l2 = k2.copy()
        
        for l in [l1 , l2]:
            eat_lunch = False
            eat_dinner = False
            for shift in np.nonzero(l)[0]:
                shift_end = shift + self.drive_time(l[shift] , shift) + 1
                if shift_end >= len(l):
                    shift_end = len(l)
                
                l[shift : shift_end] = [1] * (shift_end - shift)
                if (shift + self.drive_time(l[shift] , shift) + 1 in lunch) and (eat_lunch == False):
                    l[shift_end : shift_end + 10] = [1] * 10
                    eat_lunch = True
                    
                if (shift + self.drive_time(l[shift] , shift) + 1 in dinner) and (eat_dinner == False):
                    l[shift_end : shift_end + 10] = [1] * 10
                    eat_dinner = True
        
        s1 = set([i for i , e in enumerate(l1) if e == 0])
        s2 = set([i for i , e in enumerate(l2) if e == 0])
        k = list(s1.intersection(s2))
        
        return k

    def findtwo(self, a):   #找出交配點(雙點交配用)
        ans_list = []
        ans = []
        for i in range(len(a) - 1):
            if a[i + 1] - a[i] == 1:
                ans.append(a[i])
            else:
                ans.append(a[i])
                ans_list.append(ans)
                ans = []
    
        ans_list.append(ans)
        if [] in ans_list:
            ans_list[-1].append(a[-1])
            
        p = rd.random()
    
        if len(ans_list) == 1:
            return (0,0)
    
        if len(ans_list) == 2:
            return (ans_list[0][0] , ans_list[1][0])
    
        if p > 0.5:
            k = rd.sample(range(len(ans_list) - 1) , 2)
    
        else:
            k = rd.sample(list(np.arange(1,len(ans_list))), 2)
    
        n1 = k[0]
        n2 = k[1]
    
        if n1 > n2:
            temp = n2
            n2 = n1
            n1 = temp
        
        
        return (ans_list[n1][0] , ans_list[n2][0])
    
    def selection_p1(self):

                  #fitness:真實fitness分數    score:標準化後分數   location:染色體位置
        self.day = 0
        location = np.arange(len(d))
        score = np.zeros(len(d))

        fitness = list(map(lambda x : x.fitness_day(self.day), d))


        total_fitness = sum(fitness)
        score = list(map(lambda x : x / total_fitness , fitness))

        
        self.p1 = np.random.choice(location , p = np.array(score).ravel())   #self.p1:第一個Parent染色體位置
        
        #self.day = list(d[self.p1].fitness_list).index(max(d[self.p1].fitness_list))   #選適應值最差的那個天數
        
        self.candidate = [x for x in d if (set(d[self.p1].route[0:2]) or set(d[self.p1].route[1:]) or set([d[self.p1].route[0],d[self.p1].route[2]])) <= set(x.route) and self.day != x.dayoff[0]] 
            #candidate:第二個Parent候選人位置，先找服務相似路線的司機

        
    def selection_p2(self):
        self.find_p2 = False
        #如果self.p1只有1個班次數量-->單點交配    
        if len(np.nonzero(d[self.p1].shift[self.day])[0]) == 1:
            rd.shuffle(self.candidate)   #候選人洗牌
            for route in self.candidate:
                cross = self.find_break(d[self.p1].shift[self.day] , route.shift[self.day])
                cross_candidate = [x for x in cross if abs(x - np.nonzero(d[self.p1].shift[self.day])[0][0]) <= 10]   #選出在10單位時間內可交配的點
                
                if len(cross_candidate) == 0:
                    continue
                
                else:
                    self.p2 = route.driver_number
                   
                    while len(cross_candidate) > 0:
                        self.c = rd.choice(cross_candidate)
                        
                        #若只是鏡像交配，則重新迴圈
                        if (sum(d[self.p1].shift[self.day][:self.c]) + sum(d[self.p2].shift[self.day][:self.c]) == 0) or (sum(d[self.p1].shift[self.day][self.c:]) + sum(d[self.p2].shift[self.day][self.c:]) == 0):
                            if self.c > np.nonzero(d[self.p1].shift[self.day])[0]:
                                cross_candidate = [x for x in cross_candidate if x < np.nonzero(d[self.p1].shift[self.day])[0][0]]
                                continue
                            
                            else:
                                cross_candidate = [x for x in cross_candidate if x > np.nonzero(d[self.p1].shift[self.day])[0][0]]
                                continue
                            
                        #服務路線限制        
                        s1 = list(d[self.p1].shift[self.day][self.c : ])
                        s2 = list(d[self.p2].shift[self.day][self.c : ])
                        k1 = set(s1)
                        k2 = set(s2)
                        k1.discard(0.0)
                        k2.discard(0.0)
                        
                       
                        
                        #若皆符合限制式，則交配
                        if (k1 <= set(d[self.p2].route_number)) and (k2 <= set(d[self.p1].route_number)) is True:
                            self.find_p2 = True
                            break
                        
                        
                        else:  #若有無法服務的路線，則重新迴圈                        
                            if self.c > np.nonzero(d[self.p1].shift[self.day])[0]:
                                cross_candidate = [x for x in cross_candidate if x < np.nonzero(d[self.p1].shift[self.day])[0][0]]
                                continue
                            
                            else:
                                cross_candidate = [x for x in cross_candidate if x > np.nonzero(d[self.p1].shift[self.day])[0][0]]
                                continue

                    
                    else:                    #若交配成功，則跳出迴圈
                        continue
                    break
            
                   
        #如果self.p1有2個以上個班次數量-->雙點交配             
        else:
            rd.shuffle(self.candidate)   #候選人洗牌
            for p2 in self.candidate:            
                self.p2 = p2.driver_number
                cross = self.find_break(d[self.p1].shift[self.day] , d[self.p2].shift[self.day])  #找出可交配點
                (self.n , self.m) = self.findtwo(cross)   #選出兩交配點

                if self.n == self.m:
                    continue
                
    
                #服務路線限制        
                s1 = list(d[self.p1].shift[self.day][self.n : self.m + 1])
                s2 = list(d[self.p2].shift[self.day][self.n : self.m + 1])
                k1 = set(s1)
                k2 = set(s2)
                k1.discard(0)
                k2.discard(0)
                
                #若皆符合限制式，則交配
                if (k1 <= set(d[self.p2].route_number)) and (k2 <= set(d[self.p1].route_number)) is True :    
                    self.find_p2 = True
                    break
                 
                else: #若有無法服務的路線，則重新迴圈
                    continue
        
        if self.find_p2 == True and (k1 <= set(d[self.p2].route_number)) == True and (k2 <= set(d[self.p1].route_number)) == True:
            
            self.p1_neighbor = driver(1001)
            self.p1_neighbor.get_route([D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South])        
            self.p1_neighbor.shift[self.day] = d[self.p1].shift[self.day].copy()
            self.p2_neighbor = driver(1002)
            self.p2_neighbor.get_route([D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South])
            self.p2_neighbor.shift[self.day] = d[self.p2].shift[self.day].copy()
            
            
        else:
            self.find_p2 = False
    def mutation_2(self):
        B = [D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South]
        b = np.zeros((7,207))
        for bus in B:
            for day in range(7):        
                for i in bus.demand[day]:
                    b[day][i] += 1
        
        
        if sum(sum(b)) == 0:
            return
        
        for p in [self.p1 , self.p2]:
        
            #離群值處理            
    #        if d[p].working_time[self.day] + d[p].breaking_time[self.day] >= 720:            #若司機總工作時間超過12小時，則抓取其離群值
    #            candidate = np.nonzero(d[p].shift[self.day])[0]           #列出班次時間
    #            candidate_normal = abs(candidate.copy() - np.mean(candidate))   #列出與班次時間相差最多的班次
    #            out_shift = candidate[np.argmax(candidate_normal)]    #離群班次
    #            
    #            for route in d[p].route:
    #                if route.bus_number == d[p].shift[self.day][out_shift]:    
    #                    route.demand[self.day].append(out_shift)         #將離群班次移回需求中
    #                    d[p].shift[self.day][out_shift] = 0              #將離群班次從司機班表中移除
    #                    break
    
                            
            if d[p].breaking_time[self.day] / (d[p].working_time[self.day] + d[p].breaking_time[self.day]) >= 0.4:  #若休息時間占總工時超過40%，則進行突變
           
                if len(np.nonzero(d[p].shift[self.day])[0]) == 0:    #若當天無班次，則跳過
                    continue
               
                elif len(np.nonzero(d[p].shift[self.day])[0]) == 1:    #若當天班次只有1個，則插入班次
                    start_point = np.nonzero(d[p].shift[self.day])[0][0]
                    for route in d[p].route:
                        for shift in [x for x in route.demand[self.day] if start_point - x - max(route.driving_time) in range(-5,5)]:   #插入早班班次
                            if shift + self.drive_time(route.bus_number , shift) + 2 < start_point:
                                d[p].shift[self.day][shift] = route.bus_number
                                route.demand[self.day].remove(shift)
                                break
                        else:
                            continue
                        
                        break
                    
                    for route in d[p].route:   #插入晚班班次
                        start_route = d[p].shift[self.day][start_point]
                        candidate = [x for x in route.demand[self.day] if x - start_point - self.drive_time(start_route , start_point) - 2 in range(1,11)]
                        if len(candidate) == 0:
                            continue
                        else:
                            shift = candidate[0]
                            d[p].shift[self.day][shift] = route.bus_number
                            route.demand[self.day].remove(shift)
                            if start_point + self.drive_time(start_route , start_point) + 2 > shift:
                                print("wrong", p,self.day, start_point ,self.drive_time(route.bus_number , start_point) , shift)
                            break
                   
                else:                  
                    first_point = np.nonzero(d[p].shift[self.day])[0][0]   #第一個班次
                    bus_route = d[p].shift[self.day][first_point]   #第一個班次之公車路線
                    start_point = first_point + self.drive_time(bus_route , first_point) + 2  #設置起始突變點
                    if len(np.nonzero(d[p].shift[self.day])[0]) == 1:
                        if first_point >= 150:
                            last_point = np.nonzero(d[p].shift[self.day])[0][0]
                            start_point = np.nonzero(d[p].shift[self.day])[0][0] - 35
                        else:
                            last_point = 999
                    else:                                    
                        last_point = np.nonzero(d[p].shift[self.day])[0][1]   #第二個班次
                    
                    for bus_route in d[p].route:
                        mutation_point = [x for x in bus_route.demand[self.day] if x >= start_point and self.drive_time(bus_route.bus_number , x) + x + 2 <= last_point]
                        if len(mutation_point) == 0:  #若無突變點，則再找下一個路線
                            continue
                        
                        else:
                            point = mutation_point[0]   #交配點
                            d[p].shift[self.day][point] = bus_route.bus_number  #排班次到班表中
                            bus_route.demand[self.day].remove(point)   #移除班次需求
                            break                           
    def mutation(self):
        total = 0
        for route in [D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South]:       #計算當天剩餘班次
            total += route.left_demand[self.day] 
        if total == 0:
            return
            
            
        for p in [self.p1, self.p2]:
            if len(np.nonzero(d[p].shift[self.day])[0]) == 0:    #若當天無班次，則跳過
                continue
            
            for route in d[p].route:                           #計算當天剩餘班次
                if route.left_demand[self.day] == 0:
                    continue
                
                for demand in route.demand[self.day]:
                    time = demand + route.driving_time[demand]
                    if time in range(77,91) or range(144,168):
                        time += 8
                    if set(range(demand , time + 2)) < self.idle_time(d[p].shift[self.day]):
                        d[p].shift[self.day][demand] == route.bus_number
                        route.demand[self.day].remove(demand)
                        break
                else:
                    continue
                break

  
            
    #計算所有司機的適應值
    def fitness_his(self,d):
        total = 0
        for i in range(len(d)):
            total += d[i].fitness
        
        return total
    
class GA(algorithm):
    
    def __init__(self):
        super().__init__()
        self.his = []

    
    def crossover(self):  
        self.p1_neighbor = driver(1001)
        self.p1_neighbor.get_route([D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South])        
        self.p1_neighbor.shift[self.day] = d[self.p1].shift[self.day].copy()
        self.p2_neighbor = driver(1002)
        self.p2_neighbor.get_route([D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South])
        self.p2_neighbor.shift[self.day] = d[self.p2].shift[self.day].copy()
        
        if len(np.nonzero(d[self.p1].shift[self.day])[0]) == 1:                                
            self.p1_neighbor.shift[self.day][self.c:] = d[self.p2].shift[self.day][self.c:].copy()
            self.p2_neighbor.shift[self.day][self.c:] = d[self.p1].shift[self.day][self.c:].copy()
            
           
            d[self.p1].shift[self.day] = self.p1_neighbor.shift[self.day].copy()
            d[self.p2].shift[self.day] = self.p2_neighbor.shift[self.day].copy()                               
            self.crossover_successful = True  #交配成功
           
                   
        #如果self.p1有2個以上個班次數量-->雙點交配             
        else:            
            self.p1_neighbor.shift[self.day][self.n : self.m + 1] = d[self.p2].shift[self.day][self.n : self.m + 1].copy()
            self.p2_neighbor.shift[self.day][self.n : self.m + 1] = d[self.p1].shift[self.day][self.n : self.m + 1].copy()
            
            d[self.p1].shift[self.day] = self.p1_neighbor.shift[self.day].copy()
            d[self.p2].shift[self.day] = self.p2_neighbor.shift[self.day].copy() 
            self.crossover_successful = True  #交配成功

      
class GA_SA(algorithm):
    def __init__(self):
        super().__init__()
        self.his = []
        
    def crossover(self):   
       #如果self.p1只有1個班次的交配方式-->單點交配
        if len(np.nonzero(d[self.p1].shift[self.day])[0]) == 1:                           
            #SA部分

            
            self.p1_neighbor.shift[self.day][self.c:] = d[self.p2].shift[self.day][self.c:].copy()
            self.p2_neighbor.shift[self.day][self.c:] = d[self.p1].shift[self.day][self.c:].copy()
            
            #若交配後適應值較佳，則交配
            if self.p1_neighbor.fitness_day(self.day) + self.p2_neighbor.fitness_day(self.day) <= d[self.p1].fitness_day(self.day) + d[self.p2].fitness_day(self.day):
                d[self.p1].shift[self.day] = self.p1_neighbor.shift[self.day].copy()
                d[self.p2].shift[self.day] = self.p2_neighbor.shift[self.day].copy()  
                self.crossover_successful = True
                                
                
        #如果self.p1有2個以上個班次數量-->雙點交配             
        else:                      
            self.p1_neighbor.shift[self.day][self.n : self.m + 1] = d[self.p2].shift[self.day][self.n : self.m + 1].copy()
            self.p2_neighbor.shift[self.day][self.n : self.m + 1] = d[self.p1].shift[self.day][self.n : self.m + 1].copy()
            
            #若交配後適應值較佳，則交配
            if self.p1_neighbor.fitness_day(self.day) + self.p2_neighbor.fitness_day(self.day) <= d[self.p1].fitness_day(self.day) + d[self.p2].fitness_day(self.day):
                d[self.p1].shift[self.day] = self.p1_neighbor.shift[self.day].copy()
                d[self.p2].shift[self.day] = self.p2_neighbor.shift[self.day].copy() 
                self.crossover_successful = True

class GA_TB(GA):
    def __init__(self):
        super().__init__()
        self.c = 0  #單點交配點
        self.m = 0  #雙點交配點1
        self.n = 0  #雙點交配點2
        self.his = []
        self.chrom_num = 20   #選取染色體數量
        self.tabu_list = tabu_list()  #建立tabu list
        
    
            
             
           

class tabu_list:
    def __init__(self):     #基本架構:(self.p1, self.p2, 次數)  , n < m
        self.list = []
        self.tenure = 15
        
    def add(self , n , m):
        if n > m:
            temp = n
            n = m
            m = temp
            
        self.list.append([n, m, 0])
        
    def check(self , n , m):
        if n > m:
            temp = n
            n = m
            m = temp
        for item in self.list:       #查詢(n,m)是否已有在在Tabu list，True = 有重複，False = 無重複
            if [n ,m] == item[:2]:
                return True
            
            else:
                continue
        
        return False
    
    def update(self):
        for item in self.list:
            item[-1] += 1   #次數 + 1
            
            if item[-1] > self.tenure:  #若次數超過7，則移除
                self.list.remove(item)
                
class tabu_candidate(algorithm):
    def __init__(self , p1, p2 , day , c , m , n , p1_neighbor , p2_neighbor):
        self.p1 = p1
        self.p2 = p2
        self.day = day
        self.p1_neighbor = p1_neighbor
        self.p2_neighbor = p2_neighbor
        if len(np.nonzero(d[self.p1].shift[self.day])[0]) == 1:
            self.c = c
            self.p1_neighbor.shift[self.day][self.c:] = d[self.p2].shift[self.day][self.c:].copy()
            self.p2_neighbor.shift[self.day][self.c:] = d[self.p1].shift[self.day][self.c:].copy()
            self.Tvalue = self.p1_neighbor.fitness_day(self.day) + self.p2_neighbor.fitness_day(self.day)
        
        else:
            self.m = m
            self.n = n
            self.p1_neighbor.shift[self.day][self.n : self.m + 1] = d[self.p2].shift[self.day][self.n : self.m + 1].copy()
            self.p2_neighbor.shift[self.day][self.n : self.m + 1] = d[self.p1].shift[self.day][self.n : self.m + 1].copy()
            self.Tvalue = self.p1_neighbor.fitness_day(self.day) + self.p2_neighbor.fitness_day(self.day)
            
    def takeValue(self):
        return self.Tvalue  
        

    
class bus_route:
    def __init__(self ,bus_number, demand , driving_time):
        self.bus_number = bus_number
        self.demand = demand
        self.driving_time = driving_time
        
    @property
    def left_demand(self):
        l = np.zeros(7)
        for day in range(7):
            l[day] = len(self.demand[day])
        
        return l
       

class driver(algorithm): 
    
    def __init__(self, driver_number):
        self.driver_number = driver_number   #司機編號
        self.route = []                      #司機路線
        self.dayoff = []                     #司機休假
        self.shift = np.zeros((7,207))       #司機班表
        self.working_time = np.zeros(7)      #司機工作時間
        self.breaking_time = np.zeros(7)     #司機休息時間
        self.working_diff_time = np.zeros(7) #與8小時差異
        self.shift_number = np.zeros(7)      #司機班次數量
        self.penalty = np.zeros(7)           #班次懲罰
        self.route_number = []               #司機路線編號

    def get_route(self , l):  #input 要是list
        for r in l:           
            self.route.append(r)
            self.route_number.append(r.bus_number)
            
        self.route_number = sorted(self.route_number)
    
    def schedule_late(self):
        working_time_bound = 400
        lunch = range(77,91)
        dinner = range(144,168)
        
        for day in range(7):            #從最晚班開始排
            if day not in self.dayoff:
                free_time = 300
                work_time = 0
                while work_time <= working_time_bound:
                    best_time = -1
                    for route in self.route:                     #shift : 77 168E 168W   
                        if sum(route.demand[day]) == 0:          #判斷此路線還有沒有班可排
                            continue                    
                
                        if len([x for x in route.demand[day] if x <= free_time - route.driving_time[x]]) == 0:  #判斷此路線是否還有可行班表
                            continue
                        
                        if best_time <= max([x for x in route.demand[day] if x <= free_time - route.driving_time[x]]):
                            best_time = max([x for x in route.demand[day] if x <= free_time - route.driving_time[x]])
                            best_route = route
                            
                    if best_time == -1:
                        break
                    
                    self.shift[day][best_time] = best_route.bus_number            #排進班表
                    best_route.demand[day].remove(best_time)                      #此路線班表需求已排給司機
                    work_time += best_route.driving_time[best_time] * 5
                    
                    free_time = best_time
                    
                    free_time -= 2                                                    #加10分休息
             
                    if (free_time in lunch) or (free_time in dinner):                 #午餐、晚餐再加50分鐘
                        free_time -= 10
    
    def schedule_early(self , start_time):
        working_time_bound = 400
        lunch = range(77,91)
        dinner = range(144,168)
        
        for day in range(7):            #從最早班開始排
            if day not in self.dayoff:          #在可行的路線鍾挑最快的班次
                free_time = start_time    
                work_time = 0
                while work_time <= working_time_bound:
                    best_time = 9999
                    for route in self.route:                     #shift : 77 168E 168W   
                        if sum(route.demand[day]) == 0:          #判斷此路線還有沒有班可排
                            continue                       
                        
                        if len([x for x in route.demand[day] if x >= free_time]) == 0:  #判斷此路線是否還有可行班表
                            continue
                                                
                        if best_time >= min([x for x in route.demand[day] if x >= free_time]):
                            best_time = min([x for x in route.demand[day] if x >= free_time])   #選到的時段
                            best_route = route   #選到的路線                  

                    if best_time == 9999:                    #都沒班可排，直接跳出迴圈，排下一天的班表
                        break
                        
                    self.shift[day][best_time] = best_route.bus_number            #排進班表
                    best_route.demand[day].remove(best_time)                      #此路線班表需求已排給司機
                    work_time += best_route.driving_time[best_time] * 5
                    
                    free_time = best_time
                    free_time += best_route.driving_time[best_time]                   #加上駕駛時間
                    free_time += 2                                                    #加10分休息
             
                    if (free_time in lunch) or (free_time in dinner):                 #午餐、晚餐再加50分鐘
                        free_time += 10
                 
    def fitness_day(self, day):
        self.working_time[day] = 0
        self.breaking_time[day] = 0
        self.shift_number[day] = len(np.nonzero(self.shift[day])[0])
        if (day in self.dayoff) or (self.shift_number[day] == 0):
            return 0
        
        else:
            for i in np.nonzero(self.shift[day])[0]:                     
                self.working_time[day] += super().drive_time(self.shift[day][i] , i) * 5
                 
            if self.shift_number[day] == 1:            #休息時間
                self.breaking_time[day] += 0

            else:       
                start_time = np.nonzero(self.shift[day])[0][0]
                k = int(self.shift_number[day] - 1)
                end_time = np.nonzero(self.shift[day])[0][k]
                self.breaking_time[day] = (end_time - start_time) * 5 - self.working_time[day] + super().drive_time(self.shift[day][np.nonzero(self.shift[day])[0][k]] , np.nonzero(self.shift[day])[0][k]) * 5
                 
            self.working_diff_time[day] = abs(self.working_time[day] - 480)
            
        return self.working_diff_time[day] + self.breaking_time[day]
        
                             
    @property
    def fitness_list(self):
        l = np.zeros(7)
        for day in range(7):
            l[day] = self.fitness_day(day)
               
        return l 
    

        
    @property  
    def fitness(self):
        return sum(self.fitness_list)
               


#%%
for diff in range(2):
    iteration = 100000
            
    D77d = [] #1
    D168Ed = [] #2
    D168Wd = [] #3
    D0Northd = [] #4
    D0Southd = [] #5
    D92d = [] #6
    DY1d = [] #7
    DY1_exd = [] #8
    
    data_D = ["77D" ,"168ED" ,"168WD" , "0ND" , "0SD" , "92D" , "Y1D" ]
    data_W = ["77W" ,"168EW" ,"168WW" , "0NW" , "0SW" , "92W" , "Y1W" ]
    route_d = [D77d , D168Ed , D168Wd ,D0Northd , D0Southd , D92d , DY1d ]
    for day in range(7):
        if (day != 5) and (day != 6):
            for j in range(7):
                l = []
                file = pd.read_excel("current shift.xlsx" , sheet_name=data_D[j])
                l = list(file['new']).copy()
                route_d[j].append(l)
            l = []
            DY1_exd.append(l)
        else:
            for j in range(7):
                l = []
                file = pd.read_excel("current shift.xlsx" , sheet_name=data_W[j])
                l = list(file['new']).copy()
                route_d[j].append(l)
            l = []
            file = pd.read_excel("current shift.xlsx" , sheet_name= "Y1exW")
            l = list(file['new']).copy()
            DY1_exd.append(l)
       
    #公車路線資料匯入        
    D77 = bus_route(1, D77d, D77_drive_time)
    D168E = bus_route(2, D168Ed , D168E_drive_time)
    D168W = bus_route(3, D168Wd , D168W_drive_time)
    D0North = bus_route(4,D0Northd , D0North_drive_time)
    D0South = bus_route(5,D0Southd , D0South_drive_time)
    D92 = bus_route(6,D92d , D92_drive_time)
    DY1 = bus_route(7,DY1d , DY1_drive_time)
    DY1_ex = bus_route(8 , DY1_exd , DY1_ex_drive_time)            
    
    #initialize
    
    d = []
    
    for i in range(70):
            
        a = driver(i) 
        if i <= 58:
            a.dayoff = [i % 5]
            a.get_route(list(np.random.choice([D77,D168E,D168W,D92,D0North,D0South,DY1,DY1_ex] , 3,p = [0.16,0.17,0.17,0.08,0.08,0.13,0.13,0.08],replace = False)))
            
        else:
            a.dayoff = [(i % 2) + 5]
            a.get_route(list(np.random.choice([D77,D168E,D168W,D92,D0North,D0South,DY1] , 3,p = [0.16,0.16,0.16,0.1,0.1,0.15,0.17],replace = False)))
            
        #a.schedule_early(start_time = np.random.choice(np.arange(207) , p = np.array(c[0] / sum(c[0]).ravel())))
        
        if i < 15 :       
            a.schedule_early(start_time=0)
            
            
        else:
            a.schedule_late()
        
        d.append(a)

#sa = GA()
#start = time.time()
#
#sa.run(d,10000) 
#end = time.time()  
#plt.plot(np.arange(len(sa.his)) , sa.his, label = 'GA_SA')
#print("p0 " , sa.phase0 , "p1 " , sa.phase1 ,"p2 " , sa.phase2 ,"p3 " , sa.phase3 ,"all time: " , end - start)
#print("p1: " ,sa.p1time ,"p2: " ,sa.p2time ,"crossover: " ,sa.crosstime ,"mutation: " ,sa.mutationtime , "all time: " , end - start)
            
               
    if diff == 1:
        tb = GA_TB()
        start = time.time()
        tb.run_TB(d,iteration)
        end = time.time()
        
        tb_time = end - start
        
    elif diff == 0:
        sa = GA_SA()
        start = time.time()
        sa.run(d,iteration)
        end = time.time()
        
        sa_time = end - start
        
    else:
        ga = GA()
        start = time.time()
        ga.run(d,iteration)
        end = time.time()
        
        ga_time = end - start


#%%
D77d = [] #1
D168Ed = [] #2
D168Wd = [] #3
D0Northd = [] #4
D0Southd = [] #5
D92d = [] #6
DY1d = [] #7
DY1_exd = [] #8

data_D = ["77D" ,"168ED" ,"168WD" , "0ND" , "0SD" , "92D" , "Y1D" ]
data_W = ["77W" ,"168EW" ,"168WW" , "0NW" , "0SW" , "92W" , "Y1W" ]
route_d = [D77d , D168Ed , D168Wd ,D0Northd , D0Southd , D92d , DY1d ]
for day in range(7):
    if (day != 5) and (day != 6):
        for j in range(7):
            l = []
            file = pd.read_excel("current shift.xlsx" , sheet_name=data_D[j])
            l = list(file['new']).copy()
            route_d[j].append(l)
        l = []
        DY1_exd.append(l)
    else:
        for j in range(7):
            l = []
            file = pd.read_excel("current shift.xlsx" , sheet_name=data_W[j])
            l = list(file['new']).copy()
            route_d[j].append(l)
        l = []
        file = pd.read_excel("current shift.xlsx" , sheet_name= "Y1exW")
        l = list(file['new']).copy()
        DY1_exd.append(l)
   
#公車路線資料匯入        
D77 = bus_route(1, D77d, D77_drive_time)
D168E = bus_route(2, D168Ed , D168E_drive_time)
D168W = bus_route(3, D168Wd , D168W_drive_time)
D0North = bus_route(4,D0Northd , D0North_drive_time)
D0South = bus_route(5,D0Southd , D0South_drive_time)
D92 = bus_route(6,D92d , D92_drive_time)
DY1 = bus_route(7,DY1d , DY1_drive_time)
DY1_ex = bus_route(8 , DY1_exd , DY1_ex_drive_time)            
#%%
#initialize

d = []

for i in range(70):
        
    a = driver(i) 
    if i <= 58:
        a.dayoff = [i % 5]
        a.get_route(list(np.random.choice([D77,D168E,D168W,D92,D0North,D0South,DY1,DY1_ex] , 3,p = [0.16,0.17,0.17,0.08,0.08,0.13,0.13,0.08],replace = False)))
        
    else:
        a.dayoff = [(i % 2) + 5]
        a.get_route(list(np.random.choice([D77,D168E,D168W,D92,D0North,D0South,DY1] , 3,p = [0.16,0.16,0.16,0.1,0.1,0.15,0.17],replace = False)))
        
    #a.schedule_early(start_time = np.random.choice(np.arange(207) , p = np.array(c[0] / sum(c[0]).ravel())))
    
    if i < 15 :       
        a.schedule_early(start_time=0)
        
        
    else:
        a.schedule_late()
    
    d.append(a)

#%%
sa = GA_SA()
start = time.time()

sa.run(d,100000) 
end = time.time()  
#plt.plot(np.arange(len(sa.his)) , sa.his, label = 'GA_SA')
#print("p1: " ,sa.p1time ,"p2: " ,sa.p2time ,"crossover: " ,sa.crosstime ,"mutation: " ,sa.mutationtime , "all time: " , end - start)
print("time: ", end-start)
#print(sa.fitness_his(d))
 #%%
#班次需求分布圖--平日
B = [D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South]
weekdaydemand = np.zeros((7,207))
for bus in B:
    for day in range(5):        
        for i in bus.demand[day]:
            weekdaydemand[day][i] += 1
            

plt.bar(np.arange(len(weekdaydemand[0])),weekdaydemand[0])
plt.xlabel('Period')
plt.ylabel('Demand Trip')
plt.legend()
#plt.savefig("weekday demand.jpg")

print(sum(sum(weekdaydemand)))
#%%班次需求分布圖--假日
B = [D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South]
weekenddemand = np.zeros((7,207))
for bus in B:
    for day in range(2):        
        for i in bus.demand[day+5]:
            weekenddemand[day][i] += 1

plt.bar(np.arange(len(weekenddemand[0])),weekenddemand[0])
plt.xlabel('Period')
plt.ylabel('Demand Trip')
plt.legend()
df = pd.DataFrame(weekenddemand[0])
#df.to_excel("weekenddemand[0].xlsx")
#plt.savefig("weekend demand.jpg")
print(sum(sum(weekenddemand)))
#%%
driver_list = np.zeros((490,7))
i = 0
for driver in d:
    for day in range(7):
        j = 0
        for shift in range(207):
            if driver.shift[day][shift] != 0:
                driver_list[i][j] = shift
                j += 1
        
        i += 1
driver_list = pd.DataFrame(driver_list)
#driver_list.to_excel("driver routenumber.xlsx")
#%%
l = []
for driver in d:
    for day in range(7):
        l.append(driver.fitness_list[day])
l = pd.DataFrame(l)

l.to_excel("driver fitness.xlsx")
#%%
ga = GA()
ga.run(d,2000)
plt.plot(np.arange(len(ga.his)) , ga.his, label = 'GA')
#%%
sa = GA_SA()
sa.run(d,25000)
plt.plot(np.arange(len(sa.his)) , sa.his, label = 'GA_SA')
#%%
tb = GA_TB()
tb.run_TB(d,25000)
plt.plot(np.arange(len(tb.his)) , tb.his, label = 'GA_TB')
#%%   比較圖

plt.plot(np.arange(len(tb.his)) , tb.his , label = 'GA_TS' , linewidth = 1)
plt.plot(np.arange(len(sa.his)) , sa.his, label = 'GA_SA')
#plt.plot(np.arange(len(ga.his)) , ga.his, label = 'GA')

plt.xlabel('Iteration')
plt.ylabel('Fitness')
plt.legend()
#plt.savefig("p = 70,iter = 200000_2.jpg")
print(tb.his[-1] , sa.his[-1] , ga.his[-1])
print(tb_time , sa_time , ga_time)
#%% 判斷是否有排班時段錯誤
for t in d:
    for day in range(7):
        if t.breaking_time[day] < 0:
            print("driver:",t.driver_number ," self.day:" ,day ," breaking time:", t.breaking_time[day] )

#%%  判斷是否有排班路線錯誤
for t in d:
    for day in range(7):
        for shift in np.nonzero(t.shift[day])[0]:
            if t.shift[day][shift] not in t.route_number:
                print(t.driver_number , t.shift[day][shift] , t.route_number)
                
#%%  公車輛需求分布圖
ra = algorithm()
bus_demand = np.zeros(207)
for route in [D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South]:
    for shift in route.demand[6]:
        bus_demand[shift : shift + route.driving_time[shift] + 1] = [x + 1 for x in bus_demand[shift : shift + route.driving_time[shift] + 1]]

c = np.zeros(207)

for i in range(107):
    c[i] = sum(bus_demand[i:i + 100])
    
plt.plot(np.arange(len(bus_demand)) ,bus_demand)  
plt.xlabel('Period')
plt.ylabel('Driver')
plt.legend()
#plt.savefig("weekend driver.jpg")
#%%

cplex = pd.read_excel("shiftdemand.xlsx")
cplex = np.array(cplex)
cplex = np.transpose(cplex)
cplex[cplex==1] = 6
#%%
cplex_list = []
cplex_fitness = 0

for i in range(12):
    c = driver(i)
    c.shift[0] = cplex[i].copy()
    cplex_list.append(c)
    cplex_fitness += c.fitness
cplex_fitness
#%%
D92d = [] #6

data_D = ["92D" ]

route_d = [D92d ]

l = []
file = pd.read_excel("current shift.xlsx" , sheet_name="92D")
l = list(file['new']).copy()
D92d.append(l)

for i in range(6):
    a = list(np.zeros(207))
    D92d.append(a)

    
D92 = bus_route(6,D92d , D92_drive_time)   

d = []

for i in range(12):
        
    a = driver(i) 
    a.get_route([D92])
    a.dayoff = [5]
        
    
    
    if i < 4 :       
        a.schedule_early(start_time=0)
        
        
    else:
        a.schedule_late()
    
    d.append(a)
#%%

sa = GA_TB()
start = time.time()
sa.run_TB(d,5000)
end = time.time()
print(end-start)
#plt.plot(np.arange(len(sa.his)) , sa.his, label = 'GA_SA')
#%%
total = 0
for driver in d:
    total += driver.fitness
total
