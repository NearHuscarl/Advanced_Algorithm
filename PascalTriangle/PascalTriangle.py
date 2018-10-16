# -*- coding: utf-8 -*-

"""
Tham khảo:
    - https://en.wikipedia.org/wiki/Pascal_triangle
"""

def PascalTriangle(k):
    L = []
    for i in range(k + 1):
        L.append([0] * (k + 1))

    L[0][0] = 1
    for i in range(1, k + 1):
        L[i][0] = 1
        for j in range(1, i):
            L[i][j] = L[i - 1][j - 1] + L[i - 1][j]
        L[i][i] = 1

    return L[k]


def main():
    n = input("Enter n: ")
    print PascalTriangle(n)


main()
