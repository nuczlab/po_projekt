from config import Configuration
from map import Map
from simulator import Simulator
from visualization import Visualisation
if __name__ == "__main__":
    print("Tribe simulator v1")
    print("Loading configuration")
    config = Configuration()
    config.load_from_file("config.yaml")
    sim = Simulator(config)
    sim.generate()
    vis = Visualisation(sim)
    vis.createpreview()
    
    