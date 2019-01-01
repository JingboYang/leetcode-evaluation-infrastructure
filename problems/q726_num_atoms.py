def countOfAtoms(self, formula):
    """
    :type formula: str
    :rtype: str
    """

    def get_status(l):
        if l.isupper():
            return 'U'
        elif l.islower():
            return 'L'
        elif l.isnumeric():
            return 'N'
        elif l == '(':
            return 'B'
        elif l == ')':
            return 'E'
        elif l == '|':
            return 'E'          


    def process_elements(elements):
        keys = sorted(list(elements))
        result = ''
        for k in keys:
            if elements[k] == 1:
                result += k
            elif elements[k] > 1:
                result += k
                result += str(elements[k])
        return result
    
    def handler(string):

        elements = {'':0}
        string = string + '|'

        thing = ''
        prev_thing = ''
        status = None       # upper: 'U', lower: 'L', numeric: 'N'
        i = 0
        while i < len(string):
            cur_status = get_status(string[i])
            print(string[i])
            if cur_status == 'E':
                break

            if cur_status == 'U' or cur_status == 'E' or cur_status == 'B':
                if status == 'L' or status == 'U':
                    if thing in elements:
                        elements[thing] += 1
                    else:
                        elements[thing] = 1
                elif status == 'N':
                    if isinstance(prev_thing, dict):
                        for e in prev_thing:
                            if e in elements:
                                elements[e] += prev_thing[e] * int(thing)
                            else:
                                elements[e] = prev_thing[e] * int(thing)
                    else:
                        if prev_thing in elements:
                            elements[prev_thing] += int(thing)
                        else:
                            elements[prev_thing] = int(thing)
                elif status == 'B':
                    for e in prev_thing:
                        if e in elements:
                            elements[e] += prev_thing[e]
                        else:
                            elements[e] = prev_thing[e]

                thing = string[i]

            elif cur_status == 'L':
                thing += string[i]
                
            elif cur_status == 'N':
                if status == 'N':
                    thing += string[i]
                elif status == 'L' or status == 'U':
                    prev_thing = thing
                    thing = string[i]
                elif status == 'B':
                    thing = string[i]

            if cur_status == 'B':
                bracket = 1
                print('Searching in ' + str(string[i+1:]))
                for j in range(i + 1, len(string)):
                    if string[j] == '(':
                        bracket += 1
                    elif string[j] == ')':
                        bracket -= 1
                        if bracket == 0:
                            break
                print('Handle ' + string[i + 1:j + 1])
                prev_thing = handler(string[i + 1:j + 1])
                print('Done')
                i = j

            status = cur_status
            i += 1

            if status == 'E':
                break

        print('Handling end')
        if status == 'L' or status == 'U':
            if thing in elements:
                elements[thing] += 1
            else:
                elements[thing] = 1
        elif status == 'N':
            print(thing)
            if isinstance(prev_thing, dict):
                for e in prev_thing:
                    if e in elements:
                        elements[e] += prev_thing[e] * int(thing)
                    else:
                        elements[e] = prev_thing[e] * int(thing)
            else:
                if prev_thing in elements:
                    elements[prev_thing] += int(thing)
                else:
                    elements[prev_thing] = int(thing)
        elif status == 'B':
            for e in prev_thing:
                if e in elements:
                    elements[e] += prev_thing[e]
                else:
                    elements[e] = prev_thing[e]

        print(elements)


        return elements
    
    return process_elements(handler(formula))


modifier = ''
signature = 'def countOfAtoms(self, formula):'
test_cases = None
input_string = """"H2O"
"Mg(OH)2"
"K4(ON(SO3)2)2"
"((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"
"(H2O)5(H2O)"
"""  
