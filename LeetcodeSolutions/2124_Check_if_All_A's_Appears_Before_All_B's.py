class Solution:
    def checkString(self, s: str) -> bool:
        return True if "ba" not in s else False

class Solution:
    def checkString(self, s: str) -> bool:
        i=1
        counter=-1

        while i<len(s):
            if s[i]=="a":
                if s[i-1]=="a":
                    i+=1
                else:
                    counter=i
                    break
            i+=1
        if counter!=(-1):
            print("False")
        else:
            print("True")