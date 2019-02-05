from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet completed")
        print("Subclass it and implement enter()")
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda stink at this.",
        "Such a luser.",
        "You're worse than your dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are now the last surviving member
            and your mission is to get the neutron destruct bomb from the
            Weapons Armory, put it in the bridge, and blow the ship up after
            getting into an escape pod.

            You're running down the central corridor to the Weapons Armory when
            a Gothon jumps out, red scaly skin, dark grimy teeth, and an evil
            clown costume around his hate filled body. He's blocking the door
            to the Armory and about to pull a weapon to blast you!
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Nope. Didn't work.
                """))
            return 'death'
        elif action == "dodge!":
            print(dedent("""
                Nope. Didn't work.
                """))
            return 'death'
        elif action == "tell a joke":
            print(dedent("""
                Lucky for you, they tought you Gothon humor at the academy.
                You tell the one Gothon joke you know: Lbhe zbgure vf fb sng,
                fur fvgh nebhaq gur ubhr. The Gothon stops, tries not to laugh,
                then bursts out laughing and can't move. While he's laughing,
                you run past him and jump through the Weapon Armory door.
                """))
            return 'laser_weapon_armory'
        else:
            print("Does not compute!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You dive roll into the Weapon Armory, crouch and scan the room for
            more Gothons that might be hiding. It's dead quiet, too quiet in
            fact. You stand up and run to the far side of the room and find the
            neutron bomb in its container.
            There's a keypad lock on the box and you need the code to get the
            bomb out. If you get the code wrong 10 times then the lock closes
            forever and you cannot get the bomb. The code is 3 digits.
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print(code)
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            # Add a countdown to print out to let the player know how many guesses remain
            print("BZZZED!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open, revealing its contents. You grab the
                bomb and run as fast as hell to the bridge where you must place
                it in the right spot.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear the sickening
                sound of your own defeat. Better luck next time!
                """))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You burst onto the Bridge with the neutron destruct bomb under
            your ar and surprise 5 Gothons who are trying to take control of
            the ship. Each of them has an even uglier clown costume than the
            last. Good news, they haven't pulled their weapons out yet, as they
            see an active bomb under your arm and don't want to set it off.
            Your move, player one.
            """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb at a group of Gothons and make a leap for
                the door. You are dead.
                """))
            return 'death'
        elif action == "slowly place the bomb":
            print(dedent("""
                You take the bomb hostage, pointing your blaster at it. You back away
                slowly, planting the bomb as you move you away towards the nearest door-
                way. The bomb is placed. Time to escape, player one!
                """))
            return 'escape_pod'

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush through the ship desparately trying to make it ot the escape escape
            pdd before the whole ship explodes. It seems like hardly any Gothons are on
            the ship, so your run is clear of interference.
            You arrive at the chamber with the escape pods. Now you must pick one. Some
            may be damaged but you don't have time to look. There are 5 pods; choose
            wisely player one!
            """))

        good_pod = randint(1,5)
        print(good_pod)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                You jump into pod {guess} and hit the eject button. You hit the eject
                button once. Just enough time passes that you notice the window is broken.
                You are ejected into space and decompress immediately.
                """))
            return 'death'
        else:
            print(dedent("""
                You jump into pod {guess} and hit the eject button. The pod slides away,
                out into the bleak emptiness of space itself. You have won...or have you?
                """))

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
