class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        subs = []

        for i in range(len(s)):
            if s[i] in subs:
                if len(subs) > best:
                    best = len(subs)
                ind = subs.index(s[i])
                subs = subs[ind+1:]
                subs.append(s[i])
            else:
                subs.append(s[i])

        return max(len(subs), best)