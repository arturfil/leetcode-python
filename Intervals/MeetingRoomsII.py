from typing import List

class MeetingRoomsII:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        first = sorted([i[0] for i in intervals])
        last = sorted([i[1] for i in intervals])

        rooms, end = 0, 0

        for i in range(len(intervals)):
            if first[i] < last[end]:
                rooms+=1
            else:
                end+=1

        return rooms
