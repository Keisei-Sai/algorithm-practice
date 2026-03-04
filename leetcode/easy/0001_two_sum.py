"""
LeetCode 1. Two Sum
Approach: Hash Map
Time: O(n), Space: O(n)
"""

from typing import List, Tuple

def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Return indices (i, j) such that nums[i] + nums[j] == target.
    Assumption (as in LeetCode): exactly one solution exists, and you may not use the same element twice.

    Time: O(n) average
    Space: O(n)
    """
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        y = target - x
        if y in seen:
            return seen[y], i
        seen[x] = i

    raise ValueError("No two sum solution")
