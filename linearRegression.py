#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:41:07 2020

@author: aminghazanfari
"""

#Supervised learning example: Simple linear regression by using Scikit-learn
import matplotlib.pyplot as plt
import numpy as np

#First we genrate some random data to work with
rng = np.random.RandomState(42)
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)
plt.scatter(x, y);

#Import the linear regression model from Scikit-Learn
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)

#make the data to the siz e [n_samples,n_features]
X = x[:,np.newaxis]
X.shape

#Apply the model to the data using fit()
model.fit(X,y)

print(model.coef_)
print(model.intercept_)

#we have a trained model, we can use to predict 

xfit = np.linspace(-1, 11)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)

#plot the result
plt.scatter(x, y)
plt.plot(xfit, yfit);
