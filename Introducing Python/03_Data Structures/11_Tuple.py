# Tuple
# --> immutable
# --> duplicacy
# --> ordered

# Intialization
tpl = (1,2,3,4,5)
print(tpl)
print("-"*40)

# Accessing
print(tpl)
print(tpl[2])
print(tpl[4])
print("-"*40)

# Slicing
print(tpl)
print(tpl[1:4])
print("-"*40)

# Concatenate
tpl1 = (1,2,3,4)
tpl2 = (5,6,7,8)
print(tpl1+tpl2)
print("-"*40)

# Length
print(tpl)
print(len(tpl))
print("-"*40)

# Iterating
print(tpl)
for i in tpl:
    print(i)
print("-"*40)

# Checking
print(tpl)
print(2 in tpl)
print(11 in tpl)
print("-"*40)

# Checking the count
print(tpl)
print(tpl.count(4))
print(tpl.index(5))
print("-"*40)

# Multipying the tuple
print(tpl)
print(tpl*3)
print("-"*40)
