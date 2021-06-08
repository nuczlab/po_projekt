import cv2
import numpy


class Visualisation:
    def __init__(self, simulator) -> None:
        self.simulator = simulator
        pass

    def attach(self, simulator):
        self.simulator = simulator
    def create_image(self):
        map = self.simulator.map
        img2 = numpy.zeros((map.x, map.y, 3), numpy.uint8)
        for ix in range(map.x):
            for iy in range(map.y):
                if map.terrains[ix, iy].owner != None:
                    img2[ix, iy] = map.terrains[ix, iy].owner.color
                else:
                    img2[ix, iy] = map.terrains[ix, iy].color
        im_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        return im_rgb
    def create_preview(self):
        im_rgb = self.create_image()
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.imshow("image", im_rgb)
        cv2.resizeWindow("image", 600, 600)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
