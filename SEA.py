import random
class Sea:
    """The Sea class acts as an interface between the fish and the fishermen.
    Attributes:
        dims    a tuple containing the size of the matrix
        K       matrix



    """
    def __init__(self,dims):
        print("Creating a Sea object.")
        K_min=400
        K_max=1000
        self.dims=dims
        print("Sea size is:",self.dims,"\n\n")
        #The K attribute is probably the most important piece of data in the sea class. The implementation can be changed to test different ideas.
        self.K=[ [random.randint(K_min,K_max) for j in range(self.dims[1])] for i in range(self.dims[0]) ]
        self.fishbook=[[ set() for j in range(self.dims[1])] for i in range(self.dims[0])]

    def census(self,school_register):
        self.fishbook=[[ set() for j in range(self.dims[1])] for i in range(self.dims[0])]
        for fish in school_register:
            i,j=fish.x,fish.y
            self.fishbook[i][j].add(fish)


    def nearby_fish(self,i,j):
        return [self.fishbook[i-1][j-1], self.fishbook[i-1][j], self.fishbook[i-1][(j+1)%self.dims[1]], self.fishbook[i][j-1], self.fishbook[i][j], self.fishbook[i][(j+1)%self.dims[1]], self.fishbook[(i+1)%self.dims[0]][j-1], self.fishbook[(i+1)%self.dims[0]][j], self.fishbook[(i+1)%self.dims[0]][(j+1)%self.dims[1]] ]


    def cast_net(self,sailor):
        for sea_tile in self.nearby_fish(sailor.x,sailor.y):
            for school in sea_tile:
                fish_caught=int(0.5*school.population)
                school.population-=fish_caught
                sailor.spoils+=fish_caught
                return fish_caught


