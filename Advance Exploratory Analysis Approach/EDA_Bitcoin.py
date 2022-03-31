#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:46:25 2022

@author: emmanuel_bamidele
"""

import pandas as pd
path = "/Users/emmanuel_bamidele/Desktop/Bamspace/Data_Science_Tutorial/Books/Software for STEM Grad Students/Data/Bitcoin Historical Data - Investing.com-2015_to_2022.csv"

df = pd.read_csv(path)
print(df.head())