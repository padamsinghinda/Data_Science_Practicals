# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:02:12 2017

@author: Padam Singh
"""
import numpy as np

def moving_average(data = [], window = 1) :
    n = len(data)
    max_len = len(str(max(data)))
    avg = []
    avg_f = []
    for i in range(n):
        if(i+window <= n):
            d = []
            for j in range(i,i+window):
             d.append(data[j])
            avg.append(np.average(d))
            avg_f.append(str(np.average(d)) + "=" + "(" + f"{('+'.join(map(str,[data for data in d])))}" + str(')/') + str(max_len))
    return avg, avg_f

if __name__ == '__main__':
    data = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
    window = 3
    average, formatted_average = moving_average(data, window)
    
    print(f"\nMoving average for given input data sequence (having {len(data)} elements & window size of {window}) will have {len(data)-window+1} elements as below :\n{average}\n")
    
    print("\nMoving average is calculated as shown in below table :\n")
    max_len = len(str(max(data)))
    print(f"i     {' '.join(map(lambda x : str(x).center(max_len,' '), [j+1 for j in range(len(data))]))}")
    print(f"===== {' '.join(map(str, ['='*max_len for j in range(len(data))]))}")
    print(f"input {' '.join(map(lambda x : str(x).center(max_len,' '), [j for j in data]))}")
    
    
    for i,avg in enumerate(formatted_average) :
        s = '  '*(i+1)
        print("y{}{}{}".format(i+1,s,avg))