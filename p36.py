def palindrome(string):
    lenght = len(string)
    l_ptr = 0
    r_ptr = lenght - 1

    for i in range(lenght // 2):
        if string[l_ptr] != string[r_ptr]:
            return False
        l_ptr += 1
        r_ptr -= 1
    return True

def is_palindromic_both_bases(num):
    s_num10 = str(num)
    s_num2 = str(bin(num))[2:]

    return True if (palindrome(s_num10) and palindrome(s_num2)) else False


def main():
    k = 0
    for i in range(1_000_000):
        if is_palindromic_both_bases(i):
            k += i

    print(k)

main()
