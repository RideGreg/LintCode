# Give a String, representing the time, such as "12:34"(This is a legal input data).
# and Find the most recent time in the last 24 hours and don't include duplicate numbers.
# If it is the samllest "00:00", the reply is the largest "23:59".If the input is illegal, return -1.

class Solution:
    def lastTime(self, time):
        if not (len(time) == 5 and 0<=int(time[:2])<24 and 0<=int(time[3:])<60 \
                and time[2]==':'):
            return "-1"

        h, m = int(time[:2]), int(time[3:])
        t = 60*h + m
        while True:
            if t == 0: t = 60*24
            t -= 1

            ans = "%02d:%02d" % (t//60, t%60)
            if len(set(ans)) == 5:
                return ans


print(Solution().lastTime('')) # "-1"
print(Solution().lastTime('00:00')) # "23:59"
print(Solution().lastTime('00:02')) # "23:59"
print(Solution().lastTime('12:34')) # "12:30"
