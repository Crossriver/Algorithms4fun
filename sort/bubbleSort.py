from common_api import common_api


# 默认从小到大
def bubble_sort(alist):
    n = len(alist)
    exchange = False
    exchangetimes = 0
    for i in range(0, n):
        for j in range(i, n - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                exchange = True
        if not exchange:
            break
    return alist


def selection_sort(alist):
    n = len(alist)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


def insertion_sort(alist):
    n = len(alist)
    for i in range(1, n):
        position = i
        currentvalue = alist[i]
        for j in range(i, 0, -1):
            if currentvalue < alist[j - 1]:
                alist[j] = alist[j - 1]
                position = j - 1
            else:
                break
        alist[position] = currentvalue
    return alist


def shell_sort(blist):
    n = len(blist)
    h = 1
    while (h < n / 3): h = h * 3 + 1
    while h >= 1:
        shell_insertion_sort(alist, h, n)
        h = h // 3
    return blist


def shell_insertion_sort(alist, h, n):
    for i in range(h, n, h):
        position = i
        currentvalue = alist[i]
        for j in range(i, 0, -h):
            if currentvalue < alist[j - h]:
                alist[j] = alist[j - h]
                position = j - h
            else:
                break
        alist[position] = currentvalue
    return alist


def fast_partition(alist, lo, hi):
    i = lo + 1
    j = hi
    v = alist[lo]
    while True:
        while alist[i] < v:
            if i == hi:
                break
            i = i + 1
        while alist[j] > v:
            if j == lo:
                break
            j = j - 1
        if i >= j:
            break
        alist[i], alist[j] = alist[j], alist[i]
        print("i=%s, j=%s,alist is:%s" % (str(i), str(j), str(alist)))
    alist[i - 1], alist[lo] = alist[lo], alist[i - 1]
    print(j)
    print(alist)
    return j


def quick_sort(alist, lo, hi):
    if lo>=hi:
        return
    v = fast_partition(alist, lo, hi)
    quick_sort(alist, lo, v)
    quick_sort(alist, v, hi)


if __name__ == "__main__":
    alist = common_api.generateRandomArary(15, 10, 100)
    # bubble_sort(alist)
    # selection_sort(alist)
    # insertion_sort(alist)
    print(alist)
    # shell_sort(alist)
    # fast_partition(alist, 0, len(alist) - 1)
    quick_sort(alist,0,len(alist)-1)
    print(alist)
    # print(alist)
