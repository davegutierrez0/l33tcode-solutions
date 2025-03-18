class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        last_digit = len(digits) - 1

        for i in range(last_digit,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            
            else:
                digits[i] += 1
                return digits
            

        return [1] + digits

# Time Complexity: O(n)
# Space Complexity: O(n)
            