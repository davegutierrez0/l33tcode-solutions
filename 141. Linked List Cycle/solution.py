# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        current = head


        while current and current not in node_set:
            node_set.add(current)
            current = current.next

            if current and current in node_set:
                return True

        return False

# Time Complexity: O(N)
# Space Complexity: O(N)
# N = number of nodes in the linked list

# Approach: Hash Set
# We traverse the list and store visited nodes in a set.
# If we see the same node again, there is a cycle.