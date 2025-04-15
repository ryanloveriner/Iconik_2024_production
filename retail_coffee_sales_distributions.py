# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 11:07:48 2025

@author: ryanc
"""

import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np
#import matplotlib.ticker as ticker
#import matplotlib.patches as mpatches
#import textwrap

#Prime Retail Sales
prime_retail_sales = pd.read_csv(r"C:\Users\ryanc\OneDrive\Documents\Work Stuff\Cafe Product Pars\prime_retail_coffee_sales.csv", encoding='cp1252')
prime_ratios = prime_retail_sales['Units Sold']
prime_labels = prime_retail_sales['Category']
plt.figure(figsize=(10,5.6))
plt.pie(prime_ratios, labels=prime_labels, autopct='%1.1f%%', startangle=140)
plt.title('Prime retail coffee sales distribution 2024')

#Lupe Retail Sales
lupe_retail_sales = pd.read_csv(r"C:\Users\ryanc\OneDrive\Documents\Work Stuff\Cafe Product Pars\lupe_retail_coffee_sales.csv", encoding='cp1252')
lupe_ratios = lupe_retail_sales['Units Sold']
lupe_labels = lupe_retail_sales['Category']
plt.figure(figsize=(10,5.6))
plt.pie(lupe_ratios, labels=lupe_labels, autopct='%1.1f%%', startangle=140)
plt.title('Lupe retail coffee sales distribution 2024')

#Red Retail Sales
red_retail_sales = pd.read_csv(r"C:\Users\ryanc\OneDrive\Documents\Work Stuff\Cafe Product Pars\red_retail_coffee_sales.csv", encoding='cp1252')
red_ratios = red_retail_sales['Units Sold']
red_labels = red_retail_sales['Category']
plt.figure(figsize=(10,5.6))
plt.pie(red_ratios, labels=red_labels, autopct='%1.1f%%', startangle=140)
plt.title('Red retail coffee sales distribution 2024')
