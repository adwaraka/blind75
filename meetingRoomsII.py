'''
Given an array of meeting time interval objects consisting of start 
and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
find the minimum number of days required to schedule all meetings 
without any conflicts.
'''

def meetingRoomsII(intervals):
    startTime = sorted([i[0] for i in intervals])
    endTime = sorted([i[1] for i in intervals])
    # print(startTime, endTime)
    ptr1, ptr2, count, result = 0, 0, 0, 0
    while ptr1 < len(startTime):
        # meeting has begun
        if startTime[ptr1] < endTime[ptr2]:
            count+=1
            ptr1+=1
        # meeting has ended
        else:
            count-=1
            ptr2+=1
        # IMPORTANT: we want to see the maximum value count has gone to
        result = max(result, count)
    return result


intervals = [(0, 40), (5, 10), (15, 20), (10, 15)]
print(meetingRoomsII(intervals))

intervals = [(0, 40), (5, 10), (15, 20)]
print(meetingRoomsII(intervals))

intervals = [(0, 40), (5, 10), (15, 20), (5, 15)]
print(meetingRoomsII(intervals))
