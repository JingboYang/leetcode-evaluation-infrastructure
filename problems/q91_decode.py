def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """

    if len(s) == 0:
        return 0
    
    combos = set([str(i) for i in range(1, 27)])
    
    s = 'XX' + s
    DP = [0 for i in range(len(s))]
    DP[0] = 0
    DP[1] = 1

    for i in range(2, len(s)):
        cur = s[i]
        prev = s[i - 1]

        ways = 0
        if cur in combos:
            ways += DP[i - 1]
        
        if prev + cur in combos:
            ways += DP[i - 2]
        
        DP[i] = ways
    
    return DP[-1]




modifier = ''
signature = 'def numDecodings(self, s):'
input_string = """"301"
"""