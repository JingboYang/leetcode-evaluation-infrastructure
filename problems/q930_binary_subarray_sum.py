def temp():
    
    while i < len(A):

        cur_sum += A[i]
        right = i

        if cur_sum == S and S > 0:
            print((left, right))
            left_zeros = 1
            right_zeros = 1
            for j in range(left, right):
                if A[j] == 0:
                    left_zeros += 1
                else:
                    left = j + 1
                    cur_sum -= 1
                    break

            for j in range(right + 1, len(A)):
                if A[j] == 0:
                    right_zeros += 1
                else:
                    i = j - 1
                    break
            #print(i)
            counter += left_zeros * right_zeros
            #print(counter)

        elif cur_sum == S and S == 0:
            pass


        i += 1



def numSubarraysWithSum(self, A, S):
    """
    :type A: List[int]
    :type S: int
    :rtype: int
    """

    left = 0
    right = 0
    cur_sum = 0
    counter = 0
    i = 0

    while i < len(A):

        cur_sum += A[i]
        right = i
        print(right)

        if cur_sum == S and S > 0:
            print((left, right))
            left_zeros = 1
            right_zeros = 1
            for j in range(left, right):
                if A[j] == 0:
                    left_zeros += 1
                else:
                    left = j + 1
                    cur_sum -= 1
                    break

            for j in range(right + 1, len(A)):
                if A[j] == 0:
                    right_zeros += 1
                    i = j
                else:
                    i = j - 1
                    break
            #print(i)
            counter += left_zeros * right_zeros
            #print(counter)

        elif S == 0:

            if cur_sum == 0:

                temp = 0
                found_one = False
                for j in range(right, len(A)):

                    if A[j] == 0:
                        if found_one:
                            break
                        else:
                            temp += j - right + 1
                            i = j
                    else:
                        i = j
                        found_one = True
                    
                counter += temp
            else:
                pass

            cur_sum = 0

        i += 1
    
    return counter




modifier = ''
signature = 'def numSubarraysWithSum(self, A, S):'
input_string = """[1,1,0,0]
0
"""