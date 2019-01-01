def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    can1 = None
    can2 = None
    count1 = 0
    count2 = 0

    for n in nums:
        if n == can1:
            count1 += 1
        elif n == can2:
            count2 += 1
        elif count1 == 0:
            count1 = 1
            can1 = n
        elif count2 == 0:
            count2 = 1
            can2 = n
        else:
            count1 -= 1
            count2 -= 1
    
    count1 = 0
    count2 = 0
    for n in nums:
        if n == can1:
            count1 += 1
        elif n == can2:
            count2 += 1


    print(can1, can2, count1, count2)
    results = []
    n_3 = int(len(nums) / 3)
    if count1 > n_3:
        results.append(can1)
    if count2 > n_3:
        results.append(can2)

    return results


##### Input String #####

input_string=\
"""[2,2,1,3]
"""

# another set of inputs
"""[3,2,3]
"""