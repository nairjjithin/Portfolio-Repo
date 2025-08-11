#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#import packages
import os
import glob
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

import pickle
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from datamatrix_prediction import matrx

global app
#instantiating tkinter.
app=Tk()
#naming the app.
app.title('DOC Classifier')
#defining frame geometry.
app.geometry(f"{300}x{300}")
 
#asks the user to upload files to be classified.
def fileupload():
    global filelist 
    files=filedialog.askopenfilenames(parent=app,title='upload')
    filelist=list(files)
    return 0

#asks the user to provide destination folder.  
def folder():
    global directory
    folder=filedialog.askdirectory(parent=app,title='select destination folder')
    directory=folder
    return 0

#execute ML algorithm for data preparation and prediction.
def execute():
    matrx(filelist,directory,app)
    return 0

#labeling button1-fileupload.
label1=Label(app,text='Select files')
label1.grid(row=1,column=0)
button1=Button(app,text='upload',command=fileupload,padx=20,pady=10)
button1.grid(row=1,column=25)


#labeling button2-folder.
label2=Label(app,text='Select destination folder')
label2.grid(row=15,column=0)
button2=Button(app,text='selectfolder',command=folder,padx=20,pady=10)
button2.grid(row=15,column=25)

#defining button3 for executing ML algorithm.
button3=Button(app,text='execute',command=execute,bg='blue',padx=20,pady=10)
button3.grid(row=35,column=25)

app.mainloop()


