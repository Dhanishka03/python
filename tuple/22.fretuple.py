#to find frequency of each element
tup=(1,2,2,3,2,4,2)
feq={}
for i in tup:
    if i in feq:
        feq[i]+=1
    else:
        feq[i]=1
print("The frequency :",feq)
