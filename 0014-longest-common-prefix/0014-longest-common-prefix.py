class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        query_str = strs.pop(0)
        
        common_prefix = ""
        for idx, cha in enumerate(query_str):
            for word in strs:
                try:
                    compared_cha = word[idx]
                except IndexError:
                    return common_prefix

                if cha != word[idx]:
                    return common_prefix
                
            common_prefix += cha
        return common_prefix