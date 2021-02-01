from random import randint


# 生成随机数列
def generateRandomArary(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]
    return arr


# 判断是否有序,默认从小到大
def isSorted(alist, direction=True):
    for i in range(0, len(alist)):
        if direction:
            if alist[i] > alist[i + 1]:
                return False
        else:
            if alist[i] < alist[i + 1]:
                return False
    return True
