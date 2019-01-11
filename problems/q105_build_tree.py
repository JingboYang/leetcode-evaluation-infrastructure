from lt_helper import *

def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """

    io_index_dict = {l:i for i, l in enumerate(inorder)}
    pi_index_dict = {l:i for i, l in enumerate(preorder)}

    if len(preorder) == 0:
        return None
    
    #top_top = TreeNode(val=999999999999, level=10)
    root = TreeNode(val=preorder[0], level=0)
    root.parent = None

    pi = 1
    cur = root
    while pi < len(preorder):
        
        val = preorder[pi]
        print('Upper root is {}, cur is {}'.format(cur.val, val))

        if io_index_dict[val] < io_index_dict[cur.val]:
            cur.left = TreeNode(val=val, level=cur.level+1)
            cur.left.parent = cur
            cur = cur.left

            print(cur.parent)
        else:
            
            print('Finding correct parent')
            print(cur.parent.parent)
            prev = None
            current = cur
            might_be = None
            #while current is not None and io_index_dict[val] > io_index_dict[current.val] and (prev is None or io_index_dict[current.val] > io_index_dict[prev.val] ):
            while current is not None and io_index_dict[val] > io_index_dict[current.val]:
                print('prev is {}, parent is {}'.format(prev.val if prev is not None else None, current.val))
                if current.right is None:
                    might_be = current

                prev = current
                current = current.parent
                
                print('new current is {}'.format(current.val if current is not None else None))
                

            print('On the right of {}'.format(might_be.val))
            cur = might_be            
            cur.right = TreeNode(val=val, level=cur.level + 1)
            cur.right.parent = cur
            cur = cur.right

            print(cur.parent)
        
        pi += 1

    print('------')
    print(root)

    return root



modifier = ''
signature = 'def buildTree(self, preorder, inorder):'
test_cases = None
input_string = """[3,9,20,15,7]
[9,3,15,20,7]
[1,2,3]
[3,2,1]
[3,1,2,4]
[1,2,3,4]
"""                