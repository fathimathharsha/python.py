#Merge two dictionaries.

dict1 = {  'Ritika': 5, 'Sam': 7, 'John' : 10 }
dict2 = {'Aadi': 8,'Sam': 20,'Mark' : 11 }
dict3 = {**dict1 , **dict2}
print(dict3)