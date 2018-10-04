# debugging WHAT WHAT 
# to be fair to myself, I disabled any sort of syntax highlighting for this exercise
# to keep it enabled would unfairly aid me in spotting easy typos, etc et al

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ') # we're missing an assignment here to assign the value input to the variable height
height = input()
print("How much do you weigh?", end=' ') # was missing a closing parenthesis
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

from sys import argv
script, filename = argv # we're missing the from sys import argv at the top here

txt = open(filename) # there's a typo in the argument filenme

print("Here's your file {filename}:")
print(txt.read()) # the txt ariable was mispelled

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read()) # the read method was not called correctly, should be variable.method()

print('Let\'s practice everything.') # the apostrophe was not escaped
print("""You\'d need to know \'bout escapes 
      with \\ that do \n newlines and \t tabs.""") # pretty sure this isnt valid syntax for a multiline print, should be triple single quote or triple double-quote but not a mix of the two, womp womp

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") # missing the closing double-quote. man, got to keep an eye out for when this text editor auto-types the closing single- or double-quote
print(poem)
print("--------------") # missing the opening double-quote


five = 10 - 2 + 3 - 6 # this is either missing a final integer or has an extra subtraction sign...missing 
print(f"This should be five: {five}") # this was also missing a closing parenthesis...do the math, is it missing the integer? Yep, to be correct it should be 10 - 2 + 3 - 6

def secret_formula(started): # missing the colon
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars * 100 # was missing the multiplication character
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # we're attempting to unpack the output of of the function secret_formula into 2 variables. trouble is, this function returns 3 variables

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an format sstring
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) # typo in the argument name
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30 # typo in this variable, it should be cats
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!") # this is missing both open and closing parenthesis

if people > cats: # the same conditonal as before. the string we're printing suggests that we should reverse the conditional such that count of people is greater than cats
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: # missing a colon
    print("The world is dry!")


dogs += 5 # so now the value assigned to dogs is 20

if people >= dogs: # values assigned to people and dogs are equal
    print("People are greater than or equal to dogs.")

if people <= dogs: # values assinged to people and dogs are equal AND missing a colon
    print("People are less than or equal to dogs.") # gotcha! was missing a double-quote

if people == dogs: # a single equals sign signifies assignment, we'd want a double for comparison
    print("People are dogs.")