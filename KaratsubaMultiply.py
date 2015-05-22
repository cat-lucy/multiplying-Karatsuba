import itertools


class KaratsubaMultiply:
    def __init__(self):
        self.n1 = -1
        self.n2 = -1
        self.num = []

    def multiply(self, a, b):
        if abs(a) < 10 or abs(b) < 10:
            return a * b
        if self.breaking(a, b, self.check_bit):
            return 0
        x = [0, 0, 0, 0]
        k = 0
        for i in itertools.starmap(self.multiply,
                                   [(self.num[0], self.num[2]), (self.num[0], self.num[3]), (self.num[1], self.num[2]),
                                    (self.num[1], self.num[3])]):
            x[k] = i
            k += 1
        return (x[0] << (int(self.n1 / 2) + int(self.n2 / 2))) + (x[1] << int(self.n1 / 2)) + (
            x[2] << int(self.n2 / 2)) + x[3]

    def breaking(self, a, b, func):
        if func(a, b):
            return True
        a1 = a >> int(self.n1 / 2)
        a2 = a - (a1 << int(self.n1 / 2))
        b1 = b >> int(self.n2 / 2)
        b2 = b - (b1 << int(self.n2 / 2))
        self.num = [a1, a2, b1, b2]
        return False

    def check_bit(self, a, b):
        self.n1 = -1
        self.n2 = -1
        at = abs(a)
        while at > 0:
            self.n1 += 1
            at >>= 1
        bt = abs(b)
        while bt > 0:
            self.n2 += 1
            bt >>= 1
        if self.n1 == 0 or self.n2 == 0:
            return True
        else:
            return False
