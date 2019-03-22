def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
        
    
    remembered = [None for i in range(len(nums))]
    def recursion(index):
        if index >= len(nums):
            return 0
        
        print(remembered)
        if remembered[index] is None:

            cur =  nums[index]
            normal = recursion(index + 2)
            skip = recursion(index + 3)

            remembered[index] = max(skip, normal) + cur
            
        return remembered[index]

    print(remembered)        

    recursion(0)
    recursion(1)

    return max(remembered[0], remembered[1])


signature = 'def rob(self, nums):'
input_string = """[226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]
"""  
