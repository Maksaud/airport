from passanger_class import *
from plane_class import *
from flight_trip_class import *
from aircraft_class import *
from people_class import *

flight_trip1 = FlightTrip()
print(flight_trip1)
flight_trip1.plane_list.append(passenger1)
flight_trip1.plane_list.append(passenger2)

print(flight_trip1.plane_list)