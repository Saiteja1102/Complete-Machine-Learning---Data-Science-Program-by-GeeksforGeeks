# Problem Statement - Write a program to print Prime numbers in a given range.

print("-"*20)
start = int(input("Enter the number1: "))
end = int(input("Enter the number2: "))
print("-"*20)

for i in range(start,end+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)