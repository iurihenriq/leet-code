class Solution:
    def haveConflict(self, event1, event2):
        def to_minutes(time):
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes

        e1_start, e1_end = map(to_minutes, event1)
        e2_start, e2_end = map(to_minutes, event2)

        return not (e1_end < e2_start or e2_end < e1_start)
