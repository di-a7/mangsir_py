# File handling: process of creating, reading, updating, and deleting files using program.

# to open file
# open("file_path",mode)

# Read mode: read the contents in the file
f = open("file.txt",'r')
a = f.read()
f.close()
print(a)

# Write mode: write the context in the file if the file exists in the location, if file does not exist new file is created, exists data override by new data 
f = open('D:/Teach/magsir/file.txt', 'w')
f.write("method")
f.close()

# append mode: write the context in the file if the file exists in the location, if file does not exist new file is created,  new data is added at the end of the file 
f = open('C:/Users/ittra/Desktop/file.txt', 'a')
f.write(" hello this is append mode")

# todo:
# use file handling to store data of CLI1 program(Account)
# create a file to store userdata and a file to store userbalance