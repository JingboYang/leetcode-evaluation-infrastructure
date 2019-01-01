def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    class Sequence:
        def __init__(self, start, end):
            self.start = start
            self.end = end
        def length(self):
            return self.end - self.start + 1
        def __repr__(self):
            return '{}->{}'.format(self.start, self.end)
        def __str__(self):
            return self.__repr__()

    def insert(seq):
        starts[seq.start] = seq
        ends[seq.end] = seq
    
    def remove(seq):
        print('Removing {}'.format(seq))
        del starts[seq.start]
        del ends[seq.end]

    starts = {}
    ends = {}
    checked = set()

    for n in nums:
        print('Handling {}'.format(n))
        if n in checked:
            continue
        
        checked.add(n)
        # check if can append to start
        has_start = False
        if n + 1 in starts:
            temp = starts[n + 1]
            remove(starts[n + 1])
            temp.start = n
            insert(temp)
            has_start = True
        
        # check if can append to end
        has_end = False
        if n - 1 in ends:
            temp = ends[n - 1]
            remove(ends[n - 1])
            temp.end = n
            insert(temp)
            has_end = True
        
        if has_start and has_end:
            high = starts[n]
            low = ends[n]

            new = Sequence(low.start, high.end)
            remove(high)
            remove(low)
            insert(new)
        
        if not has_start and not has_end:
            new = Sequence(n, n)
            insert(new)            
            
        print(starts)
        print(ends)
        print('---')

    longest = max(starts, key=lambda x:starts[x].length())
    return starts[longest].length()


modifier = ''
signature = 'def longestConsecutive(self, nums):'
test_cases = None
input_string = """[100,4,200,1,3,2,4,5,6,7,8,9,101,102,103,104,105,21,20,13,12,11,0,-4,-3,-2,-1]
"""    
        