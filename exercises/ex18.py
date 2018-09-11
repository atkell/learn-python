# names, variables, code and functions
# dum dum dah! introducing the function (or proceudre)
# functions do three things:
#	1. they name pieces of code the way variables name strings and numbers
#	2. they take arguments the way our prior scripts take argv
#	3. using 1 and 2, funcrions let us make our own "mini-scripts" or "tiny commands"

# def something(argument):
#	indent and do something 

# this one is like our scripts with argv
def print_two(*args): # don't forge this colon!
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is basically pointless, we can just do this instead
def print_two_again(arg1, arg2): # you forgot the colon again
	print(f"arg1: {arg1}, arg2: {arg2}")

# this function takes just a single argument
def print_one(arg1): # really, dude, pay attention
	print(f"arg1: {arg1}")

# and this one takes no arguments
def print_none(): # colon, not a semi-colon like the first time I did this and created a syntax error
	print("I got nothing here.../shrug")

# and now we'll call our functions, passing arguments through each where applicable
# remember, when we use functions we may say "run", "call" or "use"...all meams the same thing
print_two("The","Expanse")
print_two_again("The","Expanse")
print_one("Rocinante")
print_none()