# Problem: Find if the two inputs are anagrams of each other.

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)

# Time Complexity: O(n)
# The time to create each counter is n.
# To compare it takes another n. 
# In total it's O(3n), which the order of O(n)

# Space Complexity: O(1)

# If asked this in an interview, and you're unable to use Counter,
# Just recreate the Counter function.
