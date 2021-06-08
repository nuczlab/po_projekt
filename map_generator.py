import random
from tribe import NomadTribe, Tribe
from terrain import Terrain

# import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise


class MapGenerator:
    @staticmethod
    def generate_tribes(map):
        tribes = map.config["map"]["tribes"]
        print("Generating {} starting tribes".format(tribes))
        avtribes = map.config["tribes"]["start_tribes"]
        if len(avtribes) == 0:
            raise "No tribes given in config!"
        for n in range(tribes):
            rnd = random.randrange(0, len(avtribes))
            if map.config["tribes"]["start_tribes"][rnd]["type"] == "Nomad":
                tribe = NomadTribe(map, map.config["tribes"]["start_tribes"][rnd])
                tribe.color = (random.randint(150, 255), 0, 0)
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
        Generating map with paramets given in configuration
        """
        map.x = map.config["map"]["x"]
        map.y = map.config["map"]["y"]
        print("Generating map[{0},{1}]".format(map.x, map.y))
       
        avterrains = map.config["map"]["terrains"]
        if len(avterrains) == 0:
            raise "No terrains given in config!"
        noises = {}
        perlin_seed = random.randint(0, 50000)
        for index, ter in enumerate(avterrains):
            if "perlin_octave" in ter and "perlin_threshold" in ter:
                noises[index] = PerlinNoise(
                    octaves=ter["perlin_octave"], seed=perlin_seed
                )


        for ix in range(map.x):
            for iy in range(map.y):
                rnd = random.randrange(0, len(avterrains))
                rnd = 0
                for i, v in noises.items():
                    if v([ix / map.x, iy / map.y]) > avterrains[i]["perlin_threshold"]:
                        rnd = i
                tera = Terrain(avterrains[rnd])
                tera.x = ix
                tera.y = iy
                map.terrains[ix, iy] = tera
