# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 20:47:35 2019

@author: Dharmik joshi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:46:07 2019

@author: Dharmik joshi
"""
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  #statistical analysis
from sklearn.model_selection import train_test_split
from sklearn import metrics #used to find the accuracy
from sklearn import tree
from sklearn.impute import SimpleImputer
import math
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
import sys
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.impute import SimpleImputer
from PIL import Image,ImageTk
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.linear_model import LinearRegression #for all the formulas of linear regression formuls
from sklearn.metrics import r2_score 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #for all the formulas of linear regression formuls
from sklearn.metrics import r2_score 
import statsmodels.api as sm

"""Ques 13 START============================================================================================="""
"""
Study and find out the relation between the Sentiment-polarity and sentiment-subjectivity of all the apps.
"""

def newRelation1(app,x,y):
    global dict_app_relation
        
    for i in x:
        if i==-999:
            x.remove(i)
            y.remove(i)
        
    if x==[] or y==[]:
        return
        
    data = pd.DataFrame({'Sentiment_pol':y , 'Sentiment_sub': x})
    val = data['Sentiment_pol'].corr(data['Sentiment_sub'])
        
    dict_app_relation[app] = val

def function_q13(event):
    global screen,df,dict_app_relation
    dict_app_relation={}
    
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='700',height='630',bd=4,relief=RIDGE)
    big_frame.place(x=50,y=60)
    w=800
    h=700
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))

    root.configure(background='white')

    
    df = pd.read_csv("DATA SET-1.csv")
    df=df.replace(np.NaN,-999)
    
    dict_app_index_count={}
    for index in range(len(df['App'])):
        app = df['App'][index]
        if app in dict_app_index_count:
            dict_app_index_count[app][1]+=1
        else:
            dict_app_index_count[app]=[index,1]
            
    # after this for loop dict_app_index_count will hold the app name as key and it's first index in data set and total count in data set as item
    
    for app in dict_app_index_count:
        index = dict_app_index_count[app][0]
        count = dict_app_index_count[app][1]
        sub,pol=[],[]
        
        for i in range(count):
            c = index+i
            sub.append(df['Sentiment_Subjectivity'][c])
            pol.append(df['Sentiment_Polarity'][c])
        
        newRelation1(app,sub,pol)
    
    app_no = np.arange(len(dict_app_relation.keys()))
    
    relation = []
    
    for i in dict_app_relation:
        relation.append(dict_app_relation[i])
 
    figure3 = plt.Figure(figsize=(6,4), dpi=100)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(app_no,relation, color = 'g')
    scatter3 = FigureCanvasTkAgg(figure3, big_frame) 
    scatter3.get_tk_widget().place(x=50,y=45)
    ax3.legend() 
    ax3.set_xlabel("Applications in sequence")
    ax3.set_ylabel("Correlation")
    ax3.set_title("correlation between Polarity and Subjectivity for all apps")
        
    String = """
            In this Scatter plot each point represent the correlation 
            between sentiment polarity and sentiment subjectivity for 
            all Application present in Data set from the Sentiment Analysis
            Most of apps have positive relation with between sentiment polarity and subjectivity
            """
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=0,y=420)
    
    root.mainloop()
"""Ques 13 END============================================================================================="""
    


"""Ques9 START============================================================================================="""
""""
All those apps who habve managed to get over 1,00,000 downloads, have they managed 
to get an average rating of 4.1 and above?
An we conclude something in co-relation to the number of downloads and the ratings received.
"""
def getResult(rating,installs,big_frame):

    df = pd.read_csv("DATA SET-2.csv")
    
    # Replace "NaN" with mean 
    imputer = SimpleImputer()
    df['Rating'] = imputer.fit_transform(df[['Rating']])
    
    temp = []
    for index in range(len(df['Rating'])):
        if df['Rating'][index] >= rating:
            temp.append(1)
        else:
            temp.append(0)
            
    cat_rating= pd.DataFrame(zip(temp,temp),columns=["cat_Ratings","ignore"])
    
    df = pd.concat([df,cat_rating],axis=1)
    
    df.drop("ignore",axis=1,inplace=True)
    
    df.drop(df.index[9148], inplace=True)
    
    # Data cleaning for "Installs" column
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    
    df['Installs'] = pd.to_numeric(df['Installs'])
    
    rating_sum = 0 
    
    rate=[]
    #1169
    """ """
    counter=0
    for index in range(len(df)):
        try:
            if df['Installs'][index]>=installs:
                #if df['Rating'][index]>=rating:""" """
                    rate.append(1)
                    rating_sum+=df['Rating'][index]
                    counter+=1
                    """ """
            else:
                    rate.append(0)
                
        except:
            #print(index)
            continue
        
    
    #print(len(rate))
    avg_rating = (rating_sum/counter)
    """ """
    #print(df['Installs'].corr(df['Rating']))
    
    """ """
    val = "Yes" if (rating_sum/counter)>=rating else "No"
    rel = "Greater than" if val == "Yes" else "Lesser than"
    
    fig, ax = plt.subplots(figsize=(10, 10))
    
    l1 ='{}>='.format(installs)
    l2 ='<{}'.format(installs)
    
    size=[rate.count(1),rate.count(0)]
    label = [l1,l2]
    title = 'Count of {}'.format(rating)

    figure1 = plt.Figure(figsize=(5,5), dpi=70)
    
    #color = cm.rainbow(np.linspace(0, 1, 10))
    #fig1, ax1 = plt.subplots()
    ax3 = figure1.add_subplot(111)
    ax3.pie(size, labels=label,colors = ['red','blue'], autopct='%1.1f%%', startangle=200)
    ax3.set_title(title)
    #ax3.xlim(0,3.0)
    pie_plot = FigureCanvasTkAgg(figure1, big_frame) 
    pie_plot.get_tk_widget().place(x=80,y=190)
    
    
    tk.Label(big_frame,text="--Results--",font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=220,y=470)
    
    
    String = "Average rating of all the apps who managed to get over {} download is {:.1f}".format(installs,avg_rating)
    
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=0,y=500)
      
    String ="""{}! All those apps who have managed to get over {} downloads , 
            they have to get an average rating of {:.1f} which is {} than {} """.format(val,installs,avg_rating,rel,rating)
    
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=0,y=530)
    
             
    #ax3.legend(loc=0) 
    
    
    

def function_q9(event):
    global screen,df
    
    df = pd.read_csv("DATA SET-2.csv")
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='600',height='630',bd=4,relief=RIDGE)
    big_frame.place(x=50,y=60)
    w=700
    h=700
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))

    root.configure(background='white')
    
    String="""             find the avearge rating of given installs is greater than or equal 
              to given minimum rating or not?"""
    
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=0)
    
    tk.Label(big_frame,text="Rating : ",width=13,height='1',font=("Calibri",16,'italic'),fg='#05b8ff',bg='white').place(x=0,y=70)         
    rating = tk.StringVar()
    tk.Entry(big_frame,textvar=rating,width=13,bd=10,font=("Calibri",16,'italic'),fg='#75acff',bg='white').place(x=110,y=65)
             
    tk.Label(big_frame,text="Installs : ",width=13,height='1',font=("Calibri",16,'italic'),fg='#05b8ff',bg='white').place(x=280,y=70)         
    installs = tk.StringVar()
    tk.Entry(big_frame,textvar=installs,width=13,bd=10,font=("Calibri",16,'italic'),fg='#75acff',bg='white').place(x=400,y=65)
    
    tk.Button(big_frame,text="RESULT",width=13,bd=10,font=("Calibri",16,'bold'),fg='#75acff',bg='white',command = lambda : getResult(float(rating.get()),int(installs.get()),big_frame) if(rating.get()!="" and installs.get()!="")   else tk.messagebox.showerror("ERROR","PLEASE FILL ALL THE DETAILS")).place(x=220,y=130)
    
             
    root.mainloop()



"""Ques9 END============================================================================================="""


"""Ques8 START============================================================================================="""

#try Aroil model for prediction

def value(x):
        global And,val
        val+=1
        And[str(x)]=val
        return val
def getPrediction(big_frame):
    
    global rating,size,installs,price,type,android,df
    
    df = pd.read_csv("DATA SET-2.csv")
    
    category = {'SPORTS':0,'ENTERTAINMENT':1,'SOCIAL':2,'NEWS_AND_MAGAZINES':3,'EVENTS':4,'TRAVEL_AND_LOCAL':5,'GAME':6}
    
    for index in range(len(df['Category'])):
        if df['Category'][index] in category:
            continue
        else:
            df.drop(index,axis=0,inplace=True)
            
    df['Category'] = df['Category'].map(lambda x : category[x] if(x in category) else -1)
    
    dict_content_rating = {"Adults only 18+": 0, "Everyone": 1, "Everyone 10+": 2, "Mature 17+": 3, "Teen": 4}
    
    df['Content Rating NUM'] = df['Content Rating'].map(lambda x : dict_content_rating[x] if(x in dict_content_rating) else -1 )

    # Data cleaning for "Size" column
    df['Size'] = df['Size'].map(lambda x: x.rstrip('M'))
    df['Size'] = df['Size'].map(lambda x: str(round((float(x.rstrip('k'))/1024), 1)) if x[-1]=='k' else x)
    df['Size'] = df['Size'].map(lambda x: np.nan if x.startswith('Varies') else x)
    
    df['Price'] = df['Price'].map(lambda x: x if x==0 else x.lstrip('$').rstrip())
    
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    
    # Change datatype
    df['Reviews'] = pd.to_numeric(df['Reviews'])
    df['Installs'] = pd.to_numeric(df['Installs'])
    df['Price'] = pd.to_numeric(df['Price'])
    
    # Replace "NaN" with mean 
    imputer = SimpleImputer()
    df['Rating'] = imputer.fit_transform(df[['Rating']])
    # Rounding the mean value to 1 decimal place
    df['Rating'].round(1)
    df.dropna(axis=0, inplace=True)
    
    #sns.heatmap(df.isnull())
    
    df['Type'] = df['Type'].map(lambda x : 1 if(x=="Free") else 0)
    
    global And,val
    And = {}
    val = -1
    df['Android Ver'] = df['Android Ver'].map(lambda x : And[str(x)] if(str(x) in And) else value(x))
    # Features selection
    features = ['Rating', 'Size', 'Installs', 'Price', 'Type','Android Ver']
    
    #Spliting the datat fro training and testing 
    train,test=train_test_split(df,test_size = 0.3)
    
    #creating a response and target variable 
    #taking the training data input
    train_x = train[features] #multiple indepent variable
    train_y = train['Category'] #only one dependent variable
    ##print(list(train.columns))
    train,test=train_test_split(df,test_size = 0.3)
    #train,test=train_test_split(df,test_size = 0.2)
    #taking the testing data input
    test_x = test[features]
    test_y = test['Category']
    ##print(list(test.columns))
    """
    #Creating a decision tree model based on the training data
    model = tree.DecisionTreeClassifier()
    model.fit(train_x,train_y)
    #now prediction using the trained model
    prediction = model.predict(test_x)
    #now displaying the predicted vs actual values
    #dataframe = pd.DataFrame(prediction,test_y)
    """
    #idea of random forest to improve efficiency #will create a small different trees
    """ RANDOM FOREST  """
    
    model = RandomForestClassifier(n_estimators = 100) #this will create the group of 100 data
    model.fit(train_x,train_y)
    prediction = model.predict(test_x)
    #now displaying the predicted vs actual values
    
    #print(metrics.accuracy_score(prediction,test_y))

    #print(classification_report(test_y , prediction))
    
    rating_app = float(rating.get())
    size_app = float(size.get())
    installs_app = int(installs.get())
    if type == "Free":
        price_app = 0
    else:
        price_app = int(price.get())
    if type=="Free":
        type_app = 1
    else:
        type_app=0
        
    android_app = int(And[android.get()])
    
    prediction = model.predict(np.array([rating_app,size_app,installs_app,price_app,type_app,android_app]).reshape(1,-1))
    
    #print(prediction)
    
    #print(model.score(test_x,test_y))
    
    #print(category)
    val = "" 
    for val in category:
        if category[val] == prediction:
            #print(val)
            break
    
    tk.Label(big_frame,text="-----RESULT-----",height='2',font=("Calibri",19,'bold'),fg='#ad023e',bg='white').place(x=250,y=400)
    
    #print(val)
    string = "With help of parameters {} category is most likely to be downloaded in comming years".format(val)
    tk.Label(big_frame,text=string,height='2',font=("Calibri",10,'italic'),fg='#ad023e',bg='white').place(x=0,y=450)
    
    string = "Accuracy score for this model is {:.2f}%".format(model.score(test_x,test_y)*100)
    tk.Label(big_frame,text=string,height='2',font=("Calibri",11,'italic'),fg='#ad023e',bg='white').place(x=0,y=500)        

def prediction(big_frame):

    global rating,size,installs,price,type,android
    if rating.get()==" " or size.get()==" " or installs.get()==" " or price.get()==" " or type.get()=="--Select Type--" or android.get()=="--Select Android Ver--":
        #print("1")
        tk.messagebox.showerror("ERROR","PLEASE FILL ALL THE ENTRY FIELDS")
    else:
        if 0.0>=float(rating.get())>=5.0:
            tk.messagebox.showerror("ERROR","RATING IS NOT APPROPRIATE")
        else:
            try:
                getPrediction(big_frame)
            except:
                tk.messagebox.showerror("ERROR","PLEASE OPEN NEW WINDOW")

"""Amongst sports, entertainment,social media,news,events,travel and games, 
which is the category of app that is most likely to be downloaded in the 
coming years, kindly make a prediction and back it with suitable findings."""
def function_q8(event):
    global screen,df
    
    root = Toplevel(screen)
    #root.wm_attributes('-alpha', 0.7) 
    big_frame = tk.Frame(root,bg='white',width='610',height='630',bd=4,relief=RIDGE)
    big_frame.place(x=40,y=60)

    #background = ImageTk.PhotoImage(Image.open("background.jpeg"))
    #back = tk.Label(big_frame,image=background)
    #back.place(x=0,y=0)
    w=700
    h=700
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.configure(background='white')
    
    """"PARAMETERS are['Rating', 'Size', 'Installs', 'Price', 'Content Rating NUM','Type','Android Ver']
    Validations are rating must be a float value and in range of 0.0 - 5.0
    Size must be a int value 
    Installs provide a 
    """
    global rating,size,installs,price,type,android
    
    
    tk.Label(root,text="Random",width=500,height=2,font=("Helvetica",11,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
    tk.Label(big_frame,text="IN ORDER TO PREDICT THE CATEGORY PLEASE PROVIDE THE FOLLOWING PARAMETER VALUES",
             height=2,font=("Helvetica",9,'italic'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").place(x=10,y=0)
    
    tk.Label(big_frame,text="Rating : ",width=13,height='1',font=("Calibri",16,'italic'),fg='#05b8ff',bg='white').place(x=0,y=70)         
    rating = tk.StringVar()
    tk.Entry(big_frame,textvar=rating,width=13,bd=10,font=("Calibri",16,'italic'),fg='#75acff',bg='white').place(x=110,y=65)
             
    tk.Label(big_frame,text="Size : ",width=13,height='1',font=("Calibri",16,'italic'),fg='#05b8ff',bg='white').place(x=300,y=70)         
    size = tk.StringVar()
    tk.Entry(big_frame,textvar=size,width=13,bd=10,font=("Calibri",16,'italic'),fg='#75acff',bg='white').place(x=400,y=65)
    
    tk.Label(big_frame,text="Installs : ",width=13,height='1',font=("Calibri",16,'italic'),fg='#05b8ff',bg='white').place(x=0,y=140)         
    installs = tk.StringVar()
    tk.Entry(big_frame,textvar=installs,width=13,bd=10,font=("Calibri",16,'italic'),fg='#75acff',bg='white').place(x=110,y=135)
    
    tk.Label(big_frame,text="Type : ",width=13,height='1',font=("Calibri",16,'italic'),fg='#05b8ff',bg='white').place(x=300,y=140)
    type = tk.ttk.Combobox(big_frame,values=["Free","Paid"],state="readonly",width=15,height=25,font=("Calibri",13,'italic'))#,width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    type.set("--Select Type--")
    type.place(x=400,y=135)
    
    tk.Label(big_frame,text="Price : ",width=13,height='1',font=("Calibri",16,'italic'),fg='#05b8ff',bg='white').place(x=0,y=210)         
    price = tk.StringVar()
    tk.Entry(big_frame,textvar=price,width=13,bd=10,font=("Calibri",16,'italic'),fg='#75acff',bg='white').place(x=110,y=210)

    annd = []
    for i in df['Android Ver'].unique():
        annd.append(i)
    tk.Label(big_frame,text="Android Ver: ",width=13,height='1',font=("Calibri",16,'italic'),fg='#05b8ff',bg='white').place(x=275,y=210)         
    android = tk.ttk.Combobox(big_frame,values=annd,state="readonly",width=15,height=25,font=("Calibri",13,'italic'))#,width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    android.set("--Select Android Ver--")
    android.place(x=410,y=210)
    """         
    tk.Label(big_frame,text="Android Ver: ",width=13,height='1',font=("Calibri",16,'italic'),fg='#05b8ff',bg='white').place(x=275,y=210)         
    android = tk.StringVar()
    tk.Entry(big_frame,textvar=rating,width=13,bd=10,font=("Calibri",16,'italic'),fg='#75acff',bg='white').place(x=400,y=205)
    """
      
    tk.Button(big_frame,text="Prediction",width=13,bd=10,font=("Calibri",16,'bold'),fg='#75acff',bg='white',command = lambda:prediction(big_frame)).place(x=240,y=280)
    
    tk.Label(big_frame,text="This Prediction will take some time kindly wait!!",height='2',font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=150,y=350)
    
         
    root.mainloop()
"""Ques8 END============================================================================================="""

"""Ques17 START============================================================================================="""
#Does the size of the App influence the number of installs that it gets ? if,yes the trend is positive or negative with the increase in the app size.
def function_q17(event):
    global screen,df
    df = pd.read_csv("DATA SET-2.csv")
    root = Toplevel(screen)
    big_frame = tk.Frame(root,bg='white',width='600',height='630',bd=4,relief=RIDGE)
    big_frame.place(x=50,y=60)
    w=700
    h=700
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.configure(background='white')
    
    df.drop(9148,axis=0, inplace=True)
    df.drop(10472,axis=0,inplace=True)
    
    #print(df['Installs'].head(5))
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    
    df['Installs'] = pd.to_numeric(df['Installs'])

    # Data cleaning for "Size" column
    df['Size'] = df['Size'].map(lambda x: x.rstrip('M'))
    df['Size'] = df['Size'].map(lambda x: str(round((float(x.rstrip('k'))/1024), 1)) if x[-1]=='k' else x)
    df['Size'] = df['Size'].map(lambda x: np.nan if x.startswith('Varies') else x)
    
    df['Size'] = pd.to_numeric(df['Size'])

    # Replace "NaN" with mean 
    imputer = SimpleImputer()
    df['Size'] = imputer.fit_transform(df[['Size']])
    df['Installs'] = imputer.fit_transform(df[['Installs']])
        
    #now creating linear approximation
    x = df['Size'].values.reshape(-1,1) # this reshape wil converts the data into the specific format in which fit function is required
    y = df['Installs'].values.reshape(-1,1)
    
    reg=LinearRegression()
    reg.fit(x,y)
    #reg.coef_calculates slope , reg.intercept_calculates 'C'
    #print(reg.coef_)
    #print(reg.score(x,y))

    #now creating prediction
    prediction = reg.predict(x)
    
    #now assesing efficiency using R-squared model
    x = df['Size']
    y = df['Installs']
    x2 = sm.add_constant(x) #sci-kit is used to eliminate the value of x because x is indipndent variable
    #Ordinary least squares is the simplest and most common estimator in which the two \(\beta\)s are chosen to minimize the square of the distance between
    est = sm.OLS(y,x2)
    est2 = est.fit()
    #print( est2.summary())
    
    
    figure3 = plt.Figure(figsize=(5,4), dpi=100)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(df['Size'],df['Installs'], color = 'y')
    ax3.plot(df['Size'],prediction,color='r')
    scatter_plot = FigureCanvasTkAgg(figure3, big_frame) 
    scatter_plot.get_tk_widget().place(x=50,y=20)
    ax3.legend() 
    ax3.set_xlabel("Size of the App")
    ax3.set_ylabel("Installs")
    ax3.set_title("Trend of Install")
        
    String = """          Conclusion : -  
                Here we have applied Linear Regression to find the Trend 
                As we can observe from above graph There is a Positive Trend 
                From the trend as increase in the size of App influence the 
                number of installs"""
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=450)
    
    root.mainloop()
"""Ques17 END============================================================================================="""


"""Ques15 START============================================================================================="""
#For Ques 15
def setAppSentiment(app,sentiment):
        global dict_app_sent
        p=sentiment.count(1)
        n=sentiment.count(0)
        if(p>n):
            dict_app_sent[str(app)]=1
        else:
            dict_app_sent[str(app)]=0

#Ques 15
def result(app,root):
    global dict_app_sent,df
    for a in df['App'].unique():
        if (str(a)[0:10]+"...") == app:
            if dict_app_sent[str(a).lower()] == 1:
                sentiment = "LIKE"
            else:
                sentiment = "DISLIKE"
            break
    #print(dict_app_sent)
    tk.Label(root,text="",height='2',font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=560)
    
    try:
        String = "Name of choosen app is '{}' User will {} this App".format(str(a),str(sentiment))
    except:
        String = "App Name is can not be identified"
    tk.Label(root,text=String,height='2',font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=560)
             
def function_q15(event):
    global screen
  
    root = Toplevel(screen)
    
    big_frame = tk.Frame(root,bg='white',width='600',height='630',bd=4,relief=RIDGE)
    big_frame.place(x=50,y=60)
    
    w=700
    h=700
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.configure(background='white')
    
    tk.Label(root,text="",bg='white').pack()
    tk.Label(root,text="Is it advisable to launch an app like ’10 Best foods for you’? Do the users like these apps?",
             width=500,height=2,font=("Helvetica",11,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
              
    """For this Question will use the Sentiment Analysis provided in data set"""
    """======================================================================"""
    global dict_app_sent
    dict_app_sent={}
    
    df = pd.read_csv("DATA SET-1.csv")
    
    #print(df.isnull().sum())
    
    df['Sentiment'] = df['Sentiment'].map(lambda x : 1 if x=='Positive' else 0)
    
    dict_app_index_count={}
    for index in range(len(df['App'])):
        app = df['App'][index]
        if app in dict_app_index_count:
            dict_app_index_count[str(app)][1]+=1
        else:
            dict_app_index_count[str(app)]=[index,1]
    
    for app in dict_app_index_count:
        index = dict_app_index_count[str(app)][0]
        count = dict_app_index_count[str(app)][1]
        app = app.lower()
        pol = []
        for i in range(count):
            i = index+i
            pol.append(df['Sentiment'][index])
        setAppSentiment(str(app),pol)
    """======================================================================"""
    
    """in this label i have to plot a count plot"""
    like_dislike_list = []
    for i in dict_app_sent:
        like_dislike_list.append(dict_app_sent[i])
        
    """THIS CODE WILL PRINT THE GRAPH"""
    figure = plt.Figure(figsize=(5,5), dpi=100)
    
    chart = figure.add_subplot(111)
    x=['Dis-Liked Apps' , 'Liked Apps']
    y=[like_dislike_list.count(0),like_dislike_list.count(1)]
    chart.bar(x,y, color=['red','green'])
    chart.set_ylabel("Count App's")
    figure.suptitle("Count of Liked and Disliked apps")
    chart.legend()

    canvas = FigureCanvasTkAgg(figure, master=big_frame)
    canvas.get_tk_widget().place(x=50,y=45)
    canvas.draw()
    
    tk.Label(big_frame,text="Select an App : ",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='white').place(x=40,y=515)
    app_var = tk.StringVar()
    App_name = []
    for app in df['App'].unique():
        App_name.append(str(app)[0:10]+"...")
    
    combo = tk.ttk.Combobox(big_frame,values=App_name,state="readonly",width=25,height=25,font=("Calibri",13,'italic'))#,width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    combo.set("--Select App--")
    combo.place(x=180,y=525)
    
    tk.Button(big_frame,text="CHECK",width=10,height=1,bd=4,font=("Calibri",12,'bold'),fg='#75acff',bg='#e1e5eb',command = lambda:result(combo.get(),big_frame) if combo.get()!="--Select App--" else tk.messagebox.showerror("ERROR","APP NAME IS NOT FOUND")).place(x=440,y=520)
                          
    root.mainloop()
"""Ques15 END============================================================================================="""


def reviewClick(event):
    global screen
    import InsightsDesignToStudyReview as rev
    rev.startingScreen(screen)
    
def overviewClick(event):
    global screen
    import InsightsDesign as over
    over.startingScreen(screen)
    
def lastupdateClick(event):
    global screen
    import InsightsDesignForLastUpdate as up
    up.startingScreen(screen)


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
    window.geometry("%dx%s"%(ws,hs))
    window.configure(background='white')

def startingScreen(root):
    global screen,df
    
    df=pd.read_csv('DATA SET-2.csv')
    
    root.destroy()
    
    screen = tk.Tk()
    adjustWindow(screen)
    screen.title("Insights of Google App's")
    
    tk.Label(screen,text="",bg="white").pack()
    tk.Label(screen,text="LEARNING MODELS",width=1000,height=1,font=("Helvetica",15,'bold'),fg='#2864ad',bg='#e3efff', borderwidth=2, relief="groove").pack()
    
    
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
        
    lbl_machine = tk.Label(screen,text = "Learning Models",width=25,height='2',font=("Calibri",13,'bold'),fg='#75acff',bg='white')
    #lbl_machine.bind("<Button-1>", machineClick)
    lbl_machine.place(x=255+125+125,y=65)
    
    lbl_review = tk.Label(screen,text = "Reviews",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_review.bind("<Button-1>", reviewClick)
    lbl_review.place(x=255+125+125+125+108,y=65)
                          
    lbl_lastupdate = tk.Label(screen,text = "Last Updated",width=13,height='2',font=("Calibri",13,'italic'),fg='#75acff',bg='#e1e5eb')
    lbl_lastupdate.bind("<Button-1>", lastupdateClick)
    lbl_lastupdate.place(x=255+125+125+125+125+109,y=65)
                          
    
    big_frame = tk.Frame(screen,bg='#F8E0E0',width='1520',height='730',bd=4,relief=RIDGE)
    big_frame.place(x=3,y=100)
    
    
    q15 = tk.Label(big_frame,text = '''Is it advisable to launch an app like ’10 Best foods for you’? Do the users like these
apps?''',width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    q15.bind("<Button-1>", function_q15)
    q15.place(x=50,y=10)
    
          
    q17 = tk.Label(big_frame,text = '''Does the size of the App influence the number of installs that it gets ? if,yes the
trend is positive or negative with the increase in the app size.''',width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    q17.bind("<Button-1>", function_q17)
    q17.place(x=750,y=10)
    
    q8 = tk.Label(big_frame,text = '''Amongst sports, entertainment,social media,news,events,travel and games,which
is the category of app that is most likely to be downloaded in the coming years,
kindly make a prediction and back it with suitable findings.''',width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    q8.bind("<Button-1>", function_q8)
    q8.place(x=50,y=250)       
    
    q13 = tk.Label(big_frame,text = '''Study and find out the relation between the Sentiment-polarity and 
sentimentsubjectivity of all the apps.''',width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    q13.bind("<Button-1>", function_q13)
    q13.place(x=750,y=250)
    
    q9 = tk.Label(big_frame,text = '''All those apps who habve managed to get over 1,00,000 downloads, have they
managed to get an average rating of 4.1 and above? An we conclude something in
co-relation to the number of downloads and the ratings received.''',width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE)
    q9.bind("<Button-1>", function_q9)
    q9.place(x=50,y=500) 
    
    #tk.Label(big_frame,text = "Feature 5",width=70,height=8,font=("Calibri",13,'bold'),bd=10,fg='#75acff',bg='powder blue',relief=RIDGE).place(x=750,y=500)
    
    
    screen.mainloop()
    
#startingScreen(tk.Tk())

