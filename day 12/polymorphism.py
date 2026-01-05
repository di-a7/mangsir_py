a = 10
b = 5

x = "a frunt"
y = "b kjdfsjkld"
# print(a + b)
# print(x + y)
print(a.__add__(b))
print(x.__add__(y))

# class str:
#    def __add__():
#       pass

# class int:
#    def __add__():
#       pass

# Polymorphism: Poly = multiple, morph: form
# depends on the object
# different class but same method name
# same name method but different functionality

class Dog:
   def move(self):
      print("Legs")

class Parrot:
   def move(self):
      print("Wings")

class Fish:
   def move(self):
      print("Swim")


d1 = Dog()
p1 = Parrot()
f1 = Fish()

d1.move()
p1.move()
f1.move()