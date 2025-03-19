def main():
    k = 0
    for i in range(1, 1001):
        k += i ** i
    
    str_k = str(k)
    
    return str_k[-10:]


if __name__ == '__main__':
    main()