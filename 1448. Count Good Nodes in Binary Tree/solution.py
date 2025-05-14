# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        integer_minimum = sys.maxsize * -1
        number_of_good_nodes = 0

        def countGoodNodes(node, max_so_far):
            if node:
                nonlocal number_of_good_nodes
                
                if max_so_far <= node.val:
                    number_of_good_nodes += 1
                
                countGoodNodes(node.left, max(node.val, max_so_far))
                countGoodNodes(node.right, max(node.val, max_so_far))

        countGoodNodes(root, integer_minimum)
        return number_of_good_nodes


# Time Complexity: O(n) — each node is visited once.
# Space Complexity: O(h) — call stack size depends on tree height (h).
# The function recursively traverses the tree, tracking the max value seen so far.
# A node is "good" if its value is >= max on the path from root to that node.