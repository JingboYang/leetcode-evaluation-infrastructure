def old(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False

    def recursion(i1, i2):

        #print(i1, i2)

        i3 = i1 + i2

        if i1 == len(s1) and i2 == len(s2):
            return True

        okay = False
        if i1 < len(s1) and s1[i1] == s3[i3]:
            okay = recursion(i1 + 1, i2)
        
        if i2 < len(s2) and s2[i2] == s3[i3]:
            okay = okay or recursion(i1, i2 + 1)
        
        return okay

    return recursion(0, 0)


def isInterleave(self, s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    l1 = len(s1)
    l2 = len(s2)

    DP = [[None for i in range(l2 + 1)] for j in range(l1 + 1)]

    DP[0][0] = True

    for i in range(1, l1 + 1):
        DP[i][0] = DP[i-1][0] and s1[i-1]==s3[i-1]
    
    for i in range(1, l2 + 1):
        DP[0][i] = DP[0][i-1] and s2[i-1]==s3[i-1]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):

            i3 = i + j
            if DP[i-1][j] is True:
                #print('a')
                if s1[i-1] == s3[i3-1]:
                    DP[i][j] = True
            if DP[i][j-1] is True:
                #print('b')
                if s2[j-1] == s3[i3-1]:
                    #print('c')
                    DP[i][j] = True
            
            if DP[i][j] is None:
                DP[i][j] = False

    #for d in DP:
    #    print(d)

    return DP[-1][-1]


signature = 'def isInterleave(self, s1, s2, s3):'
input_string = """"bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
"babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
"babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
"""  
