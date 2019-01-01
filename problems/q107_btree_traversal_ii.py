from lt_helper import *

def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    queue = [(root,0)]
    pstack = []
    while len(queue):
        cur,lvl = queue[0]
        queue.pop(0)

        if cur is not None:
            if len(pstack) < lvl + 1:
                pstack.append([])
            pstack[lvl].append(cur.val)

            queue.append((cur.left, lvl+1))
            queue.append((cur.right, lvl+1))
    
    return list(reversed(pstack))


modifier = 'btree'
signature = 'def levelOrderBottom(self, root)'
input_string = """[3,9,20,null,null,15,7]
"""
        