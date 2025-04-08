#1.syntax error
num=int(input("Enter a number:"))
if num % 2 == 1:  # SyntaxError: Missing colon (:)
    print("Odd number")

    
'''#2.name error
num=7
print(num)  # NameError: name 'number' is not defined

#3.value error
num = int("Hello")# ValueError: invalid literal for int() with base 10
print(num)

#4.key error
data = {"name": "Alice", "age": 25}
print(data["gender"])  # KeyError: 'gender' does not exist

#5.import error
print(math.sqrt(16))# import the module

#6.zerodivision error
x = 5 / 0  # ZeroDivisionError: division by zero

#7.recursion error
def recursive():
    return recursive()  # No base case leads to infinite recursion

print(recursive())  # RecursionError: maximum recursion depth exceeded'''
