## 1
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

## 2
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

## 3
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = [4, 5]

    def add_grade(self, grade):
        if 0 <= grade <= 5:
            self.grades.append(grade)
            return self.grades
        else:
            print("To'g'ri baho kiriting!")

    def calculate_average(self):
        len_list = len(self.grades)
        sum_list = sum(self.grades)
        if self.grades:
            summary = sum_list / len_list
            return summary
        else:
            print("Ro'yxat bo'sh")

    def print_summary(self):
        print(f"""                    Ismi: {self.name}
                    Yoshi: {self.age}
                    Baholari: {self.grades}
                    O'rtacha bahosi: {Student.calculate_average(self)}""")


# talaba = Student(name="Farrux", age=24)
# talaba.add_grade(grade=2)
# talaba.add_grade(grade=1)
# talaba.print_summary()

## 4
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius > 0:
            p = 3.1415
            answer = p * self.radius ** 2
            return answer

    def circumference(self):
        if self.radius > 0:
            p = 3.1415
            answer = p * self.radius * 2
            return answer

    def diameter(self):
        if self.radius > 0:
            answer = self.radius * 2
            return answer


# print(f"Doira yuzi: {Circle(radius=4).area()}")
# print(f"Doira aylana uzunligi: {Circle(radius=4).circumference()}")
# print(f"Doira diametri: {Circle(radius=4).diameter()}")


## 5
class Book:
    page = 0
    first_page = 1

    def __init__(self, title, author, current_page):
        self.title = title
        self.author = author
        self.current_page = current_page

    def open(self, page_num):
        if 0 < page_num <= self.current_page and page_num == int(page_num):
            print(f"Kitobning {int(page_num)} - sahifasi.")
            self.page = int(page_num)
        else:
            print(f"Kitobni betini to'g'ri kiriting! Kitob {self.current_page} betdan iborat.")

    def turn_page(self):
        print(f"Kitobning {self.page + 1} - sahifasi.")
        self.page += 1

    def restart(self):
        print(f"Kitobning {self.first_page} - sahifasi.")
        self.page = self.first_page


a_book = Book("Kichkina shahzoda", "Antuan de Sent-Ekzyuperi", 88)
a_book.open(33)
a_book.turn_page()
a_book.turn_page()
a_book.restart()
a_book.turn_page()
a_book.turn_page()
