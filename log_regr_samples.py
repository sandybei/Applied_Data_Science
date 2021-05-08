import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score, StratifiedShuffleSplit
from sklearn.metrics import accuracy_score
from methods import *
from lasso_logistic_regression import lasso_sample

# import data
scaled_data = pd.read_csv('data/scaled_data.csv')

# create dataframe 
scaled_data_dfs = []
for key in methods:
    feature_subset = methods[key]
    scaled_data_dfs.append(scaled_data[feature_subset])    


# create logistic regression model
logisticRegr = LogisticRegression(penalty='none', random_state=0, max_iter=5000)
cv = StratifiedShuffleSplit(n_splits=10, random_state=0, test_size=0.2)

# generate sample using 10-fold cross validation
sample_results = []
y = scaled_data['psqi_2_groups']
for df in scaled_data_dfs: 
  X = df
  results = cross_val_score(logisticRegr, X, y, cv=cv)
  sample_results.append(results)

# create dataframe with samples scores
method_names = list(methods.keys())
samples = pd.DataFrame(columns=method_names)
for i, method in enumerate(method_names):
  samples[method] = sample_results[i]

# add sample for lasso logistic regression method to the samples dataframe
samples['lasso_logistic_regression'] = lasso_sample

# load samples to csv
samples.to_csv('data/samples.csv')
print(samples)
