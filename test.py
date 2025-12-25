import pandas as pd

df = pd.DataFrame({"value": [1, 2, 3, 4, 5]})

print(df["value"].mean())

a = [1, None, None, 2, 3, 4, 5, None, 6]

for i in a:
    if i == None:
        index = a.index(i)
        a = a[:index] + [0] + a[index+1:]
    else:
        continue
print(a)
print(a[2:4])