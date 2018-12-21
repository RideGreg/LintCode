# Give a String, representing the time, such as "12:34"(This is a legal input data), and find its next
# time does not repeat the number. If it is the largest"23:59", the reply is the smallest"01:23".
# If the input is illegal, return "-1".

class Solution:
    def nextTime(self, time):
        if not (len(time) == 5 and time[2] == ':'):
            return "-1"
        h, m = int(time[:2]), int(time[3:])
        if not (0 <= h < 24 and 0 <= m < 60):
            return "-1"

        t = h * 60 + m
        while True:
            if t == 24 * 60 - 1:
                t = -1
            t += 1

            ans = "%02d:%02d" % (t // 60, t % 60)
            if len(set(ans)) == 5:
                return ans

print(Solution().nextTime("23:59")) # "01:23"