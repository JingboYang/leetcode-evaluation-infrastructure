from lt_helper import *

def reverseBetween(self, head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
        
    pseudo = ListNode(None)
    pseudo.next = head

    prev = pseudo
    cur = head
    counter = 0

    while cur is not None:
        counter += 1
        if counter == m:
            break
        prev = cur
        cur = cur.next

    print(prev)
    print(cur)

    prev_prev = None
    m_head = cur
    while counter <= n:
        nxt = cur.next
        cur.next = prev_prev
        prev_prev = cur
        cur = nxt
        counter += 1
    
    print(prev_prev)
    print(cur)
    print(m_head)
    prev.next = prev_prev
    m_head.next = cur
    #prev.next = cur
    #m_head.next = cur.next

    return pseudo.next

modifier = 'linkedlist'
signature = 'def reverseBetween(self, head, m, n):'
test_cases = None
input_string = """[1]
1
1
"""    
        