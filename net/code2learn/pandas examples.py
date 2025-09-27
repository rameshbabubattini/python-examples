import pandas as pd
s1 = pd.Series([1,2,3,4,5])
print(s1)
print(type(s1))

s1 = pd.Series([1,2,3,4,5], index=['b', 'a', 'c', 'd', 'e'])
print(s1)
print(type(s1))

dictionary1 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(dictionary1)
print(type(dictionary1))

dictionary2 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4}, index=['b', 'a', 'c', 'd'])
print(dictionary2)

print(dictionary2['a'])
print(dictionary2[:3])

data = pd.DataFrame({"Name": ['Bob', 'Sam', 'Anne'], "Marks" : [76, 52, 35] })
print(data)

data =