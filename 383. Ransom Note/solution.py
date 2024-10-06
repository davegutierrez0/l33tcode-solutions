class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        

        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char,"",1)
            else:
                 return False
             

        return True


# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.canConstruct(ransomNote = "a", magazine = "b"))
    print(solution.canConstruct(ransomNote = "aa", magazine = "ab"))
    print(solution.canConstruct(ransomNote = "aa", magazine = "aab"))
