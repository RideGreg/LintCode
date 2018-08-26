'''
Implement a web logger, which provide two methods:
1 hit(timestamp), record a hit at given timestamp.
2 get_hit_count_in_last_5_minutes(timestamp), get hit count in last 5 minutes.

the two methods will be called with non-descending timestamp (in sec).

The solution should OPTIMIZED for the case many hits at the same timestamp.

Example
hit(1);
hit(2);
get_hit_count_in_last_5_minutes(3); >> 2
hit(300);
get_hit_count_in_last_5_minutes(300); >> 3
get_hit_count_in_last_5_minutes(301); >> 2
'''


class WebLogger:  # USE THIS
    def __init__(self):
        self.counter = 0
        self.ts = []  # element of ts is an array [timestamp, hit count at this timestamp]

    """
    @param: timestamp: An integer
    @return: nothing
    """
    def hit(self, timestamp):
        self.counter += 1
        if self.ts and self.ts[-1][0] == timestamp:
            self.ts[-1][1] += 1
        else:
            self.ts.append([timestamp, 1])

    """
    @param: timestamp: An integer
    @return: An integer
    """
    def get_hit_count_in_last_5_minutes(self, timestamp):
        i = 0
        while i < len(self.ts) and self.ts[i][0] <= timestamp - 300:
            self.counter -= self.ts[i][1]
            i += 1

        self.ts = self.ts[i:]
        return self.counter


class WebLogger_spaceWaste: # hits at the same time are saved as multiple entries
    import bisect
    def __init__(self):
        self.ts = []

    """
    @param: timestamp: An integer
    @return: nothing
    """
    def hit(self, timestamp):
        self.ts.append(timestamp)

    """
    @param: timestamp: An integer
    @return: An integer
    """
    def get_hit_count_in_last_5_minutes(self, timestamp):
        index = bisect.bisect(self.ts, timestamp - 300)
        self.ts = self.ts[index:]
        return len(self.ts)
