def minCostII(self, costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """

    N = len(costs)
    K = len(costs[0])

    DP = [[float('inf') for i in range(K)] for j in range(N)]
    DP[0] = costs[0]


    for n in range(1, N):
        for k in range(K):
            
            best = DP[n][k]
            for prev_k in range(K):
                if prev_k != k:
                    best = min(best, DP[n-1][prev_k] + costs[n][k])
            DP[n][k] = best
            print(best)

    return min(DP[-1])



modifier = ''
signature = 'def minCostII(self, costs):'
test_cases = None
input_string = """[[1,5,3],[2,9,4]]
[[8]]
"""    