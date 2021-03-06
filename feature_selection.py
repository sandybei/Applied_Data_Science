import pandas as pd
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score as acc
from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import SequentialFeatureSelector as sfs
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel, VarianceThreshold
from sklearn.feature_selection import SelectKBest, mutual_info_classif, chi2
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
import statsmodels.api as sm
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import statsmodels.api as sm


# import data
scaled_data = pd.read_csv('data/scaled_data.csv')

# Split Data to Training and Test set
y = scaled_data['psqi_2_groups']
X = scaled_data.drop(['psqi_2_groups'], axis=1)
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.30, random_state=42)

#STEPWISE SELECTION 
log_reg = LogisticRegression(max_iter=1000, random_state=0).fit(X_train, y_train)  #LR for stepwise
step = sfs(log_reg,
           k_features=X_train.shape[1],
           forward=True,
           floating=False,
           verbose=2,
           scoring='accuracy',
           cv=10)

step = step.fit(X_train, y_train)

fig = plot_sfs(step.get_metric_dict(), kind='std_err')
plt.title('Sequential Forward Selection') #12 = best number of features
plt.grid()
plt.show()
feat_step=list(step.subsets_[12]['feature_names'])
feat_step

#CHI SQUARE
chi_scores = chi2(X_train,y_train)
p_values = pd.Series(chi_scores[1],index = X_train.columns)
feat_square=[]
for i, v in p_values.iteritems():
    if v<0.05:
        feat_square.append(i)
feat_square

#RANDOM FOREST 

forest = RandomForestClassifier(n_estimators = 100, random_state=0).fit(X_train, y_train)
importance = forest.feature_importances_
# plot feature importance
pyplot.bar([x for x in range(len(importance))], importance) 
pyplot.show()#use 0.02 as threshold 
feat_forest=[]
for i,v in enumerate(importance):
    if v>0.02:
        print('Feature: %0d, Score: %.5f' % (i,v)) #most important features
        feat_forest.append(i)
data_forest=X_train.iloc[:,feat_forest]
for col in data_forest.columns:
    print(col)

#LOGISTIC REGRESSION COEFFICIANTS
result=pd.DataFrame(zip(X_train.columns, np.transpose(log_reg.coef_.tolist()[0])), columns=['features', "pvalue"])
feat_log=list(result["features"][result['pvalue']<=0.05])
feat_log
