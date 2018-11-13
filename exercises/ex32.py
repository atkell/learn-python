# loops and lists: a list is exactly what it sounds like, a container of things that are organized in order from first to last
# conceptually, we've seen similar syntax in php and other languages building arrays but Im not so sure these are the same thing

# the left bracket [ "opens the list" while the right bracket ] "closes the list"

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know whats in it
for i in change:
    print(f"I got {i}")

# we may also build lists, first start with an empty one
elements = range(0,6)

# then use the range function to do 0 to 5 counts
# for i in range(0,6):
#     print(f"Adding {i} to the list.")
#     # append is a function that lists understand
#     elements.append(i)

# now we may print them out too
for i in elements:
    print(f"Elements was: {i}")