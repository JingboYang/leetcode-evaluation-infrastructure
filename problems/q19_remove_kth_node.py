from lt_helper import *

def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    
    pseudo = ListNode('PSEUDO')
    pseudo.next = head
    
    n1th = pseudo
    nth = head
    moveon = False
    
    cur = head
    
    counter = 0
    while cur is not None:
        
        
        counter += 1
        if moveon:
            n1th = n1th.next
            nth = nth.next
        
        if counter == n:
            moveon = True
        
        
        
        cur = cur.next
        
    
    print(n1th.val)
    print(nth.val)
    
    old_next = n1th.next
    n1th.next = nth.next
    if old_next == head:
        return nth.next
    else:
        return head



modifier = 'linkedlist,'
signature = 'def removeNthFromEnd(self, head, n)'
input_string = """[1]
1
"""