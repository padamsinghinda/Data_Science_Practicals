# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 22:53:52 2017

@author: Padam Singh
"""

def longestWord(*args):
    max_len = max(map(len, args[0]))
    longestWord = []
    for item in args[0] :
        if len(item) == max_len :
            longestWord.append(item)
    return longestWord

if __name__ == '__main__' :
    pass