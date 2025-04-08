#python program to find the HCF of two number
#define a funtion
def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=y
    for i in range (1,smaller+1):
        if ((x%i==0)and(y%i==0)):
            hcf=i
    return hcf
print("FINDING HCF")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print("The HCF is",hcf(num1,num2))
