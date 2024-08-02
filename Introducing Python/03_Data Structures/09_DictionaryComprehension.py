# Dictionary comprehension --> if you want to construct dictionaries in one line of code

# Initialization
dct = {i:i for i in range(1,6)}
print(dct)
print("-"*50)

# square
dct = {i:i**2 for i in range(1,6)}
print(dct)
print("-"*50)

# cube
dct = {i:i**3 for i in range(1,6)}
print(dct)
print("-"*50)

# Dictionary with condition
dct = {i:i**2 for i in range(1,11) if i%2==0}
print(dct)
print('-'*50)

# Dictionaries with Lists
lst = ["Apple","Banana","Oranges","Grapes"]
print(lst)
dct = {i:len(i) for i in lst}
print(dct)
print("-"*20)
dct = {len(i):i for i in lst}
print(dct)
print("-"*50)

# Special keys with String
dct = {"num_"+str(i):i for i in range(1,11)}
print(dct)
print("-"*50)

# Shortlisting based on values
dct = {"num_"+str(i):i for i in range(1,11)}
dct = {k:v for k,v in dct.items() if v%3==0}
print(dct)
print("-"*50)

# Matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
fin_dct = {(i,j):matrix[i][j] for i in range(0,3) for j in range(0,3)}
print(fin_dct)
print("-"*50)
# reverse
fin_dct = {matrix[i][j]:(i,j) for i in range(0,3) for j in range(0,3)}
print(fin_dct)
print("-"*50)