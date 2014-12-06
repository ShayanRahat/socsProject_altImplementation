#!/usr/bin/python
"""Main function for the SOCS project code. Brings together and utilizes different class definitions"""
import FISH
import SEA
import SAILOR

import random
import matplotlib.pyplot as plt
plt.ion()

#Initializeing the sea object
sea_size=(100,100)
sea=SEA.Sea(sea_size)
print("Sea carrying capacity:",sea.K)

#-------------------------------------------------------------------------
#The main script also populates the sea with a number of fish schools and keeps a list of pointers to those fish schools.
min_init_school_size=300
max_init_school_size=800
number_of_schools=90
school_register=[]
total_fish_population=0

for this_school in range(number_of_schools):
    position=(random.choice(range(sea_size[0])),random.choice(range(sea_size[1])))
    population=min(random.choice(range(min_init_school_size,max_init_school_size)),sea.K[position[0]][position[1]])
    school_register.append(FISH.Fish(position,population))
    total_fish_population+=population
    #print("Created fish school at position:",position)
    #print("School population=",population)
#print(school_register)

#----------------------------------------------------------------------------
#Let's create some sailors!
number_of_fishermen=35
sailor_register=[]
for sailor in range(number_of_fishermen):
    position=(random.choice(range(sea_size[0])),random.choice(range(sea_size[1])))
    sailor_register.append(SAILOR.Sailor(position))
    print("There's a sailor at",position)


#-----------------------------------------------------------------------------
#A test figure to see how appropriate a scatter plot would be for visualizing our data.
fig1=plt.figure()
axes=plt.subplot(111)
x=[]
y=[]
radius=[]
for i in range(len(school_register)):
    x.append(school_register[i].x)
    y.append(school_register[i].y)
    radius.append(school_register[i].population)

plt.scatter(x,y,s=radius)
plt.show()

#print(x)
#print(y)

print("Total fish population is:",total_fish_population)
#--------------------------------------------------------------------------------
#My first attempt at simulating the daily fishing dynamics
for times in range(20):
    for sailor in sailor_register:
        axes.cla()
        #The method representing the act of fishing is implimented in the sea class. Maybe not the most obvious choice, but I had my reasons.
        print("A sailor caught:",sea.cast_net(sailor))
        sea.census(school_register)
        x=[]
        y=[]
        radius=[]
        for i in range(len(school_register)):
            x.append(school_register[i].x)
            y.append(school_register[i].y)
            radius.append(school_register[i].population)
        plt.scatter(x,y,s=radius)
        fig1.canvas.draw()

for sailor in sailor_register:
    print(sailor.spoils)

total_fish_population=0
for school in school_register:
    total_fish_population+=school.population

print("Total fish population is:",total_fish_population)

#plt.scatter(x,y,s=radius)
#plt.show()
