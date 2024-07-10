# Loops
# For Loop

# Multiplication Table
n = int(input("Enter the number : "))

for i in range(1,11):
    print(n,"x",i,"=",n*i)

print("-"*20)
# Method 2
for i in range(n,(n*10)+1,n):
    print(i)

print("-"*20)

# Nested For Loop

# 2 dice each percentage
for n in range(1,13):
    number = 0
    for i in range(1,7):
        for j in range(1,7):
            if (i + j == n):
                number += 1
    
    print(n,"=",round((number/(6*6))*100,2))

print("-"*20)
# 3 dice each percentage
for n in range(1,(3*6)+1):
    number = 0
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                if (i+j+k == n):
                    number += 1
    print(n,"=",round((number/(6**3))*100,2))

print("-"*20)