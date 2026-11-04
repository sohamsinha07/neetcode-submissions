"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #create two arrays one storing start times and one storing end times
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
            
        res = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]: #(1, 5) (3, 4) (6, 8) (8,9) 
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res

