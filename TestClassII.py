class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
        self.iterable = iterable

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method