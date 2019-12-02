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
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import sys
from collections import OrderedDict 
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

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
    global sample
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

def display(x,y,z):
    for i in x:
        for j in set(i):
            y.insert('end',j)
       
def filtering(value,canvas_listbox):
    global sample
    installs=install()
    year=dates_str_to_int()
    rating=sample['Rating']
    genre=sample['Genres'].unique()
    ans=[]
    for i in genre:
        ans.append([])

    for i in range(len(installs)):
        if i!=10472 and installs[i]==value[0]:
            if rating[i]>=value[1]:
                if year[i][2]==value[2]:
                    for j in range(len(genre)):
                        if genre[j]==sample['Genres'][i]:
                            ans[j].append(sample['App'][i])
    canvas_listbox.delete(0,'end')
    display(ans,canvas_listbox,genre)


def getting(install,rating,year,canvas_listbox):
    if install.get().strip()!='' and rating.get().strip()!='' and year.get().strip()!='':
        value=[int(install.get().replace(',','').replace('+','')),float(rating.get()),int(year.get())]
        filtering(value,canvas_listbox)
    else:
        tk.messagebox.showerror('Error','Please select values')
    
    
    
    

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
    
def searchAppClick(event):
    global screen
    import InsightsDesignForSearchApp as app
    app.startingScreen(screen)

def sizeClick(event):
    print('')
    
def lastupdateClick(event):
    global screen
    import InsightsDesignForLastUpdate as up
    up.startingScreen(screen)


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
    global screen,sample
    
    root.destroy()
    
    screen = tk.Tk()
    adjustWindow(screen)
    screen.title("Insights of Google App's")
    
    tk.Label(screen,text="",bg="white").pack()
    tk.Label(screen,text="RATING",width=1000,height=1,font=("Helvetica",15,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
    
    lbl_over = tk.Label(screen,text = "Overview",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_over.bind("<Button-1>",overviewClick)
    lbl_over.place(x=5,y=65)
    
    lbl_category = tk.Label(screen,text = "Category",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_category.bind("<Button-1>", categoryClick)
    lbl_category.place(x=130,y=65)
    
    lbl_Installs = tk.Label(screen,text = "Installs",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_Installs.bind("<Button-1>", installClick)
    lbl_Installs.place(x=255,y=65)
    
    lbl_searchapp = tk.Label(screen,text = "Search App",width=13,height='2',font=("Calibri",13,'bold'),fg='#75acff',bg='white')
    lbl_searchapp.bind("<Button-1>", searchAppClick)
    lbl_searchapp.place(x=255+125,y=65)
                          
    lbl_machine = tk.Label(screen,text = "Learning Models",width=25,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_machine.bind("<Button-1>", machineClick)
    lbl_machine.place(x=255+125+125,y=65)
    
    lbl_review = tk.Label(screen,text = "Reviews",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_review.bind("<Button-1>", reviewClick)
    lbl_review.place(x=255+125+125+125+108,y=65)
                          
    lbl_lastupdate = tk.Label(screen,text = "Last Updated",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_lastupdate.bind("<Button-1>", lastupdateClick)
    lbl_lastupdate.place(x=255+125+125+125+125+109,y=65)
                                      
    
    big_frame = tk.Frame(screen,bg='#F8E0E0',width='1520',height='730',bd=4,relief=RIDGE)
    big_frame.place(x=3,y=100)
    sample=pd.read_csv('DATA SET-2.csv')
    sample.drop(index=[10472],inplace=True)
    sample=sample.replace(np.NaN,0)

    
    year=[2010,2011,2012,2013,2014,2015,2016,2017,2018]
    rating=[]
    for i in range(5):
        for j in range(10):
            rating.append(i+(j/10))
    rating.append(5.0)

    tk.Label(big_frame,text='Installs',width=10,height=1,font=("Helvetica",15,'bold'),fg='white',bg='#2864ad', borderwidth=2, relief="groove").place(x=150,y=60)
    tk.Label(big_frame,text='Rating',width=10,height=1,font=("Helvetica",15,'bold'),fg='white',bg='#2864ad', borderwidth=2, relief="groove").place(x=450,y=60)
    tk.Label(big_frame,text='Year',width=10,height=1,font=("Helvetica",15,'bold'),fg='white',bg='#2864ad', borderwidth=2, relief="groove").place(x=750,y=60)
    combo_install=ttk.Combobox(big_frame,width=17,values=['0','10+','100+','1,000+','10,000+','1,00,000+','10,00,000+','1,00,00,000+'],state="readonly")
    combo_install.place(x=150,y=110)
    combo_rating=ttk.Combobox(big_frame,width=17,values=rating,state="readonly")
    combo_rating.place(x=450,y=110)
    combo_year=ttk.Combobox(big_frame,width=17,values=year,state="readonly")
    combo_year.place(x=750,y=110)
    
    canvas=tk.Canvas(big_frame,width=970,height=450,bg='pink')
    canvas.place(x=150,y=150)
    scroll1=tk.Scrollbar(canvas)
    canvas_listbox=tk.Listbox(canvas,yscrollcommand = scroll1.set,height=20,width=96,bg='#A9D0F5',font=('Calibri',14,'bold'))
    canvas_listbox.pack( side = 'left', fill = 'both' )
    scroll1.pack(side='right', fill='y' )
    scroll1.config( command = canvas_listbox.yview )
    
    
    btn_search=tk.Button(big_frame,text='Search',bd=12,width=10,bg="powder blue",command=lambda:getting(combo_install,combo_rating,combo_year,canvas_listbox))
    btn_search.place(x=1020,y=85)

    
    screen.mainloop()
    
#startingScreen(tk.Tk())

