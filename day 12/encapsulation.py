# Encapsulation: properties are encapsulated in a single unit, data hiding(restrict the access of the values in attribute to the objects)
# '__' is used to define a private attribute and method
# if the private attributes and methods are to be called, we will have to define a normal or unprivate methods

class User:
   def __init__(self, username, password):
      self.__username = username
      self.__password = password
   
   def __details(self):
      print(f"""Username: {self.__username}
Password: {self.__password}""")
   
   def show(self):
      return self.__details()

u1 = User("Ram","ram123")
u1.show()


# create a class Account, should have attributes email, password, account_number, account_balance
# account_number, account_balance , password should have object access restriction
# also create a method that print out the details of the user account