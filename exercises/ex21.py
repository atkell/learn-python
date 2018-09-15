# functions can return something
# here we will learn how to use return to set variables to be a value from a function
import random # we want this for our extension below

def add(a, b): # add a space here for legibility
	print(f"Now adding {a} and {b}...")
	return a + b

def subtract(a, b):
	print(f"Now subtracting {b} from {a}...")
	return a - b

def multiply(a, b):
	print(f"Now multiplying {a} by {b}...")
	return a * b

def divide(a, b):
	print(f"Now dividing {a} by {b}...")
	return a / b
 
print("Cool, let's do some math by calling or using our functions!")

age = add(30, 2) # let's just say I am 32 years old
height = subtract(70, 3) # and lets say I'm 5'7" or 67"
weight = multiply(102, 2) # and that I weight 204 lbs
iq = divide(100, 2) # just dont try to divide this by 0, heh

print(f"""
Alright then, lets see here...
You said that you're {age} years old and
that you're about {height} inches tall and
weigh approximtely {weight} pounds.
Normally, I wouldn't ask about intelligence but since you broached the topic...you said {iq}
""")

# A puzzle for extra credit...
print("So, here's a puzzle...")
# fancy footwork here. we're using the return value of one function as an argument of another and so on and so forth
# could we rewrite this in a less complex way, just for the sake of understanding?
what = add(age, subtract(height, multiply(weight, divide(iq,2)))) # don't forget the order of operations here...PEMDAS
# so in essence were're first dividing our IQ by 2, then multiplying it by our weight, then subtracting height by this value and finally adding the resulting value to our age
# what2 = age * (height - (weight * (iq / 2))) # this was wrong, lets try again...DUH, I multiplyed age by all this junk, should have just added it.
what3 = age + (height - (weight * (iq / 2))) # yeah baby!

print("That becomes: ", what, "Can you do it by hand?")
# print(f" Is {what2} the same value?")
print(f" Is {what3} the same value?") # to quote my friend michael, "bingo bango

######
# could we do this by prompting the user for input instead of hardcoding age, height and weight? I bet we could :D
input_age = float(input("How old are you?  ")) # we have to enclose our input with the float function for reasons that are complicated but simple. inda like how we had to use int() in a prior exercise. basically, we could get a decimal here.
input_height = float(input("How tall are you, in inches?  "))
input_weight = float(input("How much do you weigh, in pounds?  "))
input_iq = float(input("What is your IQ in ... uh I guess, intelligence points?  "))

age = add(input_age, random.randint(1, 10))		# take the input from the user and add it to a random integer, between 1 and 10 
height = subtract(input_height, random.randint(1, 10))	# take the input from the user and subtract it by a random integer, between 1 and 10
weight = multiply(input_weight, random.randint(1, 10))	# take the input from the user and multiply it by a random integer, between 1 and 10
iq = divide(input_iq, random.randint(1, 10)) 		# take the input from the user and divide it by a random integer, between 1 and 10

# lets do this rigamaroll once more! I probably mispelled that word...terribly.
print(f"""
Alright then, lets see here...
You said that you're {age} years old and
that you're about {height} inches tall and
weigh approximtely {weight} pounds.
Normally, I wouldn't ask about intelligence but since you broached the topic...you said {iq}
""")