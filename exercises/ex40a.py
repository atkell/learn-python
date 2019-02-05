class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

people_of_the_sun = ["fifteen hundred and 16",
                    "fire, mashika"]
song2 = Song(people_of_the_sun)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

song2.sing_me_a_song()
