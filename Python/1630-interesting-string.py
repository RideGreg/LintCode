# There is now a string s consisting of only numbers and lowercase letters. If the string s is interesting,
# then s must be split into several substrings, each substring satisfies the beginning of the number,
# and the number represents the number of characters after it. For example, s = "4g12y6hunter",
# we can divide it into "4g12y" and "6hunter", so the string is interesting.
# If s is an interesting string, output "yes", otherwise output "no"

class Solution:
    def check(self, s): # dfs + memo
        def dfs(idx, s):
            if idx == len(s):
                return True

            num = 0
            for i in range(idx, len(s)):
                if not s[i].isdigit():
                    break
                num = num * 10 + int(s[i])
                nidx = i+num+1
                if idx > len(s):
                    return False
                if nidx in memo: return memo[nidx]

                if dfs(nidx, s):
                    return True
                else:
                    memo[nidx] = False
            return False

        memo = {}
        return dfs(0, s) and 'yes' or 'no'

    def check_bfs(self, s): # bfs
        import collections
        q = collections.deque([0])
        while q:
            cur = q.popleft()
            if cur == len(s): return "yes"

            num = 0
            for i in range(cur, len(s)):
                if not s[i].isdigit(): break
                num = num * 10 + int(s[i])
                if num > len(s):
                    break
                q.append(i+1+num)
        return "no"

print(Solution().check("124gray6hunter")) # "yes"
print(Solution().check("11gray6hunter")) # "yes"
print(Solution().check("31ba2a")) # "no"