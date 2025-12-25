from functions import get_data

def evaluate():
    data = []
    for i in range(100):
        choice, placeholder = get_data(2, 2)
        first_choice = choice[0]
        choice_changed = choice[1]
        if choice_changed["thing2"] > first_choice["thing1"]:
            data.append(True)
        elif choice_changed["thing2"] == first_choice["thing1"]:
            data.append("Tie")
        else:
            data.append(False)
    return data

data = evaluate()

amount_true = data.count(True)
amount_false = data.count(False)
amount_tie = data.count("Tie")



