class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (len(s)==1):
            return True
        ans = ""
        for i in s:
            if i.isalpha() or (i>='0' and i<='9'):
                ans+=i.lower()
        if (ans==ans[::-1]):
            return True
        return False
