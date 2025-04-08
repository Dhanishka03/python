t1=(('a',3),('b',9),('c',4),('d',7))
print("THe given tuple-",t1)
sort=tuple(sorted(t1,key=lambda x:x[1]))
#to sort tuple
print("Sorted tuple:",sort)
