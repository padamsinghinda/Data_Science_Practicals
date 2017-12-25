# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:08:38 2017

@author: Padam Singh
"""

def vowel_check(char) :
    """
    This function takes a character (i.e. a string of length 1) and
    returns True if it is a vowel, False otherwise.
    """  
    
    try :
        if len(char) > 1 :
            print("Plase enter a string of length 1.")
            return "None"
            
        if char in 'aeiou' :
            return 'TRUE'
        else :
            return 'FALSE'
    except :
        pass
    

def main():
    ch = input("Enter a character : ")
    
    output = vowel_check(ch)
    
    print("Vowel check for '{}' returns '{}'".format(ch,output))
 
if __name__ == '__main__':
    main()