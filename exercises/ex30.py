# else and if
# an if statement creates a "branch" in the code
# the if statement uses a colon at the end of it to signify that we're creating a new "block" of code. we indent 4 spaces within this block to let python know that
# what we've written is to be included within the block

people = 30
cars = 40
trucks = 15

# study drills: just playing around with increment by and decrement by operators
cars -= 10
trucks += 14

# so this first conditional is evaluating whether or not value assigned to the variable cars is greater than that of the value assigned to people
if cars > people or people > trucks:
    # if that's true, then print this statement
    print("We should take the cars.")
# otherwise, try this conditional branch instead
elif cars < people:
    # and if this is true, then print this statement
    print("We should not take the cars.")
# however if neither branch above evaluates to true, use this final branch instead
else:
    # and print this statement
    print("We can't decide.")

# note how python is evaluating these branches from top to bottom. it is possible to have multiple branches that are true, but only the first one will be executed

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")   
else:
    print("We still can't decide.") 

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")