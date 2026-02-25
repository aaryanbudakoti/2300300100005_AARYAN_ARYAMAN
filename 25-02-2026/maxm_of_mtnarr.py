#leetcode 162 - find peak element
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return start


if __name__ == "__main__":
    arr = [0, 10, 5, 2]
    sol = Solution()  # create an instance of Solution
    peakIndex = sol.peakIndexInMountainArray(arr)  # call method via instance
    print(f"Peak Element is present at index {peakIndex}")