# this exercise is intentionally long and all about building up stamina
# the next exericse will be the same. do them both, get them exactly right and do your checks

print("Let's practice everything we know thus far...")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("----------")
print(poem)
print("----------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	# print out the three variables assigned within this function
	return jelly_beans, jars, crates

start_point = 10000
# unpacking the output of the function secret_formula into 3 new variables: beans, jars and crates. remember that the variable names within the fucntion are just that, within the function and not globally available (scope)
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like an f"" string
print(f"We'd have {beans} beans, {jars} jars and {crates} crates.")

# remember that the variable is interpreted from the top down, so while the value above this assignment was different, it is about to change
start_point = start_point / 10

print("We can also do that this way:")
# we're assigning the output of calling the secret_formula, argument of start 
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))