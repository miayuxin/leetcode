# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head == None:
            return head

        prev = None
        curr = head
        
        while (curr != None):
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        return prev

node_4 = ListNode(4)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
head = ListNode(1, node_2)

s = Solution()
print(s.reverseList(head))
