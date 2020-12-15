class Solution():
    def findIncreaseNum(self,num:int)->int:
        temp_str = str(num)
        n = len(temp_str)
        flag_increase = True
        for i in range(1,n):
            if int(temp_str[i])>=int(temp_str[i-1]):
                continue
            else:
                flag_increase =False
                break

        if flag_increase:
            return num

        temp_num =num-1
        while not flag_increase:
            print("...")
            temp_str =str(temp_num)
            n = len(temp_str)
            flag_temp =True
            for i in range(1,n):
                if int(temp_str[i])>=int(temp_str[i-1]):
                    continue
                else:
                    flag_temp=False
                    break
            temp_num-=1
            if flag_temp:
                break

        return temp_num

def unit_test():

    so =Solution()
    print(so.findIncreaseNum(130))
           