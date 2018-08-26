'''
LFU (Least Frequently Used) is a famous cache eviction algorithm.
For a cache with capacity k, if the cache is full and need to evict a key in it, the key with the lease frequently used will be kicked out.
Implement set and get method for LFU cache.

Example: Given capacity=3
set(2,2)
set(1,1)
get(2) >> 2
get(1) >> 1
get(2) >> 2
set(3,3)
set(4,4)
get(3) >> -1  # least used freq
get(2) >> 2
get(1) >> 1
get(4) >> 4
'''

import collections

class DListNode(object):
    def __init__(self, key, value, freq):
        self.key = key
        self.val = value
        self.freq = freq
        self.next = None
        self.prev = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        node.next, node.prev = None, None  # avoid dirty node
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next, node.prev = None, None  # make node clean

class LFUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.__capa = capacity
        self.__size = 0
        self.__min_freq = 0
        self.__freq_to_nodes = collections.defaultdict(LinkedList)
        self.__key_to_node = {}
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if self.__capa <= 0:
            return

        if self.get(key) != -1:
            self.__key_to_node[key].val = value
            return

        if self.__size == self.__capa:
            del self.__key_to_node[self.__freq_to_nodes[self.__min_freq].head.key]
            self.__freq_to_nodes[self.__min_freq].delete(self.__freq_to_nodes[self.__min_freq].head)
            if not self.__freq_to_nodes[self.__min_freq].head:
                del self.__freq_to_nodes[self.__min_freq]
            self.__size -= 1

        self.__min_freq = 1
        self.__key_to_node[key] = DListNode(key, value, self.__min_freq)
        self.__freq_to_nodes[self.__key_to_node[key].freq].append(self.__key_to_node[key])
        self.__size += 1
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.__key_to_node:
            return -1

        # increment freq, move to the list with higher frequency
        old_node = self.__key_to_node[key]
        self.__key_to_node[key] = DListNode(key, old_node.val, old_node.freq)
        self.__freq_to_nodes[old_node.freq].delete(old_node)
        if not self.__freq_to_nodes[self.__key_to_node[key].freq].head:
            del self.__freq_to_nodes[self.__key_to_node[key].freq]
            if self.__min_freq == self.__key_to_node[key].freq:
                self.__min_freq += 1

        self.__key_to_node[key].freq += 1
        self.__freq_to_nodes[self.__key_to_node[key].freq].append(self.__key_to_node[key])

        return self.__key_to_node[key].val
