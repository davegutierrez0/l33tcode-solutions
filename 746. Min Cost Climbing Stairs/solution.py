class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Define base/edge case
        if len(cost) == 2:
            return min(cost)

        minimumCost = [0] * (len(cost) + 1)
        print(minimumCost)

        # Must surprass the end of the index to 
        # 'reach the top'
        for i in range(2,len(minimumCost)):
            minimumCost[i] = min(minimumCost[i-1]+cost[i-1],minimumCost[i-2]+cost[i-2])


        return minimumCost[-1]


        # Time Complexity: O(n)
        # Space Complexity: O(n)