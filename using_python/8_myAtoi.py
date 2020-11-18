INT_MAX = 2**31 - 1
INT_MIN = -2**31


class Automaton:
    def __init__(self):
        self.state = "start"
        self.sign = 1
        self.ans = 0
        self.table = {
            "start": ["start", "signed", "in_number", "end"],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == "+" or c == "-":
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == "in_number":
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(
                self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution():
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans

    def myAtoi2(self, str: str) -> int:
        flag_start = False
        sign = 1
        ans = 0
        for c in s:
            if c == " " and not flag_start:
                continue
            elif c == "+" and not flag_start:
                flag_start = True
            elif c == "-" and not flag_start:
                flag_start = True
                sign = -sign
            elif c.isdigit() and not flag_start:
                flag_start = True
                ans = ans * 10 + int(c)
            elif c.isdigit() and flag_start:
                ans = ans * 10 + int(c)

            else:
                if INT_MIN <=sign * ans <=INT_MAX:
                    return sign * ans
                elif sign * ans<INT_MIN:
                    return INT_MIN
                else: return INT_MAX
        
        if INT_MIN <=sign * ans <=INT_MAX:
                    return sign * ans
        elif sign * ans<INT_MIN:
                    return INT_MIN
        else: return INT_MAX


so = Solution()
print(so.myAtoi2("   +456464 loss"))
