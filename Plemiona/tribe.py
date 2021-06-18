from abc import abstractmethod
from Plemiona.terrain import Terrain
from Plemiona.map import Map
import random


class Tribe:
    """
    Abstract Class of Tribe
    """

    def __init__(self, map: Map, dictionary):

        self._map = map

        self.development_points = 0
        self.combat_ability = 1.0
        self.soldiers = 1
        self.growth_rate = 1
        self.points_to_expand = 20
        self.development_points_growth = 0
        self._possible_directions = []
        self.id = 0
        self.soldiers_used_to_fight = 30

        for k, v in dictionary.items():
            setattr(self, k, v)

        self._terrains = []

    @abstractmethod
    def turn(self):
        """
        Abstract method used to process turn
        """
        pass

    def perform_combat(self, enemy) -> bool:
        """
        Function used to perform combat between two tribes.
        """

    def kill_soldiers(self, n):
        """
        Function used to decrese number of soldier avaible to tribe.
        """
        # Tribe always have 1 soldier
        self.soldiers = self.soldiers - n
        if self.soldiers <= 0:
            self.soldiers = 1

    def _extend_directions(self, terrain: Terrain):
        """
        Function used to append possible directions of expansion .
        """
        # Add direction to extend of province

        self._possible_directions.extend(
            [
                ter
                for ter in self._map.get_surrounding_terrains(terrain)
                if ter.owner != self and ter.crossable
            ]
        )

    def remove_terrain(self, terrain: Terrain):
        """
        Remove terrain from tribe terrains and decrease development points growth.

        """
        self._terrains.remove(terrain)
        self.development_points_growth = (
            self.development_points_growth - terrain.production_multiplier
        )
        dir = [
            ter
            for ter in self._map.get_surrounding_terrains(terrain)
            if ter.owner != self and ter.crossable
        ]
        if terrain in self._possible_directions:
            self._possible_directions.remove(terrain)
        for d in dir:
            if d in self._possible_directions:
                self._possible_directions.remove(d)

    def add_terrain(self, terrain: Terrain):
        """
        Function used to add terain to tribe
        """
        self._terrains.append(terrain)
        self.development_points_growth = (
            self.development_points_growth + terrain.production_multiplier
        )
        if terrain in self._possible_directions:
            self._possible_directions.remove(terrain)
        self._extend_directions(terrain)

    def append_production(self):
        self.development_points = (
            self.development_points
            + self.development_points_growth * self.production_multiplier
        )
        self.soldiers = (
            self.soldiers + self.development_points_growth * self.production_multiplier
        )

    def sort_directions(self):
        pos_dir = {}
        for t in self._possible_directions:
                    pos_dir[t] = t.production_multiplier
                    if t.owner != None:
                        pos_dir[t] = (
                            pos_dir[t] * (t.owner.soldiers / self.soldiers)
                            - self._map.get_distance(self.capital, t) / 5
                        )
        directions = list(
            dict(
                sorted(pos_dir.items(), key=lambda item: item[1], reverse=True)
            ).keys())
        return directions

class SedentaryTribe(Tribe):
    """
    Tribe that's expanding self, and can attack other tribes
    """

    def init(self):
        """
        Used when tribe level up
        """
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.capital = self._terrains[0]
        for terrain in self._terrains:
            self._extend_directions(terrain)

    def turn(self):
        if len(self._terrains) > 0:
            # Check if tribe can

            
            if self.inteligent_directions:
                directions= self.sort_directions()
                
            else:
                directions = random.sample(
                    self._possible_directions, len(self._possible_directions)
                )

            while self.development_points > self.points_to_expand:
                if len(directions) > 0:
                    self.development_points = (
                        self.development_points - self.points_to_expand
                    )
                    ter = directions[0]
                    if ter.owner == None:

                        self._map.change_owner(ter.x, ter.y, self)

                    else:
                        if self.soldiers > self.soldiers_used_to_fight:
                            # self.kill_soldiers(30)
                            from Plemiona.tribe_helper import TribeHelper

                            if TribeHelper.perform_combat(self, ter.owner):

                                self._map.change_owner(ter.x, ter.y, self)
                    directions.remove(ter)
                else:
                    break

            self.append_production()


class NomadTribe(Tribe):
    """
    Tribe that's only moving and collecting productions points
    """

    def turn(self):
        if len(self._terrains) > 0:

            dir = random.randint(0, 3)
            dx = 0
            dy = 0
            x = self._terrains[0].x
            y = self._terrains[0].y
            # Randomize direction
            if dir == 0:
                dy = 1
            if dir == 1:
                dx = 1
            if dir == 2:
                dy = -1
            if dir == 3:
                dx = -1

            if x + dx > 0 and x + dx < self._map.x:
                if y + dy > 0 and y + dy < self._map.x:
                    if self._map.is_terrain_ocupied(x + dx, y + dy):
                        pass
                    else:
                        val, ter = self._map.get_terrain(x + dx, y + dy)
                        if val:
                            if ter.crossable:

                                self._map.change_owner(x + dx, y + dy, self)
                                self._map.change_owner(x, y, None)

            self.append_production()

            if self.development_points > self.points_to_evolve:
                print("[{0}] Tribe upgraded to next level".format(self.id))
                self.__class__ = SedentaryTribe
                self.init()
                pass
