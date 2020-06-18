import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

data = pd.read_csv('/Users/XXX/1.01. Simple linear regression.csv')
print(data.describe())

# define the dependent and independent variables
y = data['GPA']
x1 = data['SAT']

# explore the data
plt.scatter(x1,y)
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
# plt.show()

# regression itself
x = sm.add_constant(x1)
results = sm.OLS (y,x).fit()
print(results.summary())

plt.scatter(x1,y)
yhat = 0.275 + 0.0017 * x1
fig = plt.plot(x1,yhat,lw = 4, c='blue',label = 'regression line')
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()
