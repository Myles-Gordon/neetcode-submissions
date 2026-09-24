class Solution:
    def decodeString(self, s: str) -> str:
        stackNums = []
        stackC = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = []
                while i<len(s) and s[i].isdigit():
                    num.append(s[i])
                    i+=1
                total = "".join(num)
                stackNums.append(int(total))
            else:
                if s[i] != "]":
                    stackC.append(s[i])
                else:
                    decode = []
                    while stackC[-1] != "[":
                        decode.append(stackC.pop())
                    stackC.pop()
                    ch = ""
                    repeated="".join(reversed(decode))
                    stackC.append(repeated * stackNums.pop())
                i+=1
        
        res = []
        while stackC:
            res.append(stackC.pop())
        
        return "".join(reversed(res))