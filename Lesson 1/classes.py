'''
class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(f"This is the Point: {p}")
print(f"This is the Point X value: {p.x}")
print(f"This is the Point Y value: {p.y}")
'''

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

    #mention self in a function so that you can use self.components
    def addPassenger(self, name):
        if not self.openSeats():
            return False
        self.passenger.append(name)
        return True

    def openSeats(self):
        #return the remaining seats from the total capacity - number of passengers
        return self.capacity - len(self.passenger)


flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.addPassenger(person)
    if success:
        print(f"Added {person} to flight")
    else:
        print(f"No available seats for {person}")