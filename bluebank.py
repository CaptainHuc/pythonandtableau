# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:40:15 2022

@author: jensh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json



#json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#transform to dataframe
loandata = pd.DataFrame(data)

loandata.info()

loandata.describe()

#finding unique values for the purpase column
loandata['purpose'].unique()


#get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualIncome'] = income

#FICO Score
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

