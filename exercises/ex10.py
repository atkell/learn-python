# escape sequences, yeah baby!
# \\ = backslash
# \' = single quote
# \" = double quote"
# \a = ascii bell # this actually causes an audible sound to be emitted when used
# \b  = ascii backspace
# \f = ascii formfeed
# \n = ascii linefeed (or new line)
# \N{name} = character named name in the unicode database
# \r = carriage return # like a typewriter carriage?
# \t = horizontal tab
# \uxxxx = character with 16-bit hex value
# \Uxxxxxx = character with 32-bit hex value
# \v = vertical tab
# \ooo = character with octal value ooo
# \xhh = character with hext value hh

tabby_cat = "\tIm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"
# backslash_cat = "I'm \ a \ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\v\t* Fishies
\t* Catnip\n\v\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
