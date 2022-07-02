# Problem: 
# Check if the input is a valid palindrome.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isAlphaNumeric(c):
            return ("a" <= c <= "z") or ("A" <= c <= "Z") or ("0" <= c <= "9")
        
        start = 0
        end = len(s)-1
        s = s.lower()
        
        while start <= end:
            if not isAlphaNumeric(s[start]):
                start += 1
                continue
            if not isAlphaNumeric(s[end]):
                end -= 1
                continue
            if s[start] != s[end]:
                return False
            end -= 1
            start += 1
        return True

# Time Complexity: O(n)
# Space Complexity: O(1)
