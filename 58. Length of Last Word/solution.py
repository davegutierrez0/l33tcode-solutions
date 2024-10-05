
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Use generators for very large list (filter out empty string)
        # and then a list constructor. Length of [-1] index will be the answer as int.
        sList = list((word for word in s.split(" ") if word != ""))
        #print(sList)
        #print("length: ", len(sList[len(sList)-1]))
        return len(sList[len(sList)-1])

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord(s = "Hello World"))
    print(solution.lengthOfLastWord(s = "   fly me   to   the moon  "))
    print(solution.lengthOfLastWord(s= "luffy is still joyboy"))
    print(solution.lengthOfLastWord(s = "Hello"))
