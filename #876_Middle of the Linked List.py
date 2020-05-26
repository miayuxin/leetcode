# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        if (head == None):
            return head
        
        slow, fast = head, head
        
        while(fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
        
        return slow


node_6 = ListNode(6)
node_5 = ListNode(5, node_6)
node_4 = ListNode(4, node_5)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
head = ListNode(1, node_2)

s = Solution()
print(s.middleNode(head))
        
        
        