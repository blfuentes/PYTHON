class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self, otherFraction):
        newNum = self.num*otherFraction.den + self.den*otherFraction.num
        newDen = self.den * otherFraction.den
        common = self.gcd(newNum, newDen)
        return Fraction(newNum//common, newDen//common)

    def __eq__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den
        return firstNum == secondNum

    def __mul__(self, other):
        newNum = self.num*other.num
        newDen = self.den*other.den
        common = self.gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)
        
    def __truediv__(self, other):
        newNum = self.num*other.den
        newDen = self.den*other.num
        common = self.gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)
    
    def __sub__(self, other):
        newNum = self.num * other.den - self.den * other.num
        newDen = self.den * other.den
        common = self.gcd(newNum, newDen)
        return Fraction(newNum //common, newDen //common)
        
    def __lt__(self, other):
        return (self.num/self.den) < (other.num/other.den)

    def __gt__(self, other):
        return (self.num/self.den) > (other.num/other.den)
    
    @staticmethod
    def gcd(m, n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n
