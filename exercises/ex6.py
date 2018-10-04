# strings and text, yo
# a string is usually a bit of text you want to display to someone or "export" out of the program you are writing
# python knows that you wan something to be a string when you put either " (double-quote) or ' (single quote) around the text
# strings may contain any number of variables in your script
# a variable is any line oc code where you set a name = (equal) to a value (assignment)
# python also has another kind of formatting using the .format() syntax, but we'll cover that more later

# here we are assigning the variable types_of_people the value of 10 (integer)
types_of_people = 10
# assign this formatted string to the variable x
x = f"There are {types_of_people} types of people." # an integer placed inside a string

# assign this string to the vaiable binary
binary = "binary"
# assign this string to the variable do_not, to possibly avoid using the escape character slash /
do_not = "don't"
# assign this formatted string to the variable y
y= f"Those who know {binary} and those who {do_not} (ha ha ha)." # two strings placed inside another string

# print the variable x
print(x)
# print the variable y
print(y)

# print the formatted string that includes the variable x
print(f"I said: {x}") # a string placed inside another string
# print the formatted string that includes the variable y in single quotes
print(f"I also said: '{y}'") # a string placed inside another string placed inside single quotes

# assign the boolean value of False to the variable hillarious
hillarious = False
# assign a string that contains a placeholder for a variable that we will pass in as an argument or parameter when we print it
joke_evaluation = "Isn't that joke so funny?! {}"
# print the string assigned to the variable joke_evaluation and include the boolean assignment for the hillarious variable, too
# print(joke_evaluation.format(hillarious))

# lets try to pass in a different variable here...hey, it works!
# print(joke_evaluation.format(types_of_people))

w = "This is the left side of..."
# whoops, had a typo on my first go around
e = "a string with a right side."
# combine or concatenate the two strings assigned to variables w and e, respectively
print(w+e)