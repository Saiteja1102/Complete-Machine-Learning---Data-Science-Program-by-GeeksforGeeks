# Reversing a number

number = int(input("Enter the number : "))
lengthNumber = len(str(number))
reverseNumber = 0
while(number > 0):
    quotient = number//10
    remainder = number%10
    reverseNumber += remainder*(10**(lengthNumber-1))
    lengthNumber -= 1
    number = quotient

print("Reverse Number = ",reverseNumber)


# method 2
# first convert number to string
# use this number[::-1]
# print
