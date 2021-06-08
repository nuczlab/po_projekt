from map import Map
from config import Configuration
from map_generator import MapGenerator
import random


class Simulator:
    def __init__(self, config):
        self.config = config

    def generate(self):
        print("Creating Map")
        seed = self.config["simulation"]["seed"]
        print("Seed:{0}".format(seed))
        random.seed(seed)
        self.map = Map("A1", self.config)
        MapGenerator.generate_terrain(self.map)
        MapGenerator.generate_tribes(self.map)
        self.tribes = self.map.tribes
        self.turn = 0

    def perform_turn(self, turns=1):
        for turn in range(turns):
            if self.turn %5 ==0:
                print("[{0}]".format(self.turn))
            ls = []
            for t in range(len(self.tribes)):
                ls.append(t)
            random.shuffle(ls)  # Losujemy kolejnosc wykonywania tur przez plemiona
            for t in ls:
                self.tribes[t].turn()
            self.turn = self.turn + 1
