# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:46:07 2019

@author: Dharmik joshi
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import pypdfocr.pypdfocr_gs as pdfImg
from PIL import Image, ImageTk
#import Tkinter as tk
#import ttk
import matplotlib.cm as cm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
import sys
from collections import OrderedDict
import matplotlib.cm as cm

"""Ques 10 START==========================================================================================================="""

def month(x):
    if x[0:3]=='Jan':
        return 1
    elif x[0:3]=='Feb':
        return 2
    elif x[0:3]=='Mar':
        return 3
    elif x[0:3]=='Apr':
        return 4
    elif x[0:3]=='Ma' or x[0:3]=='May':
        return 5
    elif x[0:3]=='Jun':
        return 6
    elif x[0:3]=='Jul':
        return 7
    elif x[0:3]=='Aug':
        return 8
    elif x[0:3]=='Sep':
        return 9
    elif x[0:3]=='Oct':
        return 10
    elif x[0:3]=='Nov':
        return 11
    elif x[0:3]=='Dec':
        return 12
def install():
    Installs=[]
    global sample
    for i in sample['Installs']:  #converting string based installs into integer based
        if i=='Free':
           Installs.append(0)
        else:
           Installs.append(int(i.replace('+','').replace(',','')))
    return Installs 


def dates_str_to_int():
    global sample
    dates=sample['Last Updated']
    year=[]
    counter=0
    for i in dates:       
        year.append([int(i[-8:-6]),month(i[:-9]),int(i[-4:])])
        counter=counter+1
    return year

def qn10():
    year=dates_str_to_int()
    installs=install()
    category=list(OrderedDict.fromkeys(sample['Category']))
    temp=[]
    counter=0
    for i in category:
        temp.append([0,0,0,0,0,0,0,0,0,0,0,0])
    for i in sample['Category']:
        jcounter=0
        for j in category:
            if i==j:
                if year[counter][1]==1:
                    temp[jcounter][0]=temp[jcounter][0]+installs[counter]
                elif year[counter][1]==2:
                    temp[jcounter][1]=temp[jcounter][1]+installs[counter]
                elif year[counter][1]==3:
                    temp[jcounter][2]=temp[jcounter][2]+installs[counter]
                elif year[counter][1]==4:
                    temp[jcounter][3]=temp[jcounter][3]+installs[counter]
                elif year[counter][1]==5:
                    temp[jcounter][4]=temp[jcounter][4]+installs[counter]
                elif year[counter][1]==6:
                    temp[jcounter][5]=temp[jcounter][5]+installs[counter]
                elif year[counter][1]==7:
                    temp[jcounter][6]=temp[jcounter][6]+installs[counter]
                elif year[counter][1]==8:
                    temp[jcounter][7]=temp[jcounter][7]+installs[counter]
                elif year[counter][1]==9:
                    temp[jcounter][8]=temp[jcounter][8]+installs[counter]
                elif year[counter][1]==10:
                    temp[jcounter][9]=temp[jcounter][9]+installs[counter]
                elif year[counter][1]==11:
                    temp[jcounter][10]=temp[jcounter][10]+installs[counter]
                elif year[counter][1]==12:
                    temp[jcounter][11]=temp[jcounter][11]+installs[counter]
            jcounter=jcounter+1
        counter=counter+1
    return temp


def qn10try():
    global sample
    year=dates_str_to_int()
    installs=install()
    category=list(OrderedDict.fromkeys(sample['Category']))
    temp=[0,0,0,0,0,0,0,0,0,0,0,0]
    counter=0
    for i in year:
        if i[1]==1:
            temp[0]=temp[0]+installs[counter]
            counter=counter+1
        elif i[1]==2:
            temp[1]=temp[1]+installs[counter]
            counter=counter+1
        elif i[1]==3:
            temp[2]=temp[2]+installs[counter]
            counter=counter+1
        elif i[1]==4:
            temp[3]=temp[3]+installs[counter]
            counter=counter+1
        elif i[1]==5:
            temp[4]=temp[4]+installs[counter]
            counter=counter+1
        elif i[1]==6:
            temp[5]=temp[5]+installs[counter]
            counter=counter+1
        elif i[1]==7:
            temp[6]=temp[6]+installs[counter]
            counter=counter+1
        elif i[1]==8:
            temp[7]=temp[7]+installs[counter]
            counter=counter+1
        elif i[1]==9:
            temp[8]=temp[8]+installs[counter]
            counter=counter+1
        elif i[1]==10:
            temp[9]=temp[9]+installs[counter]
            counter=counter+1
        elif i[1]==11:
            temp[10]=temp[10]+installs[counter]
            counter=counter+1
        elif i[1]==12:
            temp[11]=temp[11]+installs[counter]
            counter=counter+1
        
    return temp
                

def function_q10(event):
    global screen,sample
    root = Toplevel(screen)
    
    big_frame = tk.Frame(root,bg='white',width='740',height=650,bd=4,relief=RIDGE)
    big_frame.place(x=10,y=60)
    
    w=750
    h=750
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')
    
    tk.Label(root,text="",bg='white').pack()
    tk.Label(root,text="Last Update",
             width=500,height=2,font=("Helvetica",11,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
    sample=pd.read_csv('DATA SET-2.csv')#reading data for the data set
    sample=sample.replace(np.NaN,0)
    sample.drop(index=[10472],inplace=True)

    cate_month = qn10()
    dict_month = {1:'Jan',2:'Feb',3:'March',4:'April',5:'May',6:'June',7:'July',8:'Aug',9:'Sept',10:'Oct',11:'Nov',12:'Dec'}
    
    categories = []#x-label
    months = [] #text
    maxinstalls = [] #y value
    
    cat = sample['Category'].unique()

    for index in range(len(cat)):
        categories.append(cat[index])
        maxinstalls.append(max(cate_month[index]))
        m = (cate_month[index].index(max(cate_month[index]))+1)    
        months.append(dict_month[m])
    
    #print(categories)
    
    #print(qn10try())#for month     list[month]=download    index+1= month
    
    
    colors = cm.rainbow(np.linspace(0, 1, len(categories)))
    
    figure2 = plt.Figure(figsize=(9,7), dpi=80)
    
    chart = figure2.add_subplot(111)
    #x=['Dis-Liked Apps' , 'Liked Apps']
    #y=[like_dislike_list.count(0),like_dislike_list.count(1)]
    bar_plot = chart.barh(categories,maxinstalls,color=colors)
    chart.set_ylabel("CATEGORY")
    chart.set_xlabel("COUNT OF TOTAL REVIEWS")
    figure2.suptitle('Maximum download month across all the year for each category')
    chart.legend()

    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=3,y=0)
    
    #print(max(maxinstalls))
    #print(categories[maxinstalls.index(max(maxinstalls))])
    #print(months[maxinstalls.index(max(maxinstalls))])
    
    install_month  =qn10try()
    
    #print(max(install_month))
    #print(install_month.index(max(install_month)))
    #print(dict_month[install_month.index(max(install_month))+1])
    
    
    String="""Out of All categories present in data set Game category has seen the maximum downloads
              Maximum downloads for Game Category came in July month across all the years"""
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=530)
    
    String="""Across all the years ,which {} month has seen the maximum downloads from each of the category.""".format(dict_month[install_month.index(max(install_month))+1])
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=580)
            
    root.mainloop()

