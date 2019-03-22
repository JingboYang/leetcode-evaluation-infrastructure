def findRotateSteps(self, ring, key):
    """
    :type ring: str
    :type key: str
    :rtype: int
    """
    BIG = 999999999999
    length = len(ring)
    len_key = len(key)
    letter_index = {}
    for i, r in enumerate(ring):
        if r in letter_index:
            letter_index[r].append(i)
        else:
            letter_index[r] = [i]
    

    def best_steps(letter, center):

        indices = [(i - center + length) % length for i in letter_index[letter]]
        results = [min(i, length - i) for i in indices]
        return results

    #print(num_steps('o', 3))

    visited = {}

    def recursion(key_i, center):
        #print(key_i, ring[center], num_steps)
        if key_i == len_key:
            return 0
        
        if (key_i, center) in visited:
            return visited[(key_i, center)]

        desired = key[key_i]
        steps = best_steps(desired, center)
        #print(steps)
        next_centers = letter_index[desired]

        best = BIG
        for i, s in enumerate(steps):
            temp = recursion(key_i + 1, next_centers[i])
            best = min(temp + s + 1, best)

        visited[(key_i, center)] = best

        return best
    
    return recursion(0, 0)




# --- Things needed for this infrastructure to run ----
modifier = ''
signature = 'def findRotateSteps(self, ring, key):'
test_cases = None
input_string = """"godding"
"gd"
"godding"
"godding"
"caotmcaataijjxi"
"oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"
"ababcab"
"acbaacba"
"""  