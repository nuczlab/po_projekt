from abc import abstractmethod
import random
class Tribe:
    def __init__(self, map, dictionary): 
        for k, v in dictionary.items():
            setattr(self, k, v)
        self.terrains = []
        self.map = map

    @abstractmethod
    def turn(self):
        """
        Abstrakcyjna metoda służaca do obsługi tur przez każde z plemion
        """
        pass

    def remove_terrain(self, terrain):
        self.terrains.remove(terrain)

    def add_terrain(self, terrain):
        self.terrains.append(terrain)

class NomadTribe(Tribe):
    def turn(self):
        if len(self.terrains) > 0: 
            # Sprawdzy czy posiada jakiekolwiek terytorium
            dir = random.randint(0,3)
            dx = 0
            dy = 0
            x = self.terrains[0].x
            y = self.terrains[0].y
            #Wybieramy kierunek rozwoju
            if dir == 0:
                dy= 1
            if dir == 1:
                dx = 1
            if dir == 2:
                dy = -1
            if dir == 3:
                dx = -1
            #Plemiona koczownicze na razie ze soba nie walcza
            if x + dx >0 and x + dx < self.map.x:
                if y + dy >0 and y + dy < self.map.x:
                    if self.map.is_terrain_ocupied(x + dx,y +dy):
                        pass
                    else:
                        self.map.change_owner(x + dx,y + dy,self)
                        self.map.change_owner(x ,y,None)
                




