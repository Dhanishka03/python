#8.Get the key of a minimum &amp; maximum value from the following dictionary
print("8")
sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}
a= min(sample_dict, key=sample_dict.get)
b= max(sample_dict, key=sample_dict.get)
print("Minimum value:", a)
print("Maximum value:", b)
