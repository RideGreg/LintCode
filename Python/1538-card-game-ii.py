# You are playing a card game with your friends, there are n cards in total. Each card costs cost[i]
# and inflicts damage[i] damage to the opponent. You have a total of totalMoney dollars and need to inflict
# at least totalDamage damage to win. And Each card can only be used once. Determine if you can win the game.

# Solution: 0-1 backpack

class Solution:
    """
    @param cost: costs of all cards
    @param damage: damage of all cards
    @param totalMoney: total of money
    @param totalDamage: the damage you need to inflict
    @return: Determine if you can win the game
    """
    def cardGame(self, cost, damage, totalMoney, totalDamage):
        dp = [0] * (totalMoney+1)
        for k in xrange(len(cost)):
            for i in reversed(xrange(cost[k], totalMoney+1)):
                dp[i] = max(dp[i], dp[i-cost[k]]+damage[k])
                if dp[i] >= totalDamage:
                    return True
        return False

print(Solution().cardGame([1,2,3,4,5], [1,2,3,4,5], 10, 10)) # True