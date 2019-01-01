from lt_helper import Interval

def insert(self, intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """

    def merge_two(left, right):
        if left.end < right.start:
            return [left, right]
        else:
            return [Interval(left.start, right.end)]

    def helper(interval, se):
        if se == 'start':
            return interval.start - 0.5
        else:
            return interval.end

    def interval_search(target, start, end, se):
        if start == end:
            return start
        elif start == end - 1:
            if helper(intervals[start], se) >= target:
                return start
            else:
                return end
        
        middle = (start + end) // 2
        if target < helper(intervals[middle], se):
            return interval_search(target, start, middle, se)
        else:
            return interval_search(target, middle, end, se)

    if len(intervals) == 0:
        return [newInterval]

    results = []
    start_index = interval_search(newInterval.start, 0, len(intervals), 'end')
    end_index = interval_search(newInterval.end, 0, len(intervals), 'start')
    #print(start_index, end_index)

    # First check if it touches nothing
    if start_index == len(intervals) or intervals[start_index].start > newInterval.end:
        intervals.insert(start_index, newInterval)
        return intervals

    # Now must have intersection
    # Handle start
    if intervals[start_index].start > newInterval.start:
        intervals[start_index].start = newInterval.start
    if intervals[start_index].end < newInterval.end:
        intervals[start_index].end = newInterval.end
    
    # Handle end
    if intervals[end_index - 1].end < newInterval.end:
        intervals[end_index - 1].end = newInterval.end
    if intervals[end_index - 1].start > newInterval.start:
        intervals[end_index - 1].start = newInterval.start
    
    #print(intervals)

    for i in range(start_index + 1, end_index - 1):
        intervals.pop(start_index + 1)

    #print(intervals)
    #print(intervals[start_index])
    if start_index + 1 >= len(intervals):
        return intervals

    #print(intervals[start_index + 1])

    temp = merge_two(intervals[start_index], intervals[start_index + 1])
    intervals.pop(start_index)
    intervals.pop(start_index)
    intervals[start_index:start_index] = temp
    
    return intervals


modifier = 'intervals, interval'
signature = 'def insert(self, intervals, newInterval):'
test_cases = None
input_string = """[[1,5]]
[2,3]
[]
[2,3]
[[2,6],[7,9]]
[15,18]
[[0,2],[3,9]]
[6,8]
"""  
