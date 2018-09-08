from sys import argv # import the sys module

script, user_name, user_lang = argv
prompt = '>> ' # we make a variable named prompt and then give this to input() instead of typing it over and over again...neat, right?

user_name = user_name.capitalize() # Let's capitalize the first letter of the response we receive from our users
user_lang = user_lang.capitalize() # Let's capitalize the first letter of the response we receive from our users

print(f"Hi {user_name}, I am the {script} script.")
print(f"You said you speak {user_lang} and well thats good, because I do too.")
print("I'd like to ask you a few questions if I may...")
print(f"Do you like me, {user_name}?")
likes = input(prompt) # we don't need to capialize this one
# likes = likes.capitalize()

print(f"Where do you live, {user_name}?")
lives = input(prompt)
lives = lives.capitalize()

print(f"What kind of computer do you have?")
computer = input(prompt)
computer = computer.capitalize()

print(f"""
Alright, so you said {likes} about whether or not you liked me. Thanks...maybe?
You live in {lives}. Not sure where that is, but I bet it is great!
And you have a {computer} computer. Sweet.
	""")