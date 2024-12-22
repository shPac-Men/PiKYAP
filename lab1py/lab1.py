class uravnenie:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None

    def get_coef(self):
        while True:
            try:
                self.a = float(input("Введите коэффициент A: "))
                self.b = float(input("Введите коэффициент B: "))
                self.c = float(input("Введите коэффициент C: "))
                break
            except ValueError:
                print("Некорректное значение. Попробуйте еще раз.")

    def discriminant(self):
        return (self.b**2) - 4 * self.a * self.c

    def solve(self):
        discriminant = self.discriminant()
        if discriminant > 0:
            print(f"Два действительных корня: {(-self.b + discriminant**0.5) / (2 * self.a)}, {(-self.b - discriminant**0.5) / (2 * self.a)}")
        elif discriminant == 0:
            print("Два совпадающих действительных корня: ", -self.b / (2 * self.a))
        else:
            print("Два комплексных корня")


def main():
    resh = uravnenie()
    resh.get_coef()
    resh.solve()
    
if __name__ == "__main__":
    main()

