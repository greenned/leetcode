class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = {}

        for s in strs:
            sorted_s = "".join(sorted(list(s)))
            lst = hash_map.get(sorted_s, [])
            lst.append(s)
            hash_map[sorted_s] = lst
        
        return list(hash_map.values())
        