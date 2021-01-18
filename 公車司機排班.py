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

#%%

D77d = [] #1
D168Ed = [] #2
D168Wd = [] #3
D0Northd = [] #4
D0Southd = [] #5
D92d = [] #6
DY1d = [] #7
DY1_exd = [] #8
    
for day in range(7):
        
    if (day != 5) and (day != 6) :
        l = []
        file = pd.read_excel("168westD_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        D168Wd.append(l)
        
        l = []
        file = pd.read_excel("168eastD_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        D168Ed.append(l)
        
        l = []
        file = pd.read_excel("77D_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        D77d.append(l)
        
        l = []
        file = pd.read_excel("0NorthD_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        D0Northd.append(l)
        
        l = []
        file = pd.read_excel("0SouthD_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        D0Southd.append(l)
        
        l = []
        file = pd.read_excel("92D_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        D92d.append(l)
        
        l = []
        file = pd.read_excel("Y1D_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        DY1d.append(l)
        
        l = []
        DY1_exd.append(l)
        
        
        
    if (day == 5) or (day == 6):
        
        l = []
        file = pd.read_excel("168westW_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        D168Wd.append(l)
        
        l = []
        file = pd.read_excel("168eastW_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        D168Ed.append(l)
        
        l = []
        file = pd.read_excel("77W_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        D77d.append(l)
        
        l = []
        file = pd.read_excel("0NorthD_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        D0Northd.append(l)
        
        l = []
        file = pd.read_excel("0SouthW_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        D0Southd.append(l)
        
        l = []
        file = pd.read_excel("92W_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        D92d.append(l)
        
        l = []
        file = pd.read_excel("Y1W_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
        DY1d.append(l)
        
        l = []
        file = pd.read_excel("Y1_exW_shift.xlsx")
        for i in range(len(file['time'])):
            l.append(int(file['time'][i] / 5))
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

for i in range(130):
        
    a = driver(i)

        
    a.get_route(rd.sample([D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South] , route_num))
    a.dayoff = [i % 7]     
    a.schedule_early(start_time = np.random.choice(np.arange(207) , p = np.array(c[0] / sum(c[0]).ravel())))
    d.append(a)

#%%
#reproduce
d2 = d.copy()
his = []
for time in range(100000):
    d1 = Reproduce(d)
    his.append(fitness_his(d1))
    d = d1.copy()

plt.plot(np.arange(len(his)) , his)


#%% 判斷是否有排班錯誤
for t in d:
    for day in range(7):
        if t.breaking_time[day] < 0:
            print(t.driver_number , day , t.breaking_time[day])

#%%
#需求分布圖
B = [D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South]
b = np.zeros((7,207))
for bus in B:
    for day in range(7):        
        for i in bus.demand[day]:
            b[day][i] += 1

c = np.zeros((7,207))

for day in range(7):
    
    for i in range(157):
        c[day][i] = sum(b[day][i:i+50])
    
plt.bar(np.arange(len(b[0])),b[0])
            
#%%

class driver:
  
    
    def __init__(self, driver_number):
        self.driver_number = driver_number   #司機編號
        self.route = []                      #司機路線
        self.dayoff = []                     #司機休假
        self.shift = np.zeros((7,207))       #司機班表
        self.working_time = np.zeros(7)      #司機工作時間
        self.breaking_time = np.zeros(7)     #司機休息時間
        self.working_diff_time = np.zeros(7) #與8小時差異
        self.shift_number = np.zeros(7)      #司機班次數量
        self.penalty = np.zeros(7)
        self.route_number = []

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
                    self.shift_number[day] += 1                                   #班次數量+1
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
                    self.shift_number[day] += 1                                   #班次數量+1
                    work_time += best_route.driving_time[best_time] * 5
                    
                    free_time = best_time
                    free_time += best_route.driving_time[best_time]                   #加上駕駛時間
                    free_time += 2                                                    #加10分休息
             
                    if (free_time in lunch) or (free_time in dinner):                 #午餐、晚餐再加50分鐘
                        free_time += 10

                        
   
    @property  
    def fitness_list(self):
        l = np.zeros(7)
        for day in range(7):  
             
             self.working_time[day] = 0
             self.breaking_time[day] = 0
             if day not in self.dayoff:                                 #計算working_time 
                if self.shift_number[day] == 1:
                    self.breaking_time[day] += 200 
                self.penalty[day] = abs(self.shift_number[day] - 4) ** 2 * 100
                self.shift_number[day] = len(np.nonzero(self.shift[day])[0])
                for i in range(len(np.nonzero(self.shift[day])[0])):
                    for route in self.route:       
                        if self.shift[day][np.nonzero(self.shift[day])[0][i]] == route.bus_number:
                            self.working_time[day] += route.driving_time[np.nonzero(self.shift[day])[0][i]] * 5
                            break
              
                for i in range(len(np.nonzero(self.shift[day])[0])):
                    if i != len(np.nonzero(self.shift[day])[0]) - 1:
                       self.breaking_time[day] += abs(np.nonzero(self.shift[day])[0][i] - np.nonzero(self.shift[day])[0][i + 1]) * 5
                            
                    else:
                        for route in self.route:
                            if self.shift[day][np.nonzero(self.shift[day])[0][i]] == route.bus_number:
                                self.breaking_time[day] += route.driving_time[np.nonzero(self.shift[day])[0][i]] * 5
                                break
                self.breaking_time[day] -= self.working_time[day]
                self.working_diff_time[day] = abs(self.working_time[day] - 480)
               
                l[day] = self.working_diff_time[day] + self.breaking_time[day] #+ self.penalty[day]
                
        return l 
        
    @property  
    def fitness(self):
        return sum(self.fitness_list)
               
#%%
       

    
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
    
#%%
        
def drive_time(number , time):
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
    
#%%
def find_break(k1,k2):    #input:某天的班表   output:回傳可交配的點
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
            shift_end = shift + drive_time(l[shift] , shift) + 1
            if shift_end >= len(l):
                shift_end = len(l)
            
            l[shift : shift_end] = [1] * (shift_end - shift)
            if (shift + drive_time(l[shift] , shift) + 1 in lunch) and (eat_lunch == False):
                l[shift_end : shift_end + 10] = [1] * 10
                eat_lunch = True
                
            if (shift + drive_time(l[shift] , shift) + 1 in dinner) and (eat_dinner == False):
                l[shift_end : shift_end + 10] = [1] * 10
                eat_dinner = True
    
    s1 = set([i for i , e in enumerate(l1) if e == 0])
    s2 = set([i for i , e in enumerate(l2) if e == 0])
    k = list(s1.intersection(s2))
    
    return k

def findtwo(a):   #找出交配點(雙點交配)
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
            

#%%    演算法
    
def Reproduce(d): 
    global p2
    fitness = []          #fitness:真實fitness分數    score:標準化後分數   location:染色體位置
    location = []
    for i in range(len(d)):   
        fitness.append(d[i].fitness)
        location.append(i)
    score = fitness.copy()
    for i in range(len(d)):
        score[i] = fitness[i] / sum(fitness)
        
    p1 = np.random.choice(location , p = np.array(score).ravel())   #p1:第一個Parent染色體位置
    
    day = list(d[p1].fitness_list).index(max(d[p1].fitness_list))   #選適應值最差的那個天數
    
    candidate = [x for x in d if sorted(x.route_number) == sorted(d[p1].route_number) and day != x.dayoff[0] ] #candidate:第二個Parent候選人位置，先找服務相同路線的司機
    if len(candidate) == 0:
        candidate = [x for x in d if x.route in d[p1].route and day != x.dayoff[0]]        #若無，則選有服務某幾條路線的司機
        
    if len(candidate) == 0:
        candidate = [x for x in d if d[p1].route in x.route and day != x.dayoff[0]]
        
    
    #########選P2
    #如果P1只有1個班次的交配方式-->單點交配
    if len(np.nonzero(d[p1].shift[day])[0]) == 1:
        Crossover = False
        rd.shuffle(candidate)   #候選人洗牌
        for route in candidate:
            cross = find_break(d[p1].shift[day] , route.shift[day])
            cross_candidate = [x for x in cross if abs(x - np.nonzero(d[p1].shift[day])[0][0]) <= 10]   #選出在10單位時間內可交配的點
            
            if len(cross_candidate) == 0:
                continue
            
            else:
                p2 = route.driver_number
                
                while len(cross_candidate) > 0:
                    c = rd.choice(cross_candidate)
                    
                    #若只是鏡像交配，則重新迴圈
                    if (sum(d[p1].shift[day][:c]) + sum(d[p2].shift[day][:c]) == 0) or (sum(d[p1].shift[day][c:]) + sum(d[p2].shift[day][c:]) == 0):
                        if c > np.nonzero(d[p1].shift[day])[0]:
                            cross_candidate = [x for x in cross_candidate if x < np.nonzero(d[p1].shift[day])[0][0]]
                            continue
                        
                        else:
                            cross_candidate = [x for x in cross_candidate if x > np.nonzero(d[p1].shift[day])[0][0]]
                            continue
                        
                    #服務路線限制        
                    s1 = list(d[p1].shift[day][c : ])
                    s2 = list(d[p2].shift[day][c : ])
                    s1.remove(0.0)
                    s2.remove(0.0)
                    k1 = set(s1)
                    k2 = set(s2)
                    
                    if (k1 <= set(d[p2].route_number)) and (k2 <= set(d[p1].route_number)) is False :  #若有無法服務的路線，則重新迴圈                        
                        if c > np.nonzero(d[p1].shift[day])[0]:
                            cross_candidate = [x for x in cross_candidate if x < np.nonzero(d[p1].shift[day])[0][0]]
                            continue
                        
                        else:
                            cross_candidate = [x for x in cross_candidate if x > np.nonzero(d[p1].shift[day])[0][0]]
                            continue
                    
                    #若皆符合限制式，則交配
                    else: 
                        #SA部分
                        
                        p1_neighbor = driver(1001)
                        p1_neighbor.get_route([D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South])
                        p2_neighbor = driver(1002)
                        p2_neighbor.get_route([D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South])
                        
                        p1_neighbor.shift[day] = d[p1].shift[day].copy()
                        p2_neighbor.shift[day] = d[p2].shift[day].copy()
                        
                        p1_neighbor.shift[day][c:] = d[p2].shift[day][c:].copy()
                        p2_neighbor.shift[day][c:] = d[p1].shift[day][c:].copy()
                        
                        #若交配後適應值較佳，則交配
                        if p1_neighbor.fitness_list[day] + p2_neighbor.fitness_list[day] <= d[p1].fitness_list[day] + d[p2].fitness_list[day]:
                            d[p1].shift[day] = p1_neighbor.shift[day].copy()
                            d[p2].shift[day] = p2_neighbor.shift[day].copy()    
                            
                        
                        
                        Crossover = True  #交配成功
                        break
                
                if Crossover == False:   #若交配無成功，則重新選P2      
                    continue
                
                else:                    #若交配成功，則跳出迴圈
                    break
                
    #如果P1有2個以上個班次數量-->雙點交配             
    else:
        rd.shuffle(candidate)   #候選人洗牌
        for k2 in candidate:            
            p2 = k2.driver_number
            cross = find_break(d[p1].shift[day] , d[p2].shift[day])  #找出可交配點
            (n , m) = findtwo(cross)   #選出兩交配點
            
            if n == m:
                continue
            
            if d[p1].route_number != d[p2].route_number:
                #服務路線限制        
                s1 = list(d[p1].shift[day][n : m + 1])
                s2 = list(d[p2].shift[day][n : m + 1])
                s1.remove(0.0)
                s2.remove(0.0)
                k1 = set(s1)
                k2 = set(s2)
                
                if (k1 <= set(d[p2].route_number)) and (k2 <= set(d[p1].route_number)) is False :  #若有無法服務的路線，則重新迴圈     
                    continue
             
            #若皆符合限制式，則交配
  
            #SA部分
            
            p1_neighbor = driver(1001)
            p1_neighbor.get_route([D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South])
            p2_neighbor = driver(1002)
            p2_neighbor.get_route([D77,D168E,D168W,D92,DY1,DY1_ex,D0North,D0South])
            
            p1_neighbor.shift[day] = d[p1].shift[day].copy()
            p2_neighbor.shift[day] = d[p2].shift[day].copy()
            
            p1_neighbor.shift[day][n : m + 1] = d[p2].shift[day][n : m + 1].copy()
            p2_neighbor.shift[day][n : m + 1] = d[p1].shift[day][n : m + 1].copy()
            
            #若交配後適應值較佳，則交配
            if p1_neighbor.fitness_list[day] + p2_neighbor.fitness_list[day] <= d[p1].fitness_list[day] + d[p2].fitness_list[day]:
                d[p1].shift[day] = p1_neighbor.shift[day].copy()
                d[p2].shift[day] = p2_neighbor.shift[day].copy()    
                
            break
        
    #突變

    for p in [p1 , p2]:                            
        if d[p].breaking_time[day] / (d[p].working_time[day] + d[p].breaking_time[day]) >= 0.4:  #若休息時間占總工時超過40%，則進行突變
            
            if len(np.nonzero(d[p].shift[day])[0]) == 0:    #若當天無班次，則跳過
                continue
            
            first_point = np.nonzero(d[p].shift[day])[0][0]   #第一個班次
            bus_route = d[p].shift[day][first_point]   #第一個班次之公車路線
            start_point = first_point + drive_time(bus_route , first_point) + 2  #設置起始突變點
            if len(np.nonzero(d[p].shift[day])[0]) == 1:
                if first_point >= 150:
                    last_point = np.nonzero(d[p].shift[day])[0][0]
                    start_point = np.nonzero(d[p].shift[day])[0][0] - 35
                else:
                    last_point = 999
            else:                                    
                last_point = np.nonzero(d[p].shift[day])[0][1]   #第二個班次
            
            for bus_route in d[p].route:
                mutation_point = [x for x in bus_route.demand[day] if x >= start_point and drive_time(bus_route.bus_number , x) + x + 2 <= last_point]
                if len(mutation_point) == 0:  #若無突變點，則再找下一個路線
                    continue
                
                else:
                    point = mutation_point[0]   #交配點
                    d[p].shift[day][point] = bus_route.bus_number  #排班次到班表中
                    bus_route.demand[day].remove(point)   #移除班次需求
                    break                           
              
    return d

    
#%%   計算所有司機適應值
def fitness_his(d):
    total = 0
    for i in range(len(d)):
        total += d[i].fitness
        
    return total
#%%
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