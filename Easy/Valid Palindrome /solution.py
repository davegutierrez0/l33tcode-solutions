import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sFiltered = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        # print("Alphanumeric string: ",sFiltered)
        
        if sFiltered == "":
            return True
        left,right = 0, len(sFiltered) - 1
        
        while left < right:
            if sFiltered[left] != sFiltered[right]:
                return False
            
            left +=1
            right -= 1
        
        return True



# Slower easy solution

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         sFiltered = re.sub(r'[^a-zA-Z0-9]','',s).lower()
#         # print("Alphanumeric string: ",sFiltered)
        
#         if sFiltered == "":
#             return True
    
#         # Python's [::-1] shorthand reverses the string or list
        
#         return sFiltered[::-1] == sFiltered
    
    
# # Time Complexity O(n*log(n))
# # Space Complexity O(n)