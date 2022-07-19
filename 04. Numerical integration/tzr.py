# applicable for only: 9.1, 9.2 & 9.3
# fp => first portion, lp => last portion

def get_h(ub, lb, n):
    return ((ub - lb) / n)


def get_i(y, h, n):
    fp = lp = 0
    
    for i in range(0, n + 1, 1):
        if i == 0 or i == n:
            fp += y[i]
        else:
            lp += y[i]

    lp *= 2

    return (h / 2 * (fp + lp))
