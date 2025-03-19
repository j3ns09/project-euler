def factorial(n: int) -> int:
    k = 1
    for i in range(1, n + 1):
        k *= i
    return k

def main():
    result = factorial(100)
    str_result = str(result)

    k = 0
    for s in str_result:
        k += int(s)
    
    return k

if __name__ == '__main__':
    main()