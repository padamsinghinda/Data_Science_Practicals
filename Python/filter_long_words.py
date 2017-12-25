# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 01:19:14 2017

@author: Inda
"""
import re

def filter_long_words(list_of_words, n):
    """ 
    Function filter_long_words takes a list of words and an integer n as arguments and returns the list of words which are longer than n.
    """
    result = []
    for item in list_of_words :
        item = item.strip()
        if len(item) > n :
            result.append(item)
    return result

def main():
    words = input("Please enter list of words : ")
    patterns = r"[,\[ \] \'\"]"
    pattern = re.compile(patterns)
    words = re.split(pattern,words)
    n = int(input("Please enter an integer : "))
    
    output = filter_long_words(words, n)
    
    print("\nList of words which are longer than integer {} are : [{}]".format(n,','.join(output)))
 
if __name__ == '__main__':
    main()