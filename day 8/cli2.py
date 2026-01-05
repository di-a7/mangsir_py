# Ecom CLI

# show 2 options to user 1. Register 2. Login
# if choice is 1: get username, password and usertype from user and store it in a file
# if choice is 2: get username, password from user and check if it in a file and get the usertype, print login successful
# after login, 
# if usertype is seller, show options 1. View my Products read the products from the file, 2. Add Product(name, description, price) store it in a file
# if usertype is buyer, show options 1. View all Products from the file, 2. Buy Product 
# if user credentials does not match, print a statement

user = [{"username":"shyam","password":"1234","usertype":"seller"},{"username":"ram","password":"1234","usertype":"buyer"},{"username":"shyam","password":"1234","usertype":"seller"},{"username":"shyam","password":"1234","usertype":"seller"}]

products = [{"name":"Books", "description":"Has Pages", "price": 400}, {"name":"Food", "description":"Eat", "price": 100}]

def login(username, password):
   for i in user:    # i = {"username":"shyam","password":"1234","usertype":"seller"}
      if username == i["username"] and password == i["password"]:
         print("Login Successful.")
         type = i["usertype"]
         if type == "seller":
            pass 
         elif type == "buyer":
            pass
      else:
         print("Invalid credentials")

name = input("Enter username: ")
passkey = input("Enter password: ")
login(name, passkey)

