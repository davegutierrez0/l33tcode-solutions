class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        # print(intervals)
        merged = [intervals[0]]
        start, end = 0, 1

        for i in range(1,len(intervals)):
            interval = intervals[i]

            if interval[start] > merged[-1][end]:
                merged.append(interval)

            elif interval[end] > merged[-1][end]:
                merged[-1][end] = interval[end]
            
        return merged

# Time Complexity: O(NlogN)
# Space Complexity: O(N)