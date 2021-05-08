# creates a dictionary with the selected feature subsets
# of each feature selection method

stepwise_selection=['Trait_Anxiety',
 'Avg_Sleep_Working_days',
 'Department_Name_Business School',
 'Department_Name_Dance',
 'Department_Name_Drama',
 'Department_Name_English and Cre',
 'Department_Name_Media, Culture',
 'Department_Name_Other',
 'Start_time_code_4',
 'Start_time_code_11',
 'Daytime_Dozing_Groups_2',
 'Daytime_Dozing_Groups_4']


random_forest= [
"Age",
"Year_of_Study",
"MEQ",
"Trait_Anxiety",
"Avg_Weekly_Sleep_Duration",
"Avg_Sleep_Working_days",
"Avg_sleep_free_days",
"Alcohol_dichotomous",
"University_2",
"Daytime_Dozing_Groups_2" ]

chi_square= ['Year_of_Study', 'MEQ', 'Trait_Anxiety', 'University_2', 'Start_time_code_8']

log_reg = [ 
 'Age',
 'Year_of_Study',
 'MEQ',
 'Trait_Anxiety',
 'Avg_Weekly_Sleep_Duration',
 'Avg_sleep_free_days',
 'coffee_dichotomous',
 'University_2',
 'Department_Name_Business School',
 'Department_Name_Dance',
 'Department_Name_English and Cre',
 'Department_Name_Life Sciences',
 'Department_Name_Media, Culture',
 'Department_Name_Other',
 'Department_Name_Psychology',
 'Start_time_code_3',
 'Start_time_code_4',
 'Start_time_code_5',
 'Start_time_code_6',
 'Start_time_code_9',
 'Daytime_Dozing_Groups_1',
 'Daytime_Dozing_Groups_3',
 'Daytime_Dozing_Groups_5']

methods = {'stepwise_selection': stepwise_selection, 
           'random_forest': random_forest, 
           'chi_square': chi_square,
           'logreg_coefficiants': log_reg}  

