# Defining
def greet():
    print("Hello")
greet()
greet()
print("-"*40)

# Defining 2
def dash():
    print("-"*40)
dash()

# Scope of the variable
global_var = 10
def ad():
    local_var = 5
    print(global_var+local_var)
ad()
# print(global_var,local_var) --> Gives Error
dash()

# Passing the Parameters
def addition(a=0,b=0):
    print(a,b,a+b)
addition(10,5)
addition(5,23)
addition(3)
addition(b = 3)
addition(b=78,a=23)
dash()

# Return
def greet():
    return "hello"
print(greet())
var = greet()
print(var)
dash()

# Multi-Return
def arithemetic(a,b):
    return (a+b,a-b,a*b)

print(arithemetic(10,6))
print(type(arithemetic(10,6)))
add,dif,mul = arithemetic(23,67)
print(add)
print(dif)
print(mul)
dash()

# Calling Different Functions
lst = [1,2,3,4,5]
def sq_lst():
    return [i**2 for i in lst]
print(sq_lst())
def cube_lst():
    return [i**3 for i in lst]
print(cube_lst())

def final_lst():
    list1 = sq_lst()
    list2 = cube_lst()
    return [list1[i]+list2[i] for i in range(len(lst))]
print(final_lst()) 
dash()