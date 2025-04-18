# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        def build_subtree(inorder_range_start, inorder_range_end):
            if inorder_range_start > inorder_range_end:
                return None

            nonlocal preorder_index
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            root.left = build_subtree(inorder_range_start,inorder_dict[root_value] - 1)
            root.right = build_subtree(inorder_dict[root_value] + 1, inorder_range_end)

            return root

        preorder_index = 0 
        inorder_dict = {}

        for index, value in enumerate(inorder):
            inorder_dict[value] = index

        return build_subtree(0, len(preorder) - 1)
                                
# Time Complexity: O(N)
# Space Complexity: O(N)

# 🌳 Analogy:

# You’re planting a tree by reading a shopping list (preorder) and checking the shelf order (inorder).

# 	•	Preorder gives you the root first → like “who goes next in line to be planted.”
# 	•	Inorder helps you figure out left vs right → like “who is to the left or right of the root on the shelf.”

# 🪜 Mental Steps:
# 	1.	Start with the first item in preorder — it’s always your current root.
# 	2.	Use the inorder list to figure out where that root splits the left and right subtree.
# 	3.	Recursively repeat for left and right subtrees.

# 🧠 Mnemonic: “Pre tells me who’s next; In tells me where to split.”