def tn(n): return (n * (n + 1)) / 2
def pn(n): return (n * ((3 * n) - 1)) / 2
def hn(n): return n * ((2 * n) - 1)


def main():

    for t in range(236, 100_000):
        ans_t = tn(t)
        for p in range(166, 100_000):
            ans_p = pn(p)

            if ans_t != ans_p:
                continue

            for h in range(144, 100_000):
                ans_h = hn(h)

                if ans_h == ans_p == ans_t:
                    print(f"Triangle numbers: T_{t}, P_{p}, H_{h}")
                else:
                    continue

    print("Not found")



main()
