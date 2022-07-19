def value_of_i(arrayY, n, h):
    fp = mp = lp = 0
    for i in range(0, n, 1):
        if i == 0 or i == n - 1:
            fp += arrayY[i]
        else:
            if i % 3 == 0:
                mp += arrayY[i]
            else:
                lp += arrayY[i]
    return round(((3 * h / 8) * (fp + (mp * 2) + (lp * 3))), 5)
