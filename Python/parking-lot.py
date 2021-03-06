'''
Design a parking lot. See CC150 OO Design for details.

1. n levels, each level has m rows of spots and each row has k spots. So each level has m x k spots.
2. The parking lot can park motorcycles, cars and buses
3. The parking lot has motorcycle spots, compact spots, and large spots
4. Each row, motorcycle spots id is in range [0,k/4)(0 is included, k/4 is not included),
compact spots id is in range [k/4,k/4*3) and large spots id is in range [k/4*3,k).
5. A motorcycle can park in any spot
6. A car park in single compact spot or large spot
7. A bus can park in five large spots that are consecutive and within same row. it can not park in small spots

Example
level=1, num_rows=1, spots_per_row=11
parkVehicle("Motorcycle_1") // return true
parkVehicle("Car_1") // return true
parkVehicle("Car_2") // return true
parkVehicle("Car_3") // return true
parkVehicle("Car_4") // return true
parkVehicle("Car_5") // return true
parkVehicle("Bus_1") // return false
unParkVehicle("Car_5")
parkVehicle("Bus_1") // return true

Solution: classes
Vehicle: tuple parking_spots, enum size, spots_needed. Subclasses: Motorcycle, Car, Bus.
    clear_spots() // reset the spots as empty, then set parking_spots as None

Level: 2D list spots; int available_spots; int spots_per_row;

    bool park_vehicle(object vehicle) // iterate each row, check if enough empty spot for the vehicle;
                                      // if yes, set the spots occupied, and assign the (level, row, start_spot) tuple to vehicle

ParkingLot: list levels;

    bool park_vehicle(object vehicle) // call Level::park_vehicle
    void unpark_vehicle(object vehicle) // call Vehicle::clear_spots

### since the spots are regularly arranged motorcycle->compact->large,
we can access eligible spots directly and don't really need the following ParkingSpot class:

ParkingSpot: object level, size, object vehicle
    can_fit_vehicle(vehicle) // must be good size and no vehicle occupied
    park(vehicle)
    remove_vehicle()
'''

# Enum in Python are created using class. https://www.geeksforgeeks.org/enum-in-python/
class VehicleSize:
    Motorcycle = 1
    Compact = 2
    Large = 3
    Other = 99


class Vehicle(object):
    def __init__(self):
        #self.parking_spots = []  # a list of ParkingSpot objects
        self.parking_spots = None # or (Level, row, start_spot) tuple
        self.spots_needed = 0
        self.size = None
        self.license_plate = None

    def get_spots_needed(self):
        return self.spots_needed

    def get_size(self):
        return self.size

#    def park_in_spot(self, spot):
#        self.parking_spots.append(spot)

    def clear_spots(self):
        if self.parking_spots:
            level, row, spot = self.parking_spots
            self.parking_spots = None

            level.spots[row][spot:spot+self.spots_needed] = [None] * self.spots_needed
            level.available_spots += self.spots_needed
#        for spot in self.parking_spots:
#            spot.remove_vehicle()

#        self.park_sports = []


