### basic inventory – "adventurer's backpack"
# to accomplish this, we'll need the following:
#   - An empty list ("backpack")
#   - A function that we may call with argument "item" to add an item to the list ("add items")
#   - A function that we may call to show the contents of the list ("show items")
#   – To tell our gamer that there is an item available to pickup and add to the list ("take")
#   – To tell the gamer that the item has been added to the list ("item added")

# create our empty inventory list
inventory = []

# create some artifacts
# should we do this here or in line...my gut says do it out here but that may be something we do later

##########
def take(artifact):
    # inform the player about the discovery
    print(f"You have found a {artifact}. Type 'take {artifact}' to take it.")
    # prompt the player to make a choice. for simplicity, let's assume the player will take the artifact
    choice = input("> ")
    while "take" in choice or "Take" in choice:
        # add the item to the list named "inventory"
        inventory.append(artifact)
        # let the player know the item was added to inventory
        print(f"{artifact} has been added.")
        break
    else:
        print(f"Type 'take {artifact}' to take it.")

def walk(destination):
    print(f"You walk towards your desintation to get a better look and discover a {artifact}. Type 'examine {artifact} to learn more.")
    print(f"To walk towards the {destination}, type 'walk to {destination}")
    choice = input("> ")
    while "walk" in choice or "Walk" in choice:
        if destintation == "gallery wall":
            galleryWall()
        # elif artifact == "lever":
        # break

def gallery():
    artifact = "dusty leather satchel"
    print("You find yourself in a dimly lit chamber. The room appears to be circular and made from dark, damp stone.")
    print("You feel goosebumps raise from the nape on your neck as a cool draft rolls lazily across your back.")
    print("You nearly trip over a dusty leather object on the floor as you pivot to avoid the draft.")
    take(artifact)

    destination = "gallery wall"
    print(f"As you stoop to pickup the satchel, you notice that there may be an object mounted on the far wall of the chamber.")
    walk(destination)

def galleryWall():
    print(f"You examine the {artifact} to discover a lifelike painting of the Spanish Armada sailing up the English Channel.")
    print("You are impressed.")
    print("Upon further observation, you notice that this frame may be large enough to crawl through")    


gallery()


# ##########
# ## Introduce the backpack
# # tell the gamer that there is a new item in view
# print("You see a dusty leather backpack. Type 'take backpack' to take it.")
# item = "backpack"

# # prompt the gamer for an action
# choice = input("> ")

# while "take" in choice or "Take" in choice:
#         # create the empty list with name backpack
#         backpack = []
#         print("You sling the dusty leather backpack over your shoulder and suddenly feel imbued with a sense of adventure.\n")
#         break
# else:
#     print("I can't do that Dave")    


# ##########
# ## Introduce the flashlight
# # tell the gamer that there is a new item in view
# print("You see a flashlight. Type 'take flashlight' to add it to your backpack.")
# item = "flashlight"

# # prompt the gamer for an action
# choice = input("> ")

# while "take" in choice or "Take" in choice:
#         # add the item to the list
#         backpack.append(item)
#         # let the gamer know the item was added
#         print(f"{item} has been added to your backpack.")
#         # print out the contents of the backpacks
#         for items in backpack:
#             print(f"The contents of your backpack now are: ", items, "\n")
#         break
# else:
#     print("I can't do that Dave")



# ##########
# ## Introduce the flashlight battery
# # create a new variable called energy to represent the remaining life of the battery

# def newBattery():
#     energy = 10
#     # print this variable to confirm the battery has increased the energy count
#     print(f"Your flashlight now has {energy} energy remaining")

# # tell the gamer that there is a new item in view
# item = "battery"
# print(f"You see a {item}. Type 'take {item}' to add it to your backpack.")

# # prompt the gamer for an action
# choice = input("> ")

# while ("take" + item) in choice or ("Take" + item) in choice:
#         # add the item to the list
#         backpack.append(item)
#         # let the gamer know the item was added
#         print(f"{item} has been added to your backpack.")
        
#         # print out the contents of the backpacks        
#         # for items in backpack:
#         #     print(f"The contents of your backpack now are: ", items, "\n")
# break

# # check and see if the backpack has a battery in it
# if "battery" in backpack:
#     print(f"You seemed to have found a battery. Type 'use battery' to use it with your flashlight.")
    
#     choice = input("> ")
    
#     if "use" in choice or "Use" in choice:
#         newBattery()
#     else:
#         print("The flashlight wont work without a battery.")


