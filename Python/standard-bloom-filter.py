'''
Implement a standard bloom filter . Support the following method:
1. StandardBloomFilter(k),The constructor and you need to create k hash functions.
2. add(string). add a string into bloom filter.
3. contains(string). Check a string whether exists in bloom filter.

Example:
StandardBloomFilter(3)
add("lint")
add("code")
contains("lint") // return true
contains("world") // return false
'''

import random

class HashFunc:
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, s):
        ans = 0
        for c in s:
            ans = (self.seed * ans + ord(c)) % self.cap
        return ans

class StandardBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.bitset = set()
        self.hashFuncs = []
        for i in xrange(k):
            self.hashFuncs.append(HashFunc(random.randint(10000, 20000), 2 * i + 3))

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        for f in self.hashFuncs:
            v = f.hash(word)
            self.bitset.add(v)

    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        for f in self.hashFuncs:
            v = f.hash(word)
            if v not in self.bitset:
                return False
        return True
