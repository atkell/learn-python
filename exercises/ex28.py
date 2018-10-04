# boolean practice

# a simple process to work through more complex Boolean logic stagements
# 1) Find an equality test (== or !=) and replace it with its truth
# 2) Find each and/or inside parenthesis and solve those first
# 3) Find each not and invert it
# 4) Find an remaining and/or and solve it
# 5) When you are done you should have True or False

# Alex tip: Just solve inside out, take your time and be patient.


print("True? ", True and True) # true
print("False? ", False and True) # false
print("False? ", 1 == 1 and 2 == 1) # false
print("True? ", "test" == "test") # true
print("True? ", 1 == 1 or 2 != 1) # true
print("True? ", True and 1 == 1)
print("False? ", False and 0 != 0)
print("True? ", True or 1 == 1)
print("False? ", "test" == "testing")
print("False? ", 1 != 0 and 2 == 1)
print("True? ", "test" != "testing")
print("False? ", "test" == 1)
print("True? ", not (True and False))
print("False? ", not (1 == 1 and 0 != 1))
print("False? ", not (10 == 1 or 1000 == 1000))
print("False? ", not (1 != 10 or 3 == 4))
print("True? ", not ("testing" == "testing" and "Zed" == "Cool Guy"))
print("True? ", 1 == 1 and (not ("testing" == 1 or 1 == 0)))
print("False? ", "chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
print("False? ", 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))

# successfully completed this! perfecto