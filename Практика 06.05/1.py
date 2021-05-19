
class Person:
    def __init__(self, n, a):
        
        self.fullname = n 
        self.age = a

    def move(self):

        print(self.fullname+" говорит сейчас")

    def talk(self):

        print(self.fullname+" говорит сейчас")


p1 = Person("Parker Cornell", 34)
p1.move()
p1.talk()
print(p1.fullname,p1.age)
