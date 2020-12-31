
class Normalization():
    def normalize(self, target: [int]) -> [int]:

        if len(target) < 2:
            return target

        mid = len(target) // 2
        leftSeq = self.normalize(target[:mid])
        rightSeq = self.normalize(target[mid:])

        return self.merge(leftSeq, rightSeq)

    def merge(self, leftSeq: [int], rightSeq: [int]) -> [int]:

        res = []

        i, j = 0, 0
        while i < len(leftSeq) and j < len(leftSeq):
            if leftSeq[i] <= rightSeq[j]:
                res.append(leftSeq[i])
                i += 1
            else:
                res.append(rightSeq[j])
                j += 1

        res.extend(leftSeq[i:])
        res.extend(rightSeq[j:])
        return res


so = Normalization()

test_data = [1, 2, 3, 4, 5, 9, 7, 5, 1, 0, 4, 55, 6,
             8, 77, 558, 6654, 131, 4, 1, 32, 45, 1, 54654]


print(so.normalize(test_data))
