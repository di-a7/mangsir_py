# Identity Operators : output Boolean : value and memory location is same or not
# is : if value and memory location is same output is True else False
a = 10
b = 15
c = 15
print(a is b)
print(id(a))
print(id(b))
print(id(c))

# is not : if value and memory location is same output is False else True
print(a is not b)
