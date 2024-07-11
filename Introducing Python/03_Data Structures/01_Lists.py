# Lists

# Creating a list
lst = ["Sai","Haswanth","Raju","Bheem","Nobita","Doremon"]
print(lst)

print("-"*40)

# Accesing the list items
print(lst[2])
print(lst[0])
print(lst[-1])

print("-"*40)

# Slicing the list
print(lst[2:6])
print(lst[-4:-1])
print(lst[3:])

print("-"*40)

# Appending
lst.append("Sunio")
print(lst)
lst.append("Jaggu")
print(lst)

print("-"*40)

# Removing
lst.remove("Raju")
print(lst)
lst.remove("Jaggu")
print(lst)

print("-"*40)

# Reversing
print(lst)
lst.reverse()
print(lst)

print("-"*40)

# Length
print("length = ",len(lst))

print("-"*40)

# Sorting
nlst = [12,58,56,23,98,15,19,78,38,95,85,28,65,5]
print(nlst)
print("Sorthing in Ascending order : ")
nlst.sort()
print(nlst)

# Sorthing in Desending order --> first sort and then reverse
print("Sorthing in Desending order : ")
nlst.reverse()
print(nlst)

print("-"*40)

# Finding the element
nlst = [12,58,56,23,98,15,19,78,38,95,85,28,65,5,95]
print(nlst)
print(nlst.index(38))
print(nlst.index(56))

print("-"*40)

# Count
print(nlst)
print("Count of 95 = ",nlst.count(95))
print("Count of 15 = ",nlst.count(15))

print("-"*40)

# Extending the list
print(nlst)
nlst.extend([25,59,634,125,64,85,26,29])
print(nlst)

print("-"*40)

# Maximum and Minimum
print("Maximum = ",max(nlst))
print("Minimum = ",min(nlst))

print("-"*40)

# Iterating the list | Direct
for i in lst:
    print(i)

print("-"*15)

# Iterating the list | Using indexing
for i in range(len(lst)):
    print(lst[i])

print("-"*15)

# Iterating the list | Using indexing reverse
for i in range(len(lst)-1,-1,-1):
    print(lst[i])

print("-"*40)
