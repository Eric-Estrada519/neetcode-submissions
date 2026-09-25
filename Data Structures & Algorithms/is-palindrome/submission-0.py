class Solution:
    def isPalindrome(self, s: str) -> bool:

        st = "".join(filter(str.isalnum, s)).lower()

        l = 0
        r = len(st) - 1

        while l < r:
            if st[l] == st[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True 
        