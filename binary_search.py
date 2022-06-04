# from icecream import ic


def BinarySearch(el, arr):
    l, r = 0, len(arr) - 1
    while(l <= r):
        m = (l + r) // 2
        if arr[m] == el:
            return m + 1
        elif arr[m] > el:
            r = m - 1
        else:
            l = m + 1
    return -1
    pass


def main():
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))
    del arr_1[0]
    del arr_2[0]
    # ic(arr_1)
    # ic(arr_2)
    output = ""
    for i in arr_2:
        output += str(BinarySearch(i, arr_1)) + " "
        # ic(output)
    print(output)


if __name__ == "__main__":
    main()
