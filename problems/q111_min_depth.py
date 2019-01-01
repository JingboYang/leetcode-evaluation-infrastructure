def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    print(root)
    print('---')
    #return
    most_shallow = [99999999]

    def dfs(node, level):

        if node.left is None and node.right is None:
            most_shallow[0] = min(most_shallow[0], level)
            return
        
        if node.left is not None:
            dfs(node.left, level + 1)
        
        if node.right is not None:
            dfs(node.right, level + 1)



    dfs(root, 0)

    return most_shallow[0]


modifier = 'btree'
signature = 'def minDepth(self, root):'
test_cases = None
input_string = """[3,9,20,null,null,15,7]
[1,2]
[1,2,3,4,null,null,5]
"""            