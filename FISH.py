import numpy as np

class Fish:
    """Each object from the Fish class represents a school of fish.
    Attributes:
        coordinates x & y
        population

    Methods:
        move
        """
    def __init__(self,position,population):
        self.x=position[0]
        self.y=position[1]
        self.population=population
    
    def __string__(self):
        return "%s fish at %s, %s"%(self.count,self.x,self.y)

    def move(self,K_submatrix):
        return "salam"
