'''
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-
overlapping intervals that cover all the intervals in the input.
'''

def mergeIntervals(intervals):
    result = []
    intervals.sort(key=lambda x: x[0])

    result.append(intervals[0])

    for interval in intervals[1:]:
        # we set lastEnd within the loop
        # lastEnd is the earlier intervals end time
        lastEnd = result[-1][1]
        # no overlap
        if lastEnd < interval[0]:
            # ... so add interval as it is
            result.append(interval)
        else:
            # modify the end time of the current interval
            # which is bigger - the new interval's end time
            # or the last interval's end time
            result[-1][1] = max(interval[1], lastEnd)
    return result


intervals = [[1, 3], [1, 5], [6, 7], [8, 10], [9, 15], [14, 30]]
print(mergeIntervals(intervals))
