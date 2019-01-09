def minCostII(self, costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """

    N = len(costs)
    K = len(costs[0])

    DP = [[float('inf') for i in range(K)] for j in range(K)]


    


modifier = ''
signature = 'def minCostII(self, costs):'
test_cases = None
input_string = """[[1,5,3],[2,9,4]]
"""    