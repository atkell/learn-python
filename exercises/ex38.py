# Exercise 37 was a symbol review
# Doing things to lists, huzzah!

# When we write mystuff.append('hello'), a few things are actually happening:
#   1. Python sees that we mentioned mystuff and looks up the variable
#   2. Once Python finds mystuff, it reads the "." operator (the period) and starts to look at variables that are part of mystuff.
#      Since mystuff is a list, it knows that mystuff has a bunch of avaible functions (like append)
#   3. It then hits append and compares the name to all the names that mystuff says it owns. If append is there (it is), Python grabs it.
#   4. Next, Python sees the open parenthesis and realizes "oh hey, this should be a function" and then calls the function (aka runs or executes)
#      just like normal, but it cals the function with an extra argument.
#   5. That extra argument is ... mystuff! Weird, right? What happens, at the end of all this, is a function call that looks like append(mystuff, 'hello')
#      instead of what we read, which is mystuff.append('hello')

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print(ten_things)

print("Wait there are not 10 things in that list. Let's address that.")

stuff = ten_things.split(' ') # here we call Split method on ten_things. Alternatively, we could call Split with 2 arguments: ten_things and ' ': split(ten_things, ' ')
print(stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee", 
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # Here we call Pop methdo on more_stuff. Alternatively, we could call Pop with argument more_stuff: pop(more_stuff)
    print("Adding: ", next_one)
    stuff.append(next_one) # Here we call Append method on stuff with the argument next_one. Alternatively, we could call Append with arguments stuff and next_one: append(stuff, next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff) # Here we call the Print method (function) with arguments "There we go: " and stuff. Could we alternatively write stuff.print("There we go: ")?
stuff.print("There we go: ") # Is the output here the same as above? This actually causes an AttributeError: 'list' object has no attribute 'print'. So no, we could not rewrite this in this manner.

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # Fancy?
print(stuff.pop())
print(' '.join(stuff))
print('\n'.join(stuff)) # Very useful for printing out list contents for our basic inventory system
print('#'.join(stuff[3:5]))
