import itertools


class KaratsubaMultiply:
    def __init__(self):
        self.n = [0, 0]
        self.num = []

    def multiply(self, a, b):
        if abs(a) < 10 or abs(b) < 10:
            return a * b
        if self.breaking(a, b):
            return 0
        n1 = self.n[0]
        n2 = self.n[1]
        num = self.num
        [num[0], num[1], num[2], num[3]] = itertools.starmap(self.multiply,
                                                             [(num[0], num[2]), (num[0], num[3]), (num[1], num[2]),
                                                              (num[1], num[3])])
        return ((num[0] << (int(n1 / 2) + int(n2 / 2))) + (num[1] << int(n1 / 2)) + (
            num[2] << int(n2 / 2)) + num[3])

    def breaking(self, a, b):
        if self.check_bit(a, b):
            return True
        n1div = int(self.n[0] / 2)
        n2div = int(self.n[1] / 2)
        a1 = a >> n1div
        a2 = a - (a1 << n1div)
        b1 = b >> n2div
        b2 = b - (b1 << n2div)
        self.num = [a1, a2, b1, b2]
        return False

    def check_bit(self, a, b):
        def f(num):
            if num > 0:
                num >>= 1
                return 1 + f(num)
            else:
                return 0

        [at, bt] = map(abs, [a, b])
        [self.n[0], self.n[1]] = map(f, [at, bt])
        return self.n[0] == 0 or self.n[1] == 0
