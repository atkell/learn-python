# study drill: write a script similar to ex15 where we use read and argv to read the file we created in ex16
from sys import argv
script, filename = argv
file = open(filename)
print(file.read())