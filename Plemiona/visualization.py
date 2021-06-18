import cv2
import numpy
from Plemiona.simulator import Simulator


class Visualisation:
    def __init__(self, simulator: Simulator) -> None:
        """
        Method used to load configuration from yaml file
        Parameters
        ----------
        simulator : Simulator
            Simulator instance we want attach to
        """
        self.simulator = simulator
        pass

    def create_image(self):
        """
        Method used to generate image of current simulaiton status (with tribes and unocupied terrains)
        """
        map = self.simulator.map
        img2 = numpy.zeros((map.x, map.y, 3), numpy.uint8)
        for ix in range(map.x):
            for iy in range(map.y):
                if map.terrains[ix, iy].owner != None:
                    img2[ix, iy] = map.terrains[ix, iy].owner.color
                else:
                    img2[ix, iy] = map.terrains[ix, iy].color
        im_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        color = (255, 255, 255)
        font_scale = 0.5
        thickness = 1
        im_rgb = cv2.putText(
            im_rgb,
            str(self.simulator.turn),
            (30, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            font_scale,
            color,
            thickness,
            cv2.LINE_AA,
        )
        return im_rgb

    def create_video(self, sim, turns=200, step=1):
        """
        Method used to generate video file with simulation
        """
        try:
            file_path = "preview.mp4"
            out = cv2.VideoWriter(
                "preview.mp4", cv2.VideoWriter_fourcc(*"MJPG"), 15, (200, 200)
            )
            for turn in range(int(turns / step)):
                out.write(self.create_image())
                sim.perform_turn(step)
            out.release()
            print("File saved to {0}".format(file_path))
        except KeyboardInterrupt:
            pass

    def create_preview(self):
        """
        Method used to generate opencv preview of current simulation status
        """
        im_rgb = self.create_image()
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.imshow("image", im_rgb)
        cv2.resizeWindow("image", 600, 600)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
