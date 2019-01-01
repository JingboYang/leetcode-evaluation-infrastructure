class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    global new_head
    new_head = None
    def swap_connect(prev_tail, n1, n2):
        print('Swapping {} {}'.format(n1.val, n2.val))
        if prev_tail is None:
            global new_head
            new_head = n2
            print(new_head)
        else:
            prev_tail.next = n2
        next_node = n2.next
        n2.next = n1
        n1.next = None
        
        return n1, next_node
        
    prev_tail = None
    is_head = True
    
    n1 = None
    n2 = None
    
    cur_node = head
    while cur_node is not None:
        print('processing ' + str(cur_node.val))
        if is_head == True:
            n1 = cur_node
            is_head = False
            cur_node = n1.next
        else:
            n2 = cur_node
            is_head = True

            if prev_tail is None:
                new_head = n2
            else:
                prev_tail.next = n2

            next_node = n2.next
            n2.next = n1

            prev_tail = n1
            prev_tail.next = None
            cur_node = next_node
            #prev_tail, cur_node = swap_connect(prev_tail, n1, n2)
            print('Tail is {}'.format(prev_tail.val))
            #print('Next is {}'.format(cur_node.val))
    
    results = []
    cur_node = new_head
    print(new_head)
    while cur_node is not None:
        print('Appending ' + str(cur_node.val))
        results.append(cur_node.val)
        cur_node = cur_node.next
    
    return results


n1 = ListNode(5)
n2 = ListNode(3)
n3 = ListNode(1)
n4 = ListNode(2)

n1.next = n2
n2.next = n3
n3.next = n4

r = swapPairs(n1)
print(r)