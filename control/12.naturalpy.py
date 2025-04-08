#to find the sum of the natural nimbers
num=int(input("Enter a number:"))
#input
if num<0:
    print("Enter the positive numbers:")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
    print("The sum is",sum)
