'''
Implement a counting bloom filter. Support the following method:
1 add(string). Add a string into bloom filter.
2 contains(string). Check a string whether exists in bloom filter.
3 remove(string). Remove a string from bloom filter.

Exmaple
CountingBloomFilter(3)
add("lint")
add("code")
contains("lint") // return true
remove("lint")
contains("lint") // return false
'''

import random, collections

class HashFunc:
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, s):
        ans = 0
        for c in s:
            ans += (self.seed * ans + ord(c)) % self.cap
        return ans

class CountingBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.bits = collections.defaultdict(int)
        self.hashFuncs = []
        for i in xrange(k):
            self.hashFuncs.append(HashFunc(random.randint(10000, 20000), i * 2 + 3))

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        for f in self.hashFuncs:
            v = f.hash(word)
            self.bits[v] += 1

    """
    @param: word: A string
    @return: nothing
    """
    def remove(self, word):
        # bloom filter is probabilistic, this is not 100% accurate.
        # It may mistakenly reduce some value to negative.
        if self.contains(word):
            for f in self.hashFuncs:
                v = f.hash(word)
                self.bits[v] -= 1

    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        for f in self.hashFuncs:
            v = f.hash(word)
            if self.bits[v] <= 0:
                return False
        return True