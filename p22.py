# with open("names.txt", 'r', encoding='UTF-8') as file:
#     buffer = file.read().strip()
#     names = buffer.replace('"', "").split(sep=',')

# Assume variable "names" is a list of all names

alphabet = {chr(i) : i-64 for i in range(65, 91)}

names.sort()

def get_score(char: str) -> int:
    return alphabet[char]

def search_name(index):
    return names[index]

def get_worth(name: str):
    worth = 0
    for letter in name:
        worth += get_score(letter)

    return worth

def main():
    total = 0

    for i, name in enumerate(names):
        total += get_worth(name) * (i+1)

    print(total)

main()
