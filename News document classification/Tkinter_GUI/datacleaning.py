#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# import packages
import os
import glob
import pandas as pd
import numpy as np
import re
import unicodedata
import warnings
warnings.filterwarnings('ignore')
import pickle
import requests


#defining text normalizer function
def cleaning(text):
    
    stopwords= ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself',             'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those',             'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',             'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of',             'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very',             's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're',             've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',            "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',            "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't",             'won', "won't", 'wouldn', "wouldn't","january","february","march","april","may","june","july","august","septemer",             "october","november","december","today","tomorrow","yesterday"]
    
 #Treat accented characters
    text=unicodedata.normalize('NFKD',text).encode('ascii','ignore').decode('utf-8','ignore')    
    
    # Decontracting Words
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can\'t", "can not", text)
    text = re.sub(r"n\'t", " not", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)
    text=re.sub(r"They'd", "they would", text)
    text=re.sub(r"don't", "do not", text)
    
    #remove html tags
    pattern=re.compile(r'<.*?>')
    text=re.sub(pattern,' ',text)
    pattern=re.compile(r'http\?s\S+')
    text=re.sub(pattern,' ',text)
    
    # remove Special characters
    text = re.sub('[^A-Za-z0-9]+', ' ', text)
    text = text.lower()

    # remove line breaks \r \n \t remove from string 
    text = text.replace('\\r', ' ')
    text = text.replace('\\"', ' ')
    text = text.replace('\\t', ' ')
    text = text.replace('\\n', ' ')

    # remove stopwords
    text = ' '.join(word.lower() for word in text.split() if word not in stopwords)

    return text


