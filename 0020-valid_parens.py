# Check if the input holds valid parentheses pairs.

class Solution(object):
    def isValid(self, s):
        stack = []

        d = {"(":")", "{":"}", "[":"]"}

        for x in s:
            if x in "({[":
                stack.append(x)
            else:
                if not stack:
                    return False

                current = stack.pop()

                if current in "({[" and d[current] != x:
                    return False

        if stack:
            return False
        return True

# Time Complexity: O(n)
# Space Complexity: O(n)
