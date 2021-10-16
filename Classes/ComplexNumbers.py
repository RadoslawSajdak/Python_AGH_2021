## Radosław Sajdak

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        print(self.real + self.imag)

    def __add__(self, complex):
        return Complex(self.real + complex.real, self.imag + complex.imag)

    def __sub__(self, complex):
        return Complex(self.real - complex.real, self.imag - complex.imag)

    def __mul__(self, complex):
        return Complex((self.real * complex.real) - (self.imag * complex.imag),
            (self.imag * complex.real) + (self.real * complex.imag))
    
    def __truediv__(self, complex):
        r = (complex.real ** 2 + complex.imag ** 2)
        return Complex((self.real * complex.real - self.imag * complex.imag) / r,
            (self.imag * complex.real + self.real * complex.imag) / r)

a = Complex(3, 8j)
b = Complex(1, 3j)

print("Results:")
a + b
a - b
a * b
a / b