import random

def get_data(pin_point, size):
    individuals_values = []
    for i in range(size):
        score = random.randint(1, 100)
        individuals_values.append({"thing" + str(i + 1): score})
        stop = pin_point * size
        stop = int(stop)
    return individuals_values, individuals_values[:stop]

def get_highest_sample(sample, comparing_value):
    for i in sample:
        for key in i:
            key = key
            value = i[key]
        if key == "thing1":
            continue
        else:
            if value >= comparing_value:
                comparing_value = value
            else:
                comparing_value = comparing_value
    highest_value = comparing_value
    return highest_value

def comparing(population, higest_sample):
    for i in population:
        for key in i:
            key = key
            value = i[key]
        if value > higest_sample:
            return value
        else:
            continue