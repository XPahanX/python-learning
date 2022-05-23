'''
Задача про рюкзак. Нужно наполнить рюкзак предметами так, чтобы стоимость украденного была максимальна.
Сначала подается количество предметов и объем рюкзака, затем стоимость предметов и доступный объем.
'''

def backpack(w, lst):
    lst.sort()
    cost = 0
    i = -1
    while (w > 0 and i > -len(lst)):
        if lst[i][2] <= w:
            w -= lst[i][2]
            cost += lst[i][1]
        else:
            cost += lst[i][0] * w
            w = 0
        i -= 1
    return f"{cost:.3f}"


def main():
    n, w = map(int, input().split())
    lst = list()
    for i in range(n):
        c, w_i = map(int, input().split())
        p = c / w_i
        lst.append([p, c, w_i])
    print(backpack(w, lst))


if __name__ == "__main__":
    main()
