class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word for word in (reversed(s.strip().split())) if word.isalnum())


# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords(s = "the sky is blue"))
    print(solution.reverseWords(s = "  hello world  "))
    print(solution.reverseWords(s = "a good   example"))
    

    
# Time Complexity O(n*m)
# Space Complexity O(n)