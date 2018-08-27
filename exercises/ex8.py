formatter = "{} {} {} {}"
# huzzah! we are introducing the concept of a function
# we're just working with integers here
print(formatter.format(1, 2, 3, 4))
# now we're working with strings
print(formatter.format("one","two","three","four"))
# now we're workign with booleans
print(formatter.format(True, False, False, True))
# now we're calling a our variable 'formatter' four times (should print out 16 pairs of curly braces)
print(formatter.format(formatter, formatter, formatter, formatter))
# now we're printing out a series of strings, using a comma to separate...just like the second line above
print(formatter.format(
	"Try your",
	"Own Text Here",
	"Maybe a poem",
	"About hotdogs and beer"
))