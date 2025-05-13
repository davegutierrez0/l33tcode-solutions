class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = [[-1] * (amount+1) for row in range(n)]

        def numberOfWays(i, amount):
            if amount == 0:
                return 1
            elif i == n:
                return 0
            elif memo[i][amount] != -1:
                return memo[i][amount]
            elif coins[i] > amount:
                memo[i][amount] = numberOfWays(i+1, amount)
                return memo[i][amount]
            else:
                memo[i][amount] = numberOfWays(i, amount - coins[i]) + numberOfWays(i + 1, amount)
                return memo[i][amount]
            
        return numberOfWays(0,amount)

# Time Complexity: O(N*A)  where N = len(coins) and A = amount
# Space Complexity: O(N*A)  for the memo table  (+ recursion depth ≤ A in the worst case)
# Mnemonic: #SpendOrSend – spend current coin (stay) or send index forward (skip)