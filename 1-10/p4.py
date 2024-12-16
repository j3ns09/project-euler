def palindrome(num):
    s_num = str(num)
    lenght = len(s_num)

    l_ptr = 0
    r_ptr = lenght - 1

    for i in range(lenght // 2):
        if s_num[l_ptr] != s_num[r_ptr]:
            return False

        l_ptr += 1
        r_ptr -= 1

    return True

def main():
    maximum = 0

    for i in range(100, 1000):
        for j in range(i, 1000):
            if palindrome(i*j):
                maximum = max(maximum, i*j)
                print(maximum, "=", i, "x", j)

            if i == 999 and j == 999:
                print("End reached")

    print(maximum)

main()
