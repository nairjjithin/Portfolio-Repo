#!/usr/bin/env python
# coding: utf-8

# In[1]:

# import packages.
import os
import glob
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from scipy.sparse import  hstack
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from datacleaning import cleaning
from sklearn.feature_selection import SelectKBest, chi2

#define matrx function for executing ML algorithm.
def matrx(filelist,directory,app):
    
    #loading trained model and data.
    with open('pickle_train','rb') as f:
        ovr,xtrain,train,ytrain,kbest=pickle.load(f)  
    
    #creating test data frame using user uploaded files.
    filename=[]
    content=[]
    for file in filelist:
        f=open(file)
        cont=f.read()
        name=file.split('/')[-1]
        filename.append(name)
        content.append(cont)
    
    test_df=pd.DataFrame()
    test_df['filename']=filename
    test_df['content']=content
    
    #extracting and separating title and article from the content.
    text=test_df['content'].str.split("\n",n=1,expand=True)
    test_df['title']=text[0]
    test_df['content']=text[1]
    
    #cleaning and preprocessing titles .
    clean_titles = []
    for title in test_df['title'].values:
        clean_title = cleaning(title)
        clean_titles.append(clean_title)
    test_df['title']=clean_titles
    #cleaning and preprocessing articles/content.
    clean_contents = []
    for content in test_df['content'].values:
        clean_content = cleaning(content)
        clean_contents.append(clean_content)
    test_df['content']=clean_contents
    
    #vectorizing title
    tf=TfidfVectorizer(ngram_range=(1,2),min_df=3)
    tf.fit(xtrain['title'].values)
    title_tetf=tf.transform(test_df['title'].values)
    
    #vectorizing content
    tf=TfidfVectorizer(ngram_range=(1,2),min_df=5)
    tf.fit(xtrain['content'].values)
    content_tetf=tf.transform(test_df['content'].values)
    
    #creating final test data matrix
    test=hstack((title_tetf,content_tetf)).tocsr()
   
    #selecting 6000 best features
    test=kbest.transform(test)
    
    #predicting the categories of uploaded content.
    ytest_pred=ovr.predict(test)
    
    #seggregating uploaded files with respect to their categories.
    final_df=pd.DataFrame()
    final_df['filename']=test_df['filename']
    final_df['category']=ytest_pred
    
    #replacing numerical representation of categories with original.
    final_df.category[final_df.category==0]='business'
    final_df.category[final_df.category==1]='entertainment'
    final_df.category[final_df.category==2]='politics'
    final_df.category[final_df.category==3]='sports'
    final_df.category[final_df.category==4]='tech'
    print(final_df.head(3))
    
    #writing the result into excel sheet and saving the same in path.
    path=directory+'/output.xlsx'
    final_df.to_excel(path)
    
    #indicating the user that ,task completed.
    label3=Label(app,text='Done!!',font=("Arial Bold",20))
    label3.grid(row=50,column=25)
    return 0


