# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if(head == None or head.next == None):
            return True
        
        fast, slow = head, head
        
        stack = []
        
        while(fast != None and fast.next != None):
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next

# In case of odd number of nodes, the middle number should be skipped when compare to the values in stack
# e.g, 1->1->2->1->1, move the slow pointer from the moddle number 2 to 1, and then compared to the stack [1, 1] 

        if (fast != None):  
            slow = slow.next
            
        while(slow != None):
            top = stack.pop()
            if top != slow.val:
                return False
            slow = slow.next
        return True

node_5 = ListNode(1)
node_4 = ListNode(1, node_5)
node_3 = ListNode(2, node_4)
node_2 = ListNode(1, node_3)
head = ListNode(1, node_2)

s = Solution()
print(s.isPalindrome(head))

# Time complexity: O(n)
# Space complexity: O(n/2), although we only store the first half of nodes, the constant value of 1/2 should be ignored, so it should be O(n).
        
        
            
        
        
        
            