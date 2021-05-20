
from abc import abstractmethod


class Tribe:
    def __init__(self,
    map: 'Map class', 
    dictionary): 
        for k, v in dictionary.items():
            setattr(self, k, v)
    @abstractmethod
    def turn():
        pass
class NomadTribe(Tribe):
    
    def turn():
        pass
