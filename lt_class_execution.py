from lt_printer import *

def cleanup_lines(input_string):
    old_lines = input_string.split('\n')
    lines = []
    for l in old_lines:
        l = l.strip()
        if len(l) == 0:
            continue
        lines.append(l)
    return lines


def match_method_params(s1, s2):
    s1 = eval(s1)
    s2 = eval(s2)

    return list(zip(s1, s2))


def execute_class(test_class, matched_params):
    print('Initializing ' + (cstring(matched_params[0][0], 'green')).center(16) + \
            ' with params ' + cstring(matched_params[0][1], 'green'))
    obj = test_class(*matched_params[0][1])

    results = []
    for i in range(1, len(matched_params)):
        print('---> Executing ' + (cstring(matched_params[i][0], 'green')).center(16) + \
            ' with params ' + cstring(matched_params[i][1], 'green'))
        func = getattr(test_class, matched_params[i][0])
        result = func(obj, *matched_params[i][1])
        
        print('Result is as follows ')
        print(str(result))
        print('-------- Finished executing ' + (cstring(cstring(matched_params[i][0], 'yellow')) +  ' ------').ljust(40, '-'))
        results.append(result)
    return results

def entry(class_name, module, input_string, t):
    test_class = getattr(module, class_name)

    lines = cleanup_lines(input_string)
    line1 = lines[t * 2]
    line2 = lines[t * 2 + 1]

    matched_params = match_method_params(line1, line2)
    result = execute_class(test_class, matched_params)

    return result, (t+1) * 2 < len(lines)
