from map import Map
from config import Configuration
import random
class Simulator:

    def __init__(self,config):
        self.config = config
    def generate(self):
        print("Creating Map")
        self.map = Map("A1",self.config)
        self.map.generate()
        self.tribes =self.map.tribes
    def performTurn(self):
        ls = []
        for t in range(len(self.tribes)):
            ls.append(t)
        
        random.shuffle(ls)
        
        for t in ls:
            self.tribes[t].turn()
