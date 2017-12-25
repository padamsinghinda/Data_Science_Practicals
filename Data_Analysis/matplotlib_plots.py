# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 22:33:33 2017

@author: Padam Singh

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def pie_chart(titanic) :
    "Pie chart to display Male/Female proportion"
    
    pie_c = plt.figure("Pie Chart")
    plt.title("Pie chart for male/female proportion")
    
    male_count, female_count = titanic['sex'].value_counts()['male'], titanic['sex'].value_counts()['female']
    labels = 'male', 'female'
    fracs = [male_count, female_count]
    plt.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True)
    pie_c.show()

def scatter_plot(titanic) :
    "Scatter plot between 'fare paid' and 'age'"
    
    scatter_p = plt.figure("Scatter Plot")
    plt.title("Plot between 'fare paid' and 'age'")
    plt.xlabel("fare paid")
    plt.ylabel("age")
    
    x1 = titanic[titanic['sex'] == 'male']['fare']
    y1 = titanic[titanic['sex'] == 'male']['age']
    x2 = titanic[titanic['sex'] == 'female']['fare']
    y2 = titanic[titanic['sex'] == 'female']['age']
    
    plt.scatter(x1,y1, c='b', marker='o', label='Male', alpha=1)
    plt.scatter(x2,y2, c='r', marker='o', label='Female', alpha=1)
    
    plt.legend()
    scatter_p.show()


if __name__ == '__main__':
    url= 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
    titanic = pd.read_csv(url)
    pie_chart(titanic)
    scatter_plot(titanic)
    
    
