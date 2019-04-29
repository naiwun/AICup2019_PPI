#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:22:25 2019

@author: naiwun
"""
import pandas as pd
import os

def f1score(gold, predict):
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    f1score = 0
    accuracy = 0
    
    
    
    return f1score



dir_data = r'./data/'
f_gold = os.path.join(dir_data, 'gold.tsv')
f_predict = os.path.join(dir_data, 'predict.tsv')
gold = pd.read_csv(f_gold, sep='\t',encoding='utf-8')
predict = pd.read_csv(f_predict, sep='\t',encoding='utf-8')
