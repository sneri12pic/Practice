"""
Definition of Interval:
import types
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        def get_start(meeting):
            return meeting.start
        
        intervals.sort(key=get_start)

        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            cur = intervals[i]

            if cur.start < prev.end:
                return False

        return True
        



