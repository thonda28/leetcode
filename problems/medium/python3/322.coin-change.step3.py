#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = 10**9
        min_coins = [inf for _ in range(amount + 1)]
        min_coins[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if min_coins[i - coin] != inf:
                    min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
        return min_coins[amount] if min_coins[amount] != inf else -1
# @lc code=end

