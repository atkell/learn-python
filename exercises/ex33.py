# while loops continue to execute the code block under it so long as the boolean expression is True
# the trouble is sometimes these loops just don't stop. to avoid this, let's follow some rules:
#   1. Make sure that we use while-loops sparingly, usually a for-loop is better
#   2. Review while statements and make sure that the Boolean test will become False at some point
#   3. When in doubt, print out your test variable at the top and bottom of the while-loop to see what it is doing
# we'll learn the while-loop while doing these three checks in this exercise...

# i = 0
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i) # remember what append does to a list?

#     i = i + 1
#     print("The contents of the Numbers list are now: ", numbers)
#     print(f"At the bottom i is {i}\n")

# print("The numbers: ")

# for num in numbers:
#     print(num)

# can we re-write this and 
#   1. convert our while-loop to a function 
#   2. use this function to rewrite the script to try different numbers
#   3. add another variable to the function arguments that allows us to change the number we increment the "i" on line 15

# this function accepts two arguments:
#   where "a" is the number we're using as part of our boolean evaluation
#   and "b" is the number we're incrementing "i" by on line 40 as part of our loop
def loop(a,b): 
    i = 0
    numbers = []

    while i < a:
        print(f"At the top i is {i}")
        numbers.append(i) # remember what append does to a list?

        i = i + b
        print("The contents of the Numbers list are now: ", numbers)
        print(f"At the bottom i is {i}\n")

# loop(6,2)

# bonus round: can we re-write this such that we prompt the user to input a and b?
# we'll need to wrap our input with the int() method so that the values passed into 
# our function are evaluated as integers and not strings

def loop2(a,b): 
    i = 0
    numbers = []

    if (a <= 0) and (b <= 0):
        print("Whoops, both of the numbers you entered wont work. Let's try this again...")
        a = int(input("i < a, where a is == "))
        b = int(input("i = i + b, where b is == "))

    elif a <= 0:
        print("Whoops, one of the numbers you entered wont work. Let's try this again...")
        a = int(input("i < a, where a is == "))

    elif b <= 0:
        print("Whoops, one of the numbers you entered wont work. Let's try this again...")
        b = int(input("i = i + b, where b is == "))

    while i < a:
        print(f"At the top i is {i}")
        numbers.append(i) # remember what append does to a list?

        i = i + b # this cannot be <= 0 otherwise it'll loop forever
        print("The contents of the Numbers list are now: ", numbers)
        print(f"At the bottom i is {i}\n")

boolean = int(input("i < a, where a is == "))
increment = int(input("i = i + b, where b is ==  "))

loop2(boolean,increment)

# for-loops vs. while-loops
#   for-loops iterate (loop) "over" a collection of things
#   while-loops are capable of any kind of iteration (looping) we desire