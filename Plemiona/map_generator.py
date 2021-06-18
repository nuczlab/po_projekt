import random
from Plemiona.tribe import NomadTribe, Tribe
from Plemiona.terrain import Terrain
from Plemiona.map import Map

# import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise


class MapGenerator:
    """
    Class used to provide confiugration all across app
    """

    @staticmethod
    def generate_tribes(map: Map):
        """
        Static method that is generating tribes according to configuration given in map
        map : Map
            Instance of map class
        """
        tribes = map.config["map"]["tribes"]
        print("Generating {} starting tribes".format(tribes))
        avtribes = map.config["tribes"]["start_tribes"]
        if len(avtribes) == 0:
            raise "No tribes given in config!"
        for n in range(tribes):
            rnd = random.randrange(0, len(avtribes))
            if map.config["tribes"]["start_tribes"][rnd]["type"] == "Nomad":
                tribe = NomadTribe(map, map.config["tribes"]["start_tribes"][rnd])
                # if tribe.color_range
                tribe.color = (
                    random.randint(tribe.color_range[0], tribe.color_range[3]),
                    random.randint(tribe.color_range[1], tribe.color_range[4]),
                    random.randint(tribe.color_range[2], tribe.color_range[5]),
                )
                tribe.id = n
                while True:
                    tx = random.randrange(0, map.x)
                    ty = random.randrange(0, map.y)

                    if (
                        map.terrains[tx, ty].owner == None
                        and map.terrains[tx, ty].crossable
                    ):
                        map.change_owner(tx, ty, tribe)
                        map.tribes.append(tribe)
                        break
    @staticmethod
    def generate_terrain(map):
        """
        Static method that is generating terrain according to configuration given in map
        map : Map
            Instance of map class
        """
        map.x = map.config["map"]["x"]
        map.y = map.config["map"]["y"]
        print("Generating map[{0},{1}]".format(map.x, map.y))

        avterrains = map.config["map"]["terrains"]  # List of all terrains possible
        if len(avterrains) == 0:
            raise "No terrains given in config!"
        noises = {}
        perlin_seed = random.randint(0, 50000)
        # We generate perlin noise for each type of terrain given in configuration
        for index, ter in enumerate(avterrains):
            if "perlin_octave" in ter and "perlin_threshold" in ter:
                noises[index] = PerlinNoise(
                    octaves=ter["perlin_octave"], seed=perlin_seed
                )
        # We iterate for every terrain in map
        for ix in range(map.x):
            for iy in range(map.y):
                rnd = random.randrange(0, len(avterrains))
                rnd = 0
                for i, v in noises.items():
                    if v([ix / map.x, iy / map.y]) > avterrains[i]["perlin_threshold"]:

                        rnd = i
                tera = Terrain(
                    avterrains[rnd]
                )  # We create new terrain with data given in config
                tera.x = ix
                tera.y = iy
                map.terrains[ix, iy] = tera
