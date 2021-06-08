from config import Configuration
from map import Map
from simulator import Simulator
from visualization import Visualisation
import time
import numpy as np
import glob
import cv2

def create_video(simulator,vis,turns=200):
    vis = Visualisation(sim)
    try:
        out = cv2.VideoWriter('preview.mp4',cv2.VideoWriter_fourcc(*'MJPG'), 15, (200,200))
        for turn in range(turns):
            out.write(vis.create_image())
            sim.perform_turn(1)
        out.release()
        
    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    print("Tribe simulator v2")
    print("Loading configuration")
    config = Configuration()
    config.load_from_file("config.yaml")
    sim = Simulator(config)
    sim.generate()
    vis = Visualisation(sim)
    print("[Map] Generated")
    print('Select option')
    print('[1]- Simulate turn by turn')
    print('[2]- Generate video file')
    input = int(input())
    if input == 1:
        try:
            for i in range(100):
                vis.create_preview()
                sim.perform_turn(turns=1)
        except KeyboardInterrupt:
            pass
    elif input == 2:
        create_video(sim,vis)
    else:
        print('Unkown command')
    exit()
    