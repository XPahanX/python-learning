'''
Разложить число на максимальное количество неповторяющихся слагаемых.
'''

def terms(n):
    lst = list()
    i = 1
    while (n - i > i):
        lst.append(i)
        n -= i
        i += 1
    lst.append(n)
    return lst


def main():
    n = int(input())
    print(len(terms(n)), "\n", *terms(n))


if __name__ == "__main__":
    main()
