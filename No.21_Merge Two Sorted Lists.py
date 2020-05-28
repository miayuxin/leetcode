# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return "->" + str(self.data)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if l1 is None:
        #     return l2
        # if l2 is None:
        #     return l1
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2

        curr = dummy = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2

        return dummy.next




l3 = ListNode(3)
l2 = ListNode(2, l3)
head = ListNode(1, l2)

s = Solution()
print(s.mergeTwoLists(head, head))

n = Node("1")
print(n)