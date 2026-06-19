class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1let = [0]*26
        res = [0]*26
        for i in range(0, len(s1)):
            s1let[ord(s1[i])-ord("a")] += 1
            res[ord(s2[i])-ord("a")] += 1

        l = 0
        r = len(s1)
        while r<len(s2):
            if res == s1let:
                return True
            else:
                res[ord(s2[l])-ord("a")] -= 1
                res[ord(s2[r])-ord("a")] += 1
                l+=1
                r+=1
        
        return res==s1let