# Sets
# --> mutable
# --> unordered
# --> unique values

# Initialization
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))
print("-"*40)

# Adding
print(my_set)
my_set.add(6)
print(my_set)
print("-"*40)

# Remove
print(my_set)
my_set.remove(5)
print(my_set)
print("-"*40)

# Pop --> Removes first element
print(my_set)
my_set.pop()
print(my_set)
print("-"*40)

# Iterating
print(my_set)
for i in my_set:
    print(i)
print("-"*40)

# Checking
print(my_set)
print(2 in my_set)
print(1 in my_set)
print("-"*40)

## Set Operations

set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}
# Union
uni_set = set_1 | set_2
print(uni_set)
print("-"*40)
# Intersection
int_set = set_1 & set_2
print(int_set)
print("-"*40)
# Difference
diff_set1 = set_1 - set_2
print(diff_set1)
print("-"*20)
diff_set2 = set_2 - set_1
print(diff_set2)
print("-"*40)
# Symetric differnce
sym_diff = set_1 ^ set_2
print(sym_diff)
print("-"*40)

# Clearing
print(my_set)
my_set.clear()
print(my_set)
print("-"*40)