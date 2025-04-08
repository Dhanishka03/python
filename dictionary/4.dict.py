#4.Merge two Python dictionaries into one
print("4")
dict1 = {"Ten":10,"Twenty":20,"Thirty":30}
dict2 = {"Thirty":30,"Forty":40,"Fifty":50}
a= {**dict1, **dict2}
print(a)
