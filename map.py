import random
from terrain import Terrain
import math

class Map:
    def __init__(self, name, config):
        self.name = name
        self.terrains = {}
        self.config = config
        self.tribes = []
        self.x = 0
        self.y = 0

    def get_terrain(self, x, y) -> bool:
        if x < self.x and x >= 0:
            if y < self.y and y >= 0:
                return True, self.terrains[x, y]
        return False, None

    def get_surrounding_terrains(self, terrain) -> list[Terrain]:
        if terrain == None:
            return []
        list = []
        for b in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            resp, ter = self.get_terrain(terrain.x + b[0], terrain.y + b[1])
            if resp:
                list.append(ter)
        return list
    def get_distance(self,terrain_a,terrain_b) -> float:
        return math.sqrt(math.pow((terrain_a.x-terrain_b.x),2)+math.pow((terrain_b.y-terrain_a.y),2))
    def is_terrain_ocupied(self, x, y) -> bool:
        if self.terrains[x, y].owner != None:
            return True
        else:
            return False

    def change_owner(self, x, y, owner):
        ter = self.terrains[x, y]
        if hasattr(ter, "owner"):
            if ter.owner != None:
                ter.owner.remove_terrain(ter)
        self.terrains[x, y].owner = owner
        if owner != None:
            owner.add_terrain(ter)
