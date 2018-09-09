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

input("Choose your adventure (hit RETURN to proceed or ^C to cancel) > ")

print("Opening the file...")
# call the open method with the paramters filename (from prompt above) and w such that the file is not opened in read-only mode
target = open(filename, 'w') # whoops! this resulted in a NameError...this option is actually a string and needs to be enclosed in quotes...
print("Huzzah! Zee file, it is open ~.~")

print("Truncating the file. Goodbye!")
target.truncate()
print("Truncation complete...")

print("Now I'm going to ask you for three lines...")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Thanks! Now I'm going to write these to a file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# we could probably print this out and show the user with another print.
print("Ah yes, a fine piece of work indeed Bashō-san")
# print(read(filename)) # did this do what we wanted it to?...maybe if it didnt genera te syntax error, hah
# no, this didnt work because it was formatted incorrectly
print(filename.read()) # lets try this instead

print("And finally, we close this sweet file.")
target.close()
print("The file, she be closed.")

