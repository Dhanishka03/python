#5.Generate a set of prime numbers from 1 to 50
prime_numbers_set = {x for x in range(2, 51) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))}
print(prime_numbers_set)
