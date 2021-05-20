import random
from terrain import Terrain
from tribe import Tribe,NomadTribe
class Map:
    def __init__(self,name:'Just name of the map',config:'Configuration class'):
        self.config = config
        self.name = name
        self.terrains = {}
        self.tribes = []
    def changeOwner(self,x,y,owner):
        
        ter = self.terrains[x,y]
        if hasattr(ter,'owner'):
            ter.owner.remove_terrain(ter)
        self.terrains[x,y].owner =owner
        owner.add_terrain(ter)
    def generate(self):
        '''
        Generating map with paramets given in configuration
        '''
        
        self.x = self.config["map"]["x"]
        self.y = self.config["map"]["y"]
        print("Generating map[{0},{1}]".format(self.x,self.y))
        tribes = self.config ["map"]["tribes"]
        avterrains = self.config["map"]["terrains"]
        if len(avterrains) == 0:
            raise "No terrains given in config!"
        for ix in range(self.x):
            for iy in range(self.y):
                rnd = random.randrange(0,len(avterrains))
                tera = Terrain(avterrains[rnd])
                tera.x = ix
                tera.y = iy
                self.terrains[ix,iy]=tera
                
        print("Generating {} starting tribes".format(tribes))
        avtribes = self.config["tribes"]["starttribes"]
        if len(avtribes) == 0:
            raise "No tribes given in config!"
        for n in range(tribes):
             rnd = random.randrange(0,len(avtribes))
             if self.config["tribes"]["starttribes"][rnd]["type"]== "Nomad":
                 tribe = NomadTribe(self,self.config["tribes"]["starttribes"][rnd])
                 tx = random.randrange(0,self.x)
                 ty = random.randrange(0,self.y)
                 tribe.color = (random.randint(150,255),0,0)
                 self.changeOwner(tx,ty,tribe)
                 self.tribes.append(tribe)

       