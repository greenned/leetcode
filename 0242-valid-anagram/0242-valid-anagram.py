class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False
        # 17ms Beats 23.64%
        
        s_map = {}
        for ss in s:
            s_map[ss] = s_map.get(ss, 0) + 1
        
        t_map = {}
        for tt in t:
            t_map[tt] = t_map.get(tt, 0) + 1
        return s_map == t_map
