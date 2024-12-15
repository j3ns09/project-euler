def tn(n): return (n * (n + 1)) / 2
def pn(n): return (n * ((3 * n) - 1)) / 2
def hn(n): return n * ((2 * n) - 1)


def main():
    for t in range(100_000):
        ans_t = tn(t)
        for p in range(100_000):
            ans_p = pn(p)

            if ans_t != ans_p:
                break

            for h in range(100_000):
                ans_h = hn(h)

                if ans_h != ans_p:
                    break

main()
