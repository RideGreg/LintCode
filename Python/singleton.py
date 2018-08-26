'''
Singleton is a most widely used design pattern. If a class has and only has one instance at every moment,
we call this design as singleton. For example, for class Mouse (not a animal mouse), we should design it in singleton.

You job is to implement a getInstance method for given class, return the same instance of this class every time you call this method.

The solution at https://www.jiuzhang.com/solution/singleton/ is not good,
because there is no way of creating private classes or private constructors in Python,
so you can't protect against multiple instantiations, other than just via getInstance() API.

Correct way to create singleton in Python
- complete ways
https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
- use module (module only loads once)
https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons
'''

# override __new__ method, the class is a singleton, it can also server as a base class
# of other classes which need to be singletons.
class Solution(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
            #The following causes 'maximum recursion depth exceeded'
            #cls._instance = Solution()
        return cls._instance


# jiuzhang solution cannot prevent instantiation via the class name.
class Solution_jiuzhang():
    _instance = None

    # @return: The same instance of this class every time
    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = Solution()
        return cls._instance


s = Solution()
s1 = Solution()

# <__main__.Solution object at 0x10bbb3210> <__main__.Solution object at 0x10bbb3210>
print s, s1

# 4491784720 4491784720
print id(s), id(s1)

# <__main__.Solution object at 0x10bbb3210> <__main__.Solution object at 0x10bbb3210>
print Solution._instance, s._instance

