# Accounting program
# show 2 options to user 1. Register 2. Login
# if choice is 1: get username and password from user and store it in a file
# if choice is 2: get username and password from user and  check if the username exists and the password matches . if yes print login successful else print login failed
# if login is successful, show 2 options, 1. Show user details, 2. Add Balance 
# if user choice 1, show user details (username and bank balance) in the file
# if user choice 2, get amount to add from user, add the amount to bank balance and store it in a file

# Ecom CLI with file handling

import json

choice = input("""1. Register
2. Login
>>""")
if choice == "1":
   username = input("Enter Userename: ")
   password = input("Enter Password: ")
   form = {username:password}
   json_form = json.dumps(form)
   f = open("userdetail.txt",'a')
   f.write(json_form + '-')
   f.close()
   print("User registered.")

elif choice == "2":
   username = input("Enter Userename: ")
   password = input("Enter Password: ")
   f = open("userdetail.txt",'r')
   a = f.read().split('-')
   print(a)
   for i in a:
      if i != '':
         dict_form = json.loads(i)
         if dict_form.get(username) == password:
            print("Login SUccess")
            ch = input("""1. Show detail
2. Add Balance""")
            if ch == "1":
               pass
            elif ch == "2":
               pass
            else:
               pass