#to count the number of even&odd number
tup=(1,2,3,4,5,6,7,8,9)
odd=0
even=0
for num in tup:
    if num%2==0:
        even=even+1
    else:
        odd=odd+1
print("Count of even numbers:",even)
print("Count of odd numbers :",odd)
