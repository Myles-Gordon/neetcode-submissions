class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for pos in range(len(s)):
            l, r = pos, pos
            while l >= 0 and r < len(s) and s[l]==s[r]:
                result+=1
                l-=1
                r+=1
            
            l, r = pos, pos+1
            while l >= 0 and r < len(s) and s[l]==s[r]:
                result+=1
                l-=1
                r+=1

        return result
        
