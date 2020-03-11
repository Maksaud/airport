# define plane class
# inherits from aircraft
from aircraft_class import *
class Plane(Aircraft):
    def __init__(self, plane_number, cargo):
        super().__init__(cargo)
        self.plane_number = plane_number
# attributes it needs:
    # plane_namber

plane1 = Plane('300', 200)

print(plane1.plane_number)