# import the relevant libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()
# load the data
data = pd.read_csv('/Users/XXX/real_estate_price_size.csv')

# print(data)
# print(data.describe())

# create the regression
# declare the dependent and the independent variables
y = data['price'] #depdent variables
x1 = data['size'] #indenpdent variables

# explore the data
plt.scatter(x1,y)
plt.ylabel('Price', fontsize = 15 )
plt.xlabel('Size', fontsize = 15)
# plt.show()

# regression itself
b = sm.add_constant(x1)
results = sm.OLS(y,b).fit()
print(results.summary())

# plot the regression line on the initial scatter
plt.scatter(x1,y)
plt.ylabel('Price', fontsize = 15 )
plt.xlabel('Size', fontsize = 15)
yhat = 101900 + 223.1787* x1
plt.plot(x1,yhat,lw =2, c='blue', label = 'regression line')
plt.show()
