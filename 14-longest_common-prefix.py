# Problem: Find the longest common prefix among an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        operator = True
        index = 0
        prefix = ""  
        
        while operator and index < len(min(strs)):
            truth = True
            pre = strs[0][index]
            
            for x in strs:
                if x[index] == pre:
                    continue
                else:
                    truth = False
                    break
            if truth:
                prefix += strs[0][index]
                index += 1
            else:
                operator = False
        
        return prefix

# Time Complexity: O(n)
# Space Complexity: O(1)
