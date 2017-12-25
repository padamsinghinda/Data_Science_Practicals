# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 22:35:58 2017

@author: Padam Singh
"""

print([item for item in "ACADGILD"])

print(['xyz'[j]*i for j in range(len('xyz')) for i in range(1,5)])

print(['xyz'[j]*i for i in range(1,5) for j in range(len('xyz')) if i % 3 != 0])

print([[j,] for i in range(2,5) for j in range(i,i+3)])

print([[j for j in range(i,i+4)] for i in range(2,6)])

print([(j,i) for i in range(1,4) for j in range(1,4)])