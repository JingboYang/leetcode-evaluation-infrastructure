class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    def __str__(self):
        string = '({}->{})'.format(self.start, self.end)
        return string

    def __repr__(self):
        return str(self)


class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
    def __str__(self):
        string = '{}'.format(self.val) + '->'
        if self.next is None:
            string += '%END%'
        else:
            string += str(self.next)
        return string

    def __repr__(self):
        return str(self)


class TreeNode:
    def __init__(self, val=None, level=0):
        self.val = val
        self.level = level
        self.left = None
        self.right = None

    def __str__(self):
        string = ''
        if self.right is not None:
            string += str(self.right)
        string += '    ' * self.level + '{}\n'.format(self.val)
        if self.left is not None:
            string += str(self.left)
        return string

    def __repr__(self):
        return str(self)


def array_to_linked_list(array):
    '''
    Returns head of corresponding linked list
    '''

    if len(array) == 0:
        return None
    
    pseudo = ListNode()
    cur = pseudo
    for a in array:
        temp = ListNode(a)
        cur.next = temp
        cur = temp
    
    return pseudo.next


def linked_list_to_array(head):

    result = []
    cur = head
    while cur is not None:
        result.append(cur.val)
        cur = cur.next
    
    return result


converted_nodes = []
def array_to_btree(array):

    if len(array) == 0:
        return []
    
    node = TreeNode(array[0])
    nodes = [node]
    index = 0

    for i in range(1, len(array), 2):
        cur = nodes[index]

        if array[i] is not None:
            left = TreeNode(array[i])
            left.level = cur.level + 1
            cur.left = left
            nodes.append(left)
        else:
            left = None
            cur.left = left

        if i + 1 < len(array):
            if array[i + 1] is not None:
                right = TreeNode(array[i + 1])
                right.level = cur.level + 1
                cur.right = right
                nodes.append(right)
            else:
                right = None
                cur.right = right

        index += 1

    global converted_nodes
    converted_nodes = nodes
    return nodes[0]


    nodes = [TreeNode(array[i]) if array[i] is not None else None for i in range(len(array))]

    for i in range(len(nodes)):
        left = i * 2 + 1
        right = i * 2 + 2
        if left < len(nodes):
            nodes[i].left = nodes[left]
            if nodes[left] is not None:
                nodes[left].level = nodes[i].level + 1
        if right < len(nodes):
            nodes[i].right = nodes[right]
            if nodes[right] is not None:
                nodes[right].level = nodes[i].level + 1

    return nodes[0]


def array_to_btreenode(val):

    for n in converted_nodes:
        if val == n.val:
            return n
    
    return None


def array_to_intervals(array):

    intervals = []
    for a in array:
        intervals.append(Interval(a[0], a[1]))
    
    return intervals


def array_to_interval(array):
    return Interval(array[0], array[1])


if __name__ == '__main__':
    #array = [1]
    #head = array_to_linked_list(array)    
    #print(head)

    #a2 = linked_list_to_array(head)
    #print(a2)

    array = [3,9,20,None,None,15,7]
    #array = '[-64,12,18,-4,-53,null,76,null,-51,null,null,-93,3,null,-31,47,null,3,53,-81,33,4,null,-51,-44,-60,11,null,null,null,null,78,null,-35,-64,26,-81,-31,27,60,74,null,null,8,-38,47,12,-24,null,-59,-49,-11,-51,67,null,null,null,null,null,null,null,-67,null,-37,-19,10,-55,72,null,null,null,-70,17,-4,null,null,null,null,null,null,null,3,80,44,-88,-91,null,48,-90,-30,null,null,90,-34,37,null,null,73,-38,-31,-85,-31,-96,null,null,-18,67,34,72,null,-17,-77,null,56,-65,-88,-53,null,null,null,-33,86,null,81,-42,null,null,98,-40,70,-26,24,null,null,null,null,92,72,-27,null,null,null,null,null,null,-67,null,null,null,null,null,null,null,-54,-66,-36,null,-72,null,null,43,null,null,null,-92,-1,-98,null,null,null,null,null,null,null,39,-84,null,null,null,null,null,null,null,null,null,null,null,null,null,-93,null,null,null,98]'
    #array = eval(array.replace('null', 'None'))
    root = array_to_btree(array)
    print(root)

    exit()

    array = [[1,2],[3,4]]
    intervals = array_to_intervals(array)
    print(intervals)
