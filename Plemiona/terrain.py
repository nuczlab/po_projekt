class Terrain:
    production_multiplier = 1

    def __init__(self, dictionary):
        self.owner = None
        self.crossable = True
        self.x = -1
        self.y = -1
        for k, v in dictionary.items():
            setattr(self, k, v)
