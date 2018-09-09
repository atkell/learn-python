# reading and writing files
# in the previous exericse and corresponding study drills we tried all sorts of commands (aka methods/functions) on a file
# here are a few more that are worth remember...
#	close: closes the file similar to using the File menu and selecting the Save menu option
#	read: reads the contents of the file. can assign the results of a variable should we so desire
#	readline: reads just one line of a text file, accepts the parameter for that line
#	truncate: empties the file
#	write: accepts a string as a paramter like write('stuff') to write "stuff" to the file
# 	seek(): moves the read/write location to a specific line. accepts the paramter of line number like use seek(0) to return to the beginning of the file

from sys import argv # import the sys module

script, filename = argv # unpack argv into script and filename variables

print(f"We're going to erase {filename}...")
print("If you don't want that, hit CTRL-C (^C)...")
print("But if you do want that, go ahead and hit that there RETURN key...")

input("Choose your adventure (hit RETURN to proceed or ^C to cancel) > ") # ask the user to proceed or cancel

print("Opening the file...")
# call the open method with the paramters filename (from prompt above) and w such that the file is not opened in read-only mode
target = open(filename, 'w') # whoops! this resulted in a NameError...this option is actually a string and needs to be enclosed in quotes...
print("Huzzah! Zee file, it is open ~.~")

# we don't really need the truncate method given that we're opening the file in write-mode
# print("Truncating the file. Goodbye!")
# target.truncate() # empty the contents of the file defined as target
# print("Truncation complete...")

print("Now I'm going to ask you for three lines...")

line1 = input("line 1: ") # ask the user for an input
line2 = input("line 2: ") # ask the user for more input
line3 = input("line 3: ") # ask the user for even more input

print(f"Thanks! Now I'm going to write these to the {filename} file.")

# target.write(line1) # write the contents of line1 to the file we've assigned to the variable target
# target.write("\n") # write a new linw to the file
# target.write(line2) # write the contents of line2 to the file
# target.write("\n") # write a new line to the file
# target.write(line3) # write the contents of line3 to the file
# target.write("\n") # write a new line to the file

# study drill 3 -- remove the repitive use (6 lines) of target.write above and re-write this into a single command w/ stings, formats and escapes
target.write(f"{line1}\n{line2}\n{line3}\n")

# we could probably print this out and show the user with another print.
print("Ah yes, a fine piece of work indeed Bashō-san")

print("And finally, we close this sweet file.")
target.close() # close the file
print("The file, she be closed.")

