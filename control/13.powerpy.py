#to display the power of 2 using anonymous function
#input
terms=int(input("Enter the power:"))
result=list(map(lambda x:2**x,range(terms)))
print("The total terms are :",terms)
for i in range(terms):
    print("2 raised to power ",i,"is",result[i])
