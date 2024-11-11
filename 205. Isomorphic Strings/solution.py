class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        iso_map = {}
        mapped_characters = set()
        
        for idx in range(len(s)):
            if s[idx] in iso_map:
                if iso_map[s[idx]] != t[idx]:
                    return False
            
            else:
                if t[idx] in mapped_characters:
                    return False
                iso_map[s[idx]] = t[idx]
                mapped_characters.add(t[idx])
                
            
        # print(iso_map)

        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isIsomorphic(s = "egg", t = "add"))
    print(solution.isIsomorphic(s = "foo", t = "bar"))
    print(solution.isIsomorphic(s = "paper", t = "title"))



# Time Complexity: O(n)
# Space Complexity: O(n)