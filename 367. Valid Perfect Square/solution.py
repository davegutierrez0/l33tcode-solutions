class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num < 2:
            return True

        left, right = 1, num // 2

        while left <= right: 
            mid = (left + right) // 2

            if mid * mid == num:
                return True
            
            elif mid * mid > num:
                right = mid - 1

            else:
                left = mid + 1

        return False


# Time Complexity: O(log(n)) due to binary search
# Space Complexity: O(1) due to only integers as variables
# Feedback: could square mid in a variable so it's only calculated once per iteration