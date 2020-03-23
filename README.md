## Airport :taco:


## Abstraction
Making code more simpler to understand by:
- documentation
- seperation of concerns
- inheritance
## encapsulation
Making items more secure by privatising attributes or methods.
Privatasing is important because there is a restriction of
access to from external functions and methods.

Getter and Setter methods are used for privatisation.
## inheritance
This allows child classes take in attributes or methods from parent classes

## polymorphism
Methods can take many forms allowing you to overwrite methods
## Git
Git is a distributed version control system
## github
## good naming
Good naming is appropriately naming entities
some practices
- snake case - for naming variables
- not referencing keywords such as break
## DRY
Do-Not
Repeat
Yourself
This is to ensure that there is no reduntant actions such as constantly repeating
code when they can be reduced by functions and arguments from methods and functions.
## Control flow

## Seperation of concerns
## dod
When all conditions of the acceptance criterea is complete
- working code
- readme.md
- git
- github

## Passengers
- as a user I can create a Passanger :tick:
- It can be created with name and passport number :tick:
- I can create 'Joana Thomson' with the Passport number 'B343123' :tick:
- I can create 'Birt Kuman' with the Passport number 'B13927' :tick:

### Plane

- As a User I can create a Plane with a plane number:tick:

### Flight trip
- As a user I can create a flight with no specific information:tick:
- as a user I can add a plane
- as a User I can add a destination
- As a user I can add a origin
- As a user I can add a Passanger to the list of passangers in the flight trip
- Passanger list is a list of object that are Passangers

## Main methods
```python
class Aircraft():
    def __init__(self, cargo = 200):
        self.cargo = cargo

class FlightTrip():
    def __init__(self, origin = '', destination = '', plane_list = []):
        self.origin = origin
        self.destination = destination
        self.plane_number = plane_list

class People():
    def __init__(self, name):
        self.name = name

class Passenger(People):
    def __init__(self, name, passport_number):
        super().__init__(name)
        self.passport_number = passport_number

```

## Child methods
```python
class Passenger(People):
    def __init__(self, name, passport_number):
        super().__init__(name)
        self.passport_number = passport_number

class Plane(Aircraft):
    def __init__(self, plane_number, cargo):
        super().__init__(cargo)
        self.plane_number = plane_number

```
# Clone

git clone https://github.com/Maksaud/airport.git

# To run
python3 run_airport.py
