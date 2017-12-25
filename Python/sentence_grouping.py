# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 08:34:13 2017

@author: Padam Singh
"""

subjects=["Americans ","Indians"] 
verbs=["play","watch"] 
objects=["Baseball","Cricket"]

for subject in subjects :
    for verb in verbs :
        for object in objects :
            print("{} {} {}.".format(subject,verb,object))
            
