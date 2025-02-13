# -*- coding: utf-8 -*-
"""Rock Vs Mine Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X8BKXQ4JyMh2MjEvL4P5vgfZd3EwkNNB

# **IMPORT**
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""# **Data Loading**"""

data = pd.read_csv(
    '/content/drive/MyDrive/Datasets/sonar data.csv', header=None)

data.head()

data.shape

data.describe()

data[60].value_counts()
# M--Mine
# R--Rock

data.groupby(60).mean()

"""# **Data And Labels**"""

X = data.drop(columns=60, axis=1)
print(X)

Y = data[60]
print(Y)

"""# **Train Test Split**"""

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.1, stratify=Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

print(X_train)

print(Y_train)

"""# **Model Training**"""

model = LogisticRegression()

"""Model Training

"""

model.fit(X_train, Y_train)

"""# **Accuracy On Traning Data**"""

X_train_Prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_Prediction, Y_train)

print(training_data_accuracy)

"""# **Accuracy on test data**"""

X_test_Prediction = model.predict(X_test)
testining_data_accuracy = accuracy_score(X_test_Prediction, Y_test)
print(testining_data_accuracy)

"""# **Making A Predictive System**"""

input_data = (0.0283, 0.0599, 0.0656, 0.0229, 0.0839, 0.1673, 0.1154, 0.1098, 0.1370, 0.1767, 0.1995, 0.2869, 0.3275, 0.3769, 0.4169, 0.5036, 0.6180, 0.8025, 0.9333, 0.9399, 0.9275, 0.9450, 0.8328, 0.7773, 0.7007, 0.6154, 0.5810, 0.4454, 0.3707,
              0.2891, 0.2185, 0.1711, 0.3578, 0.3947, 0.2867, 0.2401, 0.3619, 0.3314, 0.3763, 0.4767, 0.4059, 0.3661, 0.2320, 0.1450, 0.1017, 0.1111, 0.0655, 0.0271, 0.0244, 0.0179, 0.0109, 0.0147, 0.0170, 0.0158, 0.0046, 0.0073, 0.0054, 0.0033, 0.0045, 0.0079)

"""**input data to np arry for faster**"""

input_data_np = np.asarray(input_data)

""" **reshape the np array as we are predicting for one instance**"""

input_data_reshaped = input_data_np.reshape(1, -1)

"""# **Prediction**"""

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction == 'R'):
    print('Rock')
else:
    print('Mine')
