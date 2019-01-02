def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    def recursion(left, right):
        print(left, right)
        if left == right or left == right - 1:
            if left >= len(nums) or left < 0 or nums[left] != target:
                return -1
        
        middle = (left + right) // 2
        num = nums[middle]

        if num == target:
            return middle

        if target < num:
            return recursion(left, middle)
        else:
            return recursion(middle, right)
    
    return recursion(0, len(nums))


# --- Things needed for this infrastructure to run ----
modifier = ''
signature = 'def search(self, nums, target):'
test_cases = None
input_string = """[-1,0,3,5,9,12]
9
[-1,0,3,5,9,12,25]
25
[]
9
[1,2,3,4]
9
[5]
5
"""  