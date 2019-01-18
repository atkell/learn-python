# Modules, Classes and Objects

#######
# Modules are like Dictionaries
# We now know how dictionaries are created and used and how we may map (or relate or associate)
# one thing to another (key:value pair). This means that if we have a dict with key "apple" and we
# want to get it then we must do this:

mystuff = {'apple': 'I am apples for bannanas!'}
print(mystuff['apple'])

# Let's keep this idea of "get X from Y" in our heads while we explore modules. In fact, We've
# actually made a few so far, and we should remember them:
#   1. A Python file with some functions or variables in it...
#   2. Which we may then import...
#   3. And access the functions or variables of using the . (dot) operator.

# Let's imagine that we have a module named mystuff.py and that we put a function inside
# called 'apple'. Here's the module for mystuff.py:
def apple():
    print('I am apples for bananas!')

# Now that we have this code, we may import the module MyStuff with the import command, allowing
# us to access the 'apple' function:
import mystuff
mystuff.apple()

# Let's take this a step further and add a variable to our module MyStuff:
def apple():
    print('I am apples for bananas!')

tangerine = "Some line from a Flaming Lips' song about hair color..."

# We may access the 'tangerine' variable in the same manner as before where we accessed MyStuff
import mystuff
mystuff.apple()
print(mystuff.tangerine)

# When we refer back to how we learned about using dictionaries (or dict), we begin to see how
# similar using modules are to using dicitonaries albeit with different syntax. Check it out:
mystuff['apple']    # get apple from dict
mystuff.apple()     # get apple from the module
mystuff.tangerine   # same thing, it's just a variable

# This means that we now see a common pattern in Python:
#   1. Take a key=value style container
#   2. Retrieve something out of it by providing the name of the key

# And in the case of the dictionary, the key is a string and the syntax is [key]. In the case of a
# module, the key is an identifier and the syntax is .key (dot key).

#######
# Classes are like Modules
# We may think about modules as specialized dictionaries that may store Python code which we may
# in turn access with the . (dot) operator. Python has an additional construct that serves a
# similar purpose called a class. A class is a way to take a grouping of functions and data and
# place each inside a container so that we may access them with the . (dot) operator.

# If we were to create a class like our mystuff module, it would look something like this:
class MyStuff(object):

    def __init__(self):
        self.tangerine = "Still cant remember the name of that song..."

    def apple(self):
        print("I am one classy apple!")

# Okay, so this looks (and is) complicated compared to a module; there's definitely much going on
# by comparison. We may understand this class like a "mini-module", with MyStuff having an apple()
# function inside. The __init()__ is most definitely new and confusing but we'll get to that.

# Why classes over modules? We may use the MyStuff class above more than once and each instance (?)
# will not interfere with the other. However, when we import a module, there is only one module for
# the entire program to use (caveat -- there are hacky ways to do this).

# Before we understand this, however, we must learn about an "object" and how to work with MyStuff
# just like we worked with the mystuff.py module

#######
# Objects are like Import
# If we consider that a class is like a "mini-module", then we must consider that there is also a
# concept similar to import (remember, we import modules in our Python scripts) but for classes.
# This concept is called "instantiate", which is a fancy way of saying "create". When we
# "instantiate" (create) a class by callling the class like it is a function, we get something
# called an "object" in return. Like this:
thing = MyStuff() # here we "instantiate" MyStuff by calling it
thing.apple()
print(thing.tangerine)

# Let's break down the behind-the-scenes here step-by-step:
#   1. Python looks for MyStuff() and sees that it is a class we've defined
#   2. Python crafts an empty object with all the functions we've specified in the class using def
#   3. Python then looks to see if we made a "magic" __init()__ function and if so, calls that
#      function to initialize our newly created empty object.
#   4. In the MyStuff function __init()__ we then get an extra cariable, self, which is the empty
#      object Python created on our behalf. We may then set variables on "self" just like we would
#      with a module, dictionary or other object.\
#   5. In this case, you set self.tangerine to a song lyric and then you've initialized this Object
#   6. Now Python can take this newly minted object and assign it to the thing variable for you to work withself.

#######
# Getting Things from Things: We now have 3 ways to get things from things:
# dict style
mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
