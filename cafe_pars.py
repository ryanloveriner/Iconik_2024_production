# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 08:26:56 2025

@author: ryanc
"""

import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np
#import matplotlib.ticker as ticker
#import matplotlib.patches as mpatches
#import textwrap

# Read cafe datasets into dataframes
prime_sales = pd.read_csv(r"C:\Users\ryanc\OneDrive\Documents\Work Stuff\Cafe Product Pars\prime_simplified.csv")
lupe_sales = pd.read_csv(r"C:\Users\ryanc\OneDrive\Documents\Work Stuff\Cafe Product Pars\lupe_simplified.csv")
red_sales = pd.read_csv(r"C:\Users\ryanc\OneDrive\Documents\Work Stuff\Cafe Product Pars\red_simplified.csv")

# Cafe totals --> new dataframe
cafe_totals_2024 = pd.DataFrame({
    'Prime': prime_sales['Total'],
    'Lupe': lupe_sales['Total'],
    'Red': red_sales['Total']
})
cafe_totals_2024.index = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Plot total unit sales of cafes
cafe_totals_linegraph = cafe_totals_2024.plot(kind='line', marker='o')
plt.title('Month by Month Drink and Retail Coffee Sales 2024')
plt.ylabel('Total units all categories')
plt.grid(True, axis='y', color='black', linestyle='-', linewidth=0.5, 
         alpha=0.75)
plt.xticks(rotation=45)
cafe_totals_linegraph.patch.set_facecolor('lightgray')

#------------------------------------------------------------------------------

# Plot Prime sales by drink category
prime_sales.set_index('Month', inplace=True)

# PRIME bar drinks
plt.figure(figsize=(10, 5.6))
plt.plot(prime_sales.index, prime_sales['Bar Drinks'], marker='o')
plt.title('Prime Bar Drink Sales 2024')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.grid(True)
plt.tight_layout()

# PRIME brewed coffee (pillar, exceptional, iced)
plt.figure(figsize=(10,5.6))
plt.plot(prime_sales.index, prime_sales['Pillar Brewed'], label='Pillar Brewed', marker='o')
plt.plot(prime_sales.index, prime_sales['Exceptional Brewed'], label='Exceptional Brewed', marker='d')
plt.plot(prime_sales. index, prime_sales['Iced Coffee'], label='Iced Coffee', marker='^')
plt.title('Prime Brewed Coffee Sales 2024')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True)
plt.tight_layout()

# PRIME tea (hot and iced)
plt.figure(figsize=(10,5.6))
plt.plot(prime_sales.index, prime_sales['Hot Tea'], label='Hot Tea', marker='o')
plt.plot(prime_sales.index, prime_sales['Iced Tea'], label='Iced Tea', marker='d')
plt.title('Prime Tea Sales 2024')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True)
plt.tight_layout()

# PRIME BTC
plt.figure(figsize=(10,5.6))
plt.plot(prime_sales.index, prime_sales['BTC'], label='By the cup', marker='o')
plt.title('Prime By the Cup Sales 2024')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True)
plt.tight_layout()

# PRIME Retail
plt.figure(figsize=(10,5.6))
plt.plot(prime_sales.index, prime_sales['Retail Coffee'], label='Retail Coffee', marker='o')
plt.title('Prime Retail Coffee Sales')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True)
plt.tight_layout()

#------------------------------------------------------------------------------

# Plot Lupe sales by drink category
lupe_sales.set_index('Month', inplace=True)

# LUPE bar drinks
plt.figure(figsize=(10, 5.6))
plt.plot(lupe_sales.index, lupe_sales['Bar Drinks'], marker='o')
plt.title('Lupe Bar Drink Sales 2024')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.grid(True)
plt.tight_layout()

# LUPE brewed coffee (pillar, exceptional, iced)
plt.figure(figsize=(10,5.6))
plt.plot(lupe_sales.index, lupe_sales['Pillar Brewed'], label='Pillar Brewed', marker='o')
plt.plot(lupe_sales.index, lupe_sales['Exceptional Brewed'], label='Exceptional Brewed', marker='d')
plt.plot(lupe_sales. index, lupe_sales['Iced Coffee'], label='Iced Coffee', marker='^')
plt.title('Lupe Brewed Coffee Sales 2024')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True)
plt.tight_layout()

# LUPE tea (hot and iced)
plt.figure(figsize=(10,5.6))
plt.plot(lupe_sales.index, lupe_sales['Hot Tea'], label='Hot Tea', marker='o')
plt.plot(lupe_sales.index, lupe_sales['Iced Tea'], label='Iced Tea', marker='d')
plt.title('Lupe Tea Sales 2024')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True)
plt.tight_layout()

# LUPE Retail
plt.figure(figsize=(10,5.6))
plt.plot(lupe_sales.index, lupe_sales['Retail Coffee'], label='Retail Coffee', marker='o')
plt.title('Lupe Retail Coffee Sales')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True)
plt.tight_layout()

#------------------------------------------------------------------------------

# Plot Red sales by drink category
red_sales.set_index('Month', inplace=True)

# RED bar drinks
plt.figure(figsize=(10, 5.6))
plt.plot(red_sales.index, red_sales['Bar Drinks'], marker='o')
plt.title('Red Bar Drink Sales 2024')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.grid(True)
plt.tight_layout()

# RED brewed coffee (pillar, exceptional, iced)
plt.figure(figsize=(10,5.6))
plt.plot(red_sales.index, red_sales['Pillar Brewed'], label='Pillar Brewed', marker='o')
plt.plot(red_sales.index, red_sales['Exceptional Brewed'], label='Exceptional Brewed', marker='d')
plt.plot(red_sales. index, red_sales['Iced Coffee'], label='Iced Coffee', marker='^')
plt.title('Red Brewed Coffee Sales 2024')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True)
plt.tight_layout()

# RED tea (hot and iced)
plt.figure(figsize=(10,5.6))
plt.plot(red_sales.index, red_sales['Hot Tea'], label='Hot Tea', marker='o')
plt.plot(red_sales.index, red_sales['Iced Tea'], label='Iced Tea', marker='d')
plt.title('Red Tea Sales 2024')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True)
plt.tight_layout()

# RED BTC
plt.figure(figsize=(10,5.6))
plt.plot(red_sales.index, red_sales['BTC'], label='By the cup', marker='o')
plt.title('Red By the Cup Sales 2024')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True)
plt.tight_layout()

# RED Retail
plt.figure(figsize=(10,5.6))
plt.plot(red_sales.index, red_sales['Retail Coffee'], label='Retail Coffee', marker='o')
plt.title('Red Retail Coffee Sales')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True)
plt.tight_layout()


























