# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 09:17:31 2017

@author: Padam Singh
"""
import pandas as pd
import numpy as np


def pandas_exercise(df):    
    df['Y'] = np.where(df['X']==0, 0, np.NaN)    
    dfa = df['Y'].copy()
    #print(dfa)
    
    for index,item in enumerate(df['X']):
        if index == 0 and item != 0 :
            count = -1
        if item == 0:
            count = index
        if item != 0 :
            dfa[index] = index-count
            
    df['Y'] = dfa.astype(int)
    #print(df)
    return df

if __name__ == '__main__' :
    Data_Frame = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
    data_frame = pandas_exercise(Data_Frame)
    print(data_frame)