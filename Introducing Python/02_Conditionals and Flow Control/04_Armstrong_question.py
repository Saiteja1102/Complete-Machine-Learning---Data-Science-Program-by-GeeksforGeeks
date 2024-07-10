# Problem Statement - Write a program checking whether a number is an Armstrong number.
# An Armstrong number (also known as a narcissistic number, pluperfect digital invariant, or pluperfect number)
# is a number that is the sum of its own digits each raised to the power of the number of digits.

# Armstrong number
'''
example 1:
number = 153
(1*1*1)+(5*5*5)+(3*3*3) = 1+125+27 = 153

example 2:
number = 1634
(1*1*1*1)+(6*6*6*6)+(3*3*3*3)+(4*4*4*4) = 1+1296+81+256 = 1634
'''

number = input("Enter the number : ")
length = len(number)

newNumber = 0
for i in range(length):
    newNumber += int(number[i])**length

number = int(number)
if (newNumber == number):
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
