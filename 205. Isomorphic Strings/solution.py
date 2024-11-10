class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        iso_map = {}
        
        for idx in range(len(s)):
            if s[idx] not in iso_map.keys() and t[idx] not in iso_map.values():
                iso_map[s[idx]] = t[idx]
            
        print(iso_map)
        
        t_reproduced = ''
        
        for char in s:
            if char in iso_map.keys():
                t_reproduced += iso_map[char]
            
        return True if t_reproduced == t else False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isIsomorphic(s = "egg", t = "add"))
    print(solution.isIsomorphic(s = "foo", t = "bar"))
    print(solution.isIsomorphic(s = "paper", t = "title"))



# Time Complexity: O(n)
# Space Complexity: O(1)