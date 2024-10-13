class Solution:
    def reverse(self, x: int) -> int:
        
        result = 0
        
        INT_MIN, INT_MAX = -2**31, 2**31-1
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        x_str = str(x)[::-1]

        result = int(x_str) * sign
        
        return result if INT_MIN <= result <= INT_MAX else 0
        
        

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(x = 123))
    print(solution.reverse(x = -123))
    print(solution.reverse(x = 120))
    print(solution.reverse(x = 1534236469))
    print(solution.reverse(x = -1534236469))
    

    
# Time Complexity O(log(n))
# Space Complexity O(log(n))