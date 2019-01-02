from lt_helper import *

def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """

    def recursion(cur):

        if cur is None:
            return False

        left = recursion(cur.left)
        right = recursion(cur.right)
        this = (cur == p or cur == q)

        #print('{},{},{}'.format(cur.val, left, right))

        if isinstance(left, TreeNode):
            return left
        elif isinstance(right, TreeNode):
            return right
        elif left + right + this == 2:
            return cur
        elif left + right + this == 1:
            return True
        else:
            return False

    node = recursion(root)
    return node

    
modifier = 'btree, btreenode, btreenode'
signature = 'def lowestCommonAncestor(self, root, p, q):'
test_cases = None
input_string = """[3,5,1,6,2,0,8,null,null,7,4]
5
1
[3,5,1,6,2,0,8,null,null,7,4]
5
4
"""            
        