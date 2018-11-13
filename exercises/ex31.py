# making decisions: now that we have if, else and elif we may start to create scrpipts that decide things!
# in this exercise, we'll explore asking a user questions nd then make decisions based on the answer(s) provided

print("""You enter a dark room with two doors.
Do you go through the door #1 or door #2?""")

door = input("If it helps, one door is red and the other is not. > ")

# we're saying that the value of the input will be a string and not an integer
if door == "1":
    print("There's a giant bear here eating cheese cake and churros...")
    print("What will you do about it?")
    print("1. Take the cake and possibly the churros too.")
    print("2. Run like hell.")

    bear = input("What'll it be, boss? > ")

    # checkout how we're nesting an if-statement inside another if-statement
    if bear == "1":
        print("The bear takes one look at you and proceeds to eat your face...")
    elif bear == "2":
        print("The bear takes one look at you and chomps down on your leg...")
    else:
        print(f"Well, {bear} is possibly the best choice between the two.")
        print("You run far and away from the bear.")
        print("The bear continues to enjoy cake and churros...burp!")

elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("All your choices are insane, but choose one all the same > ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of root bear.")        
        print("Good job!")

else:
    print("You stumble around, tripping over a box of warm donuts and hot chocolate. Good job!")