# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1, list2 = [], []
        while l1 is not None:
            list1.append(str(l1.val))
            l1 = l1.next

        while l2 is not None:
            list2.append(str(l2.val))
            l2 = l2.next


        sum_total = str(int("".join(reversed(list1))) + int("".join(reversed(list2))))

        l3 = ListNode()
        current = l3

        for digit in reversed(list(sum_total)):
            new_node = ListNode(int(digit))
            current.next = new_node
            current = current.next

        return l3.next

# Time Complexity: O(n)
# Space Complexity: O(n)