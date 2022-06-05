from icecream import ic


def Merge(arr_1, arr_2):
    '''Сливает 2 упорядоченных массива'''
    ind_1, ind_2 = 0, 0
    new_arr = list()
    while ind_1 < len(arr_1) and ind_2 < len(arr_2):
        if arr_1[ind_1] <= arr_2[ind_2]:
            new_arr.append(arr_1[ind_1])
            ind_1 += 1
        else:
            new_arr.append(arr_2[ind_2])
            ind_2 += 1
    ic(ind_1, ind_2)
    ic(new_arr)
    while ind_1 < len(arr_1):
        new_arr.append(arr_1[ind_1])
        ind_1 += 1
    while ind_2 < len(arr_2):
        new_arr.append(arr_2[ind_2])
        ind_2 += 1
    ic(new_arr)
    return new_arr


def MergeSort(arr):
    '''Сортировка слиянием'''
    q = [[x] for x in arr]
    ic(q)
    while len(q) > 1:
        q.append(Merge(q[0], q[1]))
        del q[0], q[0]
        ic(q)
    return q[0]


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    ic(n)
    ic(arr)
    ic(MergeSort(arr))


if __name__ == "__main__":
    main()
