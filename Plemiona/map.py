import random
from Plemiona.terrain import Terrain
import math


class Map:
    """
    Class resposnible for providing acess to map and for performing operations on terrains
    """

    def __init__(self, name, config):
        """
        Parameters
        ----------
        name : str
            The name of the map (Pangea)
        config : Config
            Instance of configuration class
        """
        self.name = name
        self.terrains = {}
        self.config = config
        self.tribes = []
        self.x = 0
        self.y = 0

    def get_terrain(self, x, y) -> bool:
        """
        Method used to get terrain by coordinates
        Parameters
        ----------
        x : int
            Horizontal posistion of terrain
        y : int
            Horizontal posistion of terrain
        """
        if x < self.x and x >= 0:
            if y < self.y and y >= 0:
                return True, self.terrains[x, y]
        return False, None

    def get_surrounding_terrains(self, terrain: Terrain) -> list[Terrain]:
        """
        Method used to get surrounding terrains by terrain
        Parameters
        ----------
        terrain : Terrain
            Instance of class terrain
        """
        if terrain == None:
            return []
        list = []
        for b in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            resp, ter = self.get_terrain(terrain.x + b[0], terrain.y + b[1])
            if resp:
                list.append(ter)
        return list

    def is_terrain_ocupied(self, x, y) -> bool:
        """
        Method used to check if terrain is ocupied.
        Returns true or false.

        Parameters
        ----------
        x : int
            Horizontal posistion of terrain
        y : int
            Horizontal posistion of terrain
        """
        if self.terrains[x, y].owner != None:
            return True
        else:
            return False

    def get_distance(self, terrain_a: Terrain, terrain_b: Terrain) -> float:
        """
        Method used to get distance between terrains
        Parameters
        ----------
        terrain_a : Terrain
            Instance of class terrain
        terrain_a : Terrain
            Instance of class terrain
        """
        return math.sqrt(
            math.pow((terrain_a.x - terrain_b.x), 2)
            + math.pow((terrain_b.y - terrain_a.y), 2)
        )

    def change_owner(self, x, y, owner):
        """
        Method used to change ownership between tribes
        Parameters
        ----------
        x : int
            Horizontal posistion of terrain
        y : int
            Horizontal posistion of terrain
        owner : Tribe
            Tribe we want to transfer ownership to
        """
        ter = self.terrains[x, y]
        if hasattr(ter, "owner"):
            if ter.owner != None:
                ter.owner.remove_terrain(ter)
        self.terrains[x, y].owner = owner
        if owner != None:
            owner.add_terrain(ter)
