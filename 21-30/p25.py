def main():
    f1, f2 = 1, 1

    # nth fibonacci number
    # we keep track of the latest
    n = 2

    while True:
        f2, f1 = f1 + f2, f2
        n += 1

        if len(str(f2)) == 1000:
            return n

if __name__ == '__main__':
    main()