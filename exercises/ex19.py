# functions and variables 
# the takeaway here is scope, mostly that the variable we use in our functions are not connected to variables in our script

def cheese_and_crackers(cheese_count, boxes_of_crackers): # here we define our function for ex19 called cheese_and_crackers. it takes 2 arguments, cheese_count and boxes_of_crackers. we could also call these "a" and "b"
	print(f"You have {cheese_count} cheeses, oh my!") # print format string to include the value assigned to cheese_count
	print(f"You have {boxes_of_crackers} boxes of crackers.") # print format string to include the value assigned to boxes_of_crackers
	print("Man, that's enough to party!") # print a string
	print("Get a blanket and some wine.\n") # print a string

print("We may give a function the numbers directly:") # print a string
cheese_and_crackers(20, 30) # call the function cheese_and_crackers, passing along 20 and 30 as the values for the two arguments that the function accepts

print("Or we may use variables from our script:") # print a string
amount_of_cheese = 10 # assign a value of 10 to the variable named amount_of_cheese
amount_of_crackers = 50 # assign a value of 50 to the variable named amount_of_crackers

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # call the function cheese_and_crackers, passing along the variables amount_of_cheese and amount_of_cracers for the two arguments the function accepts

print("We can even do some math (as if you would want that):") # print a string
cheese_and_crackers(10 + 20, 5 + 6) # do some math

print("And we may combine the two, variables AND math...cue the Keanue woooooaaaaaah:") # print a string
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # call the function cheese_and_crackers, passing along a mix of variables and basic math