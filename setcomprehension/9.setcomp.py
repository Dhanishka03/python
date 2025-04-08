#9.Create a set of even numbers from 1 to 50 that are not divisible by 4
even_not_divisible_by_4_set = {x for x in range(2, 51, 2) if x % 4 != 0}
print(even_not_divisible_by_4_set)
