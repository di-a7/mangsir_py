# Function: like variables but intead of values or data it holds a block of code , functions are used to perform a specific task

# syntax
# def function_name():
#    # block of code

# def hello():
#    print("Hello World!")

# hello()  # function call

# Positional Arguments
# def Introduction(n,a):     # function definition with parameters(n,a)
#    print(f"Hello, my name is {n} and I am {a} years old.")

# name = "Ram"
# age = "30"
# Introduction(age,name)     # function call with arguments(name,age)
# Introduction(name,age)     # function call with arguments(name,age)


# # Keyword Arguments
# def Introduction(n,a,add):
#    print(f"""Name: {n}
# Age: {a}
# Address: {add}""")

# name = "Ram"
# age = "30"
# address = "KTM"
# Introduction(add = address, a = age, n = name)



# # Default Arguments
# def Introduction(n = "User",a = "50",add = "Earth"):
#    print(f"""Name: {n}
# Age: {a}
# Address: {add}""")

# name = "Ram"
# age = "30"
# address = "KTM"
# Introduction(add = address,a = age,n= name)

# return: by default function reatun None, end the function
y = 50         # y is global variable, can be used anywhere in the program
def add(a,b):
   global y
   z = a + b      # z is local variable, can be used only inside this function
   y = z + y
   return z

p = add(10,2)
print(p)


# todo:
# simple calculator (day 6) with functions
# weight conversion program with functions


