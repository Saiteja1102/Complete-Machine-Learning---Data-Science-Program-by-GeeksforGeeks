# Special Functions

# zip
lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10]
print(list(zip(lst1,lst2)))
print("-"*50)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print([list(row) for row in zip(matrix)])
print([list(row) for row in zip(*matrix)])
print("-"*40)

lst_1 = [2,4,5]
lst_2 = [1,3,6]
print([i*j for i,j in zip(lst_1,lst_2)])
print(sum([i*j for i,j in zip(lst_1,lst_2)]))
print("-"*70)

# Filter
lst = [1,2,3,4,5,6,7,8,9,10,11,12]
def is_even(n):
    return n%2==0

print(list(filter(is_even,lst)))
print("-"*50)

# Lambda
mul_num = lambda x,y: x*y
print(mul_num(5,8))

add_num = lambda x,y: x+y
print(add_num(9,6))
print("-"*40)