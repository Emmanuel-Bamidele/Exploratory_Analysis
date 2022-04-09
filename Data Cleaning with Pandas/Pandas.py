#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 15:05:20 2022

@author: emmanuel_bamidele
"""
#download pandas using pip install pandas in your terminal or !pip install pandas in notebook
import pandas as pd

#Specify the path of your data
path_url = "/Users/emmanuel_bamidele/Desktop/Bamspace/Data_Science_Tutorial/EDA/Pandas/commodity 2000-2022.csv"

#import data, in this case csv
df = pd.read_csv(path_url, encoding='utf-8')

#view the first five lines of the data
print(df.head())
print("\n")

#view the last five lines of the data
print(df.tail())
print("\n")

#view the top five rows of a particular column
print(df.head(5).Close)
print("\n")

#view all the headers
print(df.columns)
print("\n")

#view a particular number of rows of a column
print(df.Symbol[1000:1010])
print("\n")

#view just specific columns
print(df[['Date', 'Symbol', 'Open', 'Close']])
print("\n")

#get rows (row 10 to 15)
print(df.iloc[10:15])
print("\n")


#Check for missing value in the dataset
print("\n")
print("Obtain the number of missing values per column")
print(df.isnull().sum())

# Get the structure of the data
print("\n")
print("The dataset shape is: ", df.shape) #shape of our data
print(df.dtypes) #get data type of each column
print("\n")
print(pd.value_counts(df.dtypes)) #get how many times each data type features

#Convert the date column to datetime type
df['Date'] = df['Date'].astype('datetime64[ns]')
#df.index = df['Date'] #make date the index

print("\n")
print(df.head())
print("\n")
print(df.dtypes) #get data type of each column

#Get a statistical summary of the data
print(df.describe())
print("\n")

#Get an overview  of the data
print(df.info())
print("\n")


#Group data and assign 

#get the number of unique entry in a column
print("\n")
print("The unique features in the Symbol column are: ")
print(df.Symbol.unique())

#assign all keywords with gold to df_gold and read only columns with gold (top five)
df_gold = df.loc[df['Symbol'] == 'Gold']
print("\n")
print("The number of gold data is: ", df_gold.shape)
print("\n")
print(df_gold.head())

#assign all keywords with palladium to df_palladium and read only columns with palladium (top five)
df_palladium = df.loc[df['Symbol'] == 'Palladium']
print("\n")
print("The number of palladium data is: ", df_palladium.shape)
print("\n")
print(df_palladium.head())

#assign all keywords with nickel to df_nickel and read only columns with nickel (top five)
df_nickel = df.loc[df['Symbol'] == 'Nickel']
print("\n")
print("The number of nickel data is: ", df_nickel.shape)
print("\n")
print(df_nickel.head())


#assign all keywords with brent oil to df_brentoil and read only columns with brent oil (top five)
df_brentoil = df.loc[df['Symbol'] == 'Brent Oil']
print("\n")
print("The number of brent oil data is: ", df_brentoil.shape)
print("\n")
print(df_brentoil.head())

#assign all keywords with natural gas to df_brentoil and read only columns with natural gas (top five)
df_natural_gas = df.loc[df['Symbol'] == 'Natural Gas']
print("\n")
print("The number of natural gas data is: ", df_natural_gas.shape)
print("\n")
print(df_natural_gas.head())

#assign all keywords with gold to df_gold and read only columns with gold (top five)
df_wheat = df.loc[df['Symbol'] == 'Wheat']
print("\n")
print("The number of wheat data is: ", df_wheat.shape)
print("\n")
print(df_wheat.head())


#Another method to group data  by unique items in a column (groupby)
df_group = df.groupby('Symbol')
print("\n")
print("The first entry of each group in the Symbol column are: ")
print(df_group.first()) #get first entry of each group

#Obtain a particular group
df_gold2 = df_group.get_group('Gold')
print("\n")
print("The number of gold data is: ", df_gold2.shape)
print("\n")
print("The gold group are: ")
print(df_gold2.head())

#Group by two different columns
df_group2 = df.groupby(['Date', 'Symbol'])
print("\n")
print("The first entry of each group in the Symbol column by date are: ")
print(df_group2.first()) #get first entry of each group

#Sorting Data by Column
#recreate the data as df2 to test this
df2 = df
df2_sorted = df2.sort_values('Symbol') #sort thee symbol column
print(df2_sorted.head())
print("\n")
print(df2_sorted.tail())

#Sort two diffeerent columns
df2_sorted = df2_sorted.sort_values(['Symbol', 'Low'], ascending = True) #sort thee symbol & low columns in ascending order
print("\n")
print(df2_sorted.head())
print("\n")
print(df2_sorted.tail())

df2_sorted = df2_sorted.sort_values(['Symbol', 'Low'], ascending = False) #sort thee symbol & low columns in descending order
print("\n")
print(df2_sorted.head())
print("\n")
print(df2_sorted.tail())

#Sort columns differently
df2_sorted = df2_sorted.sort_values(['Symbol', 'Low'], ascending = [1,0]) #sort thee symbol & low columns in ascending & descending orders respectively
print("\n")
print(df2_sorted.head())
print("\n")
print(df2_sorted.tail())

#Making changes to Data
#Add a Column to a dataframe
df['Change%'] = df['Close'].pct_change()
print("\n")
print(df.head())

#Find and replace missing values
print("\n")
print(df.isnull().sum())
df['Change%'].fillna(value=df['Change%'].mean(), inplace=True) #replace missing value with column mean in Price column
print("\n")
print(df.head())

#drop a column
df2 = df2.drop(columns=['Close'])
print("\n")
print(df2.head())

#Filtering Data
#Locate all data having gold in the symbol column
df_gold3 = df.loc[df['Symbol'] == 'Gold']
print("\n")
print(df_gold3.head())

#Locate data with two different word in a column
df_gold_nickel = df.loc[(df['Symbol'] == 'Gold') | (df['Symbol'] == 'Nickel')]
print("\n")
print("The number of data with either gold or nickel is: ", df_gold_nickel.shape)
print("\n")
print(df_gold_nickel.head())

#Resetting index after making changes and get rid of old index
df_gold_nickel = df_gold_nickel.reset_index(drop=True)
print("\n")
print("This will show an index column with the renumbered index without old index")
print("\n")
print(df_gold_nickel.tail())

#Leave old index
df_gold_nickel2 = df_gold_nickel.reset_index(drop=False)
print("\n")
print("This will show an index column with the renumbered index and old index")
print("\n")
print(df_gold_nickel2.tail())

#Set new index
df_gold_nickel.index = df_gold_nickel.index
print("\n")
print("This will set the index column to index")
print("\n")
print(df_gold_nickel.tail())

#Show rows with certain strings
print("\n")
print(df.loc[df['Symbol'].str.contains('Go')][0:5])

#Remove rows with certain string
print("\n")
print(df.loc[~df['Symbol'].str.contains('Go')][0:5])

#Saving Data to different format
df_gold.to_csv('gold_price.csv', index=False)
df_wheat.to_csv('wheat.txt', index=False)
df_natural_gas.to_html('natural_gas.html', index=False)
df_nickel.to_json('nickel.json')

