# Designing and Debugging

# Rules for if-statements
#   1. Every if-statement must have an else.
#   2. If this else should never run because it doesn't make sense, then you must use a die function in the else that prints out an error message and dies, 
#      just like we did in the last exercise. This will help find many errors.
#   3. Never nest if-statements more than two deep and always try to do them one deep.
#   4. Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences. Put blank lines before and after.
#   5. Your Boolean tests should be simple. If they are complex, move their calcuations to variables earlier in the function and use a good name for the variable.

# Note: Follow these simple rules. You'll start writing good code. Return to exercise 35 and see what rules were broken.
# Double-note: For practice, we should follow these rules to build good habits. However, not all rules will work in real life. Be pragmatic.

# Rules for Loops
#   1. Use a while-loop only to loop forever, and that means probablt never. Remember, other languages may use while-loops differently than Python.
#   2. Use a for-loop for all other kinds of loop, especially if there is a fixed or limited number of things to loop over (like a list).

# Tips for Debugging
#   1. Do not use a "debugger". It may not provide you with any specific useful information, too much information or just a dish of confusion.
#   2. The best way to debug a program is to use the print command to print out the values of variables (aka var_dump in php) at points in the 
#      program to see where they go wrong.
#   3. Make sure parts of your programs work as you work on them. Don't write massive, monstrous files of code before you try to run them. 
#      Code a little, run a little, fix a little.

# Homework