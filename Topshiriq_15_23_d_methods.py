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


# a_book = Book("Kichkina shahzoda", "Antuan de Sent-Ekzyuperi", 88)
# a_book.open(33)
# a_book.turn_page()
# a_book.turn_page()
# a_book.restart()
# a_book.turn_page()
# a_book.turn_page()


## 6
class Dog:
    total_dogs = 0

    @classmethod
    def __init__(cls):
        Dog.total_dogs += 1

    @classmethod
    def get_total_dogs(cls):
        print(cls.total_dogs)


# dog_1 = Dog()
# dog_2 = Dog()
# dog_3 = Dog()
#
# Dog.get_total_dogs()


## 7
class Computer:
    total_computers = 0
    computers_list = []

    @classmethod
    def add_computer(cls, name_obj):
        cls.total_computers += 1
        cls.computers_list.append(name_obj)


# com = Computer()
# com.add_computer("com_1")
# com.add_computer("com_2")
# com.add_computer("com_3")
#
# print(Computer.total_computers, Computer.computers_list)


## 8
class Employee:
    total_employees = 0
    employees_list = []

    @classmethod
    def hire_employee(cls, emp_name):
        cls.total_employees += 1
        cls.employees_list.append(emp_name)


# emp = Employee()
# emp.hire_employee("John")
# emp.hire_employee("Doe")
# emp.hire_employee("Ali")
#
# print(Employee.total_employees, Employee.employees_list)


## 9
class Television:
    total_televisions = 0
    total_screen_size = 0
    average_screen_size = 0

    @classmethod
    def __init__(cls):
        cls.total_televisions += 1

    @classmethod
    def update_average_screen_size(cls, screen_size):
        cls.total_screen_size += screen_size
        cls.average_screen_size = cls.total_screen_size / cls.total_televisions


# tv_1 = Television()
# tv_1.update_average_screen_size(43)
# tv_2 = Television()
# tv_2.update_average_screen_size(50)
# tv_3 = Television()
# tv_3.update_average_screen_size(60)
#
# print(f"Televizorlar soni: {Television.total_televisions}")
# print(f"O'rtacha ekran: {Television.average_screen_size}")

## 10
class Course:
    total_courses = 0
    courses_list = []

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    @classmethod
    def add_course(cls, kurs):
        cls.courses_list.append(kurs)
        cls.total_courses += 1


course_1 = Course(name="Matematika", desc="Uy ishi: 3-mavzu misollari")
course_2 = Course(name="Tarix", desc="Uy ishi: 12-mavzu takrorlash")

Course.add_course(course_1)
Course.add_course(course_2)


# print("Kurslar soni:", Course.total_courses)
# for course in Course.courses_list:
#     print(f"Kurs nomi: {course.name}, Description: {course.desc}")


## 11
class Math:

    @staticmethod
    def multiply(a, b):
        c = a + b
        return c


# print(Math.multiply(3, 5))


## 12
class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9) / 5 + 32
        return celsius, fahrenheit


celsius, fahrenheit = Temperature.celsius_to_fahrenheit(30)

# print(f"Celsius: {celsius} \nFahrenheit: {fahrenheit}")

## 13
class Distance:

    @staticmethod
    def miles_to_kilometers(miles_1):
        km_1 = miles_1 * 1.609344
        km_1 = round(km_1, 2)

        return miles_1, km_1

miles, km = Distance.miles_to_kilometers(20)

# print(f"Miles: {miles} \nKilometers: {km}")


## 14
class Utility:

    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False

# print(Utility.is_even(5))


## 15
class Time:

    @staticmethod
    def seconds_to_minutes(seconds):
        minutes = seconds // 60
        second = seconds - minutes * 60
        return seconds, minutes, second

seconds_1, minute, sec = Time.seconds_to_minutes(100)

# print(f"Seconds: {seconds_1} is >>> Minutes: {minute} and seconds: {sec}")
