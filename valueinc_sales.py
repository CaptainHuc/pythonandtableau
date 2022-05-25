# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

data = pd.read_csv('transaction.csv', sep=';')

# summary of the data
data.info() 

#Cost per Transaction = Cost per Item * Number of Items Purchased
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales per Transaction = Selling Price per Item * Number of Items Purchased
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit = Sales - Cost 
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = Sales - Cost / Cost
data['Markup'] = round(( data['SalesPerTransaction'] - data['CostPerTransaction'] ) / data['CostPerTransaction'], 2)

#Combining Data fields
data['Date'] = data['Day'].astype(str) + '-' + data['Month'] + '-' + data['Year'].astype(str)

#Splitting Client Keywords and creating new Columns
split_col = data['ClientKeywords'].str.split(',' , expand = True)

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

data['ItemDescription'] = data['ItemDescription'].str.lower()

#merging files
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

data = pd.merge(data, seasons, on = 'Month')

data = data.drop('ClientKeywords' , axis = 1)
data = data.drop(['Year','Month', 'Day'] , axis = 1)

#export
data.to_csv('ValueInc_Cleaned.csv', index = False)
