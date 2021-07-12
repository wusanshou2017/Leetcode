class Solution:
    def __init__(self):
        self.dic_roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        self.dic_int2roman={ value:key for key,value in self.dic_roman.items()}
    def int2roman(self,target):
        res =""
        if target//1000>0:
            m=target//1000
            target=target-m*1000
            res+="M"*m;
        if target>=300:
            if target>=500:
                target=target-500
                c=target//100
                res+="D"+c*"C"
            else:
                target=target-()