"""Ques 10 END==========================================================================================================="""


"""Ques 6 START==========================================================================================================="""
def function_q6(event):
    global screen
  
    root = Toplevel(screen)
    
    big_frame = tk.Frame(root,bg='white',width='700',height=550,bd=4,relief=RIDGE)
    big_frame.place(x=10,y=60)
    
    w=720
    h=650
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')
    
    tk.Label(root,text="",bg='white').pack()
    tk.Label(root,text="Last Update",
             width=500,height=2,font=("Helvetica",11,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
    
    df = pd.read_csv("DATA SET-2.csv")
    
    #print(df.head(5))
    
    #df.drop(9148,axis=0, inplace=True)
    #df.drop(10472,axis=0,inplace=True)
    
    # Data cleaning for "Installs" column
    #print(df['Installs'].head(5))
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    #print(df['Installs'].head(5))
    
    
    df['Installs'] = pd.to_numeric(df['Installs'])
    
    d = pd.DatetimeIndex(df['Last Updated'])
    df['year'] = d.year
    df['month'] = d.month
    
    #print((df['year'][5]))
    
    #6) For the years 2016,2017,2018 what are the category of apps that have got the most and the least downloads. What is the percentage increase or decrease that the
    
    dict_2016 = {}
    dict_2017 = {}
    dict_2018 = {}
    
    Category = []
    for cat in df['Category'].unique():
        Category.append(cat)
        dict_2016[cat]=0
        dict_2017[cat]=0
        dict_2018[cat]=0
    #print(Category)
    
    
    for index in range(len(df)):
        if df['year'][index]==2016:
            dict_2016[df['Category'][index]] += df['Installs'][index]
        if df['year'][index]==2017:
            dict_2017[df['Category'][index]] += df['Installs'][index]
        if df['year'][index]==2018:
            dict_2018[df['Category'][index]] += df['Installs'][index]
    
    #print(len(dict_2016))
    #print(len(dict_2017))
    #print(len(dict_2018))
    
    #print(dict_2016)
    
    #print(dict_2017)
    
    #print(dict_2018)
    
    
    max_2016_install = ["",0]
    max_2017_install = ["",0]
    max_2018_install = ["",0]
    
    
    min_2016_install = ["",99999999999]
    min_2017_install = ["",99999999999]
    min_2018_install = ["",99999999999]
    
    for cat in dict_2016:
        if max_2016_install[1] < dict_2016[cat]:
            max_2016_install[1] = dict_2016[cat]
            max_2016_install[0] = cat
        if max_2017_install[1] < dict_2017[cat]:
            max_2017_install[1] = dict_2017[cat]
            max_2017_install[0] = cat
        if max_2018_install[1] < dict_2018[cat]:
            max_2018_install[1] = dict_2018[cat]
            max_2018_install[0] = cat
            
        if min_2016_install[1] > dict_2016[cat]:
            min_2016_install[1] = dict_2016[cat]
            min_2016_install[0] = cat
        if min_2017_install[1] > dict_2017[cat]:
            min_2017_install[1] = dict_2017[cat]
            min_2017_install[0] = cat
        if min_2018_install[1] > dict_2018[cat]:
            min_2018_install[1] = dict_2018[cat]
            min_2018_install[0] = cat
            
            
            
    #print(max_2016_install)
    #print(max_2017_install)
    #print(max_2018_install)
    
    
    #print(min_2016_install)
    #print(min_2017_install)
    #print(min_2018_install)


    max_install = [max_2016_install[1],max_2017_install[1],max_2018_install[1]]
    min_install = [min_2016_install[1],min_2017_install[1],min_2018_install[1]]
    Years = ['2016','2017','2018']
    
    pos = np.arange(len(Years))
    bar_width = 0.3
    
    figure2 = plt.Figure(figsize=(8,4), dpi=85)

    chart = figure2.add_subplot(111)
    
    Max_bar = chart.bar(Years,max_install,bar_width,color='blue',edgecolor='black')
    Min_bar = chart.bar(pos+bar_width,min_install,bar_width,color='pink',edgecolor='black')
    
    chart.set_ylabel("Download")
    chart.set_xlabel('Years')
    figure2.suptitle('Max and Min download across 2016-17-18 years for a category',fontsize=18)
    plt.legend(['max','min'],loc=10)
    
    max_month = [max_2016_install[0],max_2017_install[0],max_2018_install[0]]
    min_month = [min_2016_install[0],min_2017_install[0],min_2018_install[0]]
    
    for idx,rect in enumerate(Max_bar):
                height = rect.get_height()
                chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,max_month[idx],ha='center', va='bottom', rotation=0) 
          
    for idx,rect in enumerate(Min_bar):
                height = rect.get_height()
                chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,min_month[idx],ha='center', va='bottom', rotation=0) 
                

    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=5,y=10)
    
    String = """  
             Blue bar shows the maximum download
             From the Analysis Installation of Game Category is increasing over the year  
             """
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=40,y=350)
    
   
    
    root.mainloop()

"""Ques 6 END==========================================================================================================="""



