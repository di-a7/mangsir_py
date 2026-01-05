# Typecasting: change a datatype to another

a = "120"
print(type(a))

# int()
to_int = int(a)
print(to_int)
print(type(to_int))

# float()
to_float = float(a)
print(to_float)
print(type(to_float))

# str()
to_str = str(to_float)
print(to_str)
print(type(to_str))

# Group type
# list()
l = list(to_str)
print(l)
print(type(l))

# tuple()
t = tuple(l)
print(t)
print(type(t))

# set()
s = set(t)
print(s)
print(type(s))

# dict(): key value
a = [("1","apple"),("name","ram"), ("2","ram"), ("3","ram")]
b = dict(a)
print(b)
print(type(b))


# todo:
# words = ["python","api","backend","python","database","api","server","backend","deployment","python"
# ]
# remove duplicate datas from the list

# animals = ("cat","dog","cow","goat")
# check if lion exist in the tuple

# get a 2 number from user
# and compare if the first number is greater than the later

# animals = ("cat","dog","apple","cow","goat")
# change the data apple to tiger

# typecast to list
# animals[2] = tiger