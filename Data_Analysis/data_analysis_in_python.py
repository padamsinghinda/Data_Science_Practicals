# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 04:54:54 2017

@author: Padam Singh
"""
import numpy as np
import pandas as pd
import re

def fill_na(df) :
    """ Problem_1 : Fill missing values in column 'FlightNumber' of DataFrame Where values in this column need to be increased by 10 with each row."""
    
    df2 = pd.DataFrame({'FlightNumber': np.arange(10045,10085,10)})
    df3 = df['FlightNumber'].copy()    
    for item in df[df3.isnull()].index.tolist() :
        df3.loc[item] = df2['FlightNumber'].loc[item]        
    df['FlightNumber'] = df3.astype(dtype="int64")  
    return df


def create_temp_DataFrame(df) :
    """ Problem_2 : Creating a temparory DataFrame with the values in the column 'From_To'. """
    
    df1 = df.copy()
    if 'From_To' in df1.columns :        
        c1,c2 = re.split('_', 'From_To')    
        c1_values = []
        c2_values = []
        for item in df1['From_To'] :
            a,b = re.split('_',item)
            c1_values.append(a)
            c2_values.append(b)
        temp_df = pd.DataFrame({c1 : c1_values, c2 : c2_values})
    return temp_df


def standardise_DataFrame(temp_df) :
    """ Problem_3 : standardise temparory DataFrame values."""
    
    temp_df['From'] = pd.DataFrame([item for item in map(lambda x : x.capitalize(), temp_df['From'])])
    temp_df['To'] = pd.DataFrame([item for item in map(lambda x : x.capitalize(), temp_df['To'])])    
    return temp_df

def add_drop_columns(df, temp_df) :
    """ 
    Problem_4 :
    1. Delete a column from DataFrame
    2. Prefrom merge in DataFrame df and temp_df. 
    """
    
    if 'From_To' in df.columns :
        df.drop('From_To', axis=1, inplace=True)
    df = pd.concat([df, temp_df], axis=1)
    return df

def column_operations(df):
    """
    Problem_5 :
    1. Create new DataFrame delays using a existing column 'RecentDelays'.
    2. Use column names as delay_1, delay_2... etc in DataFrame delays.
    2. Use NaN for missing values.
    3. Replace column 'RecentDelays' with DataFrame 'delays'.
    """
    
    max_len = max(map(lambda x : len(x), df['RecentDelays']))
    delays = pd.DataFrame()
    for i in range(max_len) :
        temp = 'delay_'+ str(i+1)
        temp_list = []
        for j in range(df.shape[0]) :
            try :
                temp_list.append(df['RecentDelays'].iloc[j][i])
            except :
                temp_list.append(np.nan)
        delays[temp] = temp_list
    df.drop('RecentDelays', axis=1, inplace=True)
    df = pd.concat([df,delays], axis=1)
    return df

        
if __name__ == '__main__' :
    df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',  
                               'Budapest_PaRis', 'Brussels_londOn'], 
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',  
                               '12. Air France', '"Swiss Air"']})
    
    print(f"DataFrame : \n{df}\n\n")    
    df = fill_na(df)
    print(f"DataFrame after filling missing values in column 'FlightNumber' : \n{df}\n\n")
    
    temp_df = create_temp_DataFrame(df)
    print(f"Temparory DataFrame created from column 'From_To' : \n{temp_df}\n\n")
    
    temp_df = standardise_DataFrame(temp_df)
    print(f"Temparory DataFrame after standardising columns values : \n{temp_df}\n\n")
    
    df = add_drop_columns(df, temp_df)
    print(f"DataFrame after dropping column 'From_To' and merging with Temparory DataFrame: \n{df}\n\n")
    
    df = column_operations(df)
    print(f"DataFrame after operation performed on column 'RecentDelays': \n{df}\n\n")
