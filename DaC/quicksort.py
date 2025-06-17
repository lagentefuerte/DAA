from random import randint


def partition(elements, left, right):
    pivot = elements[left]
    i = left + 1
    j = right
    while True:
        while i <= right and elements[i] <= pivot:
            i += 1
        while j >= left and elements[j] > pivot:
            j -= 1
        if i > j:
            break
        elements[i], elements[j] = elements[j], elements[i]
    elements[left], elements[j] = elements[j], elements[left]
    return j

def qs_rec(elements, left, right):
    if left <= right:
        idx = partition(elements, left, right)
        qs_rec(elements, left, idx-1)
        qs_rec(elements, idx+1, right)

def quickSort(elements):
    qs_rec(elements, 0, len(elements) - 1)


def test_quickSort():
    print("Testing...")
    for _ in range(10):
        input = []
        n = randint(1, 5)
        for j in range(n):
            input.append(randint(-50, 50))
        copy = input[::]
        quickSort(input)
        copy.sort()
        assert copy == input
    print("Done")


test_quickSort()
