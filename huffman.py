import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huff_encode(s):
    h = []
    for c, f in Counter(s).items():
        h.append((f, len(h), Leaf(c)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        f_1, _count1, l = heapq.heappop(h)
        f_2, _count2, r = heapq.heappop(h)
        heapq.heappush(h, (f_1 + f_2, count, Node(l, r)))
        count += 1
    code = {}
    if h:
        [(f, count, root)] = h
        root.walk(code, "")
    return code


def huff_decode(encode, code):
    sx = []
    enc_ch = ""
    for ch in encode:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ""
                break
    return "".join(sx)


def main():
    code = {}
    k, l = map(int, input().split())
    for i in range(k):
        _l, _c = input().split(": ")
        code[_l] = _c
    encode = input()
    f = huff_decode(encode, code)
    print(f)


    # s = input()
    # code = huff_encode(s)
    # encode = "".join(code[ch] for ch in s)
    # print(len(code), len(encode))
    # for ch in sorted(code):
    #     print("{}: {}".format(ch, code[ch]))
    # print(encode)


if __name__ == "__main__":
    main()
