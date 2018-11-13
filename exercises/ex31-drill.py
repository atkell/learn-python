# study drill -- make a new game...

print("""The hero, panting, legs on fire, rounds the corner and stops abruptly at a fork in the canyon.
Should she run left or right?""")

canyon = input("> ")

if canyon == "left":
    print("""There's something obstructing the path.
It looks like you may be able to push it out of the way.
Do you attempt to move it?""")
    print("1. Yes")
    print("2. No")
    # print("3. Return to fork in canyon")

    action = input("> ")

    if action == "1":
        print("After much effort the obstacle moves just enough to create an opening.")
        print("Does the hero shimmy through the opening?")
        print("1. Yes")
        print("2. No")

        obstacle = input("> ")

        if obstacle == "1":
            print("The hero evades capture!")
        else: 
            print("The hero is captured by her foe!")

    elif action == "2":
        print("The hero carefully backpedals to the fork in the canyon and is capture by her foe!")
    # else:
    #     # we'll want to return to this as the nesting could get complex
    #     print("""THe hero returns to the fork in the canyon.
    #     Should she run left or right?""")

    #     action = input("> ")

elif canyon == "right":    
    print("Dead end.")
    print("The hero is captured by her foe!")

