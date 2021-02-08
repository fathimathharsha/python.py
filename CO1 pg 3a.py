#List comprehensions:
# (a) Generate positive list of numbers from a given list of integers

list = [10,-20,55,-40,85,-60] 
  
result = [num for num in list if num >= 0] 
  
print("Positive numbers in the list: ", result) 