import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# import data
scaled_data = pd.read_csv('data/scaled_data.csv')


# Split Data to Training and Test set
y = scaled_data['psqi_2_groups']
X = scaled_data.drop(['psqi_2_groups'], axis=1)
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.30, random_state=42)

# create model
logisticRegr = LogisticRegression(penalty='l1',  solver= 'saga', random_state=0, max_iter=10000)

# generate sample using 10-fold cross-validation
lasso_sample = cross_val_score(logisticRegr, X_train, y_train, cv=10)

# Feature Importance

# get model's parameters
logisticRegr.fit(X_train, y_train)
importances = logisticRegr.coef_[0]

# plot feautes' importance
feature_importance = pd.Series(data=importances, index=X_train.columns)
feature_importance = feature_importance.abs()
feature_importance = feature_importance.sort_values(axis=0, ascending=False)


# get bar plot for feature importances
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.barplot(x=feature_importance, y=feature_importance.index).set_title('Feature Importance')
plt.show()
