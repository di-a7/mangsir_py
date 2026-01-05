# Exception Handling
# multiple try-except blocks can be defined in a program
# a try have single except block but it can have multiple error specific except blocks 

# in the program below 
# if try block rises valueerror, the except ValueError block is executed
# if try block rises  nameerror, the except NameError block is executed
# if try block rises  any other errors beside value and name errors they are handled by except block

try :
   a = int(input("enter a number:"))
   print(a + 10)  
except ValueError:
   print("Enter Number")
except NameError:
   print("A is not defined")
except:
   print("Except block")

# todo:
# implement exception handling in simple calculator (day 5)
# implement while loop and exception handling in Mark Evaluator (day 4)
# implement while loop and exception handling in Even Odd (day 4)
# implement while loop and exception handling in task 2 (day 5)
# implement while loop and exception handling in weight conversion program (day 5)