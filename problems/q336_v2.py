def palindromePairs(self, words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """

    def check_palindrome(string, lookup):
        
        if string in lookup:
            return lookup[string]

        #print('Checking ' + string)
        for i in range(len(string) // 2):
            if string[i] != string[len(string) - 1 - i]:
                #print(False)
                lookup[string] = False
                return False
        
        #print(True)
        lookup[string] = True
        return True

    lookup = {}
    results = []
    for i, wi in enumerate(words):
        for j, wj in enumerate(words):
            if i != j:
                
                #print('Comparing {}, {}'.format(wi, wj))

                # Check wj-wi
                if len(wj) <= len(wi):
                    okay = True
                    for l in range(len(wj)):
                        #print('Comparing {}, {} for {}'.format(wi[-1-l],wj[l], wj+wi))
                        if wj[l] != wi[-1-l]:
                            okay = False
                            break
                    #print('Case 1 {}'.format(okay))
                    if len(wj) == 0:
                        okay = okay and check_palindrome(wi, lookup)
                    else:
                        okay = okay and check_palindrome(wi[:-len(wj)], lookup)
                    if okay:
                        results.append((j,i))
                
                # check wi-wj
                if len(wj) < len(wi):
                    okay = True
                    for l in range(len(wj)):
                        if wj[-1-l] != wi[l]:
                            okay = False
                            break
                    #print('Case 2 {}'.format(okay))
                    if len(wj) == 0:
                        okay = okay and check_palindrome(wi, lookup)
                    else:
                        okay = okay and check_palindrome(wi[len(wj):], lookup)
                    if okay:
                        results.append((i,j))



    return results


signature = 'def palindromePairs(self, words):'
input_string = """["a","abc","aba",""]
"""        