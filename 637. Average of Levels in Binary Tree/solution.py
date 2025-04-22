# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def depth_first_search(node, level, sums, count):
            if not node:
                return None
            
            if (level < len(sums)):
                sums[level] += node.val
                count[level] += 1

            else:
                sums.append(node.val)
                count.append(1)

            depth_first_search(node.left, level + 1, sums, count)
            depth_first_search(node.right, level + 1, sums, count)


        count = []
        sums = []

        depth_first_search(root, 0, sums, count)

        for i in range(len(sums)):
            sums[i] = sums[i] / count[i]

        return sums


# Time Complexity: O(N)
# Space Complexity: O(H)
# 📏 Count ‘n’ Collect, then Divide to Reflect
# DFS stores sum and count per level, averages at the end