import numpy as np


def my_bisection(func, a, b, tol):
    if np.sign(func(a)) == np.sign(func(b)):
        raise Exception("The scalars a and b do not bound a root")  ## Throwing Bug

    m = (a + b) / 2

    if np.abs(func(m)) < tol:
        return m
    elif np.sign(func(a)) == np.sign(func(m)):
        return my_bisection(func, m, b, tol)
    elif np.sign(func(b)) == np.sign(func(m)):
        return my_bisection(func, a, m, tol)


f = lambda x: x ** 2 - 3

r_ori = my_bisection(f, 0, 2, 0.1)
print("High Tolerances =", r_ori)
r_sophist = my_bisection(f, 0, 2, 0.01)
print("More sophisticated tolerances =", r_sophist)

print("f(r1) =", f(r_ori))
print("f(r01) =", f(r_sophist))
