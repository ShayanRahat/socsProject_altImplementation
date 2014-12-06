class Sailor:
    """The class representing each fishing boat.
    Attributes:
        coordinates x & y
        spoils
        perception

    Methods:
        move
    """
    def __init__(self,position):
        self.x=position[0]
        self.y=position[1]
        self.spoils=0


    def move(self,sea_size):

        print("I'm gonna move!")
