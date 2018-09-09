# reading files!
# this exercise involves writing two files, our usual python py file as well as a text file named ex15_sample.txt
# the goal is use our script to OPEN this file (hint: the file is already filled with text) and PRINT it out

from sys import argv # import the sys module

script, filename = argv # require the name of the file before proceeding and store that in argv

txt = open(filename) # call the open method/function passing along the paramater filename that we supplied when we first ran the script

print(f"Here's your file {filename}:\n")
print(txt.read()) # call the read method on the open file without any additional parameters
print("\n") # print a new line
print(f"Closing {filename}...")
txt.close() # call the close method on the opened file without any additional parameters
print(f"{filename} was open but now it is closed.")

print(f"Please, type the name of the file once again (hint: type {filename}): ") # do some fancy stuff here to suggest the file to be input at the following prompt
file_again = input("> ") # assign the new filename in a variable file_again

text_again = open(file_again) # call the open method/function passing along the argument (or parameter) of the file name provided from the prompt above

print(f"Great, here are the contents of {file_again}:\n")
print(text_again.read()) # call the read method once again on the new file without any additional parameters
print("\n")
print(f"Closing {filename}...")
txt.close()
print(f"{filename} was open but now it is closed.")
