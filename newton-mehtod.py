import numpy as np
import math

"""
    func : 대상 함수
    dfunc : 대상 함수의 미분 함수
    xr : 시작값
"""

def newton(func, dfunc, xr):
    # 최대 반복 횟수, 오차 최댓값, 반복 카운터 초기화
    global ea
    maxit = 500
    es = 1.0e-10 #e의 -4승
    iter_count = 0

    while True:
        xrold = xr
        xr = float(xr - func(xr) / dfunc(xr))
        iter_count = iter_count + 1

        if xr != 0:
            ea = float(np.abs((float(xr) - float(xrold)) / float(xr)) * 100)
        if int(ea < es) | int(iter_count >= maxit):
            break

    root_ = xr
    return root_, ea, iter_count


y = lambda m: m**2 - 2*m + 5
dy = lambda m: 2*m - 2

root, ea, iters = newton(y, dy, 1)


print("Start Value = 150\n")

print("Root:", root)
print("Acc :", ea, "(Must Be Zero)")
print("Iterations : ", iters)
print()
