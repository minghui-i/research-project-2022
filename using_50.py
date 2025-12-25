from functions import get_data, get_highest_sample, comparing

highest_50_trials = []
final_50_trials = []

for i in range(100):
    individuals_values, individuals_values_50 = get_data(0.50, 1000)
    comparing_value_50 = individuals_values_50[0]["thing1"]
    standard_50 = get_highest_sample(individuals_values_50, comparing_value_50)
    highest_50_trials.append(standard_50)
    final_choice = comparing(individuals_values, standard_50)
    final_50_trials.append(final_choice)
    print(standard_50)


