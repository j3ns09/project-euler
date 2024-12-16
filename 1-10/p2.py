def main():
    k = 0
    f0, f1 = 0, 1

    while f1 < 4_000_000:
        fn = f0 + f1

        if (fn & 1) == 0:
            k += fn

        f0 = f1
        f1 = fn

    print(k)

main()
