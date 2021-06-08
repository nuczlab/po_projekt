from config import Configuration
from map import Map
from simulator import Simulator
from visualization import Visualisation
import time
import numpy as np
import glob
import cv2


def create_video(simulator, vis,x,y,turns=4800):
    vis = Visualisation(sim)
    try:
        file_path = "preview.mp4"
        out = cv2.VideoWriter(
            "preview.mp4", cv2.VideoWriter_fourcc(*"MJPG"), 30, (600, 600)
        )
        for turn in range(turns):
            resized = cv2.resize(vis.create_image(), (600,600), interpolation = cv2.INTER_AREA)
            out.write(resized)
            sim.perform_turn(1)
        out.release()
        print("File saved to {0}".format(file_path))
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
    print("Select option")
    print("[1]- Simulate turn by turn")
    print("[2]- Generate video file")
    input = int(input())
    if input == 1:
        try:
            for i in range(100):
                vis.create_preview()
                sim.perform_turn(turns=1)
        except KeyboardInterrupt:
            pass
    elif input == 2:
        create_video(sim, vis,config["map"]["x"],config["map"]["y"])
    else:
        print("Unkown command")
    exit()
