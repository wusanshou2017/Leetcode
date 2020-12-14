MAX_NUM = 2**31 - 1
MIN_NUM = -2**31


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 and divisor != 0:
            return 0
        if divisor == 1:
            return dividend

        if divisor == 0:
            return 0

        dividend_temp = abs(dividend)
        divisor_temp = abs(divisor)
        count = 1
        res = 0
        while (dividend_temp >= abs(divisor)):
            if dividend_temp >= divisor_temp:
                res = res + count
                dividend_temp -= divisor_temp
                divisor_temp += divisor_temp

                count = count + count

            else:
                divisor_temp = abs(divisor)
                count = 1
                continue

        sign = 1 if (dividend > 0 and divisor > 0) or (
            dividend < 0 and divisor < 0) else -1
        res = res * sign
        if res > MAX_NUM:
            res = MAX_NUM
        if res < MIN_NUM:
            res = MIN_NUM
        return res
