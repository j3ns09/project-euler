def smallest_num():
    num = None
    n = 2
    flag = True
    while num is None:
        for i in range(1, 21):
            if n%i != 0:
                flag = False
                break
        if flag:
            num = n
            break
        else:
            flag = True
        n += 2

    return num

def check(num):
    for i in range(1, 21):
        rem = num%i
        print(num, "%", i, "=", rem)
        if rem != 0:
            return False
    return True


def main():
    e = smallest_num()

    if check(e):
        print("Correct number:", e)
    else:
        print("Incorrect result.")

main()
