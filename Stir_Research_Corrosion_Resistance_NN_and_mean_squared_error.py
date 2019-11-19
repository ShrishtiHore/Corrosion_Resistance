# -*- coding: utf-8 -*-
"""
Created on Mon Sept 30 09:08:22 2019

@author: Shrishti D Hore
"""

#import all imp libraries 
from numpy import loadtxt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler
import sklearn.model_selection as model_selection
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import os 
import csv
import time


'''
#just to see what is in the data set 
import csv
with open('corrosion_final_data.csv','rt')as file:
    data = csv.reader(file)
    for row in data:
        print(row)
'''

#Input variables are N,S,F and output variable corrosion_pit_otential/mv 
#load the dataset 
dataset = pd.read_csv('C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\corrosion_final_data.csv',delimiter = ',')

'''
print(dataset.iloc[:, :-1])
print(dataset.iloc[:, -1])
'''
#Split datasets in input values(x) and output values(y)
#data pre-processing for regression
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

#standardize dataset and reshape the dataset
X = StandardScaler().fit_transform(X)
Y = StandardScaler().fit_transform(Y.reshape(len(Y),1))[:, 0]

#split into train and test
trainX, testX, trainY, testY = model_selection.train_test_split(X, Y, train_size = 0.75, test_size = 0.25)

#Nh=Ns/(α∗(Ni+No))
#ie; 30/(2(3+1)) = 3.75 approx 4
#the first hidden layer has 4 nodes and uses relu
#the second hidden layer has 3 nodes and uses relu activation function
#the output layer had one node and uses sigmoid activation function 
#setting input layer with right no. of input features by setting it to 3 for 3 input features
model = Sequential()
model.add(Dense(4, input_dim=3, activation = 'relu', kernel_initializer= 'he_uniform'))
model.add(Dense(3, activation='relu'))
model.add(Dense(1, activation = 'sigmoid'))

#model will be fit with stochastic gradient descent with a learning rate of 0.01 and momentum of 0.9
opt = SGD(lr = 0.01, momentum=0.9)
model.compile(loss='mean_squared_error', optimizer='adam', metrics =['mean_squared_error'])

#training will be performed for 100 epochs and test set will be evaluated at the end of each epoch 
history = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=100, batch_size =10)

'''
print(trainX)
print(trainY)
print(testX)
print(testY)
'''

#evaluating the model 
# training and testing for mean squared error
train_mse = model.evaluate(trainX, trainY)
test_mse = model.evaluate(testX, testY)

#plot loss during training
plt.title('Loss ')
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()

#plot mean squared error during training
plt.title('Mean Squared Error ')
plt.plot(history.history['mean_squared_error'], label='train')
plt.plot(history.history['val_mean_squared_error'], label='test')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()
