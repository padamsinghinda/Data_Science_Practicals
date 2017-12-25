# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 19:51:51 2017

@author: Padam Singh
"""
import re

def words_length(list_of_words) :
    "This function returns list having lenght of list_of_words passed as parameter."
    iter = map(len, list_of_words)
    result = []
    for item in iter :
        if item > 0 :
            result.append(item)
    return result

def main():
    words = input("Please enter list of words : ")
    patterns = r"[,\[ \] \'\"]"
    pattern = re.compile(patterns)
    words_1 = re.split(pattern,words)
    output = words_length(words_1)
    
    print("\nMapping of list of words into length of words are : \n{} - {}".format(words,output))
 
if __name__ == '__main__':
    main()