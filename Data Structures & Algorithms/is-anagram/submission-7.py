class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dictS = {}
        dictT = {}

        for letter in s:
            dictS[letter] = dictS.get(letter,0) + 1


        for letter in t:
            dictT[letter] = dictT.get(letter,0) +1
            

        return dictS == dictT