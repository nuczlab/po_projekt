from Plemiona.config import Configuration
from Plemiona.map import Map
from Plemiona.simulator import Simulator
from Plemiona.visualization import Visualisation
import time
import numpy as np
import glob
import cv2


if __name__ == "__main__":
    print("Tribe simulator v2")
    print("Loading configuration")
    config = Configuration()
    config.load_from_file("config.yaml")
    sim = Simulator(config)
    sim.generate()
    vis = Visualisation(sim)
    print("[Map] Generated")
    print("Select option")
    print("[1]- Simulate turn by turn")
    print("[2]- Generate video file")
    input = int(input())
    if input == 1:
        try:
            for i in range(100):
                vis.create_preview()
                sim.perform_turn(turns=10)
        except KeyboardInterrupt:
            pass
    elif input == 2:
        vis.create_video(sim, turns=1000, step=10)
    else:
        print("Unkown command")
    exit()
