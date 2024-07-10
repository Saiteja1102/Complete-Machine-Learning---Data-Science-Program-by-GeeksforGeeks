n = int(input("Enter the number : "))

# if
if (n>0):
    print(n," is positive..")

if (n<0):
    print(n," is negative")

if (n==0):
    print("It is a zero")


# if else
if (n>0):
    print("Positive")
else:
    print("Negative")

# in this case 0 is not included

# if elif else
if (n==0):
    print("zero")
elif (n>0):
    print("positive")
else:
    print("negative")

# nested if else
# lets checks n is divsible by 5 and 3
if (n%5==0):
    if (n%3==0):
        print("Divsible")
    else:
        print("Not Divisible")
else:
    print("Not Divsible")

# using Logical operators
if ((n%5==0) and (n%3==0)):
    print("Divsible")
else:
    print("Not Divsible")

print("-"*35)
