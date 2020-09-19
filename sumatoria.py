
def sumatoria_cubica(n):
    res = 0
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            k = j
            while k <= (i + j):
                res += 1
                k += 1
            j += 1
        i +=1

    return res


def sumatoria_constante(n):

    res = (n ** 3 + 3 * 100 ** 2 + 2 * n) / 3

    return res
