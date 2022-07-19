def value_of_i(arrayY, n, h):
    fp = mp = lp = 0
    for i in range(0, n + 1, 1):
        if i == 0 or i == n:
            fp += arrayY[i]
        else:
            if i % 2 == 0:
                mp += arrayY[i]
            else:
                lp += arrayY[i]
    return round(((h / 3) * (fp + (mp * 2) + (lp * 4))), 5)
