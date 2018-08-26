'''
Implement a rate limiter, provide one method: is_ratelimited(timestamp, event, rate, increment).
- timestamp: The current timestamp, which is an integer and in second unit.
- event: The string to distinct different event. for example, "login" or "signup".
- rate: The rate of the limit. 1/s (1 time per second), 2/m (2 times per minute), 10/h (10 times per hour), 100/d (100 times per day). The format is [integer]/[s/m/h/d].
- increment: Whether we should increase the counter. (or take this call as a hit of the given event)

The method should return true or false to indicate the event is limited or not.

Example:
is_ratelimited(1, "login", "3/m", true), return false.
is_ratelimited(11, "login", "3/m", true), return false.
is_ratelimited(21, "login", "3/m", true), return false.
is_ratelimited(30, "login", "3/m", true), return true.
is_ratelimited(65, "login", "3/m", true), return false.
is_ratelimited(300, "login", "3/m", true), return false.
'''

import bisect, collections

# No truncate of records, so we need to optimize storage space.
class Solution:
    def __init__(self):
        # ts stores the mapping {event : hit_timestamps}. And each hit_stamps
        # is a list of lists [[timestamp1, count1], [timestamp2, count2]...]
        self.ts = collections.defaultdict(list)
        self.lookbacks = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}

    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """
    def is_ratelimited(self, timestamp, event, rate, increment):
        cap, unit = rate.split('/')
        lookback = self.lookbacks[unit]
        index = bisect.bisect([x[0] for x in self.ts[event]], timestamp - lookback)
        count, limited = 0, False
        for record in self.ts[event][index:]:
            count += record[1]
            if count >= int(cap):
                limited = True

        # add new timestamp
        if not limited and increment:
            if self.ts[event] and self.ts[event][-1][0] == timestamp:
                self.ts[event][-1][1] += 1
            else:
                self.ts[event].append([timestamp, 1])

        return limited

sol = Solution()
print sol.is_ratelimited(3, "signup", "10/s", False) #False
print sol.is_ratelimited(3, "signup", "10/s", False) #False
print sol.is_ratelimited(7, "signin", "60/s", False) #False
print sol.is_ratelimited(7, "signin", "60/s", False) #False
print sol.is_ratelimited(8, "signin", "3/m", False) #False
print sol.is_ratelimited(13, "signup", "10/s", True) #False
print sol.is_ratelimited(16, "signin", "1/m", True) #False
print sol.is_ratelimited(16, "signup", "10/s", True) #False
print sol.is_ratelimited(16, "signup", "10/s", True) #False
print sol.is_ratelimited(18, "signin", "10/s", True) #False
print sol.is_ratelimited(20, "signup", "10/s", True) #False
print sol.is_ratelimited(23, "signup", "10/s", True) #False
print sol.is_ratelimited(25, "signup", "3/m", False) #True
print sol.is_ratelimited(25, "signup", "1/m", True) #True
print sol.is_ratelimited(25, "signup", "5/m", True) #True
print sol.is_ratelimited(25, "signup", "5/m", True) #True
print sol.is_ratelimited(26, "signup", "3/m", False) #True
print sol.is_ratelimited(31, "signin", "5/m", True) #False
print sol.is_ratelimited(34, "signup", "60/s", True) #False
print sol.is_ratelimited(35, "signin", "60/s", True) #False
print sol.is_ratelimited(38, "signin", "5/m", False) #False
print sol.is_ratelimited(38, "signin", "5/m", False) #False
print sol.is_ratelimited(41, "signin", "60/s", False) #False
print sol.is_ratelimited(42, "signin", "5/m", True) #False