def wordPatternMatch(self, pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """

    def check_repeat(pd):
        ps = set()
        for d in pd:
            if pd[d][1] in ps:
                return False
            else:
                ps.add(pd[d][1])
        
        return True

    str = str + '#'       

    def recursion(str_i, pattern_i, accumulated, pattern_dict):
        
        if str_i == len(str):
            if pattern_i == len(pattern) and accumulated == '#':
                print('FOUND!!!!')
                print(pattern_dict)
                print('------')
                return check_repeat(pattern_dict)
            else:
                return False
        elif str_i == len(str) - 1:
            if pattern_i == len(pattern) and accumulated == '':
                print('FOUND!!!!')
                print(pattern_dict)
                print('------')
                return check_repeat(pattern_dict)
            #else:
            #    return False
        if pattern_i >= len(pattern):
            return False
        
        result = False
        print('Cur letter {}({})({})'.format(str[str_i], str_i, pattern_i))

        # Two options, one is to start a new pattern, one is to continue current pattern

        # Scenario 1. Pattern is known, 
        # we can only check if the pattern matches with existing
        fixed_pattern = accumulated
        accumulated += str[str_i]
        print('Accumulated {}'.format(accumulated))
        pattern_letter = pattern[pattern_i]
        fixed, pattern_word = pattern_dict[pattern_letter]
        
        # Pattern has been determined already
        if fixed and accumulated[-1] != '#':
            print('Known patterns are {}'.format(pattern_dict))
            print('Checking {} against {}'.format(accumulated, pattern_word))
            if pattern_word == accumulated:
                print('Perfect match! {},{}'.format(str_i + 1, pattern_i + 1))
                result |= recursion(str_i + 1, pattern_i + 1, '', pattern_dict)
                
            elif pattern_word.startswith(accumulated):
                result |= recursion(str_i + 1, pattern_i, accumulated, pattern_dict)
            else:
                result |= False
        else:
            # Increase length of current pattern
            print('Increasing pattern {} to {}'.format(pattern_letter, accumulated))
            temp = pattern_dict[pattern_letter]
            pattern_dict[pattern_letter] = (False, accumulated)
            print('Known patterns are {}'.format(pattern_dict))
            result |= recursion(str_i + 1, pattern_i, accumulated, pattern_dict)
            pattern_dict[pattern_letter] = temp

            # Start a new sequence
            if len(fixed_pattern) > 0:
                temp = pattern_dict[pattern_letter]
                pattern_dict[pattern_letter] = (True, fixed_pattern)
                print('Starting a new sequence for pattern {}-{}'.format(pattern_i + 1, pattern[pattern_i + 1]))
                print('Known patterns are {}'.format(pattern_dict))
                print('Going to {},{}'.format(str_i + 1, pattern_i + 1, str[str_i]))
                result |= recursion(str_i + 1, pattern_i + 1, str[str_i], pattern_dict)
                pattern_dict[pattern_letter] = temp

        return result


    pattern_dict = {}
    for p in pattern:
        if p in pattern_dict:
            continue
        else:
            pattern_dict[p] = (False, '')

    return recursion(0, 0, '', pattern_dict)


modifier = ''
signature = 'def wordPatternMatch(self, pattern, str):'
test_cases = [7]
input_string = """"abab"
"aabbaabb"
"abab"
"redblueredqblue"
"abacb"
"redblueredqblue"
"abb"
"xyx"
"a"
"cd"
"ab"
"aa"
"abba"
"baab"
"itwasthebestoftimes"
"ittwaastthhebesttoofttimesss"
"itwasthebestoftimes"
"ittwaastthhebesttoofttimes"
"""            