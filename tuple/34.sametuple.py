#to check if all item in tuple
tup=(45,45,45,45)
same=all(item==tup[0] for item in tup)
print("Are all items the same?-",same)
