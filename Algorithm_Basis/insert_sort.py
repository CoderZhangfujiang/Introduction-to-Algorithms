# _*_ coding:utf-8 _*_

"""
输入：n个数的一个序列
输出：序列的一个排序
"""


def insert_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        # insert a[i] into the sorted sequence a[1...i-1]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j+1] = key
    return a


if __name__ == '__main__':
    A = [567, 12, 123, 234, 2, 365, 5, 29, 5, 67, 29, 45, 390]
    print(insert_sort(A))

