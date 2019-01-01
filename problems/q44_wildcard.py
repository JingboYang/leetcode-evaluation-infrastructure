def v1(s, p):
    
    DP = [[False for j in range(len(s) + 1)] for i in range(len(p) + 1)]
    DP[0][0] = True

    for j in range(len(p)):
        if p[j] == '*':
            DP[j + 1][0] = DP[j][0]


    for i in range(len(p)):
        for j in range(len(s)):

            if p[i] == s[j] or p[i] == '?':
                DP[i + 1][j + 1] = DP[i][j]
            elif p[i] == '*':
                DP[i + 1][j + 1] = DP[i + 1][j] or DP[i][j] or DP[i][j + 1]

    return DP[-1][-1]



def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """

    if '*' in p and p.replace('*', '') == '':
        return True

    if len(s) == 0 and len(p) == 0:
        return True
    elif (len(s) == 0 and len(p) != 0) or (len(s) != 0 and len(p) == 0):
        return False

    if p[-1] == s[-1] or p[-1] == '?':
        return self.isMatch(s[:-1], p[:-1])
    elif p[-1] == '*':
        return self.isMatch(s[:-1], p[:]) or self.isMatch(s[:], p[:-1]) or self.isMatch(s[:-1], p[:-1])

    return False


signature = 'def isMatch(self, s, p)'
input_string = """"abckjsadha"
"?*?"
"""  
