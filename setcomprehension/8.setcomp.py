#8.Generate a set of tuples containing numbers and their squares, but only for even numbers
even_squares_set = {(x, x**2) for x in range(1, 11) if x % 2 == 0}
print(even_squares_set)
