'''
По данным n отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.
В первой строке дано число 1 ≤ n ≤ 100 отрезков.
Каждая из последующих nn строк содержит по два числа  0 ≤ l ≤ r ≤ 10^9,
задающих начало и конец отрезка.
Выведите оптимальное число m точек и сами m точек.
Если таких множеств точек несколько, выведите любое из них.
'''

# Мое решение

def point(lst):
    lst_r, lst_res = list(), list()
    for i in range(len(lst)):
        lst_r.append(lst[i][0])
    lst_r.sort()
    lst.sort()
    lst_res.append(lst_r[0])
    for i in range(len(lst_r)):
        if not (lst[i][1] <= lst_res[-1] <= lst[i][0]):
            lst_res.append(lst_r[i])
    return lst_res


def main():
    n = int(input())    # количество отрезков
    lst = list()    # список отрезков
    for i in range(n):
        l, r = list(map(int, input().split()))
        lst.append([r, l])
    lst = point(lst)
    print(len(lst))
    print(*lst)


if __name__ == "__main__":
    main()

'''
Самое короткое решение, которое я нашел:

segments = sorted([sorted(map(int,input().split())) for i in range(int(input()))], key=lambda x: x[1])
dots = [segments.pop(0)[1]]
for l, r in segments:
    if l > dots[-1]:
        dots.append(r)
print(str(len(dots)) + '\n' + ' '.join(map(str, dots)))
'''
