# Question:
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        dummy = ListNode(-1)
        dummy.next = head 
        prev = dummy
        curr = prev.next

        while (curr != None):
            if curr.val == val:
               curr = curr.next   
        
            else: # curr != val
                prev = curr
            
            curr = curr.next

        return dummy.next



node_4 = ListNode(4)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
head = ListNode(1, node_2)
val = 3

s = Solution()
print(s.removeElements(head, val))