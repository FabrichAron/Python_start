#     set = To'plam(malumot turi) (yagona unikal qiymatli tartibsiz to'plamni qaytaradi...)
# malumot qo'shish uchun .add() (agar bitta bo'lsa) .update() (agar ko'p bo'lsa)
# set_name = {-4, 'hello', 12, 'try', 'go', 'go', 3, 'foot', -6}
# print(set_name)
# >>> {'try', 'go', 12, 'hello'}
# set_1 = {11, 6, 7, 8, 9, -1, 0, 1, 2, 3, 4, 5, -0.2, 5.6, 9, 8, 11, 6, 7, 0, 3, 3, 3}
# print(set_1)
# >>> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5.6, 11, -0.2, -1}

#     set
#     dictionary
#     list
#     tuple
#[] listning qavisi
#
#
#     Qidirish
# matn ="Maktab ertadan boshlanadi"
# print("Maktab" in matn)
# >>> True
# yoki
# # matn ="Maktab ertadan boshlanadi"
# # print("Maktab" not in matn)
# # >>> False
#
#     for sikli
# for x in "banana":
#     print(x, end="\t")
# >>> b	a	n	a	n	a
#
#     String array
# a = "Hello World!"
# print(a[4])
# >>> o
#
#     index topish
# matn ="Maktab ertadan boshlanadi"
# print(matn.index("e"))
# >>> 7
#
#     string length(uzunlik)
# s = "kitob"
# uzunligi = len(s)
# print(uzunligi)
# >>> 5
# qisqarog'i
# print(len("kitob"))
# >>> 5
#
#     string slice(kesish)
# matn ="Maktab ertadan boshlanadi"
# qism = matn[0:6]
# print(qism)
# >>> Maktab
# yoki
# matn ="Maktab ertadan boshlanadi."
# qism = matn[-11:-1]
# print(qism)
# >>> boshlanadi
# yoki
# matn ="Maktab ertadan boshlanadi."
# qism = matn[-11:-1]
# print(qism)
# >>> boshlanadi
# yoki
# son = '012345678'
# qism = son[:5]
# print(qism)
# >>> 01234
# yoki
# son = '012345678'
# qism = son[2:]
# print(qism)
# >>> 2345678
# yoki
# son = '012345678'
# qism = son[:]
# print(qism)
# >>> 012345678

# Find() bilan Index() string metodlari orasidagi farq shuki Agar find()da yo'q narsani indeksi so'ralsa -1 qaytaradi index()dan so'ralsa xatolik qaytaradi.


# class Solution(object):
#     def equalFrequency(self, word):
#         print(word)
#
#
# Solution().equalFrequency("abcc")


# class Course:
#     # Class-level attributes
#     total_courses = 0
#     courses_list = []
#
#     def __init__(self, name, description):
#         # Instance-level attributes
#         self.name = name
#         self.description = description
#
#     @classmethod
#     def add_course(cls, course):
#         # Adding course instance to courses_list and updating total_courses
#         cls.courses_list.append(course)
#         cls.total_courses += 1
#
#
# # Example usage:
# course1 = Course("Mathematics", "Learn algebra, geometry, and calculus.")
# course2 = Course("Physics", "Understand the fundamentals of motion and energy.")
#
# Course.add_course(course1)
# Course.add_course(course2)
#
# print("Total courses:", Course.total_courses)
# for course in Course.courses_list:
#     print(f"Course Name: {course.name}, Description: {course.description}")

#
# class Television:
#     # Class-level attribute
#     average_screen_size = 0
#     _total_screen_size = 0
#     _total_televisions = 0
#
#     def __init__(self, screen_size):
#         self.screen_size = screen_size
#         Television._total_screen_size += screen_size
#         Television._total_televisions += 1
#         self.update_average_screen_size()
#
#     @classmethod
#     def update_average_screen_size(cls):
#         if cls._total_televisions > 0:
#             cls.average_screen_size = cls._total_screen_size / cls._total_televisions

# Example usage
# tv1 = Television(42)
# print(f"Average Screen Size after tv1: {Television.average_screen_size}")
#
# tv2 = Television(55)
# print(f"Average Screen Size after tv2: {Television.average_screen_size}")
#
# tv3 = Television(65)
# print(f"Average Screen Size after tv3: {Television.average_screen_size}")


# class color:
#    PURPLE = '\033[95m'
#    CYAN = '\033[96m'
#    DARKCYAN = '\033[36m'
#    BLUE = '\033[94m'
#    GREEN = '\033[92m'
#    YELLOW = '\033[93m'
#    RED = '\033[91m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'
#    END = '\033[0m'