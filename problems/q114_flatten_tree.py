def flatten(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    
    root = array_to_binary(root)
    print_tree(root)
    
    def traverse(node):
        
        if node.left is None and node.right is None:
            print('Node {} is leaf'.format(node))
            return node
        
        if node.left is None:
            right_end = traverse(node.right)
            return right_end
        
        if node.right is None:
            print('Switching node {}'.format(node.val))

            node.right = node.left
            left_end = traverse(node.left)
            node.left = None

            #print(node)
            return left_end
        
        left_end = traverse(node.left)
        right_end = traverse(node.right)
        
        left_end.right = node.right
        node.right = node.left
        node.left = None

        #print_tree(root)
        
        return right_end
    
    traverse(root)

    print_tree(root)


def array_to_binary(arr):
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
        def __repr__(self):
            return str(self.left) + '->' + str(self.val) + '<-' + str(self.right)

    node = [TreeNode(arr[i]) if arr[i] is not None else None for i in range(len(arr))]

    for i in range(len(arr)):
        if node[i] is not None:
            l = i * 2 + 1
            r = i * 2 + 2
            if l < len(arr):
                node[i].left = node[l]
            
            if r < len(arr):
                node[i].right = node[r]

    return node[0]


def print_tree(node):
    print('----------------------')
    print_tree_helper(node)
    print('----------------------')
    
def print_tree_helper(node, depth=0):

    if node is None:
        return

    print_tree_helper(node.left, depth + 1)
    print('  ' * depth + str(node.val))
    print_tree_helper(node.right, depth + 1)


signature = 'def flatten(self, root):'
input_string = """[1,2,None,3,4,None, None, 5]
"""        