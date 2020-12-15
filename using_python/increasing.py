class Solution():
    # 不做贪心 就会超时
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

    def monotoneIncreasingDigits(self, N: int) -> int:
        list_n = list(str(N))
        r = len(list_n) - 1
        res = []
        while r - 1 >= 0:
            if list_n[r] >= list_n[r - 1]:
                res.append(list_n[r])
            else:
                list_n[r - 1] = str(int(list_n[r - 1]) - 1)
                res = ['9'] * (len(res) + 1)
            r -= 1
        if list_n[r] != '0':
            res.append(list_n[r])
        return int(''.join(res[::-1]))


def unit_test():

    so = Solution()
    print(so.monotoneIncreasingDigits(332))


unit_test()
