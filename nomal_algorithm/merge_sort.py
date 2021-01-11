def mergesort(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq) / 2
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])

    return merge(left, right)

def merge(left, right):

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def unit_test():
    test = [1, 2, 3, 4, 5, 9, 7, 5, 1, 0, 4, 55, 6,
            8, 77, 558, 6654, 131, 4, 1, 32, 45, 1, 54654]
    data=mergesort(test)
    print(data)

unit_test()