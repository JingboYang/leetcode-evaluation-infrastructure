def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def swap(array, i1, i2):
        temp = array[i1]
        array[i1] = array[i2]
        array[i2] = temp


    def partition(array):

        okay = 0
        for i in range(len(array)):
            if array[i] > 0:
                swap(array, i, okay)
                okay += 1
        
        return okay

    okay = partition(nums)
    print(nums)
    print(okay)
    
    for i in range(okay):
        if abs(nums[i]) - 1 < okay:
            nums[abs(nums[i]) - 1] = - abs(nums[abs(nums[i]) - 1])
    
    print(nums)
    for i in range(okay):
        if nums[i] > 0:
            return i + 1



modifier = ''
signature = 'def firstMissingPositive(self, nums):'
input_string = """[-1,2,3,0,-2,-3,-4]
"""