# prompting people
# we can streamline our inputs by moving the strings within our print commands from ex11 into the input itself, still as strings
# we can go a step further and assign the output of this to a variable and then print out a string that is a combination of
# text and variables...

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")