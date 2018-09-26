# strings, bytes and character encodings
# the plot thickents, my friends...mark one for experience
# to do this right we'll need to download a file from Zed located at https://learnpythonthehardway.org/python3/languages.txt
# and remember we decode bytes and encode strings (DBES)

# in this exercise we'll explore a few things like....
#	1. how modern computers store human languages for display and processing nad how Python3 calls this `strings`
#	2. how you must "encode" and "decode" Python's strings into a type called `bytes`
#	3. how to handle errors in our string and byte handling
#	4. how to read code and find out what it means even if you've never seen it before

# note from zed – this one is complex, don't get tripped up. feel free to work on other exercises and come back to this one
# also Im listening to In Rainbows on this one

import sys # import that sys module
script, encoding, error = sys.argv # slight modification if the typical unpacking we've performed in the past

def main(language_file, encoding, errors):
	line = language_file.readline() # we know readline() at this point
	# if is new for us

	if line: # if there is a line, then do some stuff. in other words, this basicall says if something_here is True, then do somethings...
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors) # hello old friend, return

def print_line(line, encoding, errors):
	next_lang = line.strip() # strip() is a new function for me
	raw_bytes = next_lang.encode(encoding, errors=errors) # encode() is a new function, too
	cooked_string = raw_bytes.decode(encoding, errors=errors) # decode() is also new function, too

	print(raw_bytes, "<=====>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)

# modern computers are incredibly complex, but at their cores are like a huge array of light switches. computers use electricial to flip these switches on or off.
# these switches may represent 1 for on an 0 for off. we call these 1's and 0's bits.
# at the small end a computer will use 8 of these bits (1s and 0s) to encode 256 numbers (0-255)
# but what does encode mean? good question, it is merely an ageed-upon standard for how a sequence of its should be represented as a number
# today we call a "byte" a sequence of 8 bits (1s and 0s)

# once we have bytes, we may store and display text by decideing on another convention for how a number maps to a letter
# the most popular convention ended up being the American Standard Code for Information Interchange or ASCII – this standard maps a number to a letter, like 90 is Z or in bits (binary) 1011010 
# so in effect a string is merely a sequence of bytes
# To write my name, A T Kell (the caps make a difference!), in binary would be [65, 84, 75, 101, 108, 108] (hint I used ord('A') and char('90') commands to figure this out)
# most text in early computers was nothing more than this, a sequence of bytes stored in memory

# the trouble here is that ASCII only encodes English and some other languages, but not all of them which means we're SOL if we try and drop some Thai into our English
# to solve this a group of wonderful people created Unicode (universal encoding) which allows us to use 32 bits to encode a Unicode character
# a 32 bit number means we can store 4,294,967,295 characters which is ... a good bit, to say the least!

# the trouble is that this means we have a good bit of wasted space in most text we want to encode (consider all the space characters in this comment, e.g.)
# the solution here is use a clever convetion to enclode most common characters using 8 bits, then escape to into larger numbers when we need to encode more characters
# so, we have one more convetion here that is nothing more than a compression encoding, making it possible for most common characters to use 8 bits and then escape out into 16 or 32 bits as needed

# we call this convention for encoding text in Python UTF-8 or "Unicode Transforation Format 8 Bits".
# this allows us to encode a series of bytes, which are sequences of bits which then turn sequenes of switches (1s and 0s) on and off.
# other conventions (encodings) exist but for now UTF-8 is the current standard