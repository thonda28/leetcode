#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float("inf") for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                if i == coin:
                    dp[i] = 1
                if dp[i-coin] != float("inf"):
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount]==float("inf") else dp[amount]
# @lc code=end
