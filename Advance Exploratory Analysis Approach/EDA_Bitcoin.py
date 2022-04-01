#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:46:25 2022

@author: emmanuel_bamidele
"""

import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
#import Seaborn as sns

plt.rcParams.update({'font.size': 22})

path = "/Users/emmanuel_bamidele/Desktop/Bamspace/Data_Science_Tutorial/Books/Software for STEM Grad Students/Data/Bitcoin Historical Data - Investing.com-2015_to_2022.csv"

df = pd.read_csv(path)
#print(df.head())
# print('\n')

# Get the number of rows and columns in the dataframe.

# print(df.shape)
# print('\n')

# Get the data type of the entire dataframe

# print(df.dtypes)
# print('\n')
# print(pd.value_counts(df.dtypes))

# print('\n')

# Change some of the columns to Float

cols = ['Price', 'Open', 'High', 'Low']
for col in cols:
    df[col] = [float(str(i).replace(",", "")) for i in df[col]]
    
# print(df.dtypes)
# print('\n')
# print(df.head())
# print('\n')

# Change the date items to datetime datatype

df['Date'] = df['Date'].astype('datetime64[ns]')
    
# print(df.dtypes)
# print('\n')
# print(df.head())
# print('\n')

# Remove the % symbol from the last column and change the datatype to float 

df["Change %"] = df["Change %"].str.replace("%","")
df["Change %"] = df["Change %"].astype(float)

# print(df.head())
# print('\n')
# print(df.dtypes)
# print('\n')

# Get summary and statistical description of the dataframe

#print(df.info())
# print('\n')
# print(df.describe())

#Histogram distribution of a specific column

df.hist(column=["Change %"])
plt.title("Percentage Change Distribution")
plt.xlabel("% Change")
plt.ylabel("Count")


#Check for missing Values in a single column

# print(df['Price'].isnull().values.any())
# print(df['Price'].isnull().sum())

#Check for missing Values in the entire dataframe

#print(df.isnull().values.any())
#print(df.isnull().sum())
#print(df.isnull().sum().sum())

#Deleting missing values in our dataframe
df = df.dropna()
# print(df.head())

#Replacing missing values
df = df.fillna(0) #with zero
#print(df.head())


# df['Price'] = df['Price'].fillna(df.mean()) #with mean in Price column
# df['High'] = df['High'].fillna(df['High'].median()) #with median in High column
# df['Low'] = df['Low'].fillna(df['Low'].min()) #with minimum value in the Low column

#print(df.head())

df ['Adjusted Price'] = np.where(df['Price'] >= 42300.00, True, False)
# print(df.head())

#Show missing value in a box per sample

plt.figure(figsize=(8, 6))
plt.imshow(df.isna(), aspect="auto", interpolation="nearest", cmap="gray")
plt.xlabel("Col Number")
plt.ylabel("Sample Number")

#show missing values per feature

# import missingno as msno
# msno.matrix(df, labels=True, sort="descending");

# Get an overview of the data

df.plot(lw=0, marker="*", subplots=True, layout=(-1, 3), figsize=(30, 15), markersize=1);

#All distributions of feautures

df.hist(bins=25, figsize=(30,15), layout=(-1,3), edgecolor="black")
plt.tight_layout()

# Preview specific features 

# df[["Date", "Price","High","Low", "Open", "Change %"]].plot(
#   lw=0, marker=".", subplots=True, layout=(-1, 3),
#   markersize=1, figsize=(30, 15));

# #View Trends in Discrete features

# df_discrete = df[["Price", "Open", "High", "Low", "Change %"]]
# print(df_discrete.shape)

# n_cols = 5
# n_elements = len(df_discrete.columns)
# n_rows = np.ceil(n_elements/n_cols).astype("int")

# interested_col = df_discrete["Change %"]
# fig, axes = plt.subplots(ncols=n_cols, nrows=n_rows, figsize=(30,n_rows*2.5))

# for col, ax in zip(df_discrete.columns, axes.ravel()):
#     sns.stripplot(data=df, x=col, y=interested_col, ax=ax, paletter="tab10", size=1, alpha=0.5)
#     plt.tight_layout();

# Variation in Price 

df.index = df['Date']
df.plot(x="Date", y="Price", lw=1, marker="*", figsize=(10, 8), markersize=1);
df.plot(x="Date", y="Change %", lw=1, marker="*", figsize=(10, 8), markersize=1);

# Change Statistics

#print(df["Change %"].describe())

#Trend Analysis 

def trend(x):
  if x > -0.5 and x <= 0.5:
    return "Slight or No change"
  elif x > 0.5 and x <= 3:
    return "Slight Positive"
  elif x > -3 and x <= -0.5:
    return "Slight Negative"
  elif x > 1 and x <= 10:
    return "Positive"
  elif x > -10 and x <= -1:
    return "Negative"
  elif x > 10 and x <= 20:
    return "High Gain"
  elif x > -20 and x <= -10:
    return "High Loss"
  elif x > 20:
    return "Bull run"
  elif x <= -20:
    return "Bear drop"

df["Trend"]= np.zeros(df["Change %"].count())
df["Trend"]= df["Change %"].apply(lambda x:trend(x))
# print(df.head())

#Visualize trend in pire chart

df_pie_data = df.groupby('Trend')
pie_label = sorted([i for i in df.loc[:, 'Trend'].unique()])
plt.pie(df_pie_data['Trend'].count(), labels=pie_label, labeldistance=None, shadow=True, autopct="%1.1f%%", radius=3, pctdistance=0.6)
plt.legend(loc="best")