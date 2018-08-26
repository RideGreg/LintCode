'''
Support two basic uber features:
1. Drivers report their locations.
2. Rider request a uber, return a matched driver.

When rider request a uber, match a closest available driver with him, then mark the driver not available.
When next time this matched driver report his location, return with the rider's information.

You can implement it with the following instructions:
1. report(driver_id, lat, lng)
   return null if no matched rider.
   return matched trip information.
2. request(rider_id, lat, lng)
   create a trip with rider's information.
   find a closest driver, mark this driver not available.
   fill driver_id into this trip.
   return trip

Example
report(1, 36.1344, 77.5672) // return null
report(2, 45.1344, 76.5672) // return null
request(2, 39.1344, 76.5672) // return a trip, LOG(INFO): Trip(rider_id: 2, driver_id: 1, lat: 39.1344, lng: 76.5672)
report(1, 38.1344, 75.5672) // return a trip, LOG(INFO): Trip(rider_id: 2, driver_id: 1, lat: 39.1344, lng: 76.5672)
report(2, 45.1344, 76.5672) // return null
'''

'''
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
'''
from Trip import Trip, Helper

class MiniUber:
    def __init__(self):
        self.driver2Location = {}  # available drivers
        self.driver2Trip = {}

    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        if driver_id in self.driver2Trip:
            return self.driver2Trip[driver_id]

        self.driver2Location[driver_id] = (lat, lng)
        return None


    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    def request(self, rider_id, lat, lng):
        minDistance, minDriverId = float('inf'), None
        for dId, loc in self.driver2Location.items():
            curDistance = Helper.get_distance(lat, lng, loc[0], loc[1])
            if  minDistance > curDistance:
                minDistance, minDriverId = curDistance, dId

        trip = Trip(rider_id, lat, lng)
        trip.driver_id = minDriverId

        if minDriverId:
            self.driver2Trip[minDriverId] = trip
            del self.driver2Location[minDriverId]

        return trip
