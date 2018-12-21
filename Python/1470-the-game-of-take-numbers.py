# Time: O(n*n)
# Space: O(n)

# Now there is an array arr. There are two players, No. 1 and No. 2 take turns to get numbers from the array.
# They can only fetch from both ends of the array, and only one can be taken at a time. Both of them adopt
# an optimal strategy. After all number is taken, the player taking larger sum of numbers won. Player No. 1
# is taken first. Ask who will win in the end. If the No. 1 player wins or the two draw a tie , return 1
# and if the 2nd player wins, return 2.

# Solution: DP, dp[i][j] is the most value first player can get when i to j coins left,
#     sums[i] is the total when first i coins left. dp[i][j] = (sums[j+1]-sums[i]) - min(dp[i+1][j], dp[i][j-1])

class Solution:
    def theGameOfTakeNumbers(self, arr):
        n = len(arr)
        if n % 2 == 0: return 1

        sums = [0]
        for a in arr:
            sums.append(sums[-1]+a)
        dp = [0] * n
        for i in reversed(range(n)):
            for j in range(i, n):
                if j == i:
                    dp[j] = arr[j]
                else:
                    dp[j] = (sums[j+1]-sums[i]) - min(dp[j], dp[j-1])
        return dp[-1] * 2 >= sums[n]

print(Solution().theGameOfTakeNumbers([3,2,2])) # True
print(Solution().theGameOfTakeNumbers([1,2,4])) # True
print(Solution().theGameOfTakeNumbers([1,20,4])) # False


