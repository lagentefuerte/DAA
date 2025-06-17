from random import randint


def merge(first, second, output):
    f = s = k = 0
    while f < len(first) and s < len(second):
        if first[f] < second[s]:
            output[k] = first[f]
            f += 1
        else:
            output[k] = second[s]
            s += 1
        k += 1
    r = f if s == len(second) else s
    reminder = first if s == len(second) else second
    while r < len(reminder):
        output[k] = reminder[r]
        k += 1
        r += 1


def mergeSort(input):
    if len(input) > 1:
        mid = len(input) // 2
        left = input[:mid]
        right = input[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(left, right, input)


def test_MergeSort():
    print("Testing...")
    for _ in range(1000):
        input = []
        n = randint(1, 100)
        for j in range(n):
            input.append(randint(-50, 50))
        copy = input[::]
        mergeSort(input)
        copy.sort()
        assert copy == input
    print("Done")


test_MergeSort()
