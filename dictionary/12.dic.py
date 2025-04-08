#12.Delete a list of keys from a dictionary
print("12")   
sample_dict = {"name":"Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys_to_delete = ["name", "salary"]
for key in keys_to_delete:
    if key in sample_dict:
        del sample_dict[key]
print(sample_dict)
