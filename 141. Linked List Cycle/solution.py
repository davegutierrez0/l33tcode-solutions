# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        seen = set()

        seen.add(head)

        current = head

        while current.next:
            if current.next not in seen:
                seen.add(current.next)
                current = current.next

            else:
                return True

        return False


# Time Complexity: O(N)
# Space Complexity: O(N)
# N = number of nodes in the linked list
# Approach: HashSet
# Use a set to keep track of visited nodes.
# If we encounter a node that is already in the set, there is a cycle.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while fast != slow:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True


# Time Complexity: O(N)
# Space Complexity: O(1)
# N = number of nodes in the linked list

# Approach: Floyd's Tortoise and Hare (Two Pointers)
# Use a slow pointer and a fast pointer.
# If there's a cycle, the fast pointer will eventually meet the slow pointer.
# If there's no cycle, the fast pointer will reach the end of the list.