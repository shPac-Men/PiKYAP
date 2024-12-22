class uravnenie:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None

    def get_coef(self,a,b,c):
        while True:
            
            self.a = float(a)
            self.b = float(b)
            self.c = float(c)
            break


    def discriminant(self):
        return (self.b**2) - 4 * self.a * self.c

    def solve(self):
        roots = set()
        discriminant = self.discriminant()
        if discriminant > 0:
            print(f"Два действительных корня: {(-self.b + discriminant**0.5) / (2 * self.a)}, {(-self.b - discriminant**0.5) / (2 * self.a)}")
            roots.add((-self.b + discriminant**0.5) / (2 * self.a))
            roots.add((-self.b - discriminant**0.5) / (2 * self.a))
        elif discriminant == 0:
            print("Два совпадающих действительных корня: ", -self.b / (2 * self.a))
            roots.add(-self.b / (2 * self.a))
        else:
            print("Два комплексных корня")
        return sorted(roots)

