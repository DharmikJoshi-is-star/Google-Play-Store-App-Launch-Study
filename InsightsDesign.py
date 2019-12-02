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
import DesignToInsertdataset1 as ds
#import Tkinter as tk
#import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.cm as cm

def overviewClick(event):
    print('')

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

def lastupdateClick(event):
    global screen
    import InsightsDesignForLastUpdate as up
    up.startingScreen(screen)
         
def reviewClick(event):
    global screen
    import InsightsDesignToStudyReview as rev
    rev.startingScreen(screen)

def sizeClick(event):
    print("")
    
def machineClick(event):
    global screen 
    import InsightsDesignForMachineLearningModels as mac
    mac.startingScreen(screen)

def tableFormate(data,table_frame):
    global screen,df
    global string_table
    x=60
    y=30
    string="App Name\t\tCategory\tRating    \tReviews\t\tSize\tInstalls\t\tType\tPrice\tContent Rating\t Geners\t\tLast Update\tCurr ver    Android Ver\n"
    tk.Label(table_frame,text=string,font=("Helvetica",11,'bold'),fg='black',bg='#d8dce3').place (x=x-3,y=y)
    
    for index in range(len(data)):
        if index%2==0:
            color='#ffffff'
        else:
            color='#f5f5f5'
        y+=30
        string ="{}...\t\t{}\t  {}    \t{}\t\t{}\t{}   \t{}\t{}\t{}              \t{}\t{}\t{}\t  {}     \n".format(data['App'][index][0:13],str(data['Category'][index])[0:10],str(data['Rating'][index]) ,str(data['Reviews'][index]),str(data['Size'][index]),str(data['Installs'][index])[0:9],str(data['Type'][index]),str(data['Price'][index]),str(data['Content Rating'][index]),str(data['Genres'][index])[0:12],str(data['Last Updated'][index])[0:10],str(data['Current Ver'][index])[0:6],str(data['Android Ver'][index])[0:9])
        tk.Label(table_frame,text=string,font=("Helvetica",11,'bold'),fg='black',bg=color, borderwidth=2, relief="groove").place(x=x,y=y)
    
    summary = "Summary\t\t Rows : %d  Columns : %d "%(df.shape[0],df.shape[1])
    
    tk.Label(table_frame,text=summary,font=("Helvetica",11,'bold'),fg='black',bg="white" ).place(x=x,y=y+45)
    
    #insert_button = tk.Button(table_frame,fg="white",font=('Helvetica',10,'bold'),width=13,text="+ADD",bg="#7aaffa",command=mouseClick).place(x=1315,y=y+42)
    
def adjustWindow(window):
    global screen
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    window.geometry("%dx%s"%(ws,hs))

    window.configure(background='white')

