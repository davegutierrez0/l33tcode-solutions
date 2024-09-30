class Solution:
    def maxProfit(self, prices: list[int]) -> int:
         
        n = len(prices)

        if n < 2:
            return 0

        minimumPrice = float('inf')
        maximumProfit = 0    
        for price in prices:
            if price < minimumPrice:
                minimumPrice = price
            else:
                maximumProfit = max(maximumProfit,price-minimumPrice)
        
        return maximumProfit


# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,6,4]))
    print(solution.maxProfit([7,6,4,3,1]))
    print(solution.maxProfit([1,2]))
    print(solution.maxProfit([1]))
    
