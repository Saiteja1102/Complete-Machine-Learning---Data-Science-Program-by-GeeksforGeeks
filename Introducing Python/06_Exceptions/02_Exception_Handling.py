# Exception Handling

try:
    x = 10
    print(1)
    print(x/0)
    print(2)
except:
    print("There is a error!!")
print("-"*50)

# Exception with specific errors
try:
    x = 10
    print(x/10)
except ZeroDivisionError:
    print("Zero in the division")
except:
    print("Unknown Error!!")
print("-"*50)

# Final Exception with specific error
try:
    lst = [1,2,3,4]
    # print(lst[2])
    print(lst[2])
except IndexError as ie:
    print(ie)
except Exception as e:
    print(e)
else:
    print("There is no error")
finally:
    print("Program End")
    print("-"*50)