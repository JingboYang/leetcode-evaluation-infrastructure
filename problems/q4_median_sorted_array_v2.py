def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """


    n = len(nums1)
    m =  len(nums2)

    min_index = 0
    max_index = n

    median = None

    while min_index <= max_index:

        i = (min_index + max_index) // 2
        j = (n + m + 1) // 2 - i
        print(min_index, max_index)

        if i < n and j > 0 and nums1[i] < nums2[j-1]:
            min_index = i + 1
        elif j < m and i > 0 and num1[i-1] > nums2[j]:
            max_index = i - 1
        else:
            if i == 0:
                median = nums2[j-1]
            elif j == 0:
                median = nums1[i-1]
            else:
                median = max(nums1[i-1],nums2[j-1])
            
            break

    if (n+m)%2==1:
        return median
    
    if i == n:
        return (median + nums2[j]) / 2
    
    if j == m:
        return (median + nums1[i]) / 2
    
    return medina + min(nums1[i], nums2[j]) / 2




signature = 'def findMedianSortedArrays(self, nums1, nums2):'
input_string = """[1,3,3]
[2]
"""  
