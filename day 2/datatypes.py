# Datatype

# String - are defined using single or double quotes

a = 'hello world\'s 1524 2#*($(*#))'             
a = "hello \"world\"'s"
a = '''hello
"World"
ajdsfkl's
'''
a = "52"
print(a)       # Override

print(type(a))


# Integer : whole number

b = 52
print(b)
print(type(b))

# Float : decimal number

c = 52.00
print(c)
print(type(c))


# Boolean : True or False
d = True
print(d)
print(type(d))


# NoneType : represents absence of value
e = None
print(e)
print(type(e))

# Group datatype 
# List: [] is used to define a list, ordered, mutable(changeable), allows multiple data of different datatypes
my_list = [1, 2, 3, "hello", 5.6, True,3,3]
print(my_list)
print(type(my_list))


# Tuple: () is used to define tuple, ordered, immutable(can't changed) ,allows multiple data of different datatypes
my_tuple = (1, 2, 3, "hello", 5.6, True,3,3,[1, 2, 3, "hello", 5.6, True,3,3],(1, 2, 3, "hello", 5.6, True,3,3))
print(my_tuple)
print(type(my_tuple))

# Set: {} is used to define set, unordered, no duplicate datas
my_set = {1, 2, 3, "hello", 5.6, True,3,3}
print(my_set)
print(type(my_set))


# Dictionary: {} is used to define dictionary, unordered, key:value pair, key must be unique
my_dict = {1:"dia", 2:"ram","address":"KTM"}
print(my_dict)
print(type(my_dict))


