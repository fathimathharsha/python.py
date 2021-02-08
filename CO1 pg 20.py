#From a list of integers, create a list removing even numbers.

list = [10, 13, 16, 18, 21]
print( "Original list:",list)

for i  in list:
	if(i%2 == 0):
	    list.remove(i)
print("list after removing Even numbers:",list)