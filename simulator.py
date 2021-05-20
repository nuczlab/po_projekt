from map import Map
from config import Configuration
class Simulator:

    def __init__(self,config):
        self.config = config
    def generate(self):
        print("Creating Map")
        self.map = Map("A1",self.config)
        self.map.generate()
    def performTurn(self):
        ls = []
        for t in range(len(self.tribes)):
            ls.append(t)
        ls = random.shuffle(ls)
        for t in ls:
            self.tribes[t].turn()