class Motorcycle(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 1
        self.size = VehicleSize.Motorcycle

class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 1
        self.size = VehicleSize.Compact

class Bus(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 5
        self.size = VehicleSize.Large


class Level:
    def __init__(self, flr, num_rows, spots_per_row):
        self.spots = [[None] * spots_per_row for _ in xrange(num_rows)]
        self.spots_per_row = spots_per_row
        self.available_spots = num_rows * spots_per_row

    def park_vehicle(self, vehicle):
        if vehicle.parking_spots: return True

        if self.available_spots < vehicle.spots_needed: return False

        for r, row in enumerate(self.spots):
            start = 0 if vehicle.size == VehicleSize.Motorcycle else \
                self.spots_per_row / 4 if vehicle.size == VehicleSize.Compact else \
                    self.spots_per_row / 4 * 3

            for i in xrange(start, self.spots_per_row - vehicle.spots_needed + 1):
                if all(self.spots[r][j] is None for j in xrange(i, i + vehicle.spots_needed)):
                    vehicle.parking_spots = (self, r, i)
                    self.available_spots -= vehicle.spots_needed
                    self.spots[r][i:i + vehicle.spots_needed] = [1] * vehicle.spots_needed
                    return True
        return False

class ParkingLot:
    # @param {int} n number of leves
    # @param {int} num_rows  each level has num_rows rows of spots
    # @param {int} spots_per_row each row has spots_per_row spots
    def __init__(self, n, num_rows, spots_per_row):
        self.levels = []
        for i in xrange(n):
            self.levels.append(Level(i, num_rows, spots_per_row))

    # Park the vehicle in a spot (or multiple spots). Return false if failed
    def park_vehicle(self, vehicle):
        if vehicle.parking_spots:
            return True

        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    # unPark the vehicle
    def unpark_vehicle(self, vehicle):
        vehicle.clear_spots()

'''
class ParkingSpot:
    def __init__(self, lvl, r, n, sz):
        self.level = lvl  # a Level object
        self.row = r # not used in this problem
        self.spot_number = n # not used in this problem
        self.spot_size = sz
        self.vehicle = None  # a Vehicle object

    def can_fit_vehicle(self, vehicle):
        return not self.vehicle and self.spot_size >= vehicle.get_size()

    def park(self, v):
        if not self.can_fit_vehicle(v):
            return False

        self.vehicle = v
        v.park_in_spot(self)
        return True

    def remove_vehicle(self):
        self.level.spot_freed()
        self.vehicle = None


class Level:
    def __init__(self, flr, num_rows, spots_per_row):
        self.spots = []  # a list of ParkingSpot objects (2d spots stored in 1d list)
        self.spots_per_row = spots_per_row
        self.available_spots = num_rows * spots_per_row;
        self.floor = flr # not used in this problem

        # fill in spots list.
        for r in xrange(num_rows):
            for s in xrange(0, spots_per_row / 4):
                self.spots.append(ParkingSpot(self, r, r * spots_per_row + s, Size.Motorcycle))
            for s in xrange(spots_per_row / 4, spots_per_row / 4 * 3):
                self.spots.append(ParkingSpot(self, r, r * spots_per_row + s, Size.Compact))
            for s in xrange(spots_per_row / 4 * 3, spots_per_row):
                self.spots.append(ParkingSpot(self, r, r * spots_per_row + s, Size.Large))

    def park_vehicle(self, vehicle):
        if self.available_spots < vehicle.spots_needed:
            return False

        spot_num = self.find_available_spots(vehicle)

        if spot_num < 0:
            return False

        vehicle.clear_spots()
        for i in xrange(spot_num, spot_num + vehicle.get_spots_needed()):
            if not self.spots[i].park(vehicle):
                vehicle.clear_spots()
                return False

        self.available_spots -= vehicle.spots_needed
        return True

    def find_available_spots(self, vehicle):
        spots_found = 0

        for i, spot in enumerate(self.spots):
            # row change will reset spots_found
            if i % self.spots_per_row == 0:
                spots_found = 0

            if spot.can_fit_vehicle(vehicle):
                spots_found += 1
            else:
                spots_found = 0

            if spots_found == vehicle.spots_needed:
                return i - (vehicle.spots_needed - 1)

        return -1

    def spot_freed(self):
        self.available_spots += 1


class ParkingLot:
    # @param {int} n number of leves
    # @param {int} num_rows  each level has num_rows rows of spots
    # @param {int} spots_per_row each row has spots_per_row spots
    def __init__(self, n, num_rows, spots_per_row):
        self.levels = []  # a list of Level objects
        for i in xrange(n):
            self.levels.append(Level(i, num_rows, spots_per_row))

    # Park the vehicle in a spot (or multiple spots)
    # Return false if failed
    def park_vehicle(self, vehicle):
        # already parked
        if len(vehicle.parking_spots) == vehicle.get_spots_needed():
            return True

        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    # unPark the vehicle
    def unpark_vehicle(self, vehicle):
        # use vehicle's method as entry since vehicle->spots is 1->n mapping
        vehicle.clear_spots()
'''

pLot = ParkingLot(1,2,11)
m1, c1, c2, c3, c4, c5, b1, b2 = Motorcycle(), Car(), Car(), Car(), Car(), Car(), Bus(), Bus()
print pLot.park_vehicle(m1) #True
print pLot.park_vehicle(c1) #True
print pLot.park_vehicle(c2) #True
print pLot.park_vehicle(c3) #True
print pLot.park_vehicle(c4) #True
print pLot.park_vehicle(c5) #True
print pLot.park_vehicle(b1) #True
print pLot.park_vehicle(b2) #False
pLot.unpark_vehicle(c4)
print pLot.park_vehicle(b2) #False
pLot.unpark_vehicle(c5)
print pLot.park_vehicle(b2) #True
print pLot.park_vehicle(b2) #True
