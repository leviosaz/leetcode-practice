# Problem: Find the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) < 2:
            return len(s)
        
        hashmap = {}
        maxLength = 1
        
        counter = 0
        
        while counter < len(s):
            if hashmap.get(s[counter]):
                wordLength = len(hashmap.keys())
                if wordLength > maxLength:
                    maxLength = wordLength
                counter = hashmap[s[counter]]
                hashmap = {}                
            else:
                hashmap[s[counter]] = counter
            
            counter += 1
        
        return max(len(hashmap.keys()), maxLength)

# Time Complexity: O(n^n)
# Space Complexity: O(n)
