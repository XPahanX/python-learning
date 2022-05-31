'''
Первая строка входа содержит число операций 1 ≤ n ≤ 10^5. Каждая из последующих nn строк задают операцию одного из следующих двух типов:

  𝙸𝚗𝚜𝚎𝚛𝚝 x, где 0 ≤ x ≤ 10^9 — целое число;
  𝙴𝚡𝚝𝚛𝚊𝚌𝚝𝙼𝚊𝚡.
  
Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.
'''



import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
            return heapq.heappop(self._queue)[-1]


def main():
    n = int(input())
    pq = PriorityQueue()
    maxs = []
    for _ in range(n):
        command = input()
        if command.startswith('Insert'):
            _, priority = command.split()
            priority = int(priority)
            pq.push(priority, priority)
        else:
            maxs.append(pq.pop())
    for m in maxs:
        print(m)

if __name__ == '__main__':
    main()
