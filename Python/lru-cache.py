'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

- get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
- set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.
'''

import collections
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.cache:
            return -1
        ans = self.cache.pop(key)
        self.cache[key] = ans
        return ans

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

# if OrderedDict is not allowed to use, doubly linked list + hash
class DListNode(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
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


class LRUCache2:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.cache = {}
        self.dll = LinkedList()
        self.capacity = capacity

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.dll.delete(node)
        self.dll.insert(node)
        return node.val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.dll.delete(node)
        elif len(self.cache) == self.capacity:
            node = self.dll.head
            self.dll.delete(node)
            self.cache.pop(node.key)
        node = DListNode(key, value)
        self.cache[key] = node
        self.dll.insert(node)
