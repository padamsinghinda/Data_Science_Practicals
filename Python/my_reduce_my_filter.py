# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:32:39 2017

@author: Padam Singh
"""
import sys

#problem statement 1 - my reduce function
def my_reduce(func, sequence):
    try:
        if len(sequence) <= 0 :
            raise TypeError('reduce() of empty sequence with no initial value')
        elif len(sequence) == 1 :
            return sequence[0]
        else :
            i,k = sequence[0], sequence[1]
            temp = func(i,k)
            for item in sequence[2:] :
                temp = func(temp,item)
    except Exception as e:
        return sys.exc_info()[1]
    return temp

#problem statement 2 - my filter function
def my_filter(func, sequence):
    try:
        filtered_data = []
        for item in sequence :
            if func(item) :
                filtered_data.append(item)
    except Exception as e:
        return sys.exc_info()[1]
    return filtered_data

if __name__ == '__main__' :
    pass
