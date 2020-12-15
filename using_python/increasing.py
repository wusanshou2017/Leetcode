class Solution():
    def findIncreaseNum(self, num: int) -> int:
        temp_str = str(num)
        n = len(temp_str)
        flag_increase = True
        for i in range(1, n):
            if int(temp_str[i]) >= int(temp_str[i - 1]):
                continue
            else:
                flag_increase = False
                break

        if flag_increase:
            return num
        temp_num = num
        while not flag_increase:
            temp_num -= 1
            temp_str = str(temp_num)
            n = len(temp_str)
            flag_temp = True
            for i in range(1, n):
                if int(temp_str[i]) >= int(temp_str[i - 1]):
                    continue
                else:
                    flag_temp = False
                    break
            if flag_temp:
                break
        return temp_num

def unit_test():

    so = Solution()
    print(so.findIncreaseNum(99999999))


unit_test()
