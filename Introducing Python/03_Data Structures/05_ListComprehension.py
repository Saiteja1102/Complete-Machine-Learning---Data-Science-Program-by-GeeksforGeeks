# Write the code in a single line
# Example : Squaring all the elements in a list and returning in list

# Tradional way
lst = [1,2,3,4,5,6,7,8,9]
sq = []
for i in lst:
    sq.append(i**2)

print(lst)
print("-"*20)
print(sq)

print("-"*40)

# List Comprension
lst = [1,2,3,4,5,6,7,8,9]
print(lst)
print("-"*20)
lst = [i**2 for i in lst]
print(lst)

print("-"*40)

# Finding first 10 even numbers
new_lst = [i for i in range(21) if (i%2==0)]
print(new_lst)

print("-"*40)

# Multi-Dimensional List
mul_list = [[i for i in range(3)] for j in range(5)]
print(mul_list)

print("-"*40)

# Accesing all the elements of the list
print(mul_list)
print([j for i in mul_list for j in i])