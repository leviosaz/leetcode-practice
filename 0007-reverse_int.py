# Problem: Reverse the integers and return -1 if it falls out of bounds of 32 bits.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            x *= -1
            neg = True

        num = 0
        
        while x > 0:
            digit = x % 10

            num = num * 10 + digit

            x = int(x/10)   
        
        if neg:
            num *= -1
            
        if num <= (2**31-1) and num >= -2**31:
            return num

        return 0
        
# Time Complexity: O(n), n being number of digits. 
# Space Complexity: O(1)
