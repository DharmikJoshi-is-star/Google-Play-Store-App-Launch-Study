import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import sys
from collections import OrderedDict 
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import InsightsDesign as ove

data=pd.read_csv('DATA SET-2.csv')

data=data.replace(np.NaN,0)
data.drop(index=[10472],inplace=True)
sample=pd.read_csv('DATA SET-1.csv')




def saveing(x,y,z,p):
    global data
    value=[]  
    if z=='DATA SET-2.csv':
        date1=p[0].get()
        month=p[1].get()
        year=p[2].get()
        date=month+' '+date1+','+' '+year
        dd=data.columns.tolist()
    elif z=='DATA SET-1.csv':
        dd=sample.columns.tolist()
     
    for i in x:
        value.append(i.get())
    


    if z=='DATA SET-2.csv':

        
        value.insert(10,date)
        #print(value)
        value[5]=str(value[5])+'+'
        value[7]='$'+str(value[7])
        #print(value)
        #print(dd)
        dp=pd.DataFrame([value],columns=dd)
        dat=data.append(dp)
        
        
    elif z=='DATA SET-1.csv':

        dp=pd.DataFrame([value],columns=dd)
        dat=sample.append(dp)


    tk.messagebox.showinfo('Success','Data Successfully Written')
    dat.to_csv(z,index=False)
    y.config(state='disabled')
    
    
def check1(x):
        d=[]
      
        for i in x:
            if i.get()=='':
                tk.messagebox.showwarning('Fields empty','Please provide all the fields')
                return True
            
        try:
           if(isinstance(float(x[3].get()), float) and isinstance(float(x[4].get()), float)):
               if x[2].get()=='Neutral':
                   if float(x[3].get())==0 and 1>=float(x[4].get())>=0:
                       d.append(False)
                   else:
                       tk.messagebox.showwarning('Neutral sentiment','Please provide a 0 in Sentiment polarity and Sentiment Subjectivity.')
                       return True
               elif x[2].get()=='Positive':
                   if float(x[3].get())>0 and 1>=float(x[4].get())>=0:
                       d.append(False)
                   else:
                       tk.messagebox.showwarning('Positive sentiment','Please provide a positive value in Sentiment polarity and Sentiment Subjectivity.')
                       return True
               elif x[2].get()=='Negative':
                   if float(x[3].get())<0 and 1>=float(x[4].get())>=0:
                       d.append(False)
                   else:
                       tk.messagebox.showwarning('Positive sentiment','Please provide a negative value in Sentiment polarity and non negative value in Sentiment Subjectivity.')
                       return True
        except:
            tk.messagebox.showwarning('Wrong Value','Please provide a float value in Sentiment polarity and Sentiment Subjectivity.')
            return True
        
        if set(d)==False:
            return False
                   
        

def check(x,z):
    d=[]
    for i in x:    
        if i.get()=='':
            tk.messagebox.showwarning('Fields empty','Please provide all the fields')
            return True
    for i in z:
        if i.get()=='':
            tk.messagebox.showwarning('Fields empty','Please provide all the fields')
            return True

    try:
        if(isinstance(float(x[2].get()), float)):# code for checking the user entered a valid rating in the entry field
            if(float(x[2].get())<=5 and float(x[2].get())>=0):
                d.append(False)
            else:
                tk.messagebox.showerror('Out of range','Rating should be between 0 to 5 only')
                return True
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a float value in rating column')
        return True
    try:
        if(isinstance(int(x[3].get()), int)):
            d.append(False)
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a integer value in Reviews')
        return True
    try:
        
        if(isinstance(float(x[4].get()[:-1]), float)):
            if(x[4].get()[-1]=='k' or x[4].get()[-1]=='M'):
                d.append(False)
            else:
                tk.messagebox.showerror('Size',"Size should end with 'k' or 'M'")
                return True           
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a integer value followed in size column')
        return True
    try:
        if(isinstance(float(x[5].get()), float)):
            d.append(False)
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a integer value in Installs')
        return True
    try:
        if x[6].get()=='Free':
            if x[7].get()=='0':
                d.append(False)
            else:
                tk.messagebox.showwarning('Free app','Please enter 0 in price column')
                return True
    except:
        print('hi')
            
    try:
        if(isinstance(float(x[7].get()), float)):
            d.append(False)
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a float value in Price')
        return True

    
    if set(d)==False:
        return False
    
    
    
    
       
def validate2(x,y):
    App=x[0].get()
    d=0
    ap=sample['App'].unique()
    for i in ap:
        if i.strip()==App.strip():
            msg='App named '+App+' is already present'
            tk.messagebox.showerror("Error",msg)
            d=1
    if(check1(x)):
        d=1
    if d==0:
        y.config(state='normal')
    
    
         
def validate(x,y,z):
    App=x[0].get()
    d=0
    ap=data['App']
    for i in ap:
        if i.strip()==App.strip():
            msg='App named '+App+' is already present'
            tk.messagebox.showerror("Error",msg)
            d=1
            break
            
    if check(x,z):
        
        d=1

    if d==0:
        y.config(state='normal')
     
def adjustWindow(window):
    global screen
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    window.geometry("%dx%s"%(1300,hs))
    
    window.configure(background='white')

