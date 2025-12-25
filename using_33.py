from functions import get_data, get_highest_sample, comparing

highest_33_trials = []
final_33_trials = []

for i in range(100):
    individuals_values, individuals_values_33 = get_data(0.33, 1000)
    comparing_value_33 = individuals_values_33[0]["thing1"]
    standard_33 = get_highest_sample(individuals_values_33, comparing_value_33)
    highest_33_trials.append(standard_33)
    final_choice = comparing(individuals_values, standard_33)
    final_33_trials.append(final_choice)
    print(standard_33)


