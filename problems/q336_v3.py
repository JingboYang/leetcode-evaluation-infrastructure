def palindromePairs(self, words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """

    def check_palindrome(string, lookup):

        if string in lookup:
            return lookup[string]

        print('Checking {}'.format(string))
        result = string == string[::-1]
        lookup[string] = result
        print(result)
        return result

    reversed_words = {}
    for i, w in enumerate(words):
        reversed_words[w[::-1]] = i

    print(reversed_words)

    lookup = {}
    results = []
    for i, w in enumerate(words):
        
        for j in range(len(w) + 1):

            # BA case, where A = w and len(B) <= len(A)
            right_hand = w[j:]
            remain = w[0:j]
            print('Right hand {}, remmain {}'.format(right_hand, remain))
            if right_hand in reversed_words and check_palindrome(remain, lookup):
                if reversed_words[right_hand] != i:
                    results.append((reversed_words[right_hand], i))
    
            # AB case, want len(B) < len(A)
            if j == len(w):
                continue
            
            left_hand = w[:j]
            remain = w[j:]

            if left_hand in reversed_words and check_palindrome(remain, lookup):
                if reversed_words[left_hand] != i:
                    results.append((i, reversed_words[left_hand]))


    return results


signature = 'def palindromePairs(self, words):'
input_string = """["a","abc","aba",""]
"""        