"""Ques 6-part2 START==========================================================================================================="""
def function_q6_part2(event):
    global screen
  
    root = Toplevel(screen)
    
    big_frame = tk.Frame(root,bg='white',width='700',height=450,bd=4,relief=RIDGE)
    big_frame.place(x=10,y=60)
    
    w=720
    h=550
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')
    
    tk.Label(root,text="",bg='white').pack()
    tk.Label(root,text="Last Update",
             width=500,height=2,font=("Helvetica",11,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
    
    df = pd.read_csv("DATA SET-2.csv")
    
    #print(df.head(5))
    
    #df.drop(9148,axis=0, inplace=True)
    #df.drop(10472,axis=0,inplace=True)
    
    # Data cleaning for "Installs" column
    #print(df['Installs'].head(5))
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    #print(df['Installs'].head(5))
    
    
    df['Installs'] = pd.to_numeric(df['Installs'])
    
    d = pd.DatetimeIndex(df['Last Updated'])
    df['year'] = d.year
    df['month'] = d.month
    
    #print((df['year'][5]))
    
    #6) For the years 2016,2017,2018 what are the category of apps that have got the most and the least downloads. What is the percentage increase or decrease that the
    
    dict_years = {}
    
    for year in df['year'].unique():
        dict_years[year]=0
    
    for index in range(len(df)):
        dict_years[df['year'][index]] += df['Installs'][index]
        
    
    Years = []
    list_install  = []
    
    
    for year in dict_years:
        if year==2016 or year==2017 or year==2018:
            Years.append(str(year))
            list_install.append(dict_years[year])
        
    print(dict_years)    
        
    x = dict_years[2016]
    y = dict_years[2017]
    z=dict_years[2018]
    
    per2016=1
    per2017=((y-x)/(x+y))*100
    per2018=((z-y)/(y+z))*100
    print(per2016,per2017,per2018)
    
    pos = np.arange(len(Years))
    bar_width = 0.3
    
    Years.reverse()
    list_install.reverse()
    
    figure2 = plt.Figure(figsize=(8,4), dpi=85)

    chart = figure2.add_subplot(111)
    
    chart.bar(Years,list_install,bar_width,color='blue',edgecolor='black')
    #Min_bar = chart.bar(pos+bar_width,min_install,bar_width,color='pink',edgecolor='black')
    
    chart.set_ylabel("Years")
    chart.set_xlabel('Installs')
    figure2.suptitle('Barchart on Installs on each Year ',fontsize=18)
    #plt.legend(Month,loc=10)
   
    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=5,y=10)
    
    String = """  
             % increase in 2016-17 is {:.1f}% and % increase in 2017-18 is {:.1f}%
             """.format(per2017,per2018)
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=40,y=360)
    
    root.mainloop()

"""Ques 6-part2 END==========================================================================================================="""


"""Feature f1 START=========================================================================================================="""

def function_f1(event):
    global screen
  
    root = Toplevel(screen)
    
    big_frame = tk.Frame(root,bg='white',width='800',height=450,bd=4,relief=RIDGE)
    big_frame.place(x=10,y=60)
    
    w=820
    h=550
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.resizable(False,False)
    root.configure(background='white')
    
    tk.Label(root,text="",bg='white').pack()
    tk.Label(root,text="Last Update",
             width=500,height=2,font=("Helvetica",11,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
    
          
    df = pd.read_csv("DATA SET-2.csv")
    
    print(df.head(0))
    
    print(df['Last Updated'].head(5))
    
    d = pd.DatetimeIndex(df['Last Updated'])
    df['year'] = d.year
    df['month'] = d.month
    
    # Data cleaning for "Installs" column
    print(df['Installs'].head(5))
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    print(df['Installs'].head(5))
    
    df['Installs'] = pd.to_numeric(df['Installs'])
    
    print(df['year'].unique())
    print(df['month'].unique())
    
    dict_year = {}
    
    for year in df['year'].unique():
        dict_year[year] = {}
        for month in df['month'].unique():
            dict_year[year][month] = 0
            
    #print(dict_year)
    
    ############################################################
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    dict_year_month_Installs_count = {}
    dict_year_Installs_count ={}
    for year in df['year'].unique():
        dict_year_month_Installs_count[year] = {}
        dict_year_Installs_count[year]=[0,0]
       
        for month in df['month'].unique():
            dict_year_month_Installs_count[year][month] = 0
            
    
    for index in range(len(df['year'])):
        dict_year_month_Installs_count[df['year'][index]][df['month'][index]]+=df['Installs'][index]
        dict_year_Installs_count[df['year'][index]][0]+=df['Installs'][index]
        dict_year_Installs_count[df['year'][index]][1]+=1
     
    print(dict_year_Installs_count)
    for i in dict_year_Installs_count:
        dict_year_Installs_count[i] = round(dict_year_Installs_count[i][0]/ dict_year_Installs_count[i][1])
            
    
    final_list = []
    print(dict_year_Installs_count)
    for year in dict_year_Installs_count:
        for month in dict_year_month_Installs_count[year]:
            if dict_year_Installs_count[year]<dict_year_month_Installs_count[year][month]:
                final_list.append("Year is {} and month is {}".format(year,month))
                
                
    
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    ################################################################
    
    
    for index in range(len(df)):
        if dict_year[df['year'][index]][df['month'][index]] < df['Installs'][index]:
            dict_year[df['year'][index]][df['month'][index]] = df['Installs'][index]
        else:
            continue
       
        
    print(dict_year)
    count,label,text = [],[],[]
    
    dict_month = {1:"Jan",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"Aug",9:"Sept",10:"Oct",11:"Nov",12:"Dec"}
    for year in dict_year:
        max_month = ""
        max_install = 0
        for month in dict_year[year]:
            if max_install < dict_year[year][month]:
                max_install = dict_year[year][month]
                max_month = month
        print("For {} best install is in {} month with {} installs".format(year,max_month,max_install))
        count.append(max_install)
        label.append(str(year))
        text.append(str(dict_month[max_month]))
    
    bar_plot = plt.bar(label,count,tick_label=label)
    
    for idx,rect in enumerate(bar_plot):
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width()/2., 1.05*height,text[idx],ha='center', va='bottom', rotation=0)
    
    color = cm.rainbow(np.linspace(0, 1, 10))
    figure2 = plt.Figure(figsize=(7,4), dpi=100)
    
    chart = figure2.add_subplot(111)
    #x=['Dis-Liked Apps' , 'Liked Apps']
    #y=[like_dislike_list.count(0),like_dislike_list.count(1)]
    bar_plot = chart.bar(label,count,color=color)
    
    chart.set_ylabel("Installs")
    chart.set_xlabel("Year")
    figure2.suptitle("Month Indicating best downloads")
    chart.legend()

    for idx,rect in enumerate(bar_plot):
            height = rect.get_height()
            chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,text[idx],ha='center', va='bottom', rotation=0)
    

    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=0,y=10)

    
    String="The Google Play Store has 9 Year data out of which Maximum Download is seen in year 2018"
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=410)
    
    plt.show()
    
