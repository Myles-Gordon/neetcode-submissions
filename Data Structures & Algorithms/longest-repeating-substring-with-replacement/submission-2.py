class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hm = {}
        count = 0
        for i, c in enumerate(s):
            hm[c] = hm.get(c, 0) + 1
            count = max(count, hm[c])
            
            if i - l + 1 - count > k:
                hm[s[l]]-=1
                l+=1

        return len(s) - l
         
