#1.Create set by filtering greater than 25 using set comprehension.
myset = {12,34,56,3,45,67,89,1,6}
filtered_set = {x for x in myset if x > 25}
print(filtered_set)