"""Feature f1 END=========================================================================================================="""


"""Ques16 START==========================================================================================================="""

def plotGraph(big_frame,dict_year_month,year):
    
    dict_month = {1:"Jan",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"Aug",9:"Sept",10:"Oct",11:"Nov",12:"Dec"}
    
    month=[]
    installs=[]
    print(dict_year_month)
    for val in dict_year_month[int(year)]:
        print(val)
        month.append(dict_month[val[0]])
        installs.append(val[1])
    
      
    pos = np.arange(len(month))
    bar_width = 0.3
    
    #color = cm.rainbow(np.linspace(0, 1, len(month)))
    
    figure2 = plt.Figure(figsize=(7,4), dpi=90)

    chart = figure2.add_subplot(111)
    
    bar1 = chart.bar(month,installs,bar_width,color='blue',edgecolor='black')
    
    chart.set_ylabel("Installs")
    chart.set_xlabel('Year '+str(year))
    figure2.suptitle('Barchart on Maximum Installs of Month over Average downloads of year',fontsize=12)
    #plt.legend(Month,loc=10)
    """
    for idx,rect in enumerate(bar1):
                height = rect.get_height()
                chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,Month1[idx],ha='center', va='bottom', rotation=0) 
    """
    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=0,y=70)

    #Which quarter of which year has generated the highest number of install for each app used in the study?
    #String="In the above Graph Quarter of each Year with their Higher Installs are plotted"
    #tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=520)


