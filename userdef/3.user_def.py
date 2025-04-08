#3)Write a python program to illustrate function by Calculate the factorial of a number(without argument & without return)
def fact():
    num=int(input("Enter a number:"))
    fact=1
    for i in range(1,num+1):
        fact= fact*i
    print(f"The factorial of {num} is: {fact}")
fact()
