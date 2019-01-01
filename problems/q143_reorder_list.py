from lt_helper import *

def reorderList(self, head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """

    # create place holder and count
    cur = head
    nodes = []
    while cur is not None:
        nodes.append(cur)
        cur = cur.next
        
    
    print(head)

    for i in range(len(nodes) // 2):
        right = len(nodes) - 1 - i
        temp = nodes[i].next
        nodes[i].next = nodes[right]
        nodes[right].next = temp
    
    if len(nodes) % 2 == 1:
        nodes[len(nodes) // 2].next = None
    else:
        nodes[len(nodes) // 2].next = None

    print(head)
    return head


modifier = 'linkedlist'
signature = 'def reorderList(self, head):'
test_cases = None
input_string = """[1]
""" 