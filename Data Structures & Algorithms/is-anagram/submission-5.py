class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dictS = {}
        dictT = {}

        for letter in s:
            count = dictS.get(letter)
            if count:
                count += 1
                dictS.update({letter : count})
            else:
                dictS.update({letter : 1})

        for letter in t:
            count = dictT.get(letter)
            if count:
                count += 1
                dictT.update({letter : count})
            else:
                dictT.update({letter : 1})

        return dictS == dictT