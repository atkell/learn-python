# more fun with files
# here we'll write a python script to copy one file to another. it'll intentionally be short but will give us an idea of about other things we may do with files

from sys import argv # import argv method from the sys module 
from os.path import exists # import the exists method from the os.path module

script, from_file, to_file = argv # unpack the contents of argv into these variables, si vous plez

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, but how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file really exist? {exists(to_file)}") # the exists module will return True or False here
print("Hit RETURN to continue or ^C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()