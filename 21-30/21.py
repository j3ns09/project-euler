def d(n: int) -> int:
    """
        Returns the sum of every divisor of n
    """

    k = 0
    for i in range(1, n):
        if n % i == 0:
            k += i
            
    return k

def is_amicable(a: int) -> bool:
    b = d(a)
    return a != b and d(b) == a

def main():
    k = 0
    for i in range(10000):
        if is_amicable(i):
            k += i

    return k

if __name__ == '__main__':
    main()