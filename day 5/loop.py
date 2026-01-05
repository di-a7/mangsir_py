# Loop : to execute a block of code multiple times
# iteration

# while loop: conditional 
# a = 0
# b = 3
# while a < b:
#    print("hello world")
#    a += 1

# continue: end the current iteration and start new iteration 
a = 0
b = 5
while a < b:
   a += 1
   if a == 2:
      continue
   print("hello world", a)
   print("hello world", a)
print("OUTSIDE WHILE after continue")


# break: terminate the loop
a = 0
b = 5
while a < b:
   a += 1
   if a == 2:
      break
   print("hello world", a)

print("Outside while after break")

# todo:
# implement while loop in simple calculator
