def canPartitionKSubsets(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """

    total = sum(nums)
    if total % k != 0:
        return False
    
    target = total // k
    global found
    found = False
    nums.sort(reverse=True)
    print(nums)

    for n in nums:
        if n > target:
            return False

    def partition(avail, partial, visited, index):
        global found
        if found:
            return
        
        if partial == target:
            partial = 0
            #print(avail)
            #print('FOUND!')
            #print(visited)
            index = 0
            if sum(visited) == len(nums):
                found = True
                return

        #print('Trying with partial {}, avail {}'.format(partial, avail))
        it = range(len(avail))
        
        for i in it:
            if visited[i] == False:
                a = avail[i]
                visited[i] = True
                if partial + a <= target:
                    #avail.pop(i)
                    #print('Using {}'.format(a))
                    partition(avail, partial + a, visited, i)
                    #avail.insert(i, a)
                visited[i] = False
                

    partition(nums, 0, [False for i in range(len(nums))], 0)

    return found


signature = 'def canPartitionKSubsets(self, nums, k):'
input_string = """[85,35,40,64,86,45,63,16,5364,110,5653,97,95]
7
"""  