def function_q16(event):
    global screen
  
    root = Toplevel(screen)
    
    big_frame = tk.Frame(root,bg='white',width='800',height=450,bd=4,relief=RIDGE)
    big_frame.place(x=10,y=60)
    
    w=820
    h=550
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.resizable(False,False)
    root.configure(background='white')
    
    tk.Label(root,text="",bg='white').pack()
    tk.Label(root,text="Last Update",
             width=500,height=2,font=("Helvetica",11,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
    
          
    df = pd.read_csv("DATA SET-2.csv")
    
    print(df.head(0))
    
    print(df['Last Updated'].head(5))
    
    d = pd.DatetimeIndex(df['Last Updated'])
    df['year'] = d.year
    df['month'] = d.month
    
    # Data cleaning for "Installs" column
    print(df['Installs'].head(5))
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    print(df['Installs'].head(5))
    
    df['Installs'] = pd.to_numeric(df['Installs'])
    
    print(df['year'].unique())
    print(df['month'].unique())
    
    dict_year = {}
    dict_year_count_month_wise={}
    for year in df['year'].unique():
        dict_year[year] = {}
        dict_year_count_month_wise[year]=[]
        for month in df['month'].unique():
            dict_year[year][month] = 0
    dict_month = {1:"Jan",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"Aug",9:"Sept",10:"Oct",11:"Nov",12:"Dec"}
    
    #print(dict_year)
    for index in range(len(df)):
        dict_year_count_month_wise[df['year'][index]].append(dict_month[df['month'][index]])
            
    for year in dict_year_count_month_wise:
        dict_year_count_month_wise[year] = list(set(dict_year_count_month_wise[year]))
        
    print(dict_year_count_month_wise)
    ############################################################
    
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    dict_year_month_Installs_count = {}
    dict_year_Installs_count ={}
    for year in df['year'].unique():
        dict_year_month_Installs_count[year] = {}
        dict_year_Installs_count[year]=[0,0]
        
       
        for month in df['month'].unique():
            dict_year_month_Installs_count[year][month] = 0
            
    
    for index in range(len(df['year'])):
        dict_year_month_Installs_count[df['year'][index]][df['month'][index]]+=df['Installs'][index]
        dict_year_Installs_count[df['year'][index]][0]+=df['Installs'][index]
        dict_year_Installs_count[df['year'][index]][1]+=1
     
    print(dict_year_Installs_count)
    for i in dict_year_Installs_count:
        print(i)
        dict_year_Installs_count[i] = round(dict_year_Installs_count[i][0]/ len(dict_year_count_month_wise[i])) # 12)#dict_year_Installs_count[i][1])
            
    final_list = []
    dict_year_month = {}
    list_year=[]
    print(dict_year_Installs_count)
    for year in dict_year_Installs_count:
        dict_year_month[year]=[]
        dict_year_month
        for month in dict_year_month_Installs_count[year]:
            if dict_year_Installs_count[year]<dict_year_month_Installs_count[year][month]:
                
                final_list.append("Year is {} and month is {}".format(year,month))
                dict_year_month[year].append([month,dict_year_month_Installs_count[year][month]])
                print(year)
                list_year.append(year)
                
    print(dict_year_month)
    
    tk.Label(big_frame,text="Please select the year",font=("Calibri",13,'italic'),fg='#75acff',bg='white').place(x=40,y=3)
    #tk.Label(big_frame,text="Ending Year:",font=("Calibri",13,'italic'),fg='#75acff',bg='white').place(x=400+100+50,y=45)
    limit = tk.ttk.Combobox(big_frame,values=list(set(list_year)))
    limit.place(x=200,y=3)
    plotGraph(big_frame,dict_year_month,str(2018))
    tk.Button(big_frame,text="SET GRAPH",bd=10,font=("Calibri",13,'italic'),fg='#75acff',bg='white',command = lambda:plotGraph(big_frame,dict_year_month,limit.get()) if limit.get()!="" else tk.messagebox.showerror("ERROR","PLEASE SELECT THE YEAR")).place(x=400,y=3)
    
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    ################################################################

"""Ques16 END==========================================================================================================="""

"""Ques11 START========================================================================================================="""
def install():
        global Installs,sample
        Installs=[]
        for i in sample['Installs']:  #converting string based installs into integer based
            if i=='Free':
               Installs.append(0)
            else:
               Installs.append(int(i.replace('+','').replace(',','')))
        return Installs  

def dates_str_to_int():
    global sample
    dates=sample['Last Updated']
    year=[]
    counter=0
    for i in dates:       
        year.append([int(i[-8:-6]),month(i[:-9]),int(i[-4:])])
        counter=counter+1
    return year

 
def month(x):
    if x[0:3]=='Jan':
        return 1
    elif x[0:3]=='Feb':
        return 2
    elif x[0:3]=='Mar':
        return 3
    elif x[0:3]=='Apr':
        return 4
    elif x[0:3]=='Ma' or x[0:3]=='May':
        return 5
    elif x[0:3]=='Jun':
        return 6
    elif x[0:3]=='Jul':
        return 7
    elif x[0:3]=='Aug':
        return 8
    elif x[0:3]=='Sep':
        return 9
    elif x[0:3]=='Oct':
        return 10
    elif x[0:3]=='Nov':
        return 11
    elif x[0:3]=='Dec':
        return 12

        
        

def quat():
    global sample
    
    counter=0
    temp1=[0,0,0,0,0,0,0,0,0,0,0,0]
    temp2=[0,0,0,0,0,0,0,0,0,0,0,0]
    temp3=[0,0,0,0,0,0,0,0,0,0,0,0]
    temp4=[0,0,0,0,0,0,0,0,0,0,0,0]
    temp5=[0,0,0,0,0,0,0,0,0,0,0,0]
    temp6=[0,0,0,0,0,0,0,0,0,0,0,0]
    temp7=[0,0,0,0,0,0,0,0,0,0,0,0]
    temp8=[0,0,0,0,0,0,0,0,0,0,0,0]
    temp9=[0,0,0,0,0,0,0,0,0,0,0,0]
    ins=install()
    counter=0
    year=dates_str_to_int()
    for i in year:
        if i[2]==2010:
            if i[1]==1:
                temp1[0]=temp1[0]+ins[counter]
                counter=counter+1
            elif i[1]==2:
                temp1[1]=temp1[1]+ins[counter]
                counter=counter+1
            elif i[1]==3:
                temp1[2]=temp1[2]+ins[counter]
                counter=counter+1
            elif i[1]==4:
                temp1[3]=temp1[3]+ins[counter]
                counter=counter+1
            elif i[1]==5:
                temp1[4]=temp1[4]+ins[counter]
                counter=counter+1
            elif i[1]==6:
                temp1[5]=temp1[5]+ins[counter]
                counter=counter+1
            elif i[1]==7:
                temp1[6]=temp1[6]+ins[counter]
                counter=counter+1
            elif i[1]==8:
                temp1[7]=temp1[7]+ins[counter]
                counter=counter+1
            elif i[1]==9:
                temp1[8]=temp1[8]+ins[counter]
                counter=counter+1
            elif i[1]==10:
                temp1[9]=temp1[9]+ins[counter]
                counter=counter+1
            elif i[1]==11:
                temp1[10]=temp1[10]+ins[counter]
                counter=counter+1
            elif i[1]==12:
                temp1[11]=temp1[11]+ins[counter]
                counter=counter+1
            
        
        elif i[2]==2011:
            if i[1]==1:
                temp2[0]=temp2[0]+ins[counter]
                counter=counter+1
            elif i[1]==2:
                temp2[1]=temp2[1]+ins[counter]
                counter=counter+1
            elif i[1]==3:
                temp2[2]=temp2[2]+ins[counter]
                counter=counter+1
            elif i[1]==4:
                temp2[3]=temp2[3]+ins[counter]
                counter=counter+1
            elif i[1]==5:
                temp2[4]=temp2[4]+ins[counter]
                counter=counter+1
            elif i[1]==6:
                temp2[5]=temp2[5]+ins[counter]
                counter=counter+1
            elif i[1]==7:
                temp2[6]=temp2[6]+ins[counter]
                counter=counter+1
            elif i[1]==8:
                temp2[7]=temp2[7]+ins[counter]
                counter=counter+1
            elif i[1]==9:
                temp2[8]=temp2[8]+ins[counter]
                counter=counter+1
            elif i[1]==10:
                temp2[9]=temp2[9]+ins[counter]
                counter=counter+1
            elif i[1]==11:
                temp2[10]=temp2[10]+ins[counter]
                counter=counter+1
            elif i[1]==12:
                temp2[11]=temp2[11]+ins[counter]
                counter=counter+1
        
        
        elif i[2]==2012:
            if i[1]==1:
                temp3[0]=temp3[0]+ins[counter]
                counter=counter+1
            elif i[1]==2:
                temp3[1]=temp3[1]+ins[counter]
                counter=counter+1
            elif i[1]==3:
                temp3[2]=temp3[2]+ins[counter]
                counter=counter+1
            elif i[1]==4:
                temp3[3]=temp3[3]+ins[counter]
                counter=counter+1
            elif i[1]==5:
                temp3[4]=temp3[4]+ins[counter]
                counter=counter+1
            elif i[1]==6:
                temp3[5]=temp3[5]+ins[counter]
                counter=counter+1
            elif i[1]==7:
                temp3[6]=temp3[6]+ins[counter]
                counter=counter+1
            elif i[1]==8:
                temp3[7]=temp3[7]+ins[counter]
                counter=counter+1
            elif i[1]==9:
                temp3[8]=temp3[8]+ins[counter]
                counter=counter+1
            elif i[1]==10:
                temp3[9]=temp3[9]+ins[counter]
                counter=counter+1
            elif i[1]==11:
                temp3[10]=temp3[10]+ins[counter]
                counter=counter+1
            elif i[1]==12:
                temp3[11]=temp3[11]+ins[counter]
                counter=counter+1
        
    
        
        elif i[2]==2013:
            if i[1]==1:
                temp4[0]=temp4[0]+ins[counter]
                counter=counter+1
            elif i[1]==2:
                temp4[1]=temp4[1]+ins[counter]
                counter=counter+1
            elif i[1]==3:
                temp4[2]=temp4[2]+ins[counter]
                counter=counter+1
            elif i[1]==4:
                temp4[3]=temp4[3]+ins[counter]
                counter=counter+1
            elif i[1]==5:
                temp4[4]=temp4[4]+ins[counter]
                counter=counter+1
            elif i[1]==6:
                temp4[5]=temp4[5]+ins[counter]
                counter=counter+1
            elif i[1]==7:
                temp4[6]=temp4[6]+ins[counter]
                counter=counter+1
            elif i[1]==8:
                temp4[7]=temp4[7]+ins[counter]
                counter=counter+1
            elif i[1]==9:
                temp4[8]=temp4[8]+ins[counter]
                counter=counter+1
            elif i[1]==10:
                temp4[9]=temp4[9]+ins[counter]
                counter=counter+1
            elif i[1]==11:
                temp4[10]=temp4[10]+ins[counter]
                counter=counter+1
            elif i[1]==12:
                temp4[11]=temp4[11]+ins[counter]
                counter=counter+1
        
        elif i[2]==2014:
            if i[1]==1:
                temp5[0]=temp5[0]+ins[counter]
                counter=counter+1
            elif i[1]==2:
                temp5[1]=temp5[1]+ins[counter]
                counter=counter+1
            elif i[1]==3:
                temp5[2]=temp5[2]+ins[counter]
                counter=counter+1
            elif i[1]==4:
                temp5[3]=temp5[3]+ins[counter]
                counter=counter+1
            elif i[1]==5:
                temp5[4]=temp5[4]+ins[counter]
                counter=counter+1
            elif i[1]==6:
                temp5[5]=temp5[5]+ins[counter]
                counter=counter+1
            elif i[1]==7:
                temp5[6]=temp5[6]+ins[counter]
                counter=counter+1
            elif i[1]==8:
                temp5[7]=temp5[7]+ins[counter]
                counter=counter+1
            elif i[1]==9:
                temp5[8]=temp5[8]+ins[counter]
                counter=counter+1
            elif i[1]==10:
                temp5[9]=temp5[9]+ins[counter]
                counter=counter+1
            elif i[1]==11:
                temp5[10]=temp5[10]+ins[counter]
                counter=counter+1
            elif i[1]==12:
                temp5[11]=temp5[11]+ins[counter]
                counter=counter+1
        
        elif i[2]==2015:
            if i[1]==1:
                temp6[0]=temp6[0]+ins[counter]
                counter=counter+1
            elif i[1]==2:
                temp6[1]=temp6[1]+ins[counter]
                counter=counter+1
            elif i[1]==3:
                temp6[2]=temp6[2]+ins[counter]
                counter=counter+1
            elif i[1]==4:
                temp6[3]=temp6[3]+ins[counter]
                counter=counter+1
            elif i[1]==5:
                temp6[4]=temp6[4]+ins[counter]
                counter=counter+1
            elif i[1]==6:
                temp6[5]=temp6[5]+ins[counter]
                counter=counter+1
            elif i[1]==7:
                temp6[6]=temp6[6]+ins[counter]
                counter=counter+1
            elif i[1]==8:
                temp6[7]=temp6[7]+ins[counter]
                counter=counter+1
            elif i[1]==9:
                temp6[8]=temp6[8]+ins[counter]
                counter=counter+1
            elif i[1]==10:
                temp6[9]=temp6[9]+ins[counter]
                counter=counter+1
            elif i[1]==11:
                temp6[10]=temp6[10]+ins[counter]
                counter=counter+1
            elif i[1]==12:
                temp6[11]=temp6[11]+ins[counter]
                counter=counter+1
        
    
        elif i[2]==2016:
            if i[1]==1:
                temp7[0]=temp7[0]+ins[counter]
                counter=counter+1
            elif i[1]==2:
                temp7[1]=temp7[1]+ins[counter]
                counter=counter+1
            elif i[1]==3:
                temp7[2]=temp7[2]+ins[counter]
                counter=counter+1
            elif i[1]==4:
                temp7[3]=temp7[3]+ins[counter]
                counter=counter+1
            elif i[1]==5:
                temp7[4]=temp7[4]+ins[counter]
                counter=counter+1
            elif i[1]==6:
                temp7[5]=temp7[5]+ins[counter]
                counter=counter+1
            elif i[1]==7:
                temp7[6]=temp7[6]+ins[counter]
                counter=counter+1
            elif i[1]==8:
                temp7[7]=temp7[7]+ins[counter]
                counter=counter+1
            elif i[1]==9:
                temp7[8]=temp7[8]+ins[counter]
                counter=counter+1
            elif i[1]==10:
                temp7[9]=temp7[9]+ins[counter]
                counter=counter+1
            elif i[1]==11:
                temp7[10]=temp7[10]+ins[counter]
                counter=counter+1
            elif i[1]==12:
                temp7[11]=temp7[11]+ins[counter]
                counter=counter+1
        
        
        elif i[2]==2017:
            if i[1]==1:
                temp8[0]=temp8[0]+ins[counter]
                counter=counter+1
            elif i[1]==2:
                temp8[1]=temp8[1]+ins[counter]
                counter=counter+1
            elif i[1]==3:
                temp8[2]=temp8[2]+ins[counter]
                counter=counter+1
            elif i[1]==4:
                temp8[3]=temp8[3]+ins[counter]
                counter=counter+1
            elif i[1]==5:
                temp8[4]=temp8[4]+ins[counter]
                counter=counter+1
            elif i[1]==6:
                temp8[5]=temp8[5]+ins[counter]
                counter=counter+1
            elif i[1]==7:
                temp8[6]=temp8[6]+ins[counter]
                counter=counter+1
            elif i[1]==8:
                temp8[7]=temp8[7]+ins[counter]
                counter=counter+1
            elif i[1]==9:
                temp8[8]=temp8[8]+ins[counter]
                counter=counter+1
            elif i[1]==10:
                temp8[9]=temp8[9]+ins[counter]
                counter=counter+1
            elif i[1]==11:
                temp8[10]=temp8[10]+ins[counter]
                counter=counter+1
            elif i[1]==12:
                temp8[11]=temp8[11]+ins[counter]
                counter=counter+1
        
        
        elif i[2]==2018:
            if i[1]==1:
                temp9[0]=temp9[0]+ins[counter]
                counter=counter+1
            elif i[1]==2:
                temp9[1]=temp9[1]+ins[counter]
                counter=counter+1
            elif i[1]==3:
                temp9[2]=temp9[2]+ins[counter]
                counter=counter+1
            elif i[1]==4:
                temp9[3]=temp9[3]+ins[counter]
                counter=counter+1
            elif i[1]==5:
                temp9[4]=temp9[4]+ins[counter]
                counter=counter+1
            elif i[1]==6:
                temp9[5]=temp9[5]+ins[counter]
                counter=counter+1
            elif i[1]==7:
                temp9[6]=temp9[6]+ins[counter]
                counter=counter+1
            elif i[1]==8:
                temp9[7]=temp9[7]+ins[counter]
                counter=counter+1
            elif i[1]==9:
                temp9[8]=temp9[8]+ins[counter]
                counter=counter+1
            elif i[1]==10:
                temp9[9]=temp9[9]+ins[counter]
                counter=counter+1
            elif i[1]==11:
                temp9[10]=temp9[10]+ins[counter]
                counter=counter+1
            elif i[1]==12:
                temp9[11]=temp9[11]+ins[counter]
                counter=counter+1
    return temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9

def plotMyGraph(big_frame,dict,limit1,limit2):
    

    Quatmonth_list = [[],[],[]]
    Month1,Month2,Month3 = [],[],[]
    
    for year in range(limit1,limit2+1):
        #print(year)
        Quatmonth_list[0].append(dict[year][0][1])
        Quatmonth_list[1].append(dict[year][1][1])
        Quatmonth_list[2].append(dict[year][2][1])
        Month1.append(dict[year][0][0])
        Month2.append(dict[year][1][0])
        Month3.append(dict[year][2][0])
    
    Years = []
    for i in range(limit1,limit2+1):
        Years.append(str(i))
    #Years=["2010","2011","2012","2013","2014","2015","2016","2017","2018"]
    
    pos = np.arange(len(Years))
    bar_width = 0.3
    
    #color = cm.rainbow(np.linspace(0, 1, 3))
    
    figure2 = plt.Figure(figsize=(10,4), dpi=100)
    
    
    chart = figure2.add_subplot(111)
    
    bar1 = chart.bar(Years,Quatmonth_list[0],bar_width,color='blue',edgecolor='black')
    bar2 = chart.bar(pos+bar_width,Quatmonth_list[1],bar_width,color='pink',edgecolor='black')
    bar3 = chart.bar(pos+bar_width*2,Quatmonth_list[2],bar_width,color='red',edgecolor='black')
    
    chart.set_ylabel("Installs")
    chart.set_xlabel('Years')
    figure2.suptitle('Group Barchart - Quater Month across the year',fontsize=18)
    #plt.legend(Month,loc=10)
    
    for idx,rect in enumerate(bar1):
                height = rect.get_height()
                chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,Month1[idx],ha='center', va='bottom', rotation=0) 
          
    for idx,rect in enumerate(bar2):
                height = rect.get_height()
                chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,Month2[idx],ha='center', va='bottom', rotation=0) 
                
    for idx,rect in enumerate(bar3):
                height = rect.get_height()
                chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,Month3[idx],ha='center', va='bottom', rotation=0) 
                

    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=0,y=100)

    #Which quarter of which year has generated the highest number of install for each app used in the study?
    String="In the above Graph Quarter of each Year with their Higher Installs are plotted"
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=520)


