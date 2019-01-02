def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """

    if n == 0:
        return 0

    import math
    largest = int(math.sqrt(n))
    avail = [i ** 2 for i in range(1, largest + 1)]
    print(avail)
    avail.reverse()
    
    remaining_save = {}
    for a in avail:
        remaining_save[a] = 1
    def recursion(avail_index, remaining):

        print('Checking remain of {}'.format(remaining))
        if remaining in remaining_save:
            return remaining_save[remaining]

        best = 999999
        for i in range(avail_index, len(avail)):
            remain = remaining - avail[i]
            if remain > 0:
                attempt = recursion(i, remain)
                if attempt != -1:
                    best = min(best, attempt)
            else:
                continue

        if best == 999999:
            if remaining not in remaining_save:
                remaining_save[remaining] = -1
            return -1
        else:
            if remaining not in remaining_save:
                remaining_save[remaining] = best + 1 
            else:
                if remaining_save[remaining] == -1:
                    remaining_save[remaining] = best + 1 
                else:
                    remaining_save[remaining] = min(remaining_save[remaining], best + 1)
            return best + 1
    
    result = recursion(0, n)
    return result


# --- Things needed for this infrastructure to run ----
modifier = ''
signature = 'def numSquares(self, n):'
test_cases = [6]
input_string = """12
13
5
1
588
22
7168
"""