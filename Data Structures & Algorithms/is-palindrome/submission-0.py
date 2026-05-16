class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left<=right:
            if not self.isAlp(s[left]):
                left+=1
                continue
            if not self.isAlp(s[right]):
                right-=1
                continue

            if(s[left].lower() == s[right].lower()):
                left+=1
                right-=1
            else:
                return False
        
        return True
            

    def isAlp(self, s: str) -> bool:
        if(ord("A")<=ord(s)<=ord("Z")):
            return True
        if(ord("a")<=ord(s)<=ord("z")):
            return True
        if(ord("0")<=ord(s)<=ord("9")):
            return True
        
        return False