class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.recurse(s, 0)
    
    
    def recurse(self, s, pos):
        
        if pos >= int(len(s) / 2):
            return
        
        s[pos], s[len(s)-pos-1] = s[len(s)-pos-1], s[pos]
        pos+=1
        
        self.recurse(s, pos)
        