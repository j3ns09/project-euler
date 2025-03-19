def main():
    result = 2 ** 1000
    str_result = str(result)
    
    k = 0
    for s in str_result:
        k += int(s)
    
    return k

if __name__ == '__main__':
    main()