# Initializing the dictionary
dct = {1:"Sai",2:"Bheem",3:"Doremon",4:"Raju",5:"Jaggu"}
print(dct)
print("-"*40)

# Accessing the elements
print(dct[2])
print(dct[5])
print(dct.get(3))
print("-"*40)

# Adding And Updating 
print(dct)
dct[6] = "Haswanth"
print(dct)
# Updating
dct[6] = "Bunny"
print(dct)
# Deleting
del dct[6]
print(dct)
print("-"*40)

# Clearing all the elements
print(dct)
dct.clear()
print(dct)
print("-"*40)

# Iterating
dct = {1:"Sai",2:"Bheem",3:"Doremon",4:"Raju",5:"Jaggu"}
print(dct.keys())
print(dct.values())
print("-"*20)

# 2nd method
for i in dct.keys():
    print(i,dct[i])
print("-"*20)

# 3rd method
for key,value in dct.items():
    print(key,value)
print("-"*40)

# Check if the key is present or not
print(dct)
print(1 in dct)
print("1" in dct)
print("-"*40)

# Updating the dictionaries
dct1 = {1:"Sai",2:"Bheem",3:"Doremon"}
dct2 = {4:"Raju",5:"Jaggu",6:"Bunny"}

print(dct1)
print(dct2)
dct1.update(dct2) # Merging
print(dct1)
print(dct2)
print("-"*40)

# Note:
# 1. Dictionaries --> NoSQL
# 2. List --> SQL