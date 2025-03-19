class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Memo with infinity values since we are looking for minimum (would start with negative infinity for maximum)
        minimum_coins = [float('inf')] * (amount + 1)
        minimum_coins[0] = 0 # Base case 0 coins to make 0 dollars

        for coin in coins:
            for current_amount in range(coin, amount + 1):
                minimum_coins[current_amount] = min(minimum_coins[current_amount], minimum_coins[current_amount - coin]+1)

        return minimum_coins[amount] if minimum_coins[amount] != float('inf') else -1

# Time Complexity: O(N*A)
# Space Complexity: O(A)