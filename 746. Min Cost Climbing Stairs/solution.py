class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Define base/edge case
        if len(cost) == 2:
            return min(cost)

        # Must surprass the end of the index to 
        # 'reach the top'

        previous, current = 0,0

        for i in range(2,len(cost)+1):
            next_step = min(previous + cost[i-2], current + cost[i-1])
            previous, current = current, next_step


        return next_step


        # Time Complexity: O(n)
        # Space Complexity: O(1)