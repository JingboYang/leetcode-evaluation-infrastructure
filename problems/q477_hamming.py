def totalHammingDistance(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            
            n1 = nums[i]
            n2 = nums[j]
            xor = n1 ^ n2
            result += bin(xor)[2:].count('1')


    return result


input_string=\
"""
[4,14,2]
"""
