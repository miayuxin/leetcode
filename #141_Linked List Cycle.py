# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution uses fast and slow pointers
class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        fast, slow = head

        while(fast and fast.next != None):
            
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        
        return False

# Another solution uses hash table
class Solution_2:
    def hasCycle(self, head: ListNode) -> bool:
        
        visited = []
        curr = head
        
        while (curr and curr.next != None):
            if curr in visited:
                return True
            
            else:
                visited.append(curr)
                curr = curr.next
        
        return False



        

