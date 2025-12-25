# import necessary modules and data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from risk_evaluation import amount_true, amount_false, amount_tie
from using_25 import highest_25_trials, final_25_trials
from using_33 import highest_33_trials, final_33_trials
from using_50 import highest_50_trials, final_50_trials

# Converting data of whether taking risk would result in better, worse, or same result to DataFrame Object
df_risk = pd.DataFrame({"Type" : ["Better", "Worse", "Same"], "Count" : [amount_true, amount_false, amount_tie]},
                       index = [0, 1, 2])
# Graphing the DataFrame object "df_risk"
df_risk.plot(kind = "bar", x = "Type", y = ["Count"])
plt.show()
# Converting data of the highest value in the "forfeit pile" for standards 25%, 33%, and 50% after 100 trials
# in DataFrame object "df_highest_different_standards"
df_highest_different_standards = pd.DataFrame({"25%" : highest_25_trials, "33%" : highest_33_trials,
                                               "50%" : highest_50_trials}, index = ["trial" + str(i) for i in range(1,101)])
# Taking the mean of data in DataFrame "df_highest_different_standards" and storing the averages in a new DataFrame
df_average_highest_different_standards = pd.DataFrame({"Percentage" : ["25%", "33%", "50%"], "Value" : [
df_highest_different_standards["25%"].mean(), df_highest_different_standards["33%"].mean(),
    df_highest_different_standards["50%"].mean()
]})
# Graphing the DataFrame object "df_average_highest_different_standards"
df_average_highest_different_standards.plot(kind = "bar", x = "Percentage", y = ["Value"])
plt.show()
# Converting data that used the highest value in the "forfeit pile" to select the best individual that has a higher value
# (if any) than the highest value in the "forfeit pile" in the remaining population and return that value if exists
df_final_different_standards = pd.DataFrame({"25%" : final_25_trials, "33%" : final_33_trials,
                                             "50%" : final_50_trials}, index = ["trial" + str(i) for i in range(1,101)])
# In the case of there is no value in the remaining population that is higher than the highest value in the "forfeit pile,"
# the "comparing" function was designed to return a null value which means none. Therefore, I would need to convert these
# nones to 0 in order to calculate the average of the data
df_final_different_standards.fillna(value = 0, inplace= True)
# Taking the mean of data in DataFrame "df_final_different_standards" and storing the averages in a new DataFrame
df_average_final_different_standards = pd.DataFrame({"Percentage" : ["25%", "33%", "50%"], "Value" : [
df_final_different_standards["25%"].mean(), df_final_different_standards["33%"].mean(),
    df_final_different_standards["50%"].mean()
]})
#  Graphing the DataFrame object "df_average_final_different_standards"
df_average_final_different_standards.plot(kind = "bar", x = "Percentage", y = ["Value"])
plt.show()


# Getting the f-value and p-value for the highest value of "forfeit pile" of three percentages
result_standards = f_oneway(highest_25_trials, highest_33_trials, highest_50_trials)
# Print out the result so we can see
print(result_standards)
# Compile the data into one list in order to convert it to a DataFrame and perform the Tukey's test
highest_standards = highest_25_trials + highest_33_trials + highest_50_trials
# Converting to DataFrame
df_highest_standards = pd.DataFrame({"Value" : highest_standards,
                                     "Group" : np.repeat(["25%", "33%", "50%"], repeats = 100)})

# Performing the Tukey's test
tukey_standards = pairwise_tukeyhsd(endog = df_highest_standards["Value"],
                                     groups = df_highest_standards["Group"], alpha = 0.05)
# Print out the result so we can see
print(tukey_standards)

# Switching the "None" value in the lists to 0 in order for the "f_oneway" function to work properly
for i in final_25_trials:
    if i == None:
        index = final_25_trials.index(i)
        final_25_trials = final_25_trials[:index] + [0] + final_25_trials[index + 1:]
    else:
        continue
for i in final_33_trials:
    if i == None:
        index = final_33_trials.index(i)
        final_33_trials = final_33_trials[:index] + [0] + final_33_trials[index + 1:]
    else:
        continue
for i in final_50_trials:
    if i == None:
        index = final_50_trials.index(i)
        final_50_trials = final_50_trials[:index] + [0] + final_50_trials[index + 1:]
    else:
        continue
# Getting the f-value and the p-value for the value of the final selection of each percentage
result_final = f_oneway(final_25_trials, final_33_trials, final_50_trials)
# Print out the result so we can see
print(result_final)
# Compile the data into one list in order to convert it to a DataFrame and perform the Tukey's test
final_standards = final_25_trials + final_33_trials + final_50_trials
# Converting to DataFrame
df_final_standards = pd.DataFrame({"Value" : final_standards,
                                   "Group" : np.repeat(["25%", "33%", "50%"], repeats = 100)})
# Performing the Tukey's test
tukey_final = pairwise_tukeyhsd(endog = df_final_standards["Value"],
                                 groups = df_final_standards["Group"], alpha = 0.05)
# print out the result so we can see
print(tukey_final)