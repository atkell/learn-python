# even more p-p-p-p-p-p-rinting

# sublime has a shortcut to duplicate a line, it is wonderful: command + shift + d
# printing out a string
print("Mary had a little lamb.")
# printing out another string but also introducing something new where we use a placeholder ( {} ) and call the format function on it, with a period. We then pass in the argument
# for this function as a string, snow
print("Its fleece was white as {}.".format('snow'))
# and another
print("And everywhere that Mary went.")
# shortcut to print out 10 dots 
print("." * 10) # what'd that do?

# 12 assignments where we're storing a single character string in a variable
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# I removed the comman and re-ran the script. This resulted in ... "a SyntaxError: invalid syntax"
# why? we're not formatting the contents of our print command correctly as we combine variables, a string and a keyword (end)
# what if we use a plus sign instead of a comma ... another SyntaxError: keyword can't be an expression
# so what's the , end=' ' for anyhow? Well, if we omit it, things happen.
print(end1 + end2 + end3 + end4 + end5 + end6,  end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
print("." * 10) # what'd that do?
# here is the same line but with the end removed
print("Here's the same line as above but with the end=\' \' removed")
print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11 + end12)
# notice how if we include the end=' ' python wont introduce a line break or new line when it prints the next line? handy!
