class Karatsuba_Multiply:
    def __init__(self):
        self.n1 = -1
        self.n2 = -1
        self.num = []
        
    def check_bit(self, a, b):
        self.n1 = -1
        self.n2 = -1
        at = abs(a)
        while (at > 0):
            self.n1 += 1
            at = at >> 1
        bt = abs(b)
        while (bt > 0):
            self.n2 += 1
            bt = bt >> 1
        if (self.n1 == 0 | self.n2 == 0):
            return True
        else:
            return False
    
    def multiply(self, a, b):
        if (a < 10 or b < 10):
            return a*b
        if (self.breaking(a, b)):
            return 0
        n1 = self.n1
        n2 = self.n2
        a1 = self.num[0]
        a2 = self.num[1]
        b1 = self.num[2]
        b2 = self.num[3]
        x1 = self.multiply(a1, b1)
        x2 = self.multiply(a1, b2)
        x3 = self.multiply(a2, b1)
        x4 = self.multiply(a2, b2)
        return (x1 << (int(n1 / 2) + int(n2 / 2))) + (x2 << int(n1 / 2)) + (x3 << int(n2 / 2)) + x4     
        
    def breaking(self, a, b):
        if (self.check_bit(a, b)):
            return True
        a1 = a >> int(self.n1 / 2)
        a2 = a - (a1 << int(self.n1 / 2))
        b1 = b >> int(self.n2 / 2)
        b2 = b - (b1 << int(self.n2 / 2))
        self.num = [a1, a2, b1, b2]
        return False
