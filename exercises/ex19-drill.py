# 99 bottles of root beer on the wall

def ninety_nine(a):
	a = a
	print("Ninety nine bottles of root beer on the wall...")
	print(f"Take {a} down, pass it around and ")
	bottles_remaining = (99 - a)
	print(f"Now we have {bottles_remaining} botles of root beer on the wall!\n")

# one
ninety_nine(1) # take one down and pass it around
# two
ninety_nine(-1) # subtract a negative one? doesnt make the song sound great
# three
ninety_nine(1 + 1) # add one plus one
# four
ninety_nine(1 - 1) # subtract one from one
# five
ninety_nine(1 * 10) # multiply 1 by 10 ... reminder to use an asterix here and not a x!
# six
ninety_nine(10 % 1) # modulus of 10 subtracted by 1
# seven
homebrews = 22
ninety_nine(homebrews) # pass along the value assigned to the variable homebrews as the argument when we call ninety_nine
# eight
homebrews = homebrews - 10 # assign the result of the value assigned to homebrews subtracted by 10 as the new value for the variable homebrews
ninety_nine(homebrews) # use the variable as the argument once again
# nine
ninety_nine(homebrews * 3) # use the variable and multiply it by 3
# ten
ninety_nine(99) # just for fun