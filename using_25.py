# import necessary functions from functions.py
from functions import get_data, get_highest_sample, comparing

# Storing for the highest value obtained from the "forfeit pile" after 100 trials
highest_25_trials = []
# Storing for the value of the individual with the highest score after 100 trials
final_25_trials = []

# Running the below actions 100 times
for i in range(100):
    # Running "get_data" and assign the results from the function to two lists
    individuals_values, individuals_values_25 = get_data(0.25, 1000)
    # Getting the initial value for the "get_highest_sample" function by accessing the first individual in the population
    comparing_value_25 = individuals_values_25[0]["thing1"]
    # Running the "get_highest_sample" function with the "forfeit pile" (i.e., individuals_value_25) and the initial value
    standard_25 = get_highest_sample(individuals_values_25, comparing_value_25)
    # Adding the result from the "get_highest_sample" function to the highest_25_trials list located above
    highest_25_trials.append(standard_25)
    # Running the "comparing" function, the first argument being the entire population while the other being "forfeit pile"
    # and storing the result from "comparing" function as final_choice
    final_choice = comparing(individuals_values, standard_25)
    # Adding the result from the "comparing" function to the final_25_trials list located above
    final_25_trials.append(final_choice)
    print(standard_25)


