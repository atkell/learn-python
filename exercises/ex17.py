# more fun with files
# here we'll write a python script to copy one file to another. it'll intentionally be short but will give us an idea of about other things we may do with files

from sys import argv # import argv method from the sys module 
from os.path import exists # import the exists method from the os.path module

script, from_file, to_file = argv # unpack the contents of argv into these variables, si vous plez

# print(f"Copying from {from_file} to {to_file}") # study drill 1: this script is annoying, try removing superflous lines where possible

# we could do these two on one line, but how?
in_file = open(from_file)
indata = in_file.read()
# indata = open(from_file, 'r')

# print(f"The input file is {len(indata)} bytes long") # study drill 1: this script is annoying, try removing superflous lines where possible

# print(f"Does the output file really exist? {exists(to_file)}") # the exists module will return True or False here # study drill 1: this script is annoying, try removing superflous lines where possible
# print("Hit RETURN to continue or ^C to abort.") # study drill 1: this script is annoying, try removing superflous lines where possible
# input() # study drill 1: this script is annoying, try removing superflous lines where possible

out_file = open(to_file, 'w')
out_file.write(indata)

# print("Alright, all done.")  # study drill 1: this script is annoying, try removing superflous lines where possible

out_file.close()
in_file.close()