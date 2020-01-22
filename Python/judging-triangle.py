'''
Given an array arr, ask if you can find 3 elements from the array as the sides of the three sides, so that the three sides can form a triangle.

Example
Give arr=[2,3,5,8], return no.
Give arr=[3,4,5,8] , return yes.
'''
class Solution:
    """
    @param arr: The array
    @return: yes or no
    """
    def judgingTriangle(self, arr):
        if len(arr) < 3: return "no"
        arr.sort()
        return "yes" if arr[-2]+arr[-3]>arr[-1] else "no"