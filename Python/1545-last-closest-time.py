# Given a string representing the time"12:34"(This is a legal input data), return
# the most recent time within the first 24 hours.If the input is illegal, return -1.

class Solution:
    def lastTime(self, time):
        if len(time) != 5 or time[2] != ':':
            return "-1"
        h, m = int(time[:2]), int(time[3:])
        if not (0 <= h < 24 and 0 <= m < 60):
            return "-1"

        m -= 1
        if m < 0:
            h -= 1
            if h < 0:
                h += 24
            m += 60
        return "%02d:%02d" % (h, m)

print(Solution().lastTime("00:00")) # "23:59"