# Applied_Data_Science
Team members:
Tamara Rigo -  tamara.rigo@studenti.unitn.it\
Theodoros Efthymiadis - efthimiadisthodoris@gmail.com\
Kyriaki Bei - sandybei058@gmail.com

# Installation

1. Clone the repo:
```
git clone https://github.com/sandybei/Applied_Data_Science.git
```
2. Install the required packages using the following commands:

```
pip install pandas 
pip install numpy
pip install matplotlib
pip install seaborn
pip install sklearn
pip install mlxtend
pip install scipy
pip install statsmodels
```
# Data
The data that have been used for this project is the 'original_data.csv' file that can be found inside the 'data' folder of the repo. 

# Usage
Follow the next steps to generate our resuls:
# 1. Data Exploration
Run the command:
```
python data_exploration.py
```

# 2. Data Pre-processing
Run the command:
```
python data_preprocessing.py
```
to generate 2 files:
* 'processed_data.csv': These are the original data after the removal of irrelevant features,
* 'rescaled_data.csv': This are the data from the abova file after they have been rescaled.

# 3. Feature Selection
Run the command: 
```
python feature_selection.py
```
to print the best feature subsets obtained from the feature selection methods.

# 4. Logistic Regression samples
Run the command: 
```
python lasso_logistic_regression.py
```
and then:
```
python lasso_logistic_regression.py
```
to generate the 5 samples with the accuracy of the Logistic Regression model for each one of the feature selection methods.

# 4. Logistic Regression samples
Run the command: 
```
python statistical_comparison.py
```
to perform the statistical tests.


# Reference
[1] 'Time to think: Subjective sleep quality, trait anxiety and university
start time.', Ray Norbury , Simon Evans. DOI: [https://doi.org/10.1016/j.psychres.2018.11.054](https://doi.org/10.1016/j.psychres.2018.11.054)

