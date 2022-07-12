# Problem: Find the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxWord = ""
        word = ""
        counter = 0
        while counter < len(s):
            if s[counter] in word:
                if len(word) > len(maxWord):
                    maxWord = word
                if len(word) <= 1:
                    word = word[-1]
                else:
                    print(word)
                    word = word[word.index(s[counter])+1:] + s[counter]
            else:
                word += s[counter]
                print(word)
            counter+=1
        if len(maxWord) > len(word):
            return len(maxWord)
        return len(word)

# Time Complexity: O(n^n)
# Space Complexity: O(n)
