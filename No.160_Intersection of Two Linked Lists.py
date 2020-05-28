# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:    
        curr_A = headA
        curr_B = headB 
        appeardSet = set()
        
        while(curr_A != None):
            appeardSet.add(curr_A)
            curr_A = curr_A.next    
    
        while(curr_B != None):
            if (curr_B not in appeardSet):
                curr_B = curr_B.next
            else:
                return curr_B

        return None
# Above Solution code is run in O(n) time with O(n) memory.

class Solution_2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:    
        
        if (headA == None and headB == None):
            return None
        
        curr_A = headA
        curr_B = headB
    
        while(curr_A != curr_B):
            if(curr_A == None):
                curr_A = headB
            else:
                curr_A = curr_A.next
            
            if(curr_B == None):
                curr_B = headA
            else:
                curr_B = curr_B.next
            
        return curr_A
# Above Solution_2 code is run in O(n) time with O(1) memory.