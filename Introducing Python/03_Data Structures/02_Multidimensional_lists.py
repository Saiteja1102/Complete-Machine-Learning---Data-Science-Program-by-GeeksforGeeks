# Multi Dimensional lists

lst = [[1,2,3],[4,5,6],[7,8,9]]

# Acessing
print(lst)
print(lst[0])
print(lst[0][0])
print(lst[1][0])
print(lst[2][1])

print("-"*25)

# Modifing the values
print(lst)
lst[1][1] = 9
print(lst)

print("-"*25)

# Slicing the values
print(lst[0:1])
print(lst[0][0:2])

print("-"*25)

# Appending
print(lst)
lst.append([10,11,12])
print(lst)

print("-"*25)

# Delete the Index
del lst[3][2]
print(lst)
del lst[3]
print(lst)

print("-"*25)

# length ---> Gives number of lists
print("length of list = ",len(lst))

print("-"*25)

# Reverse
print(lst)
print(lst[::-1])

print("-"*25)

# Accessing all the elements
# 2D list
for i in lst:
    for j in i:
        print(j)

print("-"*25)