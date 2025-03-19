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
    # 2 is a prime number and we add it beforehand
    # because we will be iterating through odd numbers
    k = 2
    for i in range(3, 2_000_000, 2):
        if is_prime(i):
            k += i
    
    print(k)
    return k

if __name__ == '__main__':
    main()
