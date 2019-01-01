def reversePairs(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    class Node:
        def __init__(self, level=0, rep=-1, left_right=None):
            self.left = None
            self.right = None
            self.left_sum = 0
            self.right_sum = 0
            self.parent = None
            self.rep_value = rep
            self.value = 0
            self.level = level
            self.left_right = left_right

        def __repr__(self):
            
            string = ''
            if self.right:
                string += str(self.right)
            string += '  ' * self.level + '{},{},{},{}\n'.format(self.left_sum, self.right_sum, self.rep_value, self.value)
            if self.left:
                string += str(self.left)
            return string

        def __str__(self):
            return self.__repr__()


    class WeirdTree():

        def __init__(self, nums):
            self.num_lookup = {}

            self.root = Node(level=0)
            queue = [(self.root, 0)]
            index = 0
            while len(queue) > 0:
                cur, level = queue[0]
                queue = queue[1:]

                if 2 ** (level + 1) >= len(nums):
                    if index < len(nums):
                        node = Node(level=level + 1, rep=nums[index], left_right='left')
                        self.num_lookup[nums[index]] = node
                        node.parent = cur
                        cur.left = node
                        index += 1

                        if index < len(nums):
                            node = Node(level=level + 1, rep=nums[index], left_right='right')
                            self.num_lookup[nums[index]] = node
                            node.parent = cur
                            cur.right = node
                            index += 1
                    else:
                        pass
                else:
                    left = Node(level=level + 1, left_right='left')
                    right = Node(level=level + 1, left_right='right')
                    cur.left = left
                    cur.right = right
                    left.parent = cur
                    right.parent = cur
                    queue.append((left, level + 1))
                    queue.append((right, level + 1))

            #print(self.num_lookup)

        def __repr__(self):
            return str(self.root) + '-----------------'


        def update(self, key, value):
            
            cur = self.num_lookup[key]
            diff = value - cur.value
            while cur is not None and cur.parent is not None:
                upper = cur.parent
                cur.value = value
                #print(cur.left_right)
                if cur.left_right == 'left':
                    upper.left_sum += diff
                else:
                    upper.right_sum += diff

                cur = upper

            print(self)


        def query(self, key):

            total = 0
            cur = self.num_lookup[key]
            #if cur.left_right == 'right':
            #total += cur.value

            while cur.parent is not None:
                
                if cur.left_right == 'right' or cur.parent is None:
                    total += cur.parent.left_sum
                cur = cur.parent

            return total
        

        def complement_query(self, key):

            top_total = self.root.left_sum + self.root.right_sum
            less_than = self.query(key)

            return top_total - less_than

    '''
    nums = [1,2,3,4,5,6,7,8,9,10,11]
    #nums = [1,2,3,4]
    tree = WeirdTree(nums)

    print(tree)


    tree.update(1,1)
    tree.update(2,1)
    tree.update(3,1)
    tree.update(4,1)
    tree.update(5,1)
    tree.update(6,1)
    tree.update(7,1)
    tree.update(8,1)
    tree.update(9,1)
    #tree.update(4,99)
    tree.update(10,100)
    tree.update(11,1)

                
    print(tree.query(4))
    print(tree.query(1))
    print(tree.query(2))
    print(tree.query(11))
    print(tree.query(10))
    #print(tree.query(3))
    '''

    combined = [n * 2 for n in nums]
    combined.extend(nums)
    combined = list(set(combined))
    combined.sort()
    print(combined)
    tree = WeirdTree(combined)
    results = 0
    for n in nums[::-1]:
        times2 = n * 2
        print('Querying {}'.format(n))
        #temp = tree.complement_query(n)
        temp = tree.query(n)
        print(temp)

        cur_count = tree.num_lookup[times2].value
        tree.update(times2, cur_count + 1)

        results += temp
        
    
    return results


def v1(nums):
    num_count = {}

    count = 0
    for n in nums:

        #for v in range(2*n + 1, max_in_count + 1):
        #    if v in num_count:
        #        count += num_count[v]

        for v in num_count:
            if v > 2*n:
                count += num_count[v]
        
        if n in num_count:
            num_count[n] += 1
        else:
            num_count[n] = 1

        #print(max_in_count)

    return count



signature = 'def reversePairs(self, nums):'
input_string = """[2,4,3,5,1]
"""