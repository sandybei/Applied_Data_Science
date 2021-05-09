import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro
from scipy.stats import bartlett
from scipy.stats import levene
from scipy.stats import f_oneway
from scipy.stats import kruskal
from scipy.stats import wilcoxon
from statsmodels.stats.multicomp import pairwise_tukeyhsd


# This is a custom function that performs pairwise comparison of samples with the Wilcoxon test
# The function uses as input a data frame with the accuracy values of the methods and a data frame that indicates the
# different group combinations that should be compared in a pairwise manner
def pairwise_wilcoxon(samples_df, groups_df):
    a_wilc = 0.05
    for index in groups_df.index:
        group_1 = groups_df.at[index, 'group1']
        group_2 = groups_df.at[index, 'group2']
        stat_wilc, p_wilc = wilcoxon(samples_df[group_1], samples_df[group_2])
        groups_df.at[index, 'p-value'] = p_wilc
        if p_wilc < a_wilc:
            groups_df.at[index, 'Ho rejected'] = 'TRUE'
    return groups_df


# Import the data
# samples = pd.read_csv("C:\\Users\\Ires\\Desktop\\samples.csv", index_col=0)
samples = pd.read_csv('data\\samples.csv', index_col=0)
print(samples)

# Perform the Shapiro-Wilk test to check Normality using the accuracy values from each method individually
a_Shapiro = 0.05    # The significance level of the Shapiro - Wilk test
normality_counter = 0    # This counts the number of features of the data set that do satisfy the normality assumption
for column in samples.columns:
    stat_Shapiro, p_Shapiro = shapiro(samples[column])
    if p_Shapiro > a_Shapiro:
        normality_counter = normality_counter + 1
    print(column)
    print('Shapiro Results: Statistics=%.3f, p=%.3f' % (stat_Shapiro, p_Shapiro))
    print('-----------------------------------------------------------------------')


# Print the interpretation of the Shapiro-Wilk test and decide on the preferred test for homoscedasticity
if normality_counter == len(samples.columns):   # This condition checks if ALL features satisfy the normality assumption
    print('All individual samples have been sampled from a normal distribution. The homoscedasticity will be evaluated'
          ' using the Bartlett test')
else:
    print("At least one sample has not been sampled from a normal distribution. The homoscedasticity will be evaluated"
          " using the Levene's test")


# Check for homoscedacity using either the Bartlet test or Levene's test
homoscedasticity = 0   # This is a dummy counter to check for the homoscedasticity condition in line 71
if normality_counter == len(samples.columns):   # If normality is satisfied, the Bartlet test is used
    # Perform Bartlett test to check homoscedasticity
    a_Bart = 0.05  # Significance level for the Bartlett test
    stat_Bart, p_Bart = bartlett(samples['stepwise_selection'], samples['random_forest'], samples['chi_square'],
                                 samples['logreg_coefficiants'], samples['lasso_logistic_regression'])
    print('Bartlett test results: Statistics=%.3f, p=%.3f' % (stat_Bart, p_Bart))

    # Print the interpretation of the Bartlett test
    if p_Bart > a_Bart:
        homoscedasticity = 1
        print('There is evidence of homoscedasticity among the different samples. The samples will be compared using'
              ' ANOVA')
    else:
        print(
            'There is no homoscedasticity among the different samples. The samples will be compared using the Kruskal'
            ' - Wallis test')

else:   # In this case, normality is not satisfied and the Levene's test is used to check homoscedasticity
    # Perform Levene's test to check homoscedasticity
    a_Levene = 0.05  # Significance level for the Levene's test
    stat_Levene, p_Levene = bartlett(samples['stepwise_selection'], samples['random_forest'], samples['chi_square'],
                                     samples['logreg_coefficiants'], samples['lasso_logistic_regression'])
    print("Levene's test results: Statistics=%.3f, p=%.3f" % (stat_Levene, p_Levene))

    # Print the interpretation of the Levene's test
    if p_Levene > a_Levene:
        print('There is evidence of homoscedasticity among the different samples. The samples will be compared using '
              'the Kruskal - Wallis test')
    else:
        print('There is no homoscedasticity among the different samples. The samples will be compared using the Kruskal'
              ' - Wallis test')


