# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:40:15 2022

@author: jensh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json



#method1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

#transform to dataframe
loandata = pd.DataFrame(data)

#open, load and transform in one step
#data = pd.read_json('loan_data_json.json')

loandata.info()

#finding unique values for the purpase column
loandata['purpose'].unique()

#describe the data
loandata.describe()
#describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualIncome'] = income

#working with if statements
a = 40
b = 500

if b > a:
    print('b is greater than a')
    
#Let's add more conditions

a = 40
b = 500
c = 1000

if b > a and b < c:
    print('b is greater than a, but less than c')
    
#what if a condition is not met?

a = 40
b = 500
c = 20

if b > a and b < c:
    print('b is greater than a, but less than c')
else:
    print('No conditions met')
    
#another condition different metrics

a = 40
b = 500
c = 30

if b > a and b < c:
    print('b is greater than a, but less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('No conditions met')

#FICO Score

fico = 700

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    fico = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)

#For Loops

fruits = ['apple' , 'pear' , 'banana' , 'cherry']

for x in fruits:
    print(x)
    y = x+' fruit'
    print(y)

# ficocat = []
# for fico in loandata['fico']:
#     if fico >= 300 and fico < 400:
#         cat = 'Very Poor'
#     elif fico >= 400 and fico < 600:
#         cat  = 'Poor'
#     elif fico >= 601 and fico < 660:
#         cat  = 'Fair'
#     elif fico >= 660 and fico < 700:
#         cat  = 'Good'
#     elif fico >= 700:
#         cat  = 'Excellent'
#     else:
#         cat  = 'Unknown'
#     ficocat.append(cat)

# ficocat = pd.Series(ficocat)    

# loandata['ficocat'] = ficocat

ficocat = []
for x in range(0, len(loandata['fico'])):
    try:
        if loandata['fico'][x] >= 300 and loandata['fico'][x] < 400:
            cat = 'Very Poor'
        elif loandata['fico'][x] >= 400 and loandata['fico'][x] < 600:
            cat  = 'Poor'
        elif loandata['fico'][x] >= 601 and loandata['fico'][x] < 660:
            cat  = 'Fair'
        elif loandata['fico'][x] >= 660 and loandata['fico'][x] < 700:
            cat  = 'Good'
        elif loandata['fico'][x] >= 700:
            cat  = 'Excellent'
        else:
            cat  = 'Unknown'
    except:
        cat  = 'Unknown'
        
    ficocat.append(cat)

ficocat = pd.Series(ficocat)
    
loandata['ficocat'] = ficocat


#df.loc as conditional statements
#df.loc[df[columnname] condition, newColumnname] = 'value if the condition is met'

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans/rows by fico.category

catplot = loandata.groupby(['ficocat']).size()
catplot.plot.bar(color='green', width=0.1)
plt.show

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='red', width=0.2)
plt.show

#scatter plots

ypoint = loandata['annualIncome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index=True)

