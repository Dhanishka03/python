#to check if the 2 set have common element
set1={50,40,30,20,10}
set2={6,7,8,9,10}
common=set1.intersection(set2)
if common:
    print("The given set have common element",common)
else:
    print("The set does not have common element")
