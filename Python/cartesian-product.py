'''
We use a two-dimensional array setList[][] to represent a collection array, and each element in setList[i]
is an integer and is not the same. Find the cartesian product of setList[0],setList[1],...,setList[setList.length - 1].
In general, the Cartesian product of the collection A and the set B is A×B = {(x,y)|x∈A∧y∈B}。

Example
Given setList = [[1,2,3],[4],[5,6]], return [[1,4,5],[1,4,6],[2,4,5],[2,4,6],[3,4,5],[3,4,6]].

https://stackoverflow.com/questions/533905/get-the-cartesian-product-of-a-series-of-lists
'''
class Solution:
    """
    @param setList: The input set list
    @return: the cartesian product of the set list
    """
    def getSet(self, setList):
        import itertools
        return map(list, itertools.product(*setList))