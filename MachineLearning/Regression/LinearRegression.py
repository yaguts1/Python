# There are 2 types of regression models 

# Simple Regression (One independent variable is used to predict one dependent variable)
    # Can be either linear or non-linear 
        # ex: Predict co2 emission vs EngineSize of all cars



# Multiple Regression (More than one independent variable is used)
    #  Can be either linear or non-linear 
        # ex: Predicting co2 emission vs EngineSize and Cylinders of all cars

# Sample applications of regression
    # Sales forecasting
    # Satisfaction analysis 
    # Price estimation 
    # Predict Employment Income 
    # ...

# Regression algorithms:
    # Ordinal Regression ------------------------------------->
    # Poisson Regression-------------------------------------->
    # Fast forest quantile regression------------------------->
    # Linear, Polynomial, Lasso, Stepwise, Ridge Regression--->
    # Bayesian linear regression------------------------------>
    # Neural Network regression------------------------------->
    # Decision forest regression------------------------------>
    # Boosted decision tree regression------------------------>
    # KNN (k-nearest neighbors)------------------------------->

# Using Simple Linear Regression to predict continuous values (Not a discreet value)

# import pandas as pd
# from matplotlib import pyplot
# import numpy as np
# df = pd.read_csv('MachineLearning\Regression\CO2_emissions_canada.csv')

# # Trying to plot a line that connects the highest values of c02 emission for each number of cylinders
# df[['Cylinders','CO2 Emissions(g/km)']].to_numpy()
# three_cylinders = []
# four_cylinders = []
# five_cylinders = []
# six_cylinders = []
# eight_cylinders = []
# ten_cylinders = []
# twelve_cylinders = []
# sixteen_cylinders = []

# for item in df[['Cylinders','CO2 Emissions(g/km)']].to_numpy():
#     match item[0]:
#         case 3:
#             three_cylinders.append(item[1])
#         case 4:
#             four_cylinders.append(item[1])
#         case 5:
#             five_cylinders.append(item[1])
#         case 6:
#             six_cylinders.append(item[1])
#         case 8:
#             eight_cylinders.append(item[1])
#         case 10:
#             ten_cylinders.append(item[1])
#         case 12:
#             twelve_cylinders.append(item[1])
#         case 16:
#             sixteen_cylinders.append(item[1])

# max_emission = [
#     max(three_cylinders),
#     max(four_cylinders),
#     max(five_cylinders),
#     max(six_cylinders),
#     max(eight_cylinders),
#     max(ten_cylinders),
#     max(twelve_cylinders),
#     max(sixteen_cylinders)
# ]
# min_emission = [
#     min(three_cylinders),
#     min(four_cylinders),
#     min(five_cylinders),
#     min(six_cylinders),
#     min(eight_cylinders),
#     min(ten_cylinders),
#     min(twelve_cylinders),
#     min(sixteen_cylinders)
# ]
# mean_emission = [
#     sum(three_cylinders)/len(three_cylinders),
#     sum(four_cylinders)/len(four_cylinders),
#     sum(five_cylinders)/len(five_cylinders),
#     sum(six_cylinders)/len(six_cylinders),
#     sum(eight_cylinders)/len(eight_cylinders),
#     sum(ten_cylinders)/len(ten_cylinders),
#     sum(twelve_cylinders)/len(twelve_cylinders),
#     sum(sixteen_cylinders)/len(sixteen_cylinders)
# ]
# midrange_emission = [(min_emission[x] + max_emission[x])/2 for x in range(len(min_emission))]

# cylinders = df['Cylinders'].to_numpy()
# co2emissions = df['CO2 Emissions(g/km)'].to_numpy()

# xaxis = cylinders
# yaxis = co2emissions
# xaxis2 = sorted(np.unique(df['Cylinders'].to_numpy()))
# yaxis2 = max_emission
# yaxis3 = min_emission
# yaxis4 = midrange_emission
# yaxis5 = mean_emission
# pyplot.xticks(range(0,17))
# pyplot.yticks(range(0,700,50))
# pyplot.xlabel('Number of cylinders')
# pyplot.ylabel('CO2 Emissions(g/km)')
# pyplot.title('Cylinders vs CO2 emission')
# pyplot.scatter(xaxis,yaxis)
# pyplot.plot(xaxis2,yaxis2, 'r-.' ,label='maximum emission value')
# pyplot.plot(xaxis2,yaxis3, 'g-.', label= 'minimum emission value')
# pyplot.plot(xaxis2,yaxis4, 'y--', label='midrange emission value')
# pyplot.plot(xaxis2,yaxis5, 'black', label='mean emission value')
# pyplot.legend()
# pyplot.show()

# By observing the Graph it is pretty clear that there is a relation between number of cylinders and the emission of CO2. There is an upward trend.
    
# Using Simple Linear Regression to predict continuous values (Not a discreet value)

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

df = pd.read_csv('MachineLearning\Regression\FuelConsumptionCo2.csv')

# take a look at the dataset
print(df.head())
# summarize the data
print(df.describe())
# Select some features to explore more.
cdf = df[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
print(cdf)
print(cdf.head(9))
# Plotting each of these 
cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']].hist()
plt.show()
