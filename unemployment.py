# -*- coding: utf-8 -*-
"""
@author: kripa
"""

import pandas as pd
#reading the data in python
emp = pd.read_csv('unemployment.csv', delimiter= ',',
                        skiprows=6,                     
                       na_values='NA', #null values
                       usecols= ['Fips', 'Location', 'TimeFrame', 'Data Type','Data', 'MOE']) # all the columns that we need from the dirty excel file                       
                       
emp.to_csv('new_unemployment.csv',  na_rep='null',index=False)