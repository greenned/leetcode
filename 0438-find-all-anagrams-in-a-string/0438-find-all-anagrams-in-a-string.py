class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        s_cnt, p_cnt = {}, {}

        for i in range(len(p)):
            s_cnt[s[i]] = s_cnt.get(s[i], 0) + 1
            p_cnt[p[i]] = p_cnt.get(p[i], 0) + 1
        
        # # p 문자열의 문자 빈도 계산
        # for char in p:
        #     p_cnt[char] = p_cnt.get(char, 0) + 1
        
        # # 첫 번째 윈도우의 문자 빈도 계산
        # for i in range(len(p)):
        #     s_cnt[s[i]] = s_cnt.get(s[i], 0) + 1
        
        res = [0] if s_cnt == p_cnt else []


        for r in range(len(p), len(s)):
            s_cnt[s[r]] = s_cnt.get(s[r], 0) + 1
            s_cnt[s[r-len(p)]] -= 1

            if s_cnt[s[r-len(p)]] == 0:
                s_cnt.pop(s[r-len(p)])
            
            if s_cnt == p_cnt:
                res.append(r - len(p) + 1)
        return res

