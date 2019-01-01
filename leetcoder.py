import sys, os, re, time
import platform
from importlib import import_module
import traceback
import pprint as pp
import argparse
import collections

from lt_printer import *
from lt_helper import *
import lt_helper
from lt_class_execution import *

RE_FNAME = re.compile(r'q[0-9]+\w+\.py')
RE_PARAMS = re.compile(r'def\s+(?P<func_name>\w+)\((?P<params>.*)\)')
RE_CLASS = re.compile(r'class\s+(?P<class_name>\w+)\:')

def analyze_function_signature(func):
    searched = RE_PARAMS.search(func)

    if searched is not None:
        searched = searched.groupdict()
        params = searched['params']
        params = params.replace(' ', '')
        params = params.split(',')

        if 'self' in params:
            return params[1:], searched['func_name'], True
        return params[:], searched['func_name'], False
    
    else:
        searched = RE_CLASS.search(func)
        searched = searched.groupdict()
        classes = searched['class_name']

        return None, classes, False



def input_to_args(params, input_string, input_range, modifiers):
    #print(input_string)
    old_lines = input_string.split('\n')
    modifiers = modifiers.split(',')
    modifiers.extend([''] * (len(params) - len(modifiers)))

    lines = []
    for l in old_lines:
        l = l.strip()
        if len(l) == 0:
            continue
        lines.append(l)
    
    if input_range[1] > len(lines):
        return None, None
    lines = lines[input_range[0]:input_range[1]]

    args = []
    py_args = []
    for i, p in enumerate(params):
        try:
            l = lines[i]
        except:
            print('Unable to acquire next input value. Incorret input?')

        md = modifiers[i].strip() 
        
        if md == 'linkedlist':
            l = l.replace('null', 'None')
            val = array_to_linked_list(eval(l))
        elif md == 'btree':
            l = l.replace('null', 'None')
            val = array_to_btree(eval(l))
        elif md == 'btreenode':
            val = array_to_btreenode(eval(l))
        elif md == 'intervals':
            l = l.replace('null', 'None')
            val = array_to_intervals(eval(l))
        elif md == 'interval':
            l = l.replace('null', 'None')
            val = array_to_interval(eval(l))            
        else:
            val = eval(l)

        string = p + '=' + l
        args.append(string)
        py_args.append(val)

    args = ', '.join(args)
    lt_helper.converted_nodes = []
    return args, py_args


def modification_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    stat = os.stat(path_to_file)
    return stat.st_mtime

    '''
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
    '''


def execute_main(p, m, mod):

    try:
        main = getattr(mod, 'main')    
        print('Executing {}.main'.format(p))
        print('\n===> stdout')
        start = time.clock()
        main()
        end = time.clock()
        interval = round(end - start, 3)
        print('===================')
        print('Time to execute {}.main is {}s'.format(p, interval))

        return True
    except:
        print(' --- Encountered exception as follows --- ')
        print(traceback.format_exc())
        print(sys.exc_info()[0])

    return False


def execute_func(p, m, mod, first_line):
    try:
        try:
            signature = getattr(mod, 'signature')
        except:
            print('Unable to get tag "signature". Will use first line in file instead')
            signature = first_line
        print('Signature is ' + signature)

        try:
            modifier = getattr(mod, 'modifier')
        except:
            cprint('Unable to get tag "modifier". Will not use any modifer', 'red')
            modifier = ''
        print('Modifers are ' + modifier)

        params, func_name, has_self = analyze_function_signature(signature)

        if params is not None:
            print('Method is    %--' + cstring(func_name, 'magenta') + '--%')
            print('Param Names: %--' + cstring(', '.join(params), 'magenta') + '--%')
        else:
            print(cstring('Detected class! ', 'red') + 'Class is    %--' + cstring(func_name, 'magenta') + '--%')

        try:
            test_cases = getattr(mod, 'test_cases')
            if not isinstance(test_cases, collections.Iterable):
                test_cases = [i for i in range(999)]
        except:
            print('Unable to get tag "test_cases". Will run all test cases')
            test_cases = [i for i in range(999)]

        input_string = getattr(mod, 'input_string')
        for t in test_cases:
            
            if params is not None:
                input_start = t * len(params)
                input_end = (t + 1) * len(params)
                matched_params, py_args = input_to_args(params, input_string, (input_start, input_end), modifier)
                if matched_params is None and py_args is None:
                    break
                
                print('=====> Test case {} <====='.format(t))
                print('Matched parameters: ' + matched_params)

                if has_self:
                    py_args.insert(0, None)
                func = getattr(mod, func_name)
            

            start = time.time()

            print('Executing {}.{}'.format(p, func_name))
            print('\n===> stdout')
            start = time.clock()
            if params is not None:
                result = func(*py_args)
                do_continue = True
            else:
                print(cstring('Class', 'red') + ' execution ...')
                result, do_continue = entry(func_name, mod, input_string, t)
            end = time.clock()
            interval = round(end - start, 3)
            print('===================')
            print('Time to execute {}.{} is '.format(p, func_name) + cstring('{}s'.format(interval), 'green'))

            print('\n--- Result is as follows ----')
            pp.pprint(result)
            print('===> Completed test case {} <===\n\n'.format(t))

            if not do_continue:
                break
        
        return True
    except:
        print(' --- Encountered exception as follows --- ')
        print(traceback.format_exc())
        print(sys.exc_info()[0])


    return False


def leetcoder_main(fname, method):

    p, m = fname.rsplit('.', 1)
    mod = import_module(p)

    with open(fname, 'r') as f:
        line = f.readline()
        line = line.strip()


    if method is None:
        status = execute_func(p, m, mod, first_line=line)
    elif method == 'main':
        status = execute_main(p, m, mod, first_line=line)
    
    if status:
        print('======= DONE =======')
    else:
        print('===== EXCEPTION =====')


if __name__ == '__main__':
    
    banner = """
    ############################################################
    #                                                          #
    #=====>>>   Leetcode Local Evaluation Framework   <<< =====#
    #                                                          #
    ############################################################
    """
    print(banner)

    parser = argparse.ArgumentParser(description='Leetcode Local Evaluation Framework')
    parser.add_argument('fname', type=str, nargs='?', help='Filename')
    parser.add_argument('--m', action='store_const', const='main', default=None, help='Method to execute (main or leave blank)')

    args = parser.parse_args()
   
    fnames = None
    if args.fname is None:

        fnames = os.listdir('.')

        candidates = []
        for f in fnames:
            if RE_FNAME.search(f) is not None:
                #print(f)
                #print(os.path.getctime(f))
                candidates.append((modification_date(f), f))
        
        t, fname = max(candidates)

    else:

        if '.py' not in sys.argv[1]:
            fname = sys.argv[1] + '.py'
        else:
            fname = sys.argv[1]
    
    leetcoder_main(fname, args.m)
