# OOP: Object Oriented Programming: 
# class: structure, blueprint
# object: data created using class


# class intro:
#    name = "Ram"            # name, age, contact are attributes
#    age = "30"
#    contact = "9855552214"

# dia = intro()     # dia is a object, it is a data created using class intro
# print(dia.name)
# print(dia.age)
# print(dia.contact)

# dia.name = "Diya"
# dia.age = 300
# dia.contact = "958532133021"

# print("After Update")
# print(dia.name)
# print(dia.age)
# print(dia.contact)


# sita = intro()
# sita.name = "Sita"
# sita.age = 500
# sita.contact = "6565656126"
# print(sita.name)
# print(sita.age)
# print(sita.contact)


# create class named Car, define attributes like brand, color, wheels
# create a 2 object of the Car class


class Car:
   brand = None      # attribute: brand, color, wheels
   color = None
   wheels = None
   
   # method
   def get_detail(self, brand, color, wheels):
      self.brand = brand
      self.color = color
      self.wheels = wheels


car1 = Car()         # car1 is an object
print(car1.brand)
car1.get_detail("Toyota","White","4")
car1.speed = "150 km/hr"
print(car1.brand)
print(car1.speed)

car2 = Car()
car2.get_detail("TATA","Black","4")
print(car2.brand)


# create a class Animal
# define attributes eyes, legs, ears, nose
# define method to get the detail
# define a method to print out the detail

# create 2 object of class Animal

