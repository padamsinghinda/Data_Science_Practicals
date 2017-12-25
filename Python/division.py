# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 08:36:29 2017

@author: Padam Singh
"""
import sys

def division(a,b):
    """
    This functions return quotient where
    quotient = dividend ÷ divisor
    """
    try :
        return a/b
    except Exception as e:
        print("\nexception : {}".format(sys.exc_info()[1]))
        sys.exit()

def main():
    a = int(input("Enter dividend : "))
    b = int(input("Enter divisor : "))
    result = division(a,b)
    print("\noutput of {}/{} is {}".format(a,b,result))
    
if __name__  == '__main__':
    main()
