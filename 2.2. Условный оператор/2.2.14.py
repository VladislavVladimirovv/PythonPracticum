from itertools import permutations

def main():
    data = []
    for i in permutations(input(), r=2):
        if i[0] == '0':
            continue
        else:
            data.append(int(''.join(i)))
    print(min(data), max(data))

if __name__ == "__main__":
    main()