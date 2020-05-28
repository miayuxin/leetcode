# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None:
            return head

        curr = head

        while(curr != None and curr.next != None):
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

node_4 = ListNode(3)
node_3 = ListNode(2, node_4)
node_2 = ListNode(2, node_3)
head = ListNode(1, node_2)

s = Solution()
print(s.deleteDuplicates(head))

