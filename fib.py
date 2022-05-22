'''
Даны целые числа 1 <= n <= 10^18 и 2 <= m <= 10^5,
необходимо найти остаток от деления n-го числа Фибоначчи на m.

P.S. Решал сам, код естественно можно упростить и сделать короче, но все тесты прошел.
'''


def fib_mod(n, m):
    Fn_1, Fn_2 = 1, 0
    i = 0
    f = True
    lst = list()
    while (f):
        if i == 0:
            lst.append(0 % m)
        elif i == 1:
            lst.append(1 % m)
        else:
            Fn = Fn_1 + Fn_2
            Fn_2, Fn_1 = Fn_1, Fn
            lst.append(Fn % m)
        if lst[i] == 1 and lst[i - 1] == 0 and i > 1:
            f = False
        i += 1
    lst = lst[slice(i - 2)]
    return lst[n % (i - 2)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()

'''
  Самое короткое решение, которое я смог найти:
  
  n,m=map(int,input().split())
  o,i=[0,1],2
  while not (o[i-2]==0 and o[i-1]==1) or i<=2:
	  o.append((o[i-2]+o[i-1])%m)
	  i+=1
  print(o[n%(i-2)])
'''
