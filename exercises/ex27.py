# there's no actual python here as this exercise is all about memorizing logic
# I've created this file just for taking notes...so deal with it

# up to this point we've done everything we possibly could reading and writing files to the Terminal and learned a bit about Python's math capabilities, too
# from now on, we will be learning logic. not complex theories mind you, but the basics that makes real programs work and that we may use every day

# to effectively learn logic we'll be memorizing a few tables. I've done my best to capture those tables below
# the goal is to be able to write these by memory

# the truth terms: in python we have the following terms for determing if something is "True" or "False".
# logic on a computer is all about seeing if some combination of these characters and some cariables is True at that point of the program

# and, or, not
# != or ! followed by the equals sign (not equal)
# == (equal)
# >= (greater-than-equal) 
# <= (less-than-equal)
# True
# False

_________________________ 
| NOT       | True?     |
-------------------------
| not False | True      |
| not True  | False     |
-------------------------

__________________________________ 
| OR                 | True?     |
---------------------------------
| True or False     | True      |
| True or True      | True     |
| False or True     | True      |
| False or False    | False     |
---------------------------------

__________________________________ 
| AND                 | True?     |
-----------------------------------
| True and False     | False      |
| True and True      | True       |
| False and True     | False      |
| False and False    | False      |
-----------------------------------

_________________________________________ 
| NOT OR                 | True?        |
-----------------------------------------
| not (True or False)      | False      |
| not (True or True)       | False      |
| not (False or True)      | False      |
| not (False or False)     | True       |
-----------------------------------------

__________________________________________ 
| NOT AND                   | True?      |
------------------------------------------
| not (True and False)      | True       |
| not (True and True)       | False      |
| not (False and True)      | True       |
| not (False and False)     | False      |
------------------------------------------

______________________ 
| !=     | True?     |
----------------------
| 1 != 0 | True      |
| 1 != 1 | False     |
| 0 != 1 | True      |
| 0 != 0 | False     |
----------------------

______________________ 
| ==     | True?     |
----------------------
| 1 == 0 | False     |
| 1 == 1 | True      |
| 0 == 1 | False     |
| 0 == 0 | True      |
----------------------