def startingScreen(root):# main window nothing to be changed over here
    global screen,df
    
    df=pd.read_csv('DATA SET-2.csv')
    
    root.destroy()
    
    screen = tk.Tk()
    adjustWindow(screen)
    screen.title("Insights of Google App's")
    
    tk.Label(screen,text="",bg="white").pack()
    tk.Label(screen,text="OVERVIEW",width=1000,height=1,font=("Helvetica",15,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
    lbl_overview = tk.Label(screen,text = "Overview",width=13,height='2',font=("Calibri",13,'bold'),fg='#75acff',bg='white')
    lbl_overview.bind("<Button-1>",overviewClick)
    lbl_overview.place(x=5,y=65)
    
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
                          
    lbl_lastupdate = tk.Label(screen,text = "Last Updated",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_lastupdate.bind("<Button-1>", lastupdateClick)
    lbl_lastupdate.place(x=255+125+125+125+125+109,y=65)
                          
    
    big_frame = tk.Frame(screen,bg='white',width='1520',height='730',bd=4,relief=RIDGE)
    big_frame.place(x=3,y=100)
    
    """this frame is to display the data table"""
    
    table_frame = tk.Frame(big_frame,bg='white',width='1505',height='410',bd=4,relief=RIDGE)
    table_frame.place(x=10,y=310)

    tk.Label(table_frame,text="App's Data Table",width=15,height='1',font=("Calibri",11,'bold'),fg='black',bg='white').place(x=0,y=0)
    
    tableFormate(df[0:10],table_frame)
    
    insert_button = tk.Button(table_frame,bd=2,fg="white",font=('Helvetica',9,'bold'),width=16,text="+ADD",bg="#3869d1",command=lambda :ds.startingScreen(screen)).place(x=1300,y=373)
    
    
    canvas_frame1 = tk.Frame(big_frame,bg='gray',width=512,height=308,bd=4,relief=RIDGE)
    canvas_frame1.place(x=10,y=0)
    #canvas1 = tk.Canvas(canvas_frame1,bg="pink",height=307,width=498)
    #canvas1.place(x=11,y=106)
    
    df=df.replace(np.NaN,-999)

    #print(df.isnull().sum())
    
    #print(df.head(5))
    
    dict_cat_count = {}
    for index in range(len(df)):
        
        if df['Category'][index]==-999:
            continue
        
        if df['Category'][index] in dict_cat_count:
            dict_cat_count[df['Category'][index]]+=1
        else:
            dict_cat_count[df['Category'][index]]=1
            
    #print(len(dict_cat_count))
    
    y_count=[]
    x_label=[]
    for i in dict_cat_count:
        x_label.append(i)
        y_count.append(dict_cat_count[i])
        
    for i in range(len(y_count)-1):
        for j in range(len(y_count)-1):
            if y_count[j]<y_count[j+1]:
                y_count[j],y_count[j+1] = y_count[j+1],y_count[j]
                x_label[j],x_label[j+1] = x_label[j+1],x_label[j]
    #colors
    #colors = ['#ff9999','#66b3ff','#99ff99']#,'#ffcc99']
    figure1 = plt.Figure(figsize=(5,3), dpi=100)
    
    color = cm.rainbow(np.linspace(0, 1, 10))
    #fig1, ax1 = plt.subplots()
    ax3 = figure1.add_subplot(111)
    ax3.pie(y_count[:10], labels=x_label[:10],colors = color, autopct='%1.1f%%', startangle=90)
    ax3.set_title("Pie chart on Category (Top 10)")
    pie_plot = FigureCanvasTkAgg(figure1, canvas_frame1) 
    pie_plot.get_tk_widget().place(x=0,y=0)
    #ax3.legend() 
    
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    
    dict_Install_count = {}
    for index in range(len(df)):
        
        if df['Installs'][index]==-999:
            continue
        
        if df['Installs'][index] in dict_Install_count:
            dict_Install_count[df['Installs'][index]]+=1
        else:
            dict_Install_count[df['Installs'][index]]=1
            
    #print(len(dict_Install_count))
    
    y_count=[]
    x_label=[]
    for i in dict_Install_count:
        x_label.append(i)
        y_count.append(dict_Install_count[i])
        
    for i in range(len(y_count)-1):
        for j in range(len(y_count)-1):
            if y_count[j]<y_count[j+1]:
                y_count[j],y_count[j+1] = y_count[j+1],y_count[j]
                x_label[j],x_label[j+1] = x_label[j+1],x_label[j]
    
    canvas_frame2 = tk.Frame(big_frame,bg='gray',width=710,height=308,bd=4,relief=RIDGE)
    canvas_frame2.place(x=520,y=0)
    #canvas = tk.Canvas(canvas_frame2,bg="black",height="300",width="308")
    #canvas.place(x=1213,y=105)

    
    color = cm.rainbow(np.linspace(0, 1, 10))
    
    #print(y_count[:10])
    #print(x_label[:10])
    

    for i in range(len(x_label)):
        n = x_label[i].count("0")
        if n==3:
            x_label[i]=x_label[i][:1]+"k"
        if n==4:
            x_label[i]=x_label[i][:2]+"k"
        if n==5:
            x_label[i]=x_label[i][:3]+"k"
        if n==6:
            x_label[i]=x_label[i][:1]+"M"
        if n==7:
            x_label[i]=x_label[i][:2]+"M"
            

    figure2 = plt.Figure(figsize=(7,3), dpi=100)
    
    chart = figure2.add_subplot(111)
    #x=['Dis-Liked Apps' , 'Liked Apps']
    #y=[like_dislike_list.count(0),like_dislike_list.count(1)]
    chart.bar(x_label[:10],y_count[:10],color=color)
    chart.set_ylabel("Frequency")
    chart.set_xlabel("Installs")
    figure2.suptitle("Bar chart on Installs (Top 10)")
    chart.legend()

    canvas = FigureCanvasTkAgg(figure2, master=canvas_frame2)
    canvas.get_tk_widget().place(x=3,y=0)

    canvas_frame3 = tk.Frame(big_frame,bg='gray',width=400,height=308,bd=4,relief=RIDGE)
    canvas_frame3.place(x=1200,y=0)
        
    df = pd.read_csv("DATA SET-2.csv")
    
    #print(df.head(5))
    #print(df['Type'].head(5))
    
    df=df.replace(np.NaN,-999)
    
    df['Type'] = df['Type'].map(lambda x : 1 if x=="Free" else 0)
    
    count_free=0
    count_paid=0
    for i in df['Type']:
        if i == 1:
            count_free+=1
        else:
            count_paid+=1

    
    figure3 = plt.Figure(figsize=(4,4), dpi=80)
    
    chart = figure3.add_subplot(111)
    #x=['Dis-Liked Apps' , 'Liked Apps']
    #y=[like_dislike_list.count(0),like_dislike_list.count(1)]
    chart.bar(['FREE','PAID'],[count_free,count_paid],color=['red','blue'])
    chart.set_ylabel("Frequency")
    chart.set_xlabel("Type")
    figure3.suptitle("Count plot for Free Vs Paid")
    chart.legend()

    canvas = FigureCanvasTkAgg(figure3, master=canvas_frame3)
    canvas.get_tk_widget().place(x=3,y=0)
        
    plt.show()

    screen.mainloop()
    
#startingScreen(tk.Tk())

