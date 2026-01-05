# pillers of OOP:
# inheritance: a class inherites the attributes and method of anothor class
# Dog class(child) and Animal class(Parent class)
# child class can use the properties of Parent class
# child class can have unique/new attributes and method defined in them
# the methods in parent class can be overriden in child class(the name of method in child class should match the method name is parent class)
class Animal:
   eyes = 2
   legs = 4
   ears = 2
   
   def get_detail(self, eyes,legs,ears):
      self.eyes = eyes
      self.legs = legs
      self.ears = ears
   
   def show(self):
      print(f"""Eyes: {self.eyes}
Legs: {self.legs}
Ears: {self.ears}""")


class Dog(Animal):
   tail = 3
   def move(self):
      print("Dog moves in 4 legs")
   
   def show(self):
      print(f"""Eyes: {self.eyes}
Legs: {self.legs}
Ears: {self.ears}
Tail: {self.tail}""")

dog1 = Dog()
dog1.move()
dog1.show()


