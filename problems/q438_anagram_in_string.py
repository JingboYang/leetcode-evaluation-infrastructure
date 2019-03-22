def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """

    import copy

    counts = {}
    for i in p:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    
    indices = []

    left_hand = 0
    verify = copy.copy(counts)
    for i, l in enumerate(s):
        print(i,l)
        print(verify)
        if l in verify:
            verify[l] -= 1
            
            if verify[l] == 0:
                good = True
                for v in verify:
                    if verify[v] > 0:
                        good = False
                        break
                if good:
                    indices.append(i-len(p)+1)
                    verify = copy.copy(counts)
                    left_hand = i

            elif verify[l] < 0:
                print(left_hand)
                done = False
                while not done:
                    verify[l] += 1
                    if s[left_hand] == l:
                        done = True
                    
                    left_hand += 1
                    if left_hand == i:
                        done = True
        else:
            verify = copy.copy(counts)
            left_hand = i + 1

        print(verify)
        print('----')

    return indices


signature = 'def findAnagrams(self, s, p):'
input_string = """"cbaebabacd"
"abc"
"""