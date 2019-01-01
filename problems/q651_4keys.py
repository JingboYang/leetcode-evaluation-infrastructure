def maxA(self, N):
    """
    :type N: int
    :rtype: int
    """

    DP = {'A': [i for i in range(N + 1)], 'AC': [0 for i in range(N + 1)], 'V': [(0,0) for i in range(N + 1)]}

    for i in range(2, N + 1):
        AC = max(DP['A'][i - 2], DP['V'][i - 2][0])
        DP['AC'][i] = AC

        prevV = DP['V'][i-1][0] + DP['V'][i-1][1]
        copy = DP['AC'][i-1] * 2
        copy2 = DP['AC'][i-2] * 3

        best = max(prevV, copy, copy2)
        if best == copy:
            DP['V'][i] = (copy, DP['AC'][i-1])
        elif best == copy2:
            DP['V'][i] = (copy2, DP['AC'][i-2])
        else:
            DP['V'][i] = (prevV, DP['V'][i-1][1])
        
    
    for i in ['A', 'AC', 'V']:
        string = ''
        for j in DP[i]:
            string += str(j).ljust(8)
        print(string)

    return max(DP['A'][-1], DP['V'][-1][0])

modifier = ''
signature = 'def maxA(self, N):'
test_cases = None
input_string = """
1
4
7
9
12
50
"""  


'''
AAAA acVVV
'''