def function_q11(event):
    global screen
    global sample,Installs
  
    Installs = []
    root = Toplevel(screen)
    
    
    big_frame = tk.Frame(root,bg='white',width='1050',height=580,bd=4,relief=RIDGE)
    big_frame.place(x=5,y=60)
    
    tk.Label(big_frame,text="For Better Visulization please select the range",font=("Calibri",15,'bold'),fg='#75acff',bg='white').place(x=350,y=0)
    
    tk.Label(big_frame,text="Starting Year:",font=("Calibri",13,'italic'),fg='#75acff',bg='white').place(x=150+100,y=45)
    limit1 = tk.ttk.Combobox(big_frame,values=["2010","2011","2012","2013","2014","2015","2016","2017","2018"])
    limit1.place(x=240+100+25,y=49)
    
    tk.Label(big_frame,text="Ending Year:",font=("Calibri",13,'italic'),fg='#75acff',bg='white').place(x=400+100+50,y=45)
    limit2 = tk.ttk.Combobox(big_frame,values=["2010","2011","2012","2013","2014","2015","2016","2017","2018"])
    limit2.place(x=490+100+50+25,y=49)
    
    
    w=1070
    h=670
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')
    
    tk.Label(root,text="",bg='white').pack()
    tk.Label(root,text="Last Update",
             width=500,height=2,font=("Helvetica",11,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
    
    sample=pd.read_csv('DATA SET-2.csv')#reading data for the data set
    sample=sample.replace(np.NaN,0)
    sample.drop(index=[10472],inplace=True)
    
    for i in sample['Installs']:  #converting string based installs into integer based
        if i=='Free':
            Installs.append(0)
        else:
            Installs.append(int(i.replace('+','').replace(',','')))
    

    years = quat()

    dict = []
    
    for i in range(2019):
        dict.append(i)
        
    i=2010
    for year in years:
        indi = [0,0,0]
        quat1 = year[0:3]
        quat2 = year[3:6]
        quat3 = year[6:9]
        quat4 = year[9:12]
        
        #print(quat1)
        #print(quat2)
        #print(quat3)
        #print(quat4)
        
        if sum(indi)<sum(quat1):
            dict[i]=[]
            indi = quat1
            dict[i] = [["Jan",quat1[0]],["Feb",quat1[1]],["March",quat1[2]]]
        if sum(indi)<sum(quat2):
            print('')
            dict[i]=[]
            indi = quat2
            dict[i] = [["April",quat2[0]],["May",quat2[1]],["June",quat2[2]]]
        if sum(indi)<sum(quat3):
            dict[i]=[]
            indi = quat3
            dict[i] = [["July",quat3[0]],["Aug",quat3[1]],["Sept",quat3[2]]]
        if sum(indi)<sum(quat4):
            dict[i]=[]
            indi = quat4
            dict[i] = [["Oct",quat4[0]],["Nov",quat4[1]],["Dec",quat4[2]]]
         
        i+=1
        
    plotMyGraph(big_frame,dict,2010,2018)
    tk.Button(big_frame,text="SET GRAPH",bd=10,font=("Calibri",13,'italic'),fg='#75acff',bg='white',
              command = lambda:plotMyGraph(big_frame,dict,int(limit1.get()),int(limit2.get())) if (limit1.get()!=limit2.get() and limit1.get()!="" and limit2.get()!="" and int(limit1.get())<int(limit2.get()) )   else tk.messagebox.showerror("ERROR","PLEASE SELECT THE VALID RANGE")).place(x=490+100+50+25+165,y=40)
    

"""Ques11 END======================================================================================"""


def reviewClick(event):
    global screen
    import InsightsDesignToStudyReview as rev
    rev.startingScreen(screen)
    
def overviewClick(event):
    global screen
    import InsightsDesign as over
    over.startingScreen(screen)

def categoryClick(event):
    global screen
    import InsightsDesignForCategory as cat
    cat.startingScreen(screen)

def installClick(event):
    global screen
    import InsightsDesignForInstall as inst
    inst.startingScreen(screen)
    

def lastupdateClick(event):
    global screen
    import InsightsDesignForLastUpdate as up
    up.startingScreen(screen)

def searchAppClick(event):
    global screen
    import InsightsDesignForSearchApp as app
    app.startingScreen(screen)


def sizeClick(event):
    print('')

def adjustWindow(window):
    global screen
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    window.geometry("%dx%s"%(ws,hs))
    
    window.configure(background='white')

    
def machineClick(event):
    global screen 
    import InsightsDesignForMachineLearningModels as mac
    mac.startingScreen(screen)

def startingScreen(root):
    global screen,df
    
    df=pd.read_csv("DATA SET-2.csv")
    
    root.destroy()
    
    screen = tk.Tk()
    adjustWindow(screen)
    screen.title("Insights of Google App's")
    
    tk.Label(screen,text="",bg="white").pack()
    tk.Label(screen,text="LAST UPDATE",width=1000,height=1,font=("Helvetica",15,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
    lbl_over = tk.Label(screen,text = "Overview",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_over.bind("<Button-1>",overviewClick)
    lbl_over.place(x=5,y=65)
    
    lbl_category = tk.Label(screen,text = "Category",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_category.bind("<Button-1>", categoryClick)
    lbl_category.place(x=130,y=65)
    
    lbl_Installs = tk.Label(screen,text = "Installs",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_Installs.bind("<Button-1>", installClick)
    lbl_Installs.place(x=255,y=65)
    
    lbl_searchapp = tk.Label(screen,text = "Search App",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_searchapp.bind("<Button-1>", searchAppClick)
    lbl_searchapp.place(x=255+125,y=65)
        
    lbl_machine = tk.Label(screen,text = "Learning Models",width=25,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_machine.bind("<Button-1>", machineClick)
    lbl_machine.place(x=255+125+125,y=65)
    
    lbl_review = tk.Label(screen,text = "Reviews",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_review.bind("<Button-1>", reviewClick)
    lbl_review.place(x=255+125+125+125+108,y=65)
                          
    lbl_lastupdate = tk.Label(screen,text = "Last Updated",width=13,height='2',font=("Calibri",13,'bold'),fg='#75acff',bg='white')
    lbl_lastupdate.bind("<Button-1>", lastupdateClick)
    lbl_lastupdate.place(x=255+125+125+125+125+109,y=65)
                          
    
    big_frame = tk.Frame(screen,bg='#F8E0E0',width='1520',height='730',bd=4,relief=RIDGE)
    big_frame.place(x=3,y=100)
    
    """
    #11) Which quarter of which year has generated the highest number of install for each app used in the study?
    
    #16) Which month(s) of the year , is the best indicator to the average downloads that an app will generate over the entire year?
    
    6) For the years 2016,2017,2018 what are the category of apps that have got the most and the least downloads. What is the percentage increase or decrease that the

    10) Across all the years ,which month has seen the maximum downloads fr each of the category. What is the ratio of downloads for the app that qualifies as teen versus mature17+

    """
    #frame1 = tk.Frame(big_frame,bg='white',width='800',height='400',bd=4,relief=RIDGE)
    #frame1.place(x=3,y=3)
    
    #tk.Label(frame1,text=,font=("Calibri",11,'bold'),fg='#910030',bg='white')
    
    f1 = tk.Label(big_frame,text = "Max Installs Of Month Per Year ",width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    f1.bind("<Button-1>", function_f1)
    f1.place(x=50,y=10)
    
    
    q11 = tk.Label(big_frame,text = '''Which quarter of which year has generated the highest number of install for each
app used in the study?''',width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    q11.bind("<Button-1>", function_q11)
    q11.place(x=750,y=10)
    #function_q11(frame1)
    
    q6 = tk.Label(big_frame,text = '''For the years 2016,2017,2018 what are the category of apps that have got the most
and the least downloads.''',width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    q6.bind("<Button-1>", function_q6)
    q6.place(x=50,y=250)       
    
    q6_part2 = tk.Label(big_frame,text = ''' What is the percentage increase or decrease that the
apps have got over the period of three years.''',width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    q6_part2.bind("<Button-1>", function_q6_part2)
    q6_part2.place(x=50,y=490)       
    
    q10 = tk.Label(big_frame,text = '''Across all the years ,which month has seen the maximum downloads fr each of the
category. What is the ratio of downloads for the app that qualifies as teen versus
mature17+''',width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    q10.bind("<Button-1>", function_q10)
    q10.place(x=750,y=250)
    

    ques = """Which month of the year , is the best indicator to the average 
downloads that an app will generate over the entire year?"""

    q16 = tk.Label(big_frame,text = ques,width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    q16.bind("<Button-1>", function_q16)
    q16.place(x=750,y=490)
    screen.mainloop()
    
startingScreen(tk.Tk())

