from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = int(input("> "))
    if 0 in choice or 1 in choice:
        #how_much = int(choice)
        print("None? Really, come on. I bet you took at least 2 pieces...be honest!")
        gold_room()
    else:
        dead("Man, learn to type a number!")
    
    if choice > 1 and choice < 50:
        print("Nice, you're not greedy and you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("the bear has a bunch of honey.")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you, then mauls your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You may open the door now.")
            bear_moved = True
        elif choice =="taunt bear" and bear_moved:
            dead("The bear is noticably angry. You also notice it now chomping on your leg.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means...try these options\ntake honey\ntaunt bear or \nopen door")

    def cthulhu_room():
        print("Here you see the great evil Cthulu")
        print("He, it, whatever stares at you and you go insane")
        print("Do you feel for your life or eat your own hand?")

        choice = input("> ")

        if "flee" in choice:
            start()
        elif "hand" in choice:
            dead("Yummy!")
        else:
            cthulhu_room()

def dead(why):
    print(why, "Womp, womp")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()