# indexing and slicing

# indexing : access single character or data from sequential datatype
a = "mindriser"
# # m = 0
# # i = 1
# # n = 2
# # d = 3
# # r = 4
# # .

# print(a[3])

# b = "I am learning ( python."
# access (

# animals = ["cat","dog","apple","cow","goat"]
# # "cat" = 0
# # "dog" = 1
# # access apple
# animals[2] = "abc"
# print(animals)

# Slicing: get a subset or a part of the sequential data
a = "mindriser"
# a[start_index: end_index+1]
# print mind from variable a
print(a[:])

b = "I am learning ( python."
# get learn
# get python
# get I am learning

animals = ["cat","dog","apple","cow","goat"]
# animals[1:4] = "abc","djlfke"
# print(animals[2:])

# variable[start_index: end_index + 1: step]
print(animals[0:5:1])
print(animals[0:5:2])
print(animals[::3])

a = "mindriser"
animals = ["cat","dog","apple","cow","goat"]

# todo:
# print out the data in even position
# print out the data in odd position
# print out mindrisers in reverse
# print out the reverses of data in animals variable