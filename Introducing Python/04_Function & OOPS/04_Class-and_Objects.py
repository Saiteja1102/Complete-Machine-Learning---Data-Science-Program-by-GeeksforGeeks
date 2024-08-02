# OOPs
class person:
    name = "Sai"
    age = 20

p1 = person()
print(p1.name)
print(p1.age)
print("-"*30)

p1.name = "Sai Teja"
p1.age = 19
print(p1.name)
print(p1.age)
print("-"*30)

p2 = person()
print(p2.name)
print(p2.age)
print("-"*30)

class arithmetic:
    def greet(self):
        return "hello"
    
    def fact(self,n):
        s = 1
        for i in range(1,n+1):
            s *= i
        return s

math = arithmetic()
print(math.greet())
print(math.fact(5))