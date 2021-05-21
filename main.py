from config import Configuration
from map import Map
from simulator import Simulator
from visualization import Visualisation
import time
if __name__ == "__main__":
    print("Tribe simulator v1")
    print("Loading configuration")
    config = Configuration()
    config.load_from_file("config.yaml")
    sim = Simulator(config)
    sim.generate()
    vis = Visualisation(sim)
    try:
        while True:
            vis.create_preview()
            sim.perform_turn()
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
        
    
    