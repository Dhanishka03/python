list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

common = list(set(list_a) & set(list_b))

print("Common elements:", common)
