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

# import data
data = pd.read_csv('data/Time_to_think_Norbury.csv', sep=';')

# drop irrelevant features
data.drop(['Case_Number', 'PSQI_component_1', 'Daytime_Dozing', 'Start_time'], axis=1, inplace=True)
data.to_csv('data/data.csv')

# load data to csv
data = pd.read_csv('data/sleep_data.csv')


# one_hot encoding for non-dichotomous categorical features
one_hot_features = ['University', 'Department_Name', 'Start_time_code', 'Daytime_Dozing_Groups']
one_hot = pd.get_dummies(data, columns = one_hot_features, prefix=one_hot_features)

# min-max normalisation of dichotomous categorical and numerical features
scaler = MinMaxScaler()
features = ['Sex', 'Avg_Weekly_Sleep_Duration', 'Avg_Sleep_Working_days', 'Avg_sleep_free_days', 'Cigarettes_dichotomous', 'Alcohol_dichotomous', 'Caffeine_dichotomous', 'coffee_dichotomous']
one_hot[features] =scaler.fit_transform(one_hot[features])
scaled_data = one_hot

# load data to csv
scaled_data.to_csv('data/scaled_data.csv')