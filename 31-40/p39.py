# p = a + b + c
# c = sqrt(a² + b²)
# a + b + c = a + b + sqrt(a² + b²)
#

def get_solutions() -> dict[int, list]:
    solutions = {}
    for i in range(1, 1001):
        for a in range(1, 1001):
            for b in range(1, 1001):
                for c in range(1, 1001):
                    if a + b + c == i:
                        solutions[i] = [a, b, c]
    return solutions

def main():
    print(get_solutions())

main()
