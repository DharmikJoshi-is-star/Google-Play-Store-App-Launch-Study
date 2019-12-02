# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:57:13 2019

@author: Dharmik joshi
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import Listbox
from collections import OrderedDict
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.cm as cm
def list_return(x,y,positive,negative,neutral,scroll1,scroll2,scroll3):
    global data
    positive.delete(0,'end')
    negative.delete(0,'end')
    neutral.delete(0,'end')

    for i in range(len(data['Sentiment'])):
        if data['App'][i][0:10]==y.get():
                    if data['Sentiment'][i]=='Positive':
                         positive.insert('end',data['Translated_Review'][i])
                    elif data['Sentiment'][i]=='Negative':
                         negative.insert('end',data['Translated_Review'][i])
                    elif data['Sentiment'][i]=='Neutral':
                         neutral.insert('end',data['Translated_Review'][i]) 

    scroll1.pack(side='right', fill='y' )
    scroll2.pack(side='right', fill='y' )
    scroll3.pack( side='right', fill='y' )
    """
    positive.pack( side = 'left', fill = 'both' )
    negative.pack( side = 'left', fill = 'both' )
    neutral.pack( side = 'left', fill = 'both' )
    """
    scroll1.config( command = positive.yview )
    scroll2.config( command = negative.yview )
    scroll3.config( command = neutral.yview )

def Sentiment_list(positive,negative,neutral,list_positive_app,list_negative_app,list_average_app,scroll1,scroll2,scroll3):
    positive.delete(0,'end')
    negative.delete(0,'end')
    neutral.delete(0,'end')

    
    for i in range(40):
        negative.insert('end',list_negative_app[i])
        negative.insert('end',"")
    for i in range(50):
        neutral.insert('end',list_average_app[i])
    for i in range((50)):
        positive.insert('end',list_positive_app[i][0:15])
        
    scroll1.pack(side='right', fill='y' )
    scroll2.pack(side='right', fill='y' )
    scroll3.pack( side='right', fill='y' )
    
    scroll1.config( command = positive.yview )
    scroll2.config( command = negative.yview )
    scroll3.config( command = neutral.yview )

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

def adjustWindow(window):
    global screen
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    window.geometry("%dx%s"%(1200,800))
    window.resizable(False,False)
    window.configure(background='white')

def lastupdateClick(event):
    global screen
    import InsightsDesignForLastUpdate as up
    up.startingScreen(screen)

def reviewClick(event):
    global screen
    import InsightsDesignToStudyReview as rev
    rev.startingScreen(screen)
    
def machineClick(event):
    global screen 
    import InsightsDesignForMachineLearningModels as mac
    mac.startingScreen(screen)

def startingScreen(root):
    global screen,data
    
    root.destroy()
    
    data=pd.read_csv('DATA SET-1.csv')
    data=data.replace(np.nan,'Not Available')

    screen = tk.Tk()
    adjustWindow(screen)
    screen.title("Insights of Google App's")
    
    tk.Label(screen,text="",bg="white").pack()
    tk.Label(screen,text="REVIEW",width=1000,height=1,font=("Helvetica",15,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
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
    
    lbl_review = tk.Label(screen,text = "Reviews",width=13,height='2',font=("Calibri",13,'bold'),fg='#75acff',bg='white')
    lbl_review.bind("<Button-1>", reviewClick)
    lbl_review.place(x=255+125+125+125+108,y=65)
                          
    lbl_lastupdate = tk.Label(screen,text = "Last Updated",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_lastupdate.bind("<Button-1>", lastupdateClick)
    lbl_lastupdate.place(x=255+125+125+125+125+109,y=65)
                          
    
       
                          
    big_frame = tk.Frame(screen,bg='#003b6b',width='1400',height='730',bd=4,relief=RIDGE)
    big_frame.place(x=3,y=100)
    
    Apps=list(OrderedDict.fromkeys(data['App']))
    canvas=[]
    filtered=[]
    for i in Apps:
        filtered.append(i[0:10])
    
    for i in range(4):
            can=tk.Canvas(big_frame,width=320,height=720,bg='#003b6b')
            canvas.append(can)
            can.grid(row=0,column=i)
        
    
    combo=ttk.Combobox(big_frame,values=filtered,state="readonly")
    combo.place(x=650,y=20)
    """
    for i in range(0,4):
        can=tk.Canvas(canvas[i],width=280,height=600,bg='#EFEFFB')
        canvas.append(can)
        can.place(x=0,y=110)
    """
    
    #labels for interface
    l=tk.Label(big_frame,text='Select App',bg='#003b6b')
    l.config(font=("Calibri", 16,"bold"),fg="orange")
    l.place(x=540,y=14)
    l=tk.Label(big_frame,text='Positive',bg='#003b6b')
    l.config(font=("Calibri", 16,'bold'),fg='yellow')
    l.place(x=430,y=45)
    l=tk.Label(big_frame,text='Neutral',bg='#003b6b')
    l.config(font=("Calibri", 16,'bold'),fg='yellow')
    l.place(x=700,y=45)
    l=tk.Label(big_frame,text='Negative',bg='#003b6b')
    l.config(font=("Calibri", 16,'bold'),fg='yellow')
    l.place(x=950,y=45)
    
    scroll1=tk.Scrollbar(canvas[1])

    scroll2=tk.Scrollbar(canvas[2])

    scroll3=tk.Scrollbar(canvas[3])

    positive=tk.Listbox(canvas[1],yscrollcommand = scroll1.set,height=35,width=45,bg='#F5A9BC')
    negative=tk.Listbox(canvas[2],yscrollcommand = scroll2.set,height=35,width=43,bg='#F7F8E0')
    neutral=tk.Listbox(canvas[3],yscrollcommand = scroll3.set,height=35,width=45,bg='#F8E0F1')
    
    positive.pack(side = 'left', fill = 'both')
    negative.pack( side = 'left', fill = 'both' )
    neutral.pack( side = 'left', fill = 'both' )
    
    pos_box = positive
    neg_box = negative
    neu_box = neutral
    
    scroll1.pack(side='right', fill='y' )
    scroll2.pack(side='right', fill='y' )
    scroll3.pack( side='right', fill='y' )
                       
    tk.Button(big_frame,text='Review',bd=5,width=12,bg='#c90000',font=("Calibri",12,'italic'),
                         command=lambda:list_return(canvas,combo,pos_box,neg_box,neu_box,scroll1,scroll2,scroll3)).place(x=810,y=10)
    
    
    
    
    #Sentiment Analysis
    list_of_apps_most_positive_sentiments = []
    list_of_apps_most_negative_sentiments = []
    list_of_apps_most_average_sentiments = []
    list_of_apps_most_zero_sentiments = []
    
    Sample_Data = pd.read_csv("DATA SET-1.csv")
    
    dict_app = {}
    
    for app in Sample_Data['App']:
        if app in dict_app:
            dict_app[app]+=1
        else:
            dict_app[app]=1
    
    app = []
    for i in dict_app.keys():
        app.append(i)
    
    dict_sentiment = {}
    
    for i in app:
        dict_sentiment[i]=[0,0]
    
    for a in range(len(Sample_Data['App'])):
        app_name = Sample_Data['App'][a]
        app_sentiment = Sample_Data['Sentiment'][a]
        if app_name in dict_sentiment:
            if app_sentiment == "Positive":
                dict_sentiment[app_name][0]+=1
            elif app_sentiment == "Negative":
                dict_sentiment[app_name][1]+=1
        else:
             if app_sentiment == "Positive":
                dict_sentiment[app_name][0]=1
             elif app_sentiment == "Negative":
                dict_sentiment[app_name][1]=1
                
    for app_name in dict_sentiment:
        
        app = app_name 
        positive = dict_sentiment[app_name][0]
        negative = dict_sentiment[app_name][1]
        
        ratio1 = positive / dict_app[app]
        ratio2 = negative / dict_app[app]
        
        if(positive-negative<3 and positive-negative>-3)and(positive!=0):
            #avg_sentiment[app_name]=positive
            list_of_apps_most_average_sentiments.append(app_name)
        
        elif(ratio1>ratio2):
            list_of_apps_most_positive_sentiments.append(app_name)
            #print("pos ",positive)
            #print("neg ",negative)
        elif(ratio1<ratio2):
            list_of_apps_most_negative_sentiments.append(app_name)
        
        else:
            list_of_apps_most_zero_sentiments.append(app_name)
    
    y_count=[len(list_of_apps_most_positive_sentiments),len(list_of_apps_most_negative_sentiments),len(list_of_apps_most_average_sentiments)]#,len(list_of_apps_most_zero_sentiments)]
    
    x_label=['Positive','Negative','Average']#,'NONE']
    
    text = """--SENTIMENT ANALYSIS--"""
    tk.Label(canvas[0],text=text,font=("Calibri",20,"bold"),fg="yellow",bg='#003b6b').place(x=10,y=100)
    text = """COUNT OF SENTIMENTS"""
    tk.Label(canvas[0],text=text,font=("Calibri",20,"bold"),fg="yellow",bg='#003b6b').place(x=10,y=150)
    
             
    tk.Label(canvas[0],text="Positive Sentiment : "+str(len(list_of_apps_most_positive_sentiments)),font=("Calibri",15,"bold"),fg="yellow",bg='#003b6b').place(x=10,y=100+100)
    
    tk.Label(canvas[0],text="Negative Sentiment : "+str(len(list_of_apps_most_negative_sentiments)),font=("Calibri",15,"bold"),fg="yellow",bg='#003b6b').place(x=10,y=100+150)
    
    tk.Label(canvas[0],text="Neutral Sentiment : "+str(len(list_of_apps_most_average_sentiments)),font=("Calibri",15,"bold"),fg="yellow",bg='#003b6b').place(x=10,y=100+200)
    
    tk.Button(canvas[0],text="CLICK TO GET APPS",bd=10,font=("Calibri",15,"bold"),fg="yellow",bg='#003b6b',command = lambda: Sentiment_list(pos_box,neg_box,neu_box,list_of_apps_most_positive_sentiments,list_of_apps_most_negative_sentiments,list_of_apps_most_average_sentiments,scroll1,scroll2,scroll3)).place(x=10,y=100+200+50)


    
    figure1 = plt.Figure(figsize=(5,4), dpi=50)
    
    color = cm.rainbow(np.linspace(0, 1, 3))
    #fig1, ax1 = plt.subplots()
    ax3 = figure1.add_subplot(111)
    ax3.pie(y_count, labels=x_label,colors = color, autopct='%1.1f%%', startangle=200)
    ax3.set_title("Pie chart on Category")
    
    #ax3.xlim(0,3.0)
    pie_plot = FigureCanvasTkAgg(figure1, canvas[0]) 
    pie_plot.get_tk_widget().place(x=20,y=450)
    
    #ax3.legend(loc=0) 

    screen.mainloop()
    
#startingScreen(tk.Tk())

