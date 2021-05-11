# General Info
**Team members**:\
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
The data that have been used for this project can be found online [[2]](https://data.mendeley.com/datasets/cbpxxtfc95/1) and are uploaded as a csv file inside the **data** folder of the repo with the name
**original_data.csv**. 

# Usage
Follow the next steps to generate our resuls:
## 1. Data Exploration
Run the command:
```
python data_exploration.py
```
to view information about the dataset, correlations between the features and to visualize their distributions.


## 2. Data Pre-processing
Run the command:
```
python data_preprocessing.py
```
to generate 2 files:
* **processed_data.csv**: These are the original data after the removal of irrelevant features,
* **rescaled_data.csv**: These are the data from the abova file after they have been rescaled.

Both of these files can be found inside the **data** folder.

### 3. Feature Selection
Run the command: 
```
python feature_selection.py
```
to print the best feature subsets obtained from the feature selection methods.

### 4. Logistic Regression samples
Run the command: 
```
python lasso_logistic_regression.py
```
and then:
```
python lasso_logistic_regression.py
```
to generate the 5 samples with the accuracy of the Logistic Regression model for each one of the feature selection methods.

### 4. Statistical Comparison
Run the command: 
```
python statistical_comparison.py
```
to perform the different statistical tests.


# Reference
[1] 'Time to think: Subjective sleep quality, trait anxiety and university
start time.', Ray Norbury , Simon Evans. DOI: [https://doi.org/10.1016/j.psychres.2018.11.054](https://doi.org/10.1016/j.psychres.2018.11.054)\
[2] [https://data.mendeley.com/datasets/cbpxxtfc95/1](https://data.mendeley.com/datasets/cbpxxtfc95/1), DOI:10.17632/cbpxxtfc95.1
