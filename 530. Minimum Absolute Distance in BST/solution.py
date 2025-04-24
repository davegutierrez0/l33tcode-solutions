# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        values = set()

        def traverse(node,values_set):
            if not node:
                return None
            
            values_set.add(node.val)

            if node.left:
                traverse(node.left,values_set)

            if node.right:
                traverse(node.right,values_set)

        traverse(root,values)

        values_list = sorted(list(values))

        min_difference = float('inf')
        
        for i in range(1,len(values_list)):
            min_difference = min(min_difference, abs(values_list[i] - values_list[i-1]))

        return min_difference


# Time Complexity: O(N log N)
# - O(N) to traverse all nodes and collect values
# - O(N log N) to sort the values
# - O(N) to compare adjacent pairs

# Space Complexity: O(N)
# - O(N) for the set/list of node values
# - O(H) for the recursion stack (H = tree height)
# 🧺 Use a set to collect values
# 🧮 Sort to line them up
# ↔️ Loop to get diffs
# 🧠 Simple, but misses BST's power



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_difference = float('inf')

        def traverse(node):
            if not node:
                return None


            traverse(node.left)
                        
            if self.prev is not None:
                self.min_difference = min(self.min_difference, node.val - self.prev)
            self.prev = node.val

            traverse(node.right)

        traverse(root)
        return self.min_difference

# Time Complexity: O(N)  # Visit each node exactly once
# Space Complexity: O(H)  # H = tree height (log N for balanced, N for skewed)# 📜 Traverse left ➝ check min ➝ go right
# 🔁 In-order = sorted
# 🔍 Compare only neighbors
# 🧠 prev + current = min diff magic