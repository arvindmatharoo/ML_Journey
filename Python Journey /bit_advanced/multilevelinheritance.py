class Animal :
    def sound(self):
        print("generic animal sound")
class mammal(Animal):
    def eat(self):
        print("mammal eats")
class Dog(mammal):
    def bark(self):
        print("dog is barking")
c1 = Dog()
c1.sound()
c1.eat()