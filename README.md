# LeetCoder Use Guide
Convenient Leetcode Python3 local evaluation infrastructure.

## Tested Environment
This framework has been tested under

* Windows 10 + Anaconda with Python 3.5.5
* MacOS + Python 3.6.5 (no Anaconda)

## To Use
* `cd` to root directory of **Leetcoder**
* Create a new file under *Leetcoder/problems*. Filename must follow patter `q###(question number)_question_name.py`.
* Follow to [Basics](#Basics) to set up the file
* Execute `python3 leetcoder.py`
  * You **DO NOT** need to specify filename. The most recent file will be executed.
  * To run a specific file, use `python3 leetcoder.py <filename>` (do not include directory *problems*)
* You will see something like the follwong
```

    ############################################################
    #                                                          #
    #=====>>>   Leetcode Local Evaluation Framework   <<< =====#
    #                                                          #
    ############################################################

Signature is def convertToBase7(self, num):
Modifers are
Method is    %--convertToBase7--%
Param Names: %--num--%
=====> Test case 0 <=====
Matched parameters: num=100
Executing problems.q504_base7.convertToBase7

===> stdout
===================
Time to execute problems.q504_base7.convertToBase7 is 0.0s

--- Result is as follows ----
'202'
===> Completed test case 0 <===s
```


## Basics
For example, we solve [*Problem 504. Base 7*] (https://leetcode.com/problems/base-7/) using this framework. 

```python
def convertToBase7(self, num):
    """
    :type num: int
    :rtype: str
    """
    vals = []
    minus = False
    if num < 0:
        minus = True

    num = abs(num)
    while num > 0:
        num, r = divmod(num, 7)
        vals.insert(0, str(r))

    if not minus:
        return ''.join(vals)
    else:
        return '-' + ''.join(vals)

# --- Things needed for this infrastructure to run ----
modifier = ''
signature = 'def convertToBase7(self, num):'
test_cases = None
input_string = """100
-200
"""  
```

Notice that the first part is exactly the same as how you would solve the problem on Leetcode. The last few lines describe what input is required. 
* *modifier* Leetcode represents binary tree, linked list and intervals as lists. Check the following files as references
  * *Binary Tree* See [Q236 Common Ancestor](problems/q236_ancestor.py)
  * *Intervals* See [Q57 Insert Interval](problems/q57_insert_interval.py)
  * *Linked List* See [Q92 Partial Linked List Reversal](problems/q92_reverse_linkedlist.py)



