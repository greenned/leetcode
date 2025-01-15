class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_cnt = {}
        for char in magazine:
            mag_cnt[char] = mag_cnt.get(char, 0) + 1
        
        for rchar in ransomNote:
            if rchar not in mag_cnt:
                return False
            mag_cnt[rchar] -= 1
            if mag_cnt[rchar] < 0:
                return False
        return True
