class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1let = [0]*26
        for letter in s1:
            s1let[ord(letter)-97] += 1
        
        res = [0]*26
        for i in range(0, len(s1)):
            res[ord(s2[i])-97] += 1

        l = 0
        r = len(s1)
        while r<len(s2):
            if res == s1let:
                return True
            else:
                res[ord(s2[l])-97] -= 1
                res[ord(s2[r])-97] += 1
                l+=1
                r+=1
        
        return res==s1let