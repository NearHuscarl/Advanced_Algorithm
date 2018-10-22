# -*- coding: utf-8 -*-

"""
Cho vali chứa được trọng lượng tối đa là W. Có n đồ vật được đánh số từ 1 đến n,
đồ vật thứ i có khối lượng weight[i] và giá trị value[i], 1 <= i <= n. Tìm cách
xếp đồ vật vào vali sao cho tổng giá trị các đồ vật trong vali là lớn nhất
"""

weight = [3, 4, 5, 2, 1]
value = [4, 5, 6, 3, 1]


def BaiToanBalo(i, w):
    if i < 0:
        return 0

    if weight[i-1] > w:
        return BaiToanBalo(i-1, w - weight[i-1])

    return max(BaiToanBalo(i-1, w),
               BaiToanBalo(i-1, w - weight[i-1]) + value[i-1])


def main():
    W = 13
    print BaiToanBalo(len(weight), W)


main()
