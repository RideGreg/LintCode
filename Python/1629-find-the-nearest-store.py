# There are some stores and houses on a street. Please find the nearest store to each house.
#
# You are given two array represent the location of the stores and houses.
#
# Return an array with the location of the nearest store to each house. If there are two stores that are
# the same distance from the house return the left one.
#
# Tips:
# 1. There are multiple stores and houses in the same location. And the locations in array are disordered.
# 2. The array of location must not be empty.

class Solution(object):
    def findNearestStore(self, stores, houses):
        def search(stores, h):
            l, r = 0, len(stores) - 1
            while l < r - 1:
                m = l + (r - l) / 2
                if stores[m] == h:
                    return h
                elif stores[m] < h:
                    l = m
                else:
                    r = m
            return stores[l] if abs(stores[l] - h) <= abs(stores[r] - h) else stores[r]

        ans = []
        stores.sort()
        for h in houses:
            ans.append(search(stores, h))
        return ans