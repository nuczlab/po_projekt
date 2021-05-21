
class Terrain:
    def __init__(self, dictionary): 
        for k, v in dictionary.items():
            setattr(self, k, v)
        self.owner = None
    
    
