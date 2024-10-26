class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Left stays constant unless we run into duplicates 
        # Length measured by right minus left plus one 
        # If s[right] is a character that has been seen before
        # remove s[left] and increment up until we've got a fully unique string
        
        max_length = 0

        left = 0
        s_set = set()
        
        for right in range(len(s)):
            
            while s[right] in s_set:
                s_set.remove(s[left])
                left += 1
            
            s_set.add(s[right])
            
            max_length = max(max_length, right - left + 1)


        return max_length


            
        # First easy/elegant solution but bad for long strings (times out)
        # Loop through length descending
        # See if the whole string is unique characters
        # If not decrease length by 1 and check all possible variations of that
        # So if  len(s) == 6, try the whole string, then s[0:5], s[1:6] etc.
        # Slide window incrementing one to see if there are any matches of 
        # len(substring) == len(set(substring))
        # If there is a match, return len(substr)
        # for substring_length in range(len(s),-1,-1):            
            # for i in range(len(s) - substring_length + 1):
            #     substring = s[i:i + substring_length] 
            #     if len(substring) == len(set(substring)):
            #         return len(substring)


# Test Cases

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring( s = " " ))
    print(solution.lengthOfLongestSubstring( s = "abcabcbb" ))
    print(solution.lengthOfLongestSubstring( s = "bbbbb" ))
    print(solution.lengthOfLongestSubstring( s = "pwwkew" ))

# Time Complexity: O(n)
# Space Complexity: O(n)