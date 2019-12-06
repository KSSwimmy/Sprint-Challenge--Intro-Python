# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4): # it has 4 wheels now
        self.num_wheels = num_wheels

    def drive(self): # added the method to return vroom vroom
			  return 'vroooom'

    


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle): # inheritance 
	  def __init__(self, num_wheels=2): # 2 wheels because it's a motorcycle... 
		  super().__init__(num_wheels) # the constructor that calls the su

	  def drive(self):
		  return 'BRAAAP!!'


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

res = [v.drive() for v in vehicles]
