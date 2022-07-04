# Problem: Given array of strings, group the anagrams together.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        
        for x in strs:
            sortedString = ''.join(sorted(x))
            if hashmap.get(sortedString):
                hashmap[sortedString].append(x)
            else:
                hashmap[sortedString] = [x]
        
        return hashmap.values()

# Time Complexity: O(n)
# Space Complexity: O(n)
