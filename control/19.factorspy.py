def print_factor(x):
    print("The factors of ",x,"are")
    for i in range(1,x+1):
        if x%i==0:
            print(i)
num=int(input("Enter a number:"))
print_factor(num)
