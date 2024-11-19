# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def yuza(self):
#         return math.pi * self.radius ** 2
#
#     @property
#     def perimetr(self):
#         return 2 * math.pi * self.radius
#
#
# aylana = Circle(radius=5)
#
# print(aylana.yuza)  # 78.53981633974483
# print(aylana.perimetr) # 31.41592653589793
#
#
#


# class Shopping:
#     def __init__(self, basket, buyer):
#         self.basket = list(basket)
#         self.buyer = buyer
#
#     def __len__(self):
#         print('Redefine length')
#         count = len(self.basket)
#         # count total items in a different way
#         # pair of shoes and shir+pant
#         return count * 2
#
# shopping = Shopping(['Shoes', 'dress'], 'Jessa')
# print(len(shopping))
#
#
#


# class Person:
#     origin_country = "USA"
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def speak(self, words):
#         print(f"{self.name} speaks: {words}")
#
#
# class Employee(Person):
#     def __init__(self, name, age, gender, salary, job_title):
#         super().__init__(name, age, gender)
#         self.salary = salary
#         self.job_title = job_title
#
#     def display_info(self, a):
#         print(f"Employee {self.name} works {a} as a {self.job_title}")
#
#
# Employee(1, 2, 3, 4, 5).display_info(36666)
#
#
#


# t = 'abc'
# d = {'sep': '-', 'end': '?'}
# print(*t, **d)
