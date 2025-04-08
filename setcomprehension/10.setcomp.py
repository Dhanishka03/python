#10.Checking for palindrome words
words = ['refer', 'hello', 'civic', 'level']
palindromes = {word for word in words if word == word[::-1]}
print(palindromes)

