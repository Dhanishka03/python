#1) Write a python program to illustrate a function that accepts 2 values and return its sum, subtraction and multiplication.(pass argument and return value)
def calc(a,b):
    add=a+b
    sub=a-b
    multiply=a*b
    return add,sub,multiply
v1=20
v2=10
add,sub,multiply=calc(v1,v2)
print(f"Sum:{add}")
print(f"Difference:{sub}")
print(f"Multiplication:{multiply}")
