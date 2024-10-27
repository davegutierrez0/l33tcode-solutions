from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        
        # Case where len(prices) == 1
        if len(prices) < 2:
            return 0
        

        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                max_profit += prices[i+1] - prices[i]

        return max_profit



# Test Cases

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit( prices = [7,1,5,3,6,4] ))
    print(solution.maxProfit( prices = [1,2,3,4,5] ))
    print(solution.maxProfit( prices = [7,6,4,3,1] ))

# Time Complexity: O(n)
# Space Complexity: O(1)