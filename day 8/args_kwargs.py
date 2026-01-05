# Args: *arg_name is used to define args, it allows function to take multiple positional arguments, it returns tuple
# def Introduction(*args):     # function definition with parameters(n,a)
#    print(args)
#    print(args[1])
#    for i in args:
#       print(i)


# name = "Ram"
# age = "30"
# Introduction(name,age, "Ktm","*985465655","a@gmail.com","male","sdjhfskld","sldfj")


# # Kwargs: **kwarg_name is used to define kwargs, it allows function to take multiple keyword arguments, it returns dictionary
# def Introduction(**kwargs):     # function definition with parameters(n,a)
#    print(kwargs)
#    for key, value in kwargs.items():
#       print(f"{key}: {value}")


# name = "Ram"
# age = "30"
# Introduction(Name = name, Age = age, Address = "KTM", Contact = "9565463351")


def Introduction(name,*args,**kwargs):     # function definition with parameters(n,a)
   print(name)
   print(args)
   print(kwargs)
   for key, value in kwargs.items():
      print(f"{key}: {value}")


name = "Ram"
age = "30"
Introduction(name, age, "ram","b","shyam",Address = "KTM", Contact = "9565463351")


# todo:
# Accounting program
# create a dictionary with username and password where username is key and password is value
# create a dictionary with username and bank_balance where username is key and bank_balance is value
# get user ko username and password 
# check if the username exists and the password matches . if yes print login successful else print login failed
# if login is successful, show 2 options, 1. Show user details, 2. Add Balance
# if user choice 1, show user details (username and bank balance)
# if user choice 2, get amount to add from user, add the amount to bank balance and show updated bank balance

# function based, while loop, exception handling