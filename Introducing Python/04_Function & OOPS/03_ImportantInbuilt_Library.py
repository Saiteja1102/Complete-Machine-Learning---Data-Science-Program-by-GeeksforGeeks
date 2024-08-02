# Math
import math

x = 25.6
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))
print("-"*30)

x = 9
print(math.exp(x))
print(math.log10(x))
print("-"*30)

x = 90
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))
print("-"*30)

print(math.pi)
print(math.e)
print("-"*30)

print(math.factorial(5))
print("-"*50)

# Random
import random

print(random.random())
print(random.randint(1,21))
print(random.choice([1,2,3,4,5,6,7]))
print(random.sample([1,2,3,4,5,6,7],3))
print(random.uniform(1.0,5.0))
print("-"*50)

# datetime
import datetime

print(datetime.datetime.now())
print(datetime.datetime(2024,2,11,8,30,45))
print(datetime.datetime.now().strftime("%m/%d/%y %H:%M"))
date_1 = datetime.datetime.now()
date_2 = datetime.datetime(2024,2,11,8,30,45)
print(date_1 - date_2)
print(date_2 - date_1)
print("-"*50)

# Collections
import collections

lst = [1,2,3,4,2,3,6,2,5,1,2,5,6,1,1,1]
print(collections.Counter(lst))
print("-"*50)

# Strings
import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print("-"*30)

print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print("-"*30)

print(string.punctuation)
print("-"*50)