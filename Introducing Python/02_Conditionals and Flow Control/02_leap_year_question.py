# Problem Statement - Write a program that determines whether a year is a leap year or not. 
# In the Gregorian calendar, a leap year occurs every four years to compensate for the fact that the 
# Earth's orbit around the Sun takes approximately 365.25 days.

# ------------------------------------------------------------------------------------------------------

year = int(input("Enter the year : "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("Leap Year")
        else:
            print("Not a Leap year")
    else:
        print("Leap Year")
else:
    print("Not a Leap year")

print("-"*25)
# 2nd Method using logical operators
if (year % 4 == 0):
    if (year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap year")
else:
    print("Not a Leap year")    