def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    if len(nums) == 0:
        return -1

    def find_middle(left, right):
        if left == right or left == right + 1:
            return right
        
        middle = (left + right) // 2

        if nums[left] < nums[middle]:
            return find_middle(middle, right)
        else:
            return find_middle(left, middle)
        
    middle_index = find_middle(0, len(nums))
    max_val = nums[middle_index]
    print(middle_index)

    def binary(left, right):
        if left == right or left + 1 == right:
            return left
        
        middle = (left + right) // 2
        mid_val = nums[middle]

        if target < mid_val:
            return binary(left, middle)
        else:
            return binary(middle, right)


    if target >= nums[0]:
        print('Search in bottom')
        index = binary(0, middle_index + 1)
    else:
        print('Search in top')
        index = binary(middle_index + 1, len(nums))
    
    print(index)
    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1



signature = 'def search(self, nums, target):'
input_string = """[2,3,4,5,0,1]
0
[1]
0
"""  
