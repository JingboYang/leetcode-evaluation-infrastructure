def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    def mid(pair):
        a,b = pair
        return int((a + b) / 2)
    
    def shrink_bound(bound, direction='high'):
        print('Using {} side of {}'.format(direction, bound))
        if direction == 'high':
            return [mid(bound), bound[1]]
        elif direction == 'low':
            return [bound[0], mid(bound)]

    nums = [nums1, nums2]
    total = len(nums2) + len(nums1)

    more_than = mid((len(nums2), len(nums1)))

    use = 0 if len(nums1) > len(nums2) else 1
    other = 1 - use
    nums_u = nums[use]
    nums_o = nums[other]

    if len(nums_o) == 0:
        m = mid((0, len(nums_u)))
        if total % 2 == 0:
            return (nums_u[m] + nums_u[m - 1]) / 2
        else:
            return nums_u[m]

    bound = [0, len(nums[use])]
    
    done = False
    med_vals = []
    while done is False:

        mid_index = mid(bound)
        mid_value = nums_u[mid_index]

        print('Checking bound={}, corresponding to value {}'.format(bound, nums_u[bound[0]:bound[1]]))
        print('Mid value ={}'.format(mid_value))
        o_left_count = more_than - mid_index - 1
        print('Need {} more'.format(o_left_count))

        if o_left_count < 0:
            bound = shrink_bound(bound, 'low')
        else:
            o_corr_val = nums[1 - use][o_left_count]

            if mid_value >= o_corr_val \
                and (o_left_count + 1 >= len(nums_o) or mid_value <= nums[1 - use][o_left_count + 1]):
                done = True
                med_vals = [mid_value, o_corr_val]
            elif mid_value <= o_corr_val \
                and (o_left_count - 1 < 0 or mid_value >= nums[1 - use][o_left_count - 1]):
                done = True
                med_vals = [mid_value, o_corr_val]
            elif mid_value <= o_corr_val:
                bound = shrink_bound(bound, 'high')
            else:
                bound = shrink_bound(bound, 'low')

    print(med_vals)

    if total % 2 == 1:
        return med_vals[0]
    else:
        return sum(med_vals) / 2



signature = 'def findMedianSortedArrays(self, nums1, nums2):'
input_string = """[3]
[-2,-1]
"""