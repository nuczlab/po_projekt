
from abc import abstractmethod


class Tribe:
    def __init__(self,
    map: 'Map class', 
    dictionary): 
        for k, v in dictionary.items():
            setattr(self, k, v)
        self.terrains = []
    @abstractmethod
    def turn(self):
        pass
    def remove_terain(self,terrain):
        self.terrains.pop(terrain)
    def add_terrain(self,terrain):
        self.terrains.append(terrain)
class NomadTribe(Tribe):
    def turn():
        pass
