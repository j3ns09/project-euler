def is_prime(n: int) -> bool:
    i = 2
    while True:
        if i * i > n:
            break
        elif (n % i) == 0:
            return False
        i += 1

    return True

def main():
    nth = 0
    i = 1
    while nth < 10001:
        i += 1
        if is_prime(i):
            nth += 1
    print(nth)
    print(i)



if __name__ == '__main__':
    main()