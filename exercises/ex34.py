# accessing elenents of a list
# kind of reminds me of php, accessing elements within an array by providing and index value
# remember index == 0 is the start of any list

# ordinal number ("ordered"): a number defining a thing's position in a series, such as “first,” “second,” or “third.” Ordinal numbers are used as adjectives, nouns, and pronouns. Compare with cardinal number.
# cardinal number ("numbered"): a number denoting quantity (one, two, three, etc.), as opposed to an ordinal number (first, second, third, etc.).  
# how to find the index of a list element: cardinal number (index) = ordinal number - 1 (which is how we may conceputally understand the "zero" cardinal number)

# example
exampleList = ["bear", "tiger", "lions", "flying howler monkey things"]
bear = exampleList[0]

print(exampleList[2])
print(bear)

# exercise
animals = ["bear", "python3.7", "peacock", "kangaroo", "whale", "platypus"]

# the animal at 1 is the 2nd animal and is a "python3.7"
# the third (3rd) animal is at 2 and is a "peacock"
# the first (1st) animal is at 0 and is a "bear"
# the animal at 3 is the 4th animal and is a "kangaroo"
# the fifth (5th) animal is at 4 and is a "whale"
# the animal at 2 is the 3rd animal and is a "peacock"
# the sixth (6th) animal is at 5 and is a "platypus"
# the animal at 4 is the 5th animal and is "whale"