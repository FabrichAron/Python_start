class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, summa):
        if summa > 0:
            self.balance += summa
            print(f"{summa} so'm depozit qilindi. Yangi balans: {self.balance} so'm")
        else:
            print("Notog'ri depozit summasi.")

    def withdraw(self, summa):
        if 0 < summa <= self.balance:
            self.balance -= summa
            print(f"{summa} so'm yechildi. Qolgan balans: {self.balance} so'm")
        else:
            print("Balans yetarli emas yoki noto'g'ri summa.")

    def check_balance(self):
        print(f"Joriy balans: {self.balance} so'm")


# hisob = BankAccount(100000)
# hisob.check_balance()
# hisob.deposit(50000)
# hisob.withdraw(30000)
# hisob.check_balance()


class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def area(self):
        if self.length > 0 and self.width > 0:
            area_1 = self.width * self.length
            print(f"To'rburchakning yuzi: {area_1}")
        else:
            print("Tomonlar uzunligini to'g'ri kiriting!")

    def perimeter(self):
        if self.length > 0 and self.width > 0:
            perimetr_1 = 2 * (self.width + self.length)
            print(f"To'rburchakning perimetri: {perimetr_1}")
        else:
            print("Tomonlar uzunligini to'g'ri kiriting!")

    def is_square(self):
        if self.length > 0 and self.width > 0:
            if self.length == self.width:
                print("Bu to'rtburchak kvadrat.")
            else:
                print("Bu to'rtburchak kvadrat emas.")
        else:
            print("Tomonlar uzunligini to'g'ri kiriting!")


# Rectangle(4, 5).area()
# Rectangle(4, 5).perimeter()
# Rectangle(4, 5).is_square()
