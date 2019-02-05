# Let's learn about the data structure called a Dictionary (or dict for short). A dict is a way
# to store data just like a list, but instead of using only humbers to get hte data, we may use 
# almost anything. This, in turn, allows us to treat a dict like it's a database for storing
# and organizing data.

lines = "-" * 10

# print("Let's review what we may do with lists: ")
# print(lines)
# print("First, let's create the list 'things', things = ['a', 's', 'd', 'f']: ")
# things = ['a', 's', 'd', 'f']
# print("\nSecond, let's print the entire list, print(things): ")
# print(things)
# print("\nThird, let's print out the item located at index 1, things[1]: ")
# print(things[1])
# print("\nFourth, let's assign a new value, 'z', for the item at index 2, things[2] = 'z': ")
# things[2] = 'z'
# print(things[2])
# print("\nAnd finally, let's print the list once again to see what changed: ")
# print(things)

# We recall that we are able to use numbers to index a list. In order words, we may use numbers
# discover what's in a list. In fact, we may ONLY use numbers to retrieve items from a list.

# print(f"""\n
# {lines * 4}
# \n""")

# A dictionary (or dict, remember?) allows us to use anything in order to retrieve items from
# a list. We may associate one thing with another, no matter what it is. Let's have a look:

# print("Now, let's have a look at how dictionaries work.")
# print(lines)
# print("First, let's create a dict named 'stuff', stuff = {'name': 'Alex', 'age': '31', 'height': 5 * 12 + 6}")
# stuff = {'name': 'Alex', 'age': '31', "height": 5 * 12 + 6}
# print("\nSecond, let's print out the contents of this dict, print(stuff): ")
# print(stuff)
# print("\nThird, let's print out the value associated with key 'name', print(stuff['name']): ")
# print(stuff['name'])
# print("\nAgain, let's continue practicing printing, print(stuff['age']): ")
# print(stuff['age'])
# print("\nAgain, let's continue practicing printing, print(stuff['height']): ")
# print(stuff['height'])
# print("\nFinally, let's create a new entry in our dict with key:value of city:Atlanta, stuff['city'] = 'Atlanta': ")
# stuff['city'] = "Atlanta"
# print("\nBonus, let's continue practicing printing, print(stuff['city']): ")
# print(stuff['city'])

# print("\nWait a sec, Zed said we may use anything...can we use a nunber here to create a new entry?")
# print("Create a new key:value pair, stuff[1] = 'Amazing': ")
# stuff[1] = "Amazing"
# print("And then let's print it out: ")
# print(stuff[1])

# print("\nBut what if we want to delete an item within the dictionary (or dict)? ")
# print("We delete items from the dict with the del keyword like del stuff['city']:")
# del stuff['city'] 
# print(stuff)

# Let's jump into an exercise! In the following example, we will begin mapping states to their
# abbreivations and then the abbreivations to cities in the states. (Hint: mapping == associating)

states = {
    'Georgia': 'GA',
    'Alabama': 'AL',
    'Mississippi': 'MS',
    'Louisana': 'LA'
}

cities = {
    'GA': 'Atlanta',
    'AL': 'Montgommery',
    'MS': 'Jackson',
    'LA': 'Baton Rouge'
}

# manually add a new city and state
states['New York'] = 'NY'
cities['NY'] = "New York City"

# print out some cities
print(lines)
print("GA State has city: ", cities['GA'])
print("LA State has city: ", cities['LA'])

# print out some states
print(lines)
print("Georgia's abbreviation is: ", states['Georgia'])
print("Mississippi's abbreviation is: ", states['Mississippi'])

# print it again by using the state then cities dict
print(lines)
print("Georgia has city: ", cities[states['Georgia']])

# print out every state abbreviation!
print(lines)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in each state
print(lines)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now let's try to do both at the very same time...
print(lines)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print(lines)
# safely get an abbreviation by state that might not be there
whatState = input("What state would you like to find an abbreviation for?  ")
state = states.get(whatState)

if not state:
    print(f"Sorry, no {whatState}")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")