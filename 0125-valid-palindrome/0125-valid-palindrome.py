class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [cha for cha in s if cha.isalnum()]

        if s == list(reversed(s)):
            return True
        else:
            return False
        