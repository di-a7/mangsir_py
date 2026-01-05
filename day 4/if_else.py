# if else: conditional statement, multilined statement
# if the condition is True, the block of code inside the if block is executed
# elif takes conditions, multiple elif can be defined
# else: if all the conditions in if and elif are false, else block executed
# if condition:
#    statments1
#    statments2
#    statments3

a = 10
b = 15
c = 5
# # print a is greater b than print a is greater
if a > b:
   if a > c:                           # Nested
      print("A is greater than C")
   elif a < c:
      print(" A is greater than B")
elif a < b:
   if a > c:                           # Nested
      print("A is greater than C")
   elif a < c:
      print(" A is greater than B")
   print("B is greater")
elif a == b:
   print("A and B are equal")
else:
   if a > c:                           # Nested
      print("A is greater than C")
   elif a < c:
      print(" A is greater than B")
   print("Else block")

# todo:
# create a list of names
# get a name from user 
# check if the name exists in the list of names, 
#  if yes print a statement like "Name" exists.
#  if no print out a statement

# get 2 numbers from user
# check which one is greater and print it out

# Simple Calculator
# get 2 number from user
# get a operator(+,-,/,*) from user
# if operator is +, add two numbers
# if operator is -, subtract two numbers
# if operator is /, divide two numbers
# if operator is *, multiple two numbers

# Mark Evaluator
# ask user for their exam mark
# if the mark of user is greater or equal than 90 and less than 100, print "Excellent"
# if the mark of user is greater or equal than 80 and less than 90, print "Very Good"
# if the mark of user is greater or equal than 70 and less than 80, print "Good"
# if the mark of user is greater or equal than 60 and less than 70, print "Better"
# if the mark of user is greater or equal than 50 and less than 60, print "Fair"
# if the mark of user is greater or equal than 40 and less than 50, print "Pass"
# if the mark of user is less than 40, print "Fail"

# Even Odd
# get a number from user
# check if the number is even or odd

# ask the age of the user # Nested
# if the age is greater or equal to 18, ask the user if they have license, if yes print out a statement, if not print out a statement
# if the age is less 18, ask the user if they want to get license, if yes print out a statement, if no print out a statement
# if the age in not a number, print out a statement



# user_data = input("Enter your name: ") # input string datatype store
# print(type(user_data))

# abc = int(user_data)
# print(type(abc))