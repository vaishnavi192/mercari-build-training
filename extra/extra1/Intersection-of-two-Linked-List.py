#Time Complexity - O(N) Space COmplexity - O(N)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        
        nodes_set = set()
        while headA:
            nodes_set.add(headA)
            headA = headA.next
        
        while headB:
            if headB in nodes_set:
                return headB
            headB = headB.next
        
        return None
#Time Complexity - O(N) Space Complexity - O(1)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def getLength(node):
            length = 0
            while node: 
                length += 1
                node = node.next
            return length
        
        lenA, lenB = getLength(headA), getLength(headB)
        currA, currB = headA, headB
        
        while lenA > lenB:
            currA = currA.next
            lenA -= 1
        while lenB > lenA:
            currB = currB.next
            lenB -= 1
        
        while currA != currB:
            currA = currA.next
            currB = currB.next
        
        return currA 

#Implementation using two pointers 
#O(N) time complexity and O(1) space complexity
#tried to implement Floyd's Linked List Cycle Finding Algorithm
class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        tailA = headA
        while tailA.next:
            tailA = tailA.next
        tailA.next = headB  # Connecting the tail of list A to the head of list B
       
        intersection_node = self.detectCycle(headA)
        
        # We will then reset the linked list structure
        tailA.next = None
        
        return intersection_node
    
    def detectCycle(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        
        return None
        