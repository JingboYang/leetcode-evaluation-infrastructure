def maxSubarraySumCircular(self, A):
    """
    :type A: List[int]
    :rtype: int
    """

    cur_max = 0
    cur_min = 0
    max_overall = -float('inf')
    min_overall = float('inf')

    for i in range(len(A)):
        cur_max = max(cur_max + A[i], A[i])
        cur_min = min(cur_min + A[i], A[i])

        max_overall = max(cur_max, max_overall)
        min_overall = min(cur_min, min_overall)

    total = sum(A)

    if max_overall > 0:
        return max(total - min_overall, max_overall)
    else:
        return max_overall


signature = 'def maxSubarraySumCircular(self, A)'
input_string = """[1,-99,4, -2, 3,-1,3,-2]
"""