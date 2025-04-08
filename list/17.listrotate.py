list = [1, 2, 3, 4, 5]
n = 2

# Rotate the list
for _ in range(n):
    list.insert(0, list.pop())

print("Rotated list:", list)
