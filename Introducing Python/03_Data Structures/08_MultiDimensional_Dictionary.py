# Initializing
dct = {1:{"name":"Sai","Phoneno":987789678},
       2:{"name":"Bheem","Phoneno":789789678},
       3:{"name":"Raju","Phoneno":456378567}}
print(dct)
print("-"*50)

# Accessing
print(dct)
print(dct[1])
print(dct[1]["name"])
print(dct[2]["Phoneno"])
print("-"*50)

# Adding
print(dct)
dct[4] = {"name":"Doremon","Phoneno":678098456}
print(dct)
print("-"*50)

# Updating
print(dct)
dct[4]["name"] = "Bunny"
print(dct)
print("-"*50)

# Deleting
print(dct)
del dct[4]
print(dct)
print("-"*50)

# Going through the data
for i in dct.keys():
    print(i,dct[i])
print("-"*50)

for i in dct.keys():
    print(i,dct[i]["name"],dct[i]["Phoneno"])
print("-"*50)

# Going a level deeper with marks
data = {1:{"name":"Sai","Phoneno":987789678},"marks":{"hin":32,"eng":45,"sci":49},
       2:{"name":"Bheem","Phoneno":789789678},"marks":{"hin":32,"eng":45,"sci":49},
       3:{"name":"Raju","Phoneno":456378567},"marks":{"hin":32,"eng":45,"sci":49}}
print(data)

for i in data.keys():
    print(i,data["marks"]["hin"])