list = [3, 4, 7, 8, 9, 11]

# Find the missing numbers
missing_num = []
for num in range(min(list), max(list)):
    if num not in list:
        missing_num.append(num)

print("Missing numbers:", missing_num)
