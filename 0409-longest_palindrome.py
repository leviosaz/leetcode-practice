# Problem: Longest palindrome from the available characters given in string s. 

from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letters = Counter(s)
        
        length = 0
        add = 0
        for x in letters:
            if letters[x] % 2 == 1:
                add = 1
            length += letters[x] // 2 * 2
            
            
        return length + add

# Time Complexity: O(n)
# Space Complexity: O(n)
