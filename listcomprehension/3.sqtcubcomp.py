# the list even numbers and odd numbers cubed from 1 to 10
sqtcub=[num**2 if num %2==0 else num **3 for num in range(1,10)]
print("The Numbers are:",sqtcub)
