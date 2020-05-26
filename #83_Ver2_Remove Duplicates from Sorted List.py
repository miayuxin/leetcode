# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None:
            return head

        tail = head
        appeardSet = set()
        appeardSet.add(head.val)
        curr = head.next

        while(curr != None):
            if (curr.val not in appeardSet):
                appeardSet.add(curr.val)
                tail.next = curr
                tail = curr
            curr = curr.next
        
        tail.next = None
        return head


node_5 = ListNode(1)
node_4 = ListNode(3, node_5)
node_3 = ListNode(2, node_4)
node_2 = ListNode(2, node_3)
head = ListNode(1, node_2)

s = Solution()
print(s.deleteDuplicates(head))
