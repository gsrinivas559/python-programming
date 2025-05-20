# 5. Dictionary --> unordered sequence of data of key-value pair form and similar to the hash table type.
# Dictionaries are written within curly braces in the form key:value
# a sample dictionary variable

a = {1: "first name", 2: "last name", "age": 33}

# print value having key=1
print(a[1])  # first name
# print value having key=2
print(a[2])  # last name
# print value having key="age"
print(a["age"])  # 33 and if the key is string, we have to give in double quotes

# creating dictionary at the runtime
personDetails = {}
personDetails["firstName"] = "John"
personDetails["lastName"] = "Wick"
personDetails["gender"] = "Male"
print(personDetails)  # {'firstName': 'John', 'lastName': 'Wick', 'gender': 'Male'}
print(personDetails["lastName"])  # Wick
