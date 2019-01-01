def shortestSubarray(self, A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """

    sum_til = [0]
    for a in A:
        sum_til.append(a + sum_til[-1])

    dq = []

    min_count = 999999
    for i in range(len(A) + 1):

        while len(dq) > 0 and sum_til[i] - sum_til[dq[0]] >= K:
            min_count = min(min_count, i - dq.pop(0))
        
        while len(dq) > 0 and sum_til[i] <= sum_til[dq[-1]]:
            dq.pop()

        
        dq.append(i)

    if min_count == 999999:
        return -1

    return min_count
            




signature = 'def shortestSubarray(self, A, K):'
input_string = """[-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6]
151
"""