class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = ""
        for char in s:
            if char.isalnum():
                res+=char.lower()

        reverse_str = res[::-1]
    
        if res == reverse_str:
            return True
    
        return False

       
