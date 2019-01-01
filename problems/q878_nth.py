def nthMagicalNumber(self, N, A, B):

    import math

    small = A if A < B else B
    big = A if A >= B else B


    gcd = math.gcd(A,B)
    lcm = A * B / gcd

    per_lcm = int(lcm / A + lcm / B - 1)

    lcm_count = N // per_lcm
    left_over = N % per_lcm

    print(lcm_count)
    print(per_lcm)

    if left_over == 0:
        return  int(lcm_count * lcm)

    nums = []
    for i in range(1, B):
        nums.append(A*i)
    
    for i in range(1,A):
        nums.append(B*i)

    nums.sort()
    next_num = nums[left_over - 1]

    
    print(nums)
    print(next_num)

    final = lcm_count * lcm + next_num

    return int(final)


signature = 'def nthMagicalNumber(self, N, A, B):'
input_string = """5
2
4
"""