import pandas as pd
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
import seaborn as sns

# import data
data = pd.read_csv('data/original_data.csv', sep=';')
data.head()

data.shape #(546, 21)
data.dtypes 

data.isnull().sum() #there are no NAs

data['PSQI_component_1'].unique() #check the outcome

data['psqi_2_groups'].unique() #check the dichotomous outcome

#check correlations and distribution of the numeric variables with pairs graph:  
pair = sns.pairplot(data, vars=[ "MEQ", "Trait_Anxiety", "Avg_Weekly_Sleep_Duration",  "Avg_Sleep_Working_days", "Avg_sleep_free_days" , "Daytime_Dozing", "Age"  ])

#Check distribution of the main categorical variables:
categorical_features = ["University", "Sex", "Year_of_Study", "Department_Name", "Start_time", "Daytime_Dozing_Groups", "Cigarettes_dichotomous", "Alcohol_dichotomous", "Caffeine_dichotomous", "coffee_dichotomous", 'psqi_2_groups' ]
for col in data[categorical_features]:
    data[col].value_counts().sort_index(ascending=False).plot(kind="barh").set_title(col)
    plt.show()
