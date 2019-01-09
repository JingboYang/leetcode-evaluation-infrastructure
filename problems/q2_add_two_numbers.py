from lt_helper import *

def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    
    carry = 0
    done = False
    prev_node = None
    start = None
    while not done:
        
        val1 = 0
        val2 = 0
        if l1 is not None:
            val1 = l1.val
        if l2 is not None:
            val2 = l2.val
        
        result = val1 + val2 + carry
        carry = result // 10
        cur = result % 10
        
        node = ListNode(cur)
        if prev_node is not None:
            prev_node.next = node
        else:
            start = node
        prev_node = node
        
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
        
        if l1 is None and l2 is None and carry == 0:
            done = True
    
    return start



modifier = 'linkedlist, linkedlist'
signature = 'def addTwoNumbers(self, l1, l2):'
input_string = """[2,4,3]
[5,6,4]
"""  
