'''
Design a simple yelp system. Support the following features:
1. Add a restaurant with name and location.
2. Remove a restaurant with id.
3. Search the nearby restaurants by given location.

A location is represented by latitude and longitude, both in double. A Location class is given in code.

Nearby is defined by distance smaller than k Km .

Restaurant class is already provided and you can directly call Restaurant.create() to create a new object.
Also, a Helper class is provided to calculate the distance between two location, use Helper.get_distance(location1, location2).

A GeoHash class is provided: GeoHash.encode(location) to convert location to a geohash string and
GeoHash.decode(string) to convert a string to location.

Example:
addRestauraunt("Lint Cafe", 10.4999999, 11.599999) // return 1
addRestauraunt("Code Cafe", 10.4999999, 11.512109) // return 2
neighbors(10.5, 11.6, 6.7) // return ["Lint Cafe"]
removeRestauraunt(1)
neighbors(10.5, 9.6, 6.7) // return []


// The distance between location(10.5, 11.6) and "Lint Code" is 0.0001099 km
// The distance between location(10.5, 11.6) and "Code Code" is 9.6120978 km
'''

from YelpHelper import Location, Restaurant, GeoHash, Helper
import bisect

# USE THIS. Sort restaurants by geohash. Use bisect to limit the search scope.
class MiniYelp:
    def __init__(self):
        self.restaurants = {}
        self.id2hashcode = {}  # only used for remove_restaurant which index by id
        self.geo_value = []  # sorted list by geohash

    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        r = Restaurant.create(name, location)
        # add r.id incase two locations has the same geohash
        hashcode = "{}.{}".format(GeoHash.encode(location), r.id)

        self.restaurants[hashcode] = r
        self.id2hashcode[r.id] = hashcode
        bisect.insort(self.geo_value, hashcode)
        return r.id

    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        if restaurant_id in self.id2hashcode:
            hashcode = self.id2hashcode[restaurant_id]
            del self.restaurants[hashcode]
            del self.id2hashcode[restaurant_id]

            index = bisect.bisect_left(self.geo_value, hashcode)
            self.geo_value.pop(index)

    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return {str[]} a list of restaurant's name and sort by
    # distance from near to far.
    def neighbors(self, location, k):
        def getBitLength(k):
            errors = [2500, 630, 78, 20, 2.4, 0.61, 0.076, 0.019, 0.0024, 0.0006, 0.000074]
            for i, v in enumerate(errors):
                if k > v:
                    return i
            return len(errors)

        # the first bitLength bits must match in order to be within distance k Km.
        bitLength = getBitLength(k)
        code = GeoHash.encode(location)[:bitLength]
        left = bisect.bisect_left(self.geo_value, code)
        right = bisect.bisect_right(self.geo_value, code + '{')  # '{' is after 'z'

        ans = []
        for index in xrange(left, right):
            hashcode = self.geo_value[index]
            r = self.restaurants[hashcode]
            distance = Helper.get_distance(location, r.location)
            if distance < k:
                ans.append((distance, r.name))
        ans.sort(key=lambda x: x[0])
        return [x[1] for x in ans]


# Brute force solution: linear scan all restaurants
class MiniYelp_linear:
    def __init__(self):
        self.restaurants = {}

    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        r = Restaurant.create(name, location)
        self.restaurants[r.id] = r
        return r.id

    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        if restaurant_id in self.restaurants:
            self.restaurants.pop(restaurant_id)

    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return {str[]} a list of restaurant's name and sort by
    # distance from near to far.
    def neighbors(self, location, k):
        ans = []
        for r in self.restaurants.values():
            dist = Helper.get_distance(r.location, location)
            if dist < k:
                ans.append((dist, r.name))
        ans.sort(key=lambda x: x[0])
        return [x[1] for x in ans]