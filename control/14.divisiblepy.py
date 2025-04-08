num=int(input("Enter a number:"))
ans=[]
for i in range(2,num):
    if num%i==0:
        ans.append(i)
if ans:
     print(ans)
else:
     print("Given is a prime number")
