# Sentiment analysis and SVR

import csv
import matplotlib.pyplot as plt
# Market analysis
import numpy as np
from sklearn.svm import SVR
# NLP
import tweepy
from textblob import TextBlob

# Setting graphical backend for plotting
plt.switch_backend('Qt5Agg')

# Lists to be filled with CSV data
dates = []
prices = []

# Writing CSV data to lists
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader) # Ignoring first row
        for row in csvFileReader:
            dates.append((int(row[0].split('-')[1]) - 1) * 31 + int(row[0].split('-')[2])) # Jan and Feb
            prices.append(float(row[1]))
    return

# SVR
def predict_prices(dates, prices, x):
    # Converting array to N-by-1 matrix
    dates = np.reshape(dates, (len(dates), 1))
    
    # Creating 3 SVR models
    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma='auto')
    
    # Training them
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)
    
    # Plotting the results
    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()
    
    # Returning the predicted price for given day
    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]
    
    
get_data("GOOG.csv")
print(predict_prices(dates, prices, np.array(35).reshape(1,-1)))
