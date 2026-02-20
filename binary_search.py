"""
LeetCode: Binary Search
Approach: Binary search on a sorted array (half-open interval [left, right))
Time: O(log n)
Space: O(1)
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # [left, right)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid

        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))   # 4
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))   # -1
