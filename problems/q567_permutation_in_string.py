def checkInclusion(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    
    if len(s2) < len(s1):
        return False

    smap = {}
    counter = 0
    for s in s1:
        if s in smap:
            smap[s] += 1
        else:
            smap[s] = 1
    
    counted = smap.copy()
    start = 0
    for i in range(len(s2)):
        s = s2[i]

        if s in smap:
            if counted[s] > 0:
                counted[s] -= 1
                counter += 1
                if counter == len(s1):
                    return True
            else:
                prev = start
                while counted[s] == 0:
                    prev_s = s2[prev]
                    counted[prev_s] += 1
                    counter -= 1
                    prev += 1
                    
                counted[s] -= 1
                counter += 1
                if counter == len(s1):
                    return True
                start = prev

        else:
            counted = smap.copy()
            counter = 0
            start = i + 1
    
    return False


# --- Things needed for this infrastructure to run ----
modifier = ''
signature = 'def checkInclusion(self, s1, s2):'
test_cases = None
input_string = """"ab"
"eidbaooo"
"ab"
"eidbqaooo"
"qab"
"eidbqaooo"
"qaab"
"eidbbbbbbqaooo"
"adc"
"dcda"
"""  