
from math import sqrt

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, name = "TBD", x=0, y=0, weight=1000, numLaunches=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        self.name = name
        self.weight = weight
        self.numLaunches = numLaunches
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return distance

    def get_name(self):
        #simply return the name
        return self.name

    def launch(self):
        self.numLaunches += 1
        print("Launching {} for the {} launch in".format(self.name, self.numLaunches))
        for i in reversed(range(1, 11)):
            print(i)
        print("BLASTOFF")

    def land(self):
        self.y = 0

    
# Make two rockets, at different places.
rocket1 = Rocket()
rocket2 = Rocket("Tom",10,5)
myRocket = Rocket("YUM", 1, 1, 10000, 25)
print(rocket1.name)
print(rocket2.name)
print(rocket2.name)

# Show the distance between them.
distance = rocket1.get_distance(rocket2)
print("The rockets are %f units apart." % distance)

# Move rocket1 up a bit
rocket1.move_rocket(0,2)
distance = rocket1.get_distance(rocket2)
print("The rockets are,", distance, " units apart.")
rocket1.move_rocket(0,2)
distance = rocket1.get_distance(rocket2)
print("The rockets are %f units apart." % distance)
print(rocket1)

# Launch the rocket
myRocket.launch()

# Print all values in a the class
attrs = vars(myRocket)
print(', '.join("%s: %s" % item for item in attrs.items()))
