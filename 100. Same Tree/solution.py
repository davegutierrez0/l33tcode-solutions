# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def checkVals(first: Optional[TreeNode],second: Optional[TreeNode]) -> bool:
        
            if first and second and first.val == second.val:
                return checkVals(first.left,second.left) and checkVals(first.right,second.right) 

            elif not first and not second:
                return True

            else: 
                return False

        return checkVals(p, q)


# Time Complexity: O(N)
# Space Complexity: O(H)
# Mnemonic: Same Structure + Same Values = Same Tree 🧱🪵
# Check both nodes exist and match → check children → else False