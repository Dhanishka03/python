#Check if an element exists in a tuple.
tup = (10, 20, 30, 40, 50)
a=int(input("Enter an element:"))
if a in tup:
    print(f"{a} exists in the tuple.")
else:
    print(f"{a} does not exist in the tuple.")
