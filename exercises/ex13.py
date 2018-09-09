from sys import argv # import the sys module / library
# read the what you should see (WYSS) section for how to run this
script, first, second, third = argv # take whatever is in argv, unpack it, and assign it to all these variables on the left in order
# attention! if we don't provide 3 variables here, we'll end up with a ValueError: not enough values to unpack

print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# study drill -- combine argv with an input
fourth = input("What's your fourth variable? ")
print(fourth)