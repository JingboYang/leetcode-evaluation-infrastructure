def maxEnvelopes(self, envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """

    def longest_decreasing_sequence(arr, index):
        if len(arr) == 0:
            return 0
        DP = [1 for i in range(len(arr))]

        for i in range(1, len(arr)):
            a = arr[i]
            best = 1
            for j in range(0, i):
                if arr[i][index] < arr[j][index] and arr[i][1- index] < arr[j][1-index]:
                    best = max(best, DP[j] + 1)
            DP[i] = best

        print(DP)
        return max(DP)

    wsorted = sorted(envelopes, reverse=True)

    print(wsorted)

    longest = longest_decreasing_sequence(wsorted, 1)

    return longest



modifier = ''
signature = 'def maxEnvelopes(self, envelopes):'
test_cases = None
input_string = """[[5,4],[6,4],[6,7],[2,3],[9,2]]
[[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]
[[4,5],[4,6],[6,7],[2,3],[1,1]]
"""  
