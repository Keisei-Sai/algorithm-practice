"""
LeetCode: Valid Parentheses
Approach: Stack (LIFO)
Time: O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        pairs = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()[]{}"))  # True

