def merge(intervals):

    intervals.sort()

    result = []
    current = intervals[0]
    for i in range(1, len(intervals)):
        interval = intervals[i]

        if interval[0] <= current[1]:
            current[1] = max(current[1], interval[1])
        else:
            result.append(current)
            current = interval

    result.append(current)


    return result


#result = merge([[1,3],[2,6],[8,10],[15,18]])
result = merge([[1,4],[4,5]])
print(result)