# Perform the comparison of the samples using either ANOVA or Kruskal - Wallis test
if ( (normality_counter == len(samples.columns)) & (homoscedasticity == 1) ):  # Normality and homoscedasticity => ANOVA
    a_ANOVA = 0.05   # The significance of the ANOVA test
    stat_ANOVA, p_ANOVA = f_oneway(samples['stepwise_selection'], samples['random_forest'], samples['chi_square'],
                                   samples['logreg_coefficiants'], samples['lasso_logistic_regression'])
    print('ANOVA: Statistics=%.3f, p=%.3f' % (stat_ANOVA, p_ANOVA))

    if p_ANOVA < a_ANOVA:   # This condition holds when the ANOVA null hypothesis is rejected
        print(
            "The difference between the groups is statistically significant. Pairwise comparison will be performed with"
            "the usage of Tukey's test")

        # Performing the Tukey post-hoc test. Some data preprocessing is required
        a_Tukey = 0.05   # The significance of the Tukey test

        # Concatenate all accuracy values in a single list to feed to the Tukey test function
        numbers = []
        for column in samples.columns:
            numbers = numbers + samples[column].tolist()

        # Create the groups list to be used in as input for the Tukey function
        groups = []
        for column in samples.columns:
            for i in range(len(samples[column])):
                groups.append(column)

        tukey = pairwise_tukeyhsd(endog=numbers,  # Data
                                  groups=groups,  # Groups
                                  alpha=a_Tukey)  # Significance level

        print('Results of the Tukey test:')
        print(tukey.summary())     # See test summary
        tukey.plot_simultaneous()  # Plot group confidence intervals
        plt.show()
    else:   # In this case, the ANOVA null hypothesis cannot be rejected
        print("The ANOVA null hypothesis cannot be rejected. Thus, the difference between the groups is not "
              "statistically significant")
else:
    # Perform the Kruskal - Wallis test
    a_Kruskal = 0.05  # The significance of the Kruskal - Wallis test
    stat_Kruskal, p_Kruskal = kruskal(samples['stepwise_selection'], samples['random_forest'], samples['chi_square'],
                                      samples['logreg_coefficiants'], samples['lasso_logistic_regression'])
    print('Kruskal-Wallis test results: Statistics=%.3f, p=%.3f' % (stat_Kruskal, p_Kruskal))

    if p_Kruskal < a_Kruskal:   # This condition holds when the Kruskal null hypothesis is rejected
        print(
            "The difference between the groups is statistically significant. Pairwise comparison will be performed with"
            "the usage of Wilcoxon test")

        # The pairwise Wilcoxon test will be conducted here. Some preprocessing is necessary
        group1 = ['chi_square', 'chi_square', 'chi_square', 'chi_square', 'lasso_logistic_regression',
                  'lasso_logistic_regression', 'lasso_logistic_regression', 'logreg_coefficiants',
                  'logreg_coefficiants',
                  'random_forest']
        group2 = ['lasso_logistic_regression', 'logreg_coefficiants', 'random_forest', 'stepwise_selection',
                  'logreg_coefficiants', 'random_forest', 'stepwise_selection', 'random_forest', 'stepwise_selection',
                  'stepwise_selection']

        groups = pd.DataFrame({'group1': group1, 'group2': group2, 'p-value': ['-' for i in range(10)], 'Ho rejected':
                              ['FALSE' for i in range(10)]})

        # Doing the test and printing results
        wilc_results = pairwise_wilcoxon(samples, groups)   # Data frame with the results using the custom function
        print('Results of the Pairwise Wilcoxon test:')
        print(wilc_results)

    else:    # In this case, there was no significant difference between the samples
        print("The Kruskal - Wallis null hypothesis cannot be rejected. Thus, the difference between the groups is not "
              "statistically significant")