def startingScreen(root):
    global screen,df,data
    dates=[]
    month=['January', 'February', 'March', 'April','May','June','July','August','September', 'October', 'November','December']
    years=[]
    for i in range(1,32):
        dates.append(i)
    for i in range(2010,2020):
        years.append(i)

    root.destroy()
    
    screen = tk.Tk()
    adjustWindow(screen)
    screen.title("Insights of Google App's")
    
    tk.Label(screen,text="",bg="white").pack()
    tk.Label(screen,text="INSERT VALUES",width=1000,height=1,font=("Helvetica",15,'bold'),fg='white',bg='#F8E0E0', borderwidth=2, relief="groove").pack()
    
    insertition_frame_1 = tk.Frame(screen,bg='#F8E0E0',width = 500,height = 640,bd=4,relief=RIDGE)
    insertition_frame_1.place(x=100,y=80)
    
    header=data.columns.tolist()
    category= list(OrderedDict.fromkeys(data['Category']))
    content=list(OrderedDict.fromkeys(data['Content Rating']))
    genre=list(OrderedDict.fromkeys(data['Genres']))
    header2=sample.columns.tolist()
    screen.title('Data Modifying')
    txt=[]
    datecombo=[]
    for i in range(1,14):
        tk.Label(insertition_frame_1,text=header[i-1],width=11,font=("Calibri",11,'italic'),fg='#ab3059',bg='#F8E0E0').place(x=50,y=40*i)
        
    for i in range(1,14):
        if i!=2 and i!=10 and i!=9 and i!=7 and i!=11 and i!=13:
            txtfield=tk.Entry(insertition_frame_1,bd=10,insertwidth=4,bg="white")
            txt.append(txtfield)
            txtfield.place(x=150,y=40*i)
        elif i==2:
            combo=ttk.Combobox(insertition_frame_1,values=category)
            txt.append(combo)
            combo.place(x=150,y=40*i)
        elif i==9:
            combo=ttk.Combobox(insertition_frame_1,values=content,state="readonly")
            txt.append(combo)
            combo.place(x=150,y=40*i)
        elif i==10:
            combo=ttk.Combobox(insertition_frame_1,values=genre,state="readonly")
            txt.append(combo)
            combo.place(x=150,y=40*i)
        elif i==7:
            combo=ttk.Combobox(insertition_frame_1,values=['Free','Paid'],state="readonly")
            txt.append(combo)
            combo.place(x=150,y=40*i)
        elif i==11:
            combo=ttk.Combobox(insertition_frame_1,values=dates,width=2,state="readonly")
            datecombo.append(combo)
            combo.place(x=150,y=40*i)
            
            combo=ttk.Combobox(insertition_frame_1,values=month,width=10,state="readonly")
            datecombo.append(combo)
            combo.place(x=190,y=40*i)
            
            combo=ttk.Combobox(insertition_frame_1,values=years,width=5,state="readonly")
            datecombo.append(combo)
            combo.place(x=278,y=40*i)
        elif i==13:
            combo=ttk.Combobox(insertition_frame_1,values=list(data['Android Ver'].unique()),state="readonly")
            txt.append(combo)
            
            combo.place(x=150,y=40*i)

    btn_save=tk.Button(insertition_frame_1,text='Save',state="disabled",bd=12,width=10,bg="powder blue",command=lambda:saveing(txt,btn_save,'DATA SET-2.csv',datecombo))    
    btn_validate=tk.Button(insertition_frame_1,text='Validate',bd=12,width=10,bg="powder blue",command=lambda:validate(txt,btn_save,datecombo))
    btn_validate.place(x=100,y=580)
    btn_save.place(x=250,y=580)   

    insertition_frame_2 = tk.Frame(screen,bg='#F8E0E0',width = 500,height = 640,bd=4,relief=RIDGE)
    insertition_frame_2.place(x=700,y=80)
    
    txt2=[]
    for i in range(1,6):
        tk.Label(insertition_frame_2,text=header2[i-1],width=17,font=("Calibri",11,'italic'),fg='#ab3059',bg='#F8E0E0').place(x=50,y=40*i)
        
    for i in range(1,6):
            if i!=3:
                txtfield=tk.Entry(insertition_frame_2,bd=10,insertwidth=4,bg="white")
                txt2.append(txtfield)
                txtfield.place(x=250,y=40*i)
            elif i==3:
                combo=ttk.Combobox(insertition_frame_2,values=['Positive','Negative','Neutral'],state="readonly")
                txt2.append(combo)
                combo.place(x=250,y=40*i)

    btn_save1=tk.Button(insertition_frame_2,text='Save',state="disabled",bd=12,width=10,bg="powder blue",command=lambda:saveing(txt2,btn_save1,'DATA SET-1.csv',''))    
    btn_validate1=tk.Button(insertition_frame_2,text='Validate',bd=12,width=10,bg="powder blue",command=lambda:validate2(txt2,btn_save1))
    btn_validate1.place(x=100,y=580)
    btn_save1.place(x=250,y=580)
    
    tk.Button(screen,text="BACK TO OVERVIEW",bd=10,font=("Calibri",13,'italic'),bg='powder blue',command = lambda: ove.startingScreen(screen) ).place(x=550,y=730)
    
    screen.mainloop()
    

#startingScreen(tk.Tk())
