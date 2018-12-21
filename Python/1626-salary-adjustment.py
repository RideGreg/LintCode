# Given a list of salaries, find out a minimal cap to let the sum of adjusted salary be equal to or larger then
# the given target. cap is defined as: if the current salary is smaller than cap, then cap is used
# as the new salary, otherwise Keep the original salary

class Solution:
    def getCap(self, a, target):
        n = len(a)
        l, r = 0, -(-target//n)
        while l < r:
            m = l + (r-l)/2
            if sum(max(m, v) for v in a) >= target:
                r = m
            else:
                l = m + 1
        return l

print(Solution().getCap([1,2,3,4], 13)) # 3
print(Solution().getCap([1,2,3,4], 16)) # 4