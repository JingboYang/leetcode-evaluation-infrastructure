from lt_helper import *

def traversal(node, pos):
    if node is None:
        return
    
    global left_most
    global right_most
    global pos_dict
    left_most = min(left_most, pos)
    right_most = max(right_most, pos)

    if pos in pos_dict:
        pos_dict[pos].append(node)
    else:
        pos_dict[pos] = [node]
    
    #print(pos_dict)
    #print(left_most)
    #print(right_most)

    traversal(node.right, pos + 1)
    traversal(node.left, pos - 1)
    


def verticalOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    pos_dict = {}
    left_most = 9999999
    right_most = -9999999

    queue = [(root, 0)]
    while len(queue) > 0:
        cur, pos = queue[0]
        queue.pop(0)

        if cur is None:
            continue

        left_most = min(left_most, pos)
        right_most = max(right_most, pos)

        if pos in pos_dict:
            pos_dict[pos].append(cur)
        else:
            pos_dict[pos] = [cur]

        queue.append((cur.left, pos - 1))
        queue.append((cur.right, pos + 1))
        

    print(root)

    #print(pos_dict)
    #print(left_most)
    #print(right_most)
    #traversal(root, 0)
    output = []
    for i in range(left_most, right_most + 1):
        output.append([])
        for v in pos_dict[i]:
            output[-1].append(v.val)


    return output



modifier = 'btree'
signature = 'def verticalOrder(self, root):'
test_cases = None
input_string = """[3,9,20,null,null,15,7]
[3,9,8,4,0,1,7,null,null,null,2,5]
[-64,12,18,-4,-53,null,76,null,-51,null,null,-93,3,null,-31,47,null,3,53,-81,33,4,null,-51,-44,-60,11,null,null,null,null,78,null,-35,-64,26,-81,-31,27,60,74,null,null,8,-38,47,12,-24,null,-59,-49,-11,-51,67,null,null,null,null,null,null,null,-67,null,-37,-19,10,-55,72,null,null,null,-70,17,-4,null,null,null,null,null,null,null,3,80,44,-88,-91,null,48,-90,-30,null,null,90,-34,37,null,null,73,-38,-31,-85,-31,-96,null,null,-18,67,34,72,null,-17,-77,null,56,-65,-88,-53,null,null,null,-33,86,null,81,-42,null,null,98,-40,70,-26,24,null,null,null,null,92,72,-27,null,null,null,null,null,null,-67,null,null,null,null,null,null,null,-54,-66,-36,null,-72,null,null,43,null,null,null,-92,-1,-98,null,null,null,null,null,null,null,39,-84,null,null,null,null,null,null,null,null,null,null,null,null,null,-93,null,null,null,98]
"""        