#7.Create a set of unique characters from a list of words
words = ['apple', 'banana', 'cherry']
unique_chars_set = {char for word in words for char in word}
print(unique_chars_set)
