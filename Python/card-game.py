'''
1448. Card Game

A card game that gives you two non-negative integers: totalProfit, totalCost, and n cards'information. The ith card
has a profit value a[i] and a cost value b[i]. It is possible to select any number of cards from these cards, form a scheme.
Now we want to know how many schemes are satisfied that all selected cards' profit values are greater than totalProfit
and the costs are less than totalCost.
Since this number may be large, you only need to return the solution number mod 1e9 + 7.

Example
Given n = 2, totalProfit = 3, totalCost = 5, a = [2,3], b = [2,2], return 1.

Explanation:
At this time, there is only one legal scheme, which is to select both cards.
At this time, a[1]+a[2] = 5 > totalProfit and b[1] + b[2] < totalCost.

Example
Given n = 3, totalProfit = 5, totalCost = 10, a = [6,7,8], b = [2,3,5], return 6.

Explanation:
Suppose a legal scheme (i,j) indicates that the i-th card and the j-th card are selected.
The legal solutions at this time are:
(1),(2),(3),(1,2),(1,3),(2,3)

Solution:
Let dp[i][j] is the number of schemes for profit = i and cost = j,
traverse each card: the transition function is dp[i+a[x]][j+b[x]] += dp[i][j]

Time complexity: O(n * totalProfit * totalCost)
'''

class Solution:
    """
    @param n: The number of cards
    @param totalProfit: The totalProfit
    @param totalCost: The totalCost
    @param a: The profit of cards
    @param b: The cost of cards
    @return: Return the number of legal plan
    """
    def numOfPlan(self, n, totalProfit, totalCost, a, b): # USE THIS: less space
        if totalCost == 0:
            return 1 if totalProfit == 0 else 0

        mod = 10 ** 9 + 7
        dp = [[0] * (totalCost) for _ in xrange(totalProfit + 2)]
        dp[0][0] = 1
        for k in xrange(len(a)):
            for i in reversed(xrange(totalProfit + 2)):
                for j in reversed(xrange(totalCost)):
                    if dp[i][j] > 0 and j + b[k] < totalCost:
                        row = min(totalProfit + 1, i + a[k]) # accumulate all profits larger than profit-threshold to this single row
                        dp[row][j + b[k]] += dp[i][j]
                        dp[row][j + b[k]] %= mod
        return sum(dp[totalProfit + 1]) % mod

    def numOfPlan_allProfit(self, n, totalProfit, totalCost, a, b):
        if totalCost == 0:
            return 1 if totalProfit == 0 else 0

        mod = 10**9+7
        allProfit = sum(a)
        dp = [ [0]*(totalCost) for _ in xrange(allProfit+1) ] # space is not constant-constrained
        dp[0][0] = 1
        for k in xrange(len(a)):
            for i in reversed(xrange(a[k], allProfit+1)):
                for j in reversed(xrange(b[k], totalCost)):
                    if dp[i-a[k]][j-b[k]] > 0:
                        dp[i][j] += dp[i-a[k]][j-b[k]]
                        dp[i][j] %= mod

        ans = 0
        for i in xrange(totalProfit+1, allProfit+1):
            ans += sum(dp[i])
            ans %= mod
        return ans

print(Solution().numOfPlan(2, 3, 5, [2,3], [2,2])) # 1
print(Solution().numOfPlan(3, 5, 10, [6,7,8], [2,3,5])) # 6
print(Solution().numOfPlan(11, 2, 24,
[30,55,21,76,97,16,55,96,46,63,0],
[1,0,1,0,2,1,1,2,0,0,1])) # 2046