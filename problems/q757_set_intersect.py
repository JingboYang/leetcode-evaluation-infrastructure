def intersectionSizeTwo(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals = sorted(intervals, key=lambda x: x[1])
    print(intervals)

    S = set()
    S_heap = []
    for interval in intervals:

        sat_count = 0
        '''
        for i in range(interval[0], interval[1] + 1):
            if i in S:
                sat_count += 1

            if sat_count >= 2:
                break
        '''
        S_temp = list(S)
        for i in range(len(S_temp)-1, -1, -1):
            s = S_temp[i]
            if s >= interval[0] and s <= interval[1]:
                sat_count += 1

            if sat_count >= 2:
                break

        if sat_count < 2:

            back = 0
            while sat_count < 2:
                num = interval[1] - back
                if num not in S: 
                    S.add(num)
                    sat_count += 1
                back += 1

    #print(S)
    return len(S)



signature = 'def intersectionSizeTwo(self, intervals):'
input_string = """[[0,9],[0,2],[2,7],[8,10],[6,7],[3,7],[1,9],[0,9],[3,9],[3,9]]
"""