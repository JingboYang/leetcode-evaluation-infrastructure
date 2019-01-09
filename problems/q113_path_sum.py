def pathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """

    results = []

    def recursion(node, so_far, vals):
        so_far = so_far + node.val
        
        if node.left is None and node.right is None:
            if so_far == sum:
                results.append(vals + [node.val])
            return

        if node.left is not None:
            recursion(node.left, so_far, vals + [node.val])
        if node.right is not None:
            recursion(node.right, so_far, vals + [node.val])

    recursion(root, 0, [])

    return results



# --- Things needed for this infrastructure to run ----
modifier = 'btree'
signature = 'def pathSum(self, root, sum):'
test_cases = None
input_string = """[5,4,8,11,null,13,4,7,2,null,null,5,1]
22
"""  