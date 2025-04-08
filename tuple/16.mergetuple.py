#to merge the two tuples and remove the duplicate
# Given tuples
tup1 = (1, 2, 3)
tup2 = (3, 4, 5)
merge = tuple(set(tup1 + tup2))
print("Merged tuple with duplicates removed:", merge)

