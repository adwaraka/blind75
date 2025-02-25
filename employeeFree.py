'''
Find time slots where all employees are free
'''

def employeeFreeTime(schedule):
    intervals = []
    for emp in schedule:
        # print(emp)
        intervals.extend(emp)
    intervals.sort(key=lambda x: x[0])
    print(intervals)

    result = []
    prev = intervals[0][1]  # which would be first interval's end time
    for interval in intervals:
    	# [t01, t02], [t11, t12]; checking if t02 < t11
        if prev < interval[0]:
        	# if yes, [(t02, t11)] is a valid interval
            result.append([prev, interval[0]])
        # Important: which is greater; current endtime or prev endtime
        prev = max(prev, interval[1])
        # print(prev)
    return result

schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
print(employeeFreeTime(schedule))
