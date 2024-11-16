# def generator_tub():
#     def tub_natija(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     son = 2
#     while True:
#         if tub_natija(son):
#             yield son
#         son += 1
#
#
# gen = generator_tub()
# for _ in range(5):
#     print(next(gen))


# import itertools
# from functools import reduce
#
#
# def password_generator(input_str):
#     for pwd in itertools.permutations(input_str):
#         yield ''.join(pwd)
#
# input_string = input("So'z kiriting: ")
# passwords = password_generator(input_string)
# for _ in range(reduce(lambda x, y: x * y, range(1, len(input_string) + 1))):
#     print(next(passwords))

# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fibonacci = fibonacci_generator()
# for _ in range(10):
#     print(next(fibonacci))

# #
# import itertools
#
#
# def group_generator(lst, n):
#     for group_1 in itertools.combinations(lst, n):
#         yield group_1
#
#
# my_list = [1, 2, 3, 4]
# m = 2
# groups = group_generator(my_list, m)
# for group in groups:
#     print(group)

# # 4. Listdagi elementlarni n tadan guruhlanganda barcha mavjud guruhlarni generatsiya qiladigan generator yarating.

# from functools import reduce  # Reduce ni ishlatishimiz uchun functools dan import qilamiz.
#
#
# def tuple_generator():
#     for i in my_list:  # birinchi sikl: funksiyadan qaytgan natijani birinchi elementni olib beradi.
#         for n in my_list:  # ikkinchi sikl: funksiyadan qaytgan natijani ikkinchi elementni olib beradi.
#             a_b = i, n  # Ikki sikldan olingan natijani bitta o'zgaruvchiga tenglash.
#             a_b_copy = list(a_b).copy()  # Natijani nusxalash
#             a_b_copy.reverse()  # Nusxani teskarisiga yozish
#             if i != n and my_sort.count(
#                     a_b_copy) == 0:  # Agar natijadagi sonlar bir-biriga teng emas va teskarisi o'zidan avval ishlatilmagan bo'lsa.
#                 my_sort.append(list(a_b))  # O'xshash bo'lmagan elementlarni yig'ish uchun ro'yhatga qo'shish.
#                 yield a_b  # Funksiya qaytaradigan natija
#
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Berilagn ro'yhat.
#
# my_sort = []  # O'xshash bo'lmagan elementlarni yig'ish uchun ro'yhat.
# couple = tuple_generator()  # Funksiyadan qaytgan natijani o'zgaruvchiga tenglash.
# for _ in range(reduce(lambda x, y: x + y, range(1, len(my_list)))): # Generator bittalab natijalarni funksiyadan berib turishi uchun ishlatilgan sikl.
#     print(next(couple))  # Natijani consolga chiqarish.

