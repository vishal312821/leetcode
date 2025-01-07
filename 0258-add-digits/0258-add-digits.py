class Solution:
    def addDigits(self, num: int) -> int:
        li=list(map(int,str(num)))
        if len(li)==1:
            return li[0]
        while len(li)>1:
            s=sum(li)
            li.clear()
            li=list(map(int,str(s)))
        return s

       