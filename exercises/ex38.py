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

stuff = ten_things.split(' ')
print(stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee", 
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # fancy?
print(stuff.pop())
print(' '.join(stuff))
print('\n'.join(stuff)) # very useful for printing out list contents for our basic inventory system
print('#'.join(stuff[3:5]))
