def findMaximizedCapital(self, k, W, Profits, Capital):
    """
    :type k: int
    :type W: int
    :type Profits: List[int]
    :type Capital: List[int]
    :rtype: int
    """

    indicies = [i for i in range(len(Profits))]
    gi = sorted(indicies, key=lambda x: (-Profits[x], Capital[x]))
    
    for g in gi:
        print(g, Profits[g], Capital[g])

    p = W
    for i in range(k):
        for j in range(len(gi)):
            g = gi[j]
            if Capital[g] <= W:
                p += Profits[g]
                W = W + Profits[g]
                gi.pop(j)
                print('Chose {}. Remaining W: {}'.format(g, W))
                break
    
    return p


modifier = ''
signature = 'def findMaximizedCapital(self, k, W, Profits, Capital):'
test_cases = None
input_string = """
2
0
[1,2,3]
[0,1,1]
11
11
[1,2,3]
[11,12,13]
"""  
