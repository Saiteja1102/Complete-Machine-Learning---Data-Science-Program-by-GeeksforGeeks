# Problem Statement - Create a Python program that prompts the user to enter positive numbers continuously. 
# The program should use a while loop to collect input data until the user enters a non-positive number. 
# Implement simple data validation to ensure entered values are valid positive numbers. 
# Finally, output the list of positive numbers entered by the user. The objective is to create an interactive 
# and error-tolerant program for collecting and handling user input.

numbers = []

num = 0
while (num >= 0):
    numberInput = int(input("Enter the number : "))
    if (numberInput>=0):
        numbers.append(numberInput)
    else:
        break
    num = numberInput

print(numbers) 
