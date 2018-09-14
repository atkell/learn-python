# functions and files and such
# dont forget to use the checklist here if we get caught up

from sys import argv # import the sys module

script, input_file = argv # unpack argv into two variables, script and input_file

def print_all(f): # create a new function and name it print_all. this function accepts a single argument, f
	print(f.read()) # call the read function on the argument, f, which will be a file...maybe and then print it all out!

def rewind(f): # create a new function and name it rewind. this function accepts a single argument, f
	f.seek(0) # call the seek function on the argument, f, with the option 0 which will tell python to move from the current line back to line 0 or the beginning / start of the file
	# so what I wrote here is actually incorrect. seek is not about line numbers but rather bytes. so seek(0) moves the file to the 0 byte (first byte) of the file

def print_a_line(line_count, f): # create a new function and name it line_count. this function accepts two arguments, line_count and f
	print(line_count, f.readline()) # pass in the arguments of line_count (probably a line number) and then call the function readline() on whatever is assigned to the variable f

current_file = open(input_file) # create a new variable called current_file and assign it to the output of calling the function open() on the contents of input_file

print("First lets print the entire file:\n")

print_all(current_file) # call the print_all function and provide the argument with the contents of what is assigned to the variable current_file

print("Now let's rewind, kinda like a tape.")

rewind(current_file) # call the rewind function and provide the argument with the contents of what is assigned to the variable current_file

print(f"Let's print three lines from {input_file}:")

current_line = 1
print_a_line(current_line, current_file) # call the print_a_line function and give it two arguments, the value assigned to the variable current_line AND the output assigned to current_file

# current_line = current_line + 1 # getting fancy here...increase the value assigned to current_line and then assign that to current_line. we could also rewrite this but how?
current_line += 1 # this is a bit simpler, no?
# this sets the value of curent line to 2
print_a_line(current_line, current_file) # the same as line 30 ... but a different output

# current_line = current_line + 1 # the same as before but now plus one # we could also rewrite this but how?
current_line += 1 # mmm less to type sounds great to me
# this sets the value of curent line to 3
print_a_line(current_line, current_file) # the same as line 33 ... but a different output

