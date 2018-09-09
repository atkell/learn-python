# reading files!
# this exercise involves writing two files, our usual python py file as well as a text file named ex15_sample.txt
# the goal is use our script to OPEN this file (hint: the file is already filled with text) and PRINT it out

from sys import argv # import the sys module

script, filename = argv # require the name of the file before proceeding and store that in argv

txt = open(filename) # call the open method to open the filename we provided when we executed the script from the terminal

print(f"Here's your file {filename}:")
print(txt.read()) # call the read method on the open file

print(f"Please, type the name of the file once again (hint: type {filename}): ")
file_again = input("> ") # assign the new filename in a variable file_again

text_again = open(file_again)

print(text_again.read())
