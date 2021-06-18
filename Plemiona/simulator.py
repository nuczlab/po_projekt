from Plemiona.map import Map
from Plemiona.config import Configuration
from Plemiona.map_generator import MapGenerator
import random


class Simulator:
    """
    Class resposnible for processing simulation
    """

    def __init__(self, config: Configuration):
        """

        Parameters
        ----------
        config : Config
            Instance of configuration class
        """
        self.config = config

    def generate(self):
        """
        Function used to generate map and tribes according to given configuration
        Parameters
        ----------
        config : Config
            Instance of configuration class
        """
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
        """
        Method used to perform turn in simulation
        Parameters
        ----------
        turns : int, optional
            How many turn we want to perform in method
        """
        for turn in range(turns):
            print("[{0}]".format(self.turn))
            ls = []
            for t in range(len(self.tribes)):
                ls.append(t)
            random.shuffle(ls)  # We want to randomize order of performing turns
            for t in ls:
                self.tribes[t].turn()
            self.turn = self.turn + 1
