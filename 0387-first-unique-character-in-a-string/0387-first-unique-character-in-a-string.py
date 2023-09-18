class Solution:
    def firstUniqChar(self, s: str) -> int:
        for idx, value in enumerate(s):
            if s.count(value) == 1:
                return idx
        return -1
            