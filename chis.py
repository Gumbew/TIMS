import scipy.stats as ss


def get_r(n):
    i = 0
    while not (pow(2, i) < n <= pow(2, i + 1)):
        i += 1
    return i


def main():
    # k, mu
    print(ss.poisson.pmf(2, 1))
    print(ss.poisson.cdf(4, 3))
    print(ss.poisson.interval(0.8, 2))

    res = ss.chisquare(
        [28, 22],
        [25, 25]
    )

    res2 = ss.chi2.isf(0.05, 1)

    print(res)
    print(res2)


main()
