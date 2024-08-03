# 1

print("-"*50)
class person:

    def __init__(self,name,age):
        print("Hello")
        # print(name)
        # print(age)
        self.name = name
        self.age = age
    
    def run(self):
        print(self.name)
        print(self.age)
        print("run!")

p1 = person("Sai",20)
p2 = person("Sai Teja",19)
p1.run()
p2.run()

print("-"*50)

# 2 --> Game

class agent:

    def __init__(self,name,age):
        print("Welcome to the game -",name)
        self.name = name
        self.age = age
        self.health = 100
        self.alive = True
    
    def currenthealth(self):
        print("Current health of",self.name,"is",self.health)
        # if self.health <= 0:
        #     self.alive = False
    
    def punched(self):
        self.health -= 10
        print("Health =",self.health)
        # if self.health <= 0:
        #     self.alive = False
    
    def shooted(self):
        self.health -= 40
        print("Health =",self.health)
        # if self.health <= 0:
        #     self.alive = False
    

    def info(self):
        if self.health <= 0:
            self.alive = False
        print("Name     :",self.name)
        print("Age      :",self.age)
        print("Health   :",self.health)
        print("Alive    :",self.alive)

p1 = agent("Sai",20)
p1.currenthealth()
p1.punched()
p1.shooted()
p1.info()
print("-"*30)

p2 = agent("Haswanth",19)
p2.currenthealth()
p2.shooted()
p2.shooted()
p2.punched()
p2.shooted()
p2.info()
print("-"*30)
print("-"*50)
print("-"*30)

# Inheritance

class boss(agent):
    def __init__(self,name,age):
        self.health = 1000
        self.name = name
        self.age = age
        self.alive = True

    def bossfly(self):
        print("Boss is Boss!!!")
    
p3 = boss("Sai Teja Goud",20)
p3.bossfly()
p3.info()
