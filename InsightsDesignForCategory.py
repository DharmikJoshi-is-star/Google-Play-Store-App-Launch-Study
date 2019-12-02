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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.cm as cm


def function_q5(event):
        
        global screen
        
        root = Toplevel(screen)
        big_frame = tk.Frame(root,bg='white',width='800',height='710',bd=4,relief=RIDGE)
        big_frame.place(x=25,y=60)
        w=850
        h=790
        ws=screen.winfo_screenwidth()
        hs=screen.winfo_screenheight()
        x=(ws/2)-(w/2)
        y=(hs/2)-(h/2)
        root.geometry("%dx%d+%d+%d"%(w,h,x,y))
        
        root.configure(background='white')

    
        df = pd.read_csv("DATA SET-2.csv")
        df=df.replace(np.NaN,-999)
        
        dict_cat_count = {}
        for index in range(len(df)):
            
            if df['Category'][index]==-999:
                continue
            
            if df['Category'][index] in dict_cat_count:
                dict_cat_count[df['Category'][index]]+=1
            else:
                dict_cat_count[df['Category'][index]]=1
                
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
        figure1 = plt.Figure(figsize=(7,6), dpi=100)
        
        color = cm.rainbow(np.linspace(0, 1, 10))
        #fig1, ax1 = plt.subplots()
        ax3 = figure1.add_subplot(111)
        ax3.barh(x_label, y_count,color = color)
        ax3.set_title("CHART ON TREND OF DOWNLOAD OVER THE CATEGORY")
        bar_plot = FigureCanvasTkAgg(figure1, big_frame) 
        bar_plot.get_tk_widget().place(x=0,y=0)
        ax3.set_xlabel("Downloads")
        #ax3.legend() 
    
        root.mainloop()

""" Ques 5 END=============================================================================================="""



""" Ques 3 START=============================================================================================="""
def qn3(category):
    global sample
    Installs = []
    sample.drop(index=10472,axis=0,inplace=True)
    sample=sample.replace(np.NaN,0)

    for i in sample['Installs']:  #converting string based installs into integer based
        if i=='Free':
            Installs.append(0)
        else:
            Installs.append(int(i.replace('+','').replace(',','')))
    ans=[]
    count = []
    
    for i in category:
        total=0
        c=0
        for j in range(len(sample['Category'])):
            if j!=10472:
                if sample['Category'][j]==i:
                    total=total+Installs[j]
                    c+=1
                    
        ans.append(total)
        count.append(c)
        
        
    cat,avg = [],[]    
    for index in range(len(ans)):
        cat.append(category[index])
        avg.append(round(ans[index]/count[index]))
    
    return  cat,avg

def function_q3(event):
    
    global screen,sample
    
    sample = pd.read_csv("DATA SET-2.csv")
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='800',height='710',bd=4,relief=RIDGE)
    big_frame.place(x=25,y=60)
    w=850
    h=790
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')

    category=sample['Category'].unique()
    
    cat,avg = qn3(category)
    #print(len(cat))
    #print(len(avg))
    
    #print(cat[avg.index(max(avg))])
    #print(max(avg))
     
    #print(cat[avg.index(min(avg))])
    #print(min(avg)) 
    
    lowest = []
    for index in range(len(avg)):
        if avg[index]<250000:
            lowest.append(category[index])
        
    label = category
    val = avg
    
    color = cm.rainbow(np.linspace(0, 1, len(label)))
    figure2 = plt.Figure(figsize=(7,6), dpi=100)
    
    chart = figure2.add_subplot(111)
    
    bar_plot = chart.barh(label,val,color=color)
    
    chart.set_ylabel("Category")
    chart.set_xlabel("Average Installs")
    figure2.suptitle("Category with Their Average Download")
    chart.legend()
    
    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=10,y=0)
    
    String="""
            There are 33 Unique Categories are available in the Data set where {} Category has 
            managed to get the Maximum Downloads across all the years and {} Category has got 
            the Lowest Downloads except {} and {} Category All the categories have managed to get 
            the average of 2,50,000 Downloads
    """.format(cat[avg.index(max(avg))],cat[avg.index(min(avg))],lowest[0],lowest[1])
    
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=0,y=565)
    
    root.mainloop()

""" Ques 3 END================================================================================================="""


"""Feature cat_download size START============================================================================="""
def feature_cat_size(event):
    
    global screen,df
    
    df = pd.read_csv("DATA SET-2.csv")
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='750',height='690',bd=4,relief=RIDGE)
    big_frame.place(x=10,y=60)
    w=800
    h=790
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')

    
    df = pd.read_csv("DATA SET-2.csv")
    
    #print(df.head(5))
    
    
    # Data cleaning for "Size" column
    #print(df['Size'].head(5))
    df['Size'] = df['Size'].map(lambda x: x.rstrip('M'))
    df['Size'] = df['Size'].map(lambda x: str(round((float(x.rstrip('k'))/1024), 1)) if x[-1]=='k' else x)
    df['Size'] = df['Size'].map(lambda x: np.nan if x.startswith('Varies') else x)
    #print(df['Size'].head(5))
    
    
    df=df.replace(np.NaN,-999)
    #print(df.isnull().sum())
    
    #print(df['Category'].unique())
    total = 0
    count=0
    dict_cat_size = {} 
    for index in range(len(df)):
            if df['Category'][index]==-999 or df['Size'][index]==-999 :
                continue
            if df['Category'][index] in dict_cat_size:
                dict_cat_size[df['Category'][index]][0]+=float(df['Size'][index])
                dict_cat_size[df['Category'][index]][1]+=1
            else:
                dict_cat_size[df['Category'][index]]=[float(df['Size'][index]),1]
    #print(dict_cat_size)
    
    for category in dict_cat_size:
        try:
            size = dict_cat_size[category][0]  
            count = dict_cat_size[category][1]
            dict_cat_size[category]=float(size/count)
        except:
            print('')
            
            
    #print(dict_cat_size)
            
            
    #print(len(dict_cat_size))
    
    x_label,y_count = [],[]
    
    for cat in dict_cat_size:
        x_label.append(cat)
        y_count.append(dict_cat_size[cat])
    
    colors = cm.rainbow(np.linspace(0, 1, len(x_label)))
    
    figure2 = plt.Figure(figsize=(9,7), dpi=80)
    
    chart = figure2.add_subplot(111)
    #x=['Dis-Liked Apps' , 'Liked Apps']
    #y=[like_dislike_list.count(0),like_dislike_list.count(1)]
    bar_plot = chart.barh(x_label,y_count,color=colors)
    chart.set_ylabel("CATEGORY")
    chart.set_xlabel("Download size")
    figure2.suptitle('Download size per Category')
    chart.legend()

    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=3,y=0)
    
    #'TRAVEL_AND_LOCAL,Family,game,sports 
    String="""
            The Google Play Store shows apps’ actual download sizes. 
            Game and Family app categories have the highest average download size,
            while TOOLS category is the smallest on average.
           """
           
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=50,y=520)
   
    root.mainloop()
    

"""Feature cat_download size END============================================================================="""

"""Feature cat_rev START============================================================================="""
def feature_cat_review(event):
    
    global screen,df
    
    df = pd.read_csv("DATA SET-2.csv")
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='750',height='690',bd=4,relief=RIDGE)
    big_frame.place(x=10,y=60)
    w=800
    h=790
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')

    
    df = pd.read_csv("DATA SET-2.csv")
    
    df=df.replace(np.NaN,-999)

    dict_cat_review = {}
    for index in range(len(df)):
        
        if df['Category'][index]==-999:
            continue
        
        if df['Category'][index] in dict_cat_review:
            dict_cat_review[df['Category'][index]]+=df['Reviews'][index]
        else:
            dict_cat_review[df['Category'][index]]=df['Reviews'][index]
  
    y_count=[]
    x_label=[]
    for i in dict_cat_review:
        x_label.append(i)
        y_count.append(dict_cat_review[i])
        
    
    #print(y_count)
    
    colors = cm.rainbow(np.linspace(0, 1, len(x_label)))
    
    figure2 = plt.Figure(figsize=(9,7), dpi=80)
    
    chart = figure2.add_subplot(111)
    #x=['Dis-Liked Apps' , 'Liked Apps']
    #y=[like_dislike_list.count(0),like_dislike_list.count(1)]
    bar_plot = chart.barh(x_label,y_count,color=colors)
    chart.set_ylabel("CATEGORY")
    chart.set_xlabel("COUNT OF TOTAL REVIEWS")
    figure2.suptitle('COUNT OF TOTAL REVIEW UNDER DIFFERENT CATEGORY')
    chart.legend()

    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=3,y=0)
    
    String="""
           It looks like only a small number of users take the time to write 
           an app review.Our analysis has shown that users tend to leave more 
           reviews for apps in Games,Social,Communication and Family categories
           """
           
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=50,y=520)
   
    root.mainloop()
    

"""Feature cat_rev END============================================================================="""

""" Ques 4 START================================================================================================================================="""

def function_q4(event):
   
    global screen,df
    
    df = pd.read_csv("DATA SET-2.csv")
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='580',height='530',bd=4,relief=RIDGE)
    big_frame.place(x=10,y=60)
    w=600
    h=600
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.configure(background='white')

    df = pd.read_csv("DATA SET-2.csv")
    df=df.replace(np.NaN,-999)
    #print(df.isnull().sum())
    #print(df.head(5))
    total_rating = 0
    dict_cat_review = {}
    for index in range(len(df)):
        
        if df['Category'][index]==-999 or df['Rating'][index]==-999:
            continue
        
        if df['Category'][index] in dict_cat_review:
            dict_cat_review[df['Category'][index]][0]+=df['Rating'][index]
            dict_cat_review[df['Category'][index]][1]+=1
            total_rating+=df['Rating'][index]
        else:
            dict_cat_review[df['Category'][index]]=[df['Rating'][index],1]
            total_rating+=df['Rating'][index]
    
    
    total=0
    count=0
    for i in df['Rating']:
        if i!=-999:
            total+=i
            count+=1
    avg_rating= total/count

    y_count=[]
    x_label=[]
    for i in dict_cat_review:
        if dict_cat_review[i][0]/dict_cat_review[i][1]>=avg_rating:
            avg = (dict_cat_review[i][0]/dict_cat_review[i][1])    
            x_label.append(i)
            y_count.append(float(avg))
    
    
    figure3 = plt.Figure(figsize=(7,4), dpi=80)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(y_count,x_label,color='r')
    scatter3 = FigureCanvasTkAgg(figure3, big_frame) 
    scatter3.get_tk_widget().place(x=10,y=0)
    ax3.legend() 
    ax3.set_xlabel("RATING")
    ax3.set_ylabel("CATEGORY")
    ax3.set_title('CATEGORIES WITH HIGHEST MAXIMUM AVERAGE RATING')

    String = """
            There are Total 33 Unique categories are present in the data set 
            but out of {} Categories has managed to get the Highest Maximum 
            Average Rating of From the User
            Average Rating from given data set is {:.1f}
            """.format(len(x_label),avg_rating)
            
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=300)
    
    root.mainloop()

""" Ques 4 END================================================================================================================================="""

def data():
    global frame
    
    for i in range(50):
       tk.Label(frame,text=i).grid(row=i,column=0)
       tk.Label(frame,text="my text"+str(i)).grid(row=i,column=1)
       tk.Label(frame,text="..........").grid(row=i,column=2)


def myfunction(event):
    global canvas
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

def overviewClick(event):
    global screen
    import InsightsDesign as over
    over.startingScreen(screen)

def categoryClick(event):
    global screen
    import InsightsDesignForCategory as cat
    cat.startingScreen(screen)


def reviewClick(event):
    global screen
    import InsightsDesignToStudyReview as rev
    rev.startingScreen(screen)
    
def machineClick(event):
    global screen 
    import InsightsDesignForMachineLearningModels as mac
    mac.startingScreen(screen)

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


def sizeClick(event):
    print("")

def adjustWindow(window):
    global screen
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    window.geometry("%dx%s"%(ws,hs))
    
    window.configure(background='white')

def startingScreen(root):
    global screen,df,canvas_big_frame,frame
    
    df=pd.read_csv('DATA SET-2.csv')
    
    root.destroy()
    
    screen = tk.Tk()
    adjustWindow(screen)
    screen.title("Insights of Google App's")
    
    tk.Label(screen,text="",bg="white").pack()
    tk.Label(screen,text="CATEGORY",width=1000,height=1,font=("Helvetica",15,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
    lbl_over = tk.Label(screen,text = "Overview",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_over.bind("<Button-1>",overviewClick)
    lbl_over.place(x=5,y=65)
    
    lbl_category = tk.Label(screen,text = "Category",width=13,height='2',font=("Calibri",13,'bold'),fg='#75acff',bg='white')
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
                          
    
    big_frame=tk.Frame(screen,bg='#F8E0E0',width='1520',height='730',bd=4,relief=RIDGE)# to change background in category page
    big_frame.place(x=3,y=100)
    
    """
    4) Which category of apps have managed to get the highest maximum average ratings from the users.

    3) Which category of apps have managed to get the most,least and an average of 2,50,000 downloads atleast.

    """
    
    q4 = tk.Label(big_frame,text = "The apps that managed to get the highest maximum rating from the user.",width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    q4.bind("<Button-1>", function_q4)
    q4.place(x=50,y=10)
    
    
    feat_cat_rev = tk.Label(big_frame,text = "Category V/S Review",width=52,height=6,font=("Calibri",17,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    feat_cat_rev.bind("<Button-1>", feature_cat_review)
    feat_cat_rev.place(x=750,y=10)
    
    #function_q11(frame1)
    
    feat_cat_size = tk.Label(big_frame,text = "Category V/S Size",width=52,height=6,font=("Calibri",17,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    feat_cat_size.bind("<Button-1>", feature_cat_size)
    feat_cat_size.place(x=50,y=250)       
    
    q3 = tk.Label(big_frame,text = "Category of apps that managed to get most, least an average of 2,50,000 downloads.",width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    q3.bind("<Button-1>", function_q3)
    q3.place(x=750,y=250)       
    
    q5 = tk.Label(big_frame,text = "Category wise download trend for the data is available over the period.",width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    q5.bind("<Button-1>", function_q5)
    q5.place(x=50,y=490)       
    



    screen.mainloop()
    
#startingScreen(tk.Tk())
