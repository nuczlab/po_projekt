from abc import abstractmethod
from terrain import Terrain
from map import Map
import random


class Tribe:
    def __init__(self, map: Map, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

        self.map = map
        self.terrains = []
        self.development_points = 0
        self.combat_ability = 1.0
        self.soldiers = 1
        self.growth_rate = 1
        self.points_to_expand = 10
        self.development_points_growth = 0
        self.possible_directions = []
        self.id = 0
        self.soldiers_used_to_fight = 15

    @abstractmethod
    def turn(self):
        """
        Abstrakcyjna metoda służaca do obsługi tur przez każde z plemion
        """
        pass

    def perform_combat(self, enemy) -> bool:
        """
        Function used to perform combat between two tribes.
        """
        point_ratio = self.soldiers / enemy.soldiers
        win_threadshold = 50 / point_ratio + 5
        rand = random.randint(0, 100)
        self.kill_soldiers(self.soldiers_used_to_fight * ((100 - rand) / 100))
        enemy.kill_soldiers(self.soldiers_used_to_fight * ((rand) / 100))
        if rand > win_threadshold:
            return True
        return False

    def kill_soldiers(self, n):
        """
        Function used to decrese number of soldier avaible to tribe.
        """
        # Tribe always have 1 soldier
        self.soldiers = self.soldiers - n
        if self.soldiers <= 0:
            self.soldiers = 1

    def extend_directions(self, terrain):
        """
        Function used to append possible directions of expansion .
        """
        # Add direction to extend of province

        self.possible_directions.extend(
            [
                ter
                for ter in self.map.get_surrounding_terrains(terrain)
                if ter.owner != self and ter.crossable
            ]
        )

    def remove_terrain(self, terrain):
        """
        Remove terrain from tribe terrains and decrease development ponits growth.
        WARNING: This functions doesn't change owner of terrain!

        """
        self.terrains.remove(terrain)
        self.development_points_growth = (
            self.development_points_growth - terrain.production_multiplier
        )
        dir = [
            ter
            for ter in self.map.get_surrounding_terrains(terrain)
            if ter.owner != self and ter.crossable
        ]
        if terrain in self.possible_directions:
            self.possible_directions.remove(terrain)
        for d in dir:
            if d in self.possible_directions:
                self.possible_directions.remove(d)

    def add_terrain(self, terrain):
        """
        Function used to add terain to tribe
        WARNING: This functions doesn't change the owner of terrain
        """
        self.terrains.append(terrain)
        self.development_points_growth = (
            self.development_points_growth + terrain.production_multiplier
        )
        if terrain in self.possible_directions:
            self.possible_directions.remove(terrain)
        self.extend_directions(terrain)

    def append_production(self):
        self.development_points = (
            self.development_points + self.development_points_growth
        )
        self.soldiers = self.soldiers + self.development_points_growth


class SedentaryTribe(Tribe):
    def init(self):
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.capital = self.terrains[0]
        for terrain in self.terrains:
            self.extend_directions(terrain)

    def turn(self):
        if len(self.terrains) > 0:
            # update
            pos_dir = {}
            for t in self.possible_directions:

                pos_dir[t]= t.production_multiplier
                if t.owner != None:
                    pos_dir[t] = pos_dir[t]*(t.owner.soldiers/self.soldiers)- self.map.get_distance(self.capital,t)
            directions = dict(sorted(pos_dir.items(), key=lambda item: item[1],reverse=True))
            
            # Check if tribe can
            if len(directions) > 0:
                while self.development_points > self.points_to_expand:
                    self.development_points = (
                        self.development_points - self.points_to_expand
                    )
                   
                    ter = list(directions.keys())[0]
                    if ter.owner == None:

                        self.map.change_owner(ter.x, ter.y, self)

                    else:
                        if self.soldiers > self.soldiers_used_to_fight:
                            # self.kill_soldiers(30)
                            if self.perform_combat(ter.owner):

                                self.map.change_owner(ter.x, ter.y, self)

            self.append_production()


class NomadTribe(Tribe):
    def turn(self):
        if len(self.terrains) > 0:
            # Sprawdzy czy posiada jakiekolwiek terytorium
            dir = random.randint(0, 3)
            dx = 0
            dy = 0
            x = self.terrains[0].x
            y = self.terrains[0].y
            # Wybieramy kierunek rozwoju
            if dir == 0:
                dy = 1
            if dir == 1:
                dx = 1
            if dir == 2:
                dy = -1
            if dir == 3:
                dx = -1
            # Plemiona koczownicze na razie ze soba nie walcza
            if x + dx > 0 and x + dx < self.map.x:
                if y + dy > 0 and y + dy < self.map.x:
                    if self.map.is_terrain_ocupied(x + dx, y + dy):
                        pass
                    else:
                        val, ter = self.map.get_terrain(x + dx, y + dy)
                        if val:
                            if ter.crossable:

                                self.map.change_owner(x + dx, y + dy, self)
                                self.map.change_owner(x, y, None)
            # Generowanie punktów rozwoju
            self.append_production()
            # Sprawdzanie czy plemie moze ewoluowac
            if self.development_points > self.points_to_evolve:
                #print("[{0}] Tribe upgraded to next level".format(self.id))
                self.__class__ = SedentaryTribe
                self.init()
                pass
