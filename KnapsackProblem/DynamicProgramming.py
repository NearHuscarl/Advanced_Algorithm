# -*- coding: utf-8 -*-

"""
Cho vali chứa được trọng lượng tối đa là W. Có n đồ vật được đánh số từ 1 đến n,
đồ vật thứ i có khối lượng weight[i] và giá trị value[i], 1 <= i <= n. Tìm cách
xếp đồ vật vào vali sao cho tổng giá trị các đồ vật trong vali là lớn nhất
"""


def KnapsackProblem(W, n, weight, value):
    weight.insert(0, 0)
    value.insert(0, 0)

    L = []
    for i in range(n+1):
        L.append([-1]*(W+1))

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0:
                L[i][w] = 0
            elif w - weight[i] < 0:
                L[i][w] = L[i-1][w]
            else:
                L[i][w] = max(L[i-1][w], L[i-1][w - weight[i]] + value[i])

    return L[i][w]


def main():
    W = 13
    weight = [3, 4, 5, 2, 1]
    value = [4, 5, 6, 3, 1]
    n = len(weight)

    print KnapsackProblem(W, n, weight, value)


main()
