class UnionFind():
    def __init__(self, n):
        self.cnt = n
        self.id = range(n)

    def find(self, i):
        if self.id[i] != i:
            self.id[i] = self.find(self.id[i])
        return self.id[i]

    def union(self, i, j):
        rooti, rootj = self.find(i), self.find(j)
        if rooti != rootj:
            self.id[min(rooti, rootj)] = max(rooti, rootj)
            self.cnt -= 1

class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def setUnion(self, sets):
        uf = UnionFind(len(sets))
        sets = [set(i) for i in sets]
        for i in xrange(len(sets)):
            for j in xrange(i+1, len(sets)):
                if sets[i] & sets[j]:
                    uf.union(i, j)
        return uf.cnt

print Solution().setUnion([[1,2,3],[3,9,7],[4,5,10]])
print Solution().setUnion([[1],[1,2,3],[4],[8,7,4,5]])
