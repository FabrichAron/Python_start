# # 1. "user_data" funksiyasini elon qilasizlar.
# # Funksiyani 3 ta parametri bor (first_name, last_name, age). Input orqalik ism, familiya va yoshni kiritamiz.
# # va bu bu qiymatlarni "user_data" funksiyasini chaqirib argumentlariga beramiz.
# # "user_data" funksiyasi bu (first_name, last_name, age) o'zgaruvchilarni qiymatini
#
#
# #   Ism: Alisher
# #   Familiya: Olimov
# #   Yosh: 27
#
# # ko'rinishiga print qilib bersin.
#
# def user_data(first_name, last_name, age):
#     print(f"""
#             Ism: {first_name}
#             Familiya: {last_name}
#             Yosh: {age}
# """)
#
#
# ism = input("Ism: ")
# familiya = input("Familiya: ")
# yosh = input("Yosh: ")
#
# user_data(ism, familiya, yosh)
#
#
# # 2. "find_max" funksiyasini elon qilasizlar.
# # Funksiyani 3 ta parametri bor (a, b, c). Input orqalik 3 ta son kiritamiz. va bu sonlarni "find_max" funksiyasi
# # chaqirib argumentlariga beramiz. "find_max" funksiyasini bu (a, b, c) o'zgaruvchilardan eng kattasini
# # topib print qiladi.
#
# # Eng katta son - A = 10
# # yoki
# # Eng katta son - A va B = 10
# # yoki
# # Eng katta son - A va B va C = 10
#
# def find_max(a, b, c):
#     if a == b == c:
#         print(f"Eng katta son A va B va C - {a}")
#     elif a == b != c and c < a:
#         print(f"Eng katta son A va B - {a}")
#     elif a == c != b and b < a:
#         print(f"Eng katta son A va C - {a}")
#     elif b == c != a and a < b:
#         print(f"Eng katta son B va C - {b}")
#     else:
#         if b < a and c < a:
#             print(f"Eng katta son A - {a}")
#         elif a < b and c < b:
#             print(f"Eng katta son B - {b}")
#         else:
#             print(f"Eng katta son C - {c}")
#
#
# A = int(input("A = "))
# B = int(input("B = "))
# C = int(input("C = "))
# find_max(A, B, C)
#
#
# # 3. "find_letter_count" funksiyasini elon qilasizlar.
# # Funksiyani 2 ta parametri bor (word, letter). Input orqalik so'z kiritamiz, keyin esa shu so'zda qidirmoqchi
# # bolgan so'zimizni kiritamiz. va bu qiymatlarni "find_letter_count" funksiyasini chaqirib argumentlariga beramiz.
# # "find_letter_count" funksiyasi bu (word, letter) o'garuvchilardan foydalanib "word" da "letter" nechi martda
# # qatnashganini print qilsin.
#
# # "Programing" so'zida "r" dan 2 ta.
#
# def find_letter_count(word, letter):
#     return word.count(letter)
#
#
# javob = find_letter_count("banan", "a")
# print(javob)
#
#
# # 4. "list_sum" funksiyasi elon qilasizlar.
# # Funksiyani 1 ta pametrni bor (myList). "myList" funksiyasini chaqirib unda argumentini berasizlar. uni ichida esa
# # myList elementlarini yig'indisini print qilasizlar.
#
# # Listning elementlar yig'indisi = 32
#
# def work_with_list(a):
#     m = min(a)
#     for i in range(len(a)):
#         a[i] *= m
#     return a
#
#
# print(work_with_list([2, 4, 3]))
#
#
# # 5. daraja(a, b) - bu funksiya a ni b darajasini print qilsin.
#
# def daraja(a, b):
#     print(a ** b)
#
#
# A = int(input("Son kiriting: "))
# B = int(input("Darajani kiriting: "))
# daraja(A, B)
#
#
# # 6. daraja4(a, b, c, d) - bu funksiya a ni b, c va d chi darajasini print qilsin.
#
# def daraja4(a, b, c, d):
#     print(f"b darajasi -> {a ** b}")
#     print(f"c darajasi -> {a ** c}")
#     print(f"d darajasi -> {a ** d}")
#
#
# A = int(input("Son kiriting: "))
# B = int(input("b darajani kiriting: "))
# C = int(input("c darajani kiriting: "))
# D = int(input("d darajani kiriting: "))
# daraja4(A, B, C, D)
#
# # 7. digit_count_and_sum(word) - bu funksiya "word" ni ichidagi raqamni aniqlab ularni yig'indisini va nechtaligini
# # print qilsin.
#
# son = input("Son kiriting: ")
#
#
# def digit_count_and_sum(word):
#     natija = 0
#     for i in word:
#         a = int(i)
#         natija += a
#     return word.isdigit(), len(word), natija
#
#
# print(digit_count_and_sum(son))
#
#
# # 8. add_right(a, b) - bu funksiya a sonini o'ng tomoniga b sonini birlashtirib qo'ysin va print qilsin.
#
# def add_right(a, b):
#     a += b
#     print(a)
#
#
# A = input("a darajani kiriting: ")
# B = input("b darajani kiriting: ")
#
# add_right(A, B)
#
#
# # 9. add_left(a, b) - bu funksiya a sonini chap tomoniga b sonini birlashtirib qoysin va print qilsin.
#
# def add_left(a, b):
#     b += a
#     print(b)
#
#
# A = input("a darajani kiriting: ")
# B = input("b darajani kiriting: ")
#
# add_left(A, B)
#
#
# # 10. work_with_list(a) - bu funksiya a listdan eng kichik sonni topib list elementlariga ko'paytirib qiymatini
# # o'zgartiradi va listni print qilsin.
#
# def work_with_list(a):
#     b = []
#     y = min(a)
#     for i in a:
#         b.append(i * y)
#     print(b)
#
#
# sonlar = [2, 3, 4, 6, 7, 8, 10, 13]
#
# work_with_list(sonlar)

# # 11. big_sales(sales) funksiyasini yarating.
# # sales bu dictionary:
# # {
# #   "yanvar": 12000,
# #   "mart": 6000,
# #   "aprel": 15000,
# #   "sentabr": 9000,
# #   "dekabr": 10000,
# # }

# def big_sales(sales):
#     mk = None
#     mv = list(sales.values())[0]
#     for k, v in sales.items():
#         if v > mv:
#             mv = v
#             mk = k
#     return mk
#
#
# print(big_sales({
#     "yanvar": 12000,
#     "mart": 16000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 19000,
# }))

# # 12. min_max(numbers, max_num, min_num) max_num numbers ichigagi eng katta sonmi yoki yoqmi shuni aniqlang,
# # min_num numbers ichigagi eng kichik sonmi yoki yoqmi shuni aniqlang.

# import random
#
#
# def min_max(numbers, max_num, min_num):
#     if max(numbers) == max_num and min(numbers) == min_num:
#         print(f"{max_num} ro'yxatdagi eng katta son. {min_num} ro'yxatdagi eng kichik son.")
#     elif max(numbers) == max_num:
#         print(f"{max_num} ro'yxatdagi eng katta son. {min_num} ro'yxatdagi eng kichik son emas.")
#     elif min(numbers) == min_num:
#         print(f"{max_num} ro'yxatdagi eng katta son emas. {min_num} ro'yxatdagi eng kichik son.")
#     elif max(numbers) != max_num and min(numbers) != min_num:
#         print(f"{max_num} ro'yxatdagi eng katta son emas. {min_num} ro'yxatdagi eng kichik son emas.")
#
#
# sonlar = [2, 3, 4, 6, 7, 8, 10, 13, 15, 17, 21]
#
# num_random_max = random.choice(sonlar)
# num_random_min = random.choice(sonlar)
# min_max(sonlar, num_random_max, num_random_min)

# # 13. expensiveProduct(products) - funksiyadagi products - list.
# # Unga products sifatida [
# #   {
# #     "name": "Iphone X",
# #     "price": 600
# #   },
# #   {
# #     "name": "Iphone 12",
# #     "price": 1500
# #   },
# #   {
# #     "name": "Samsung Note 9",
# #     "price": 800
# #   },
# #   {
# #     "name": "Samsung S10",
# #     "price": 1100
# #   },
# # ] shunaqa qiymat beriladi.
# # Eng qimmat telefon nomini print qilib bersin bu funksiya.

# def expensive_product(products):
#     mk = products[0]["name"]
#     mv = products[0]["price"]
#     for i in products:
#         if i["price"] > mv:
#             mv = i["price"]
#             mk = i["name"]
#     return mk
#
#
# print(expensive_product([
#     {
#         "name": "Iphone X",
#         "price": 900
#     },
#     {
#         "name": "Samsung Note 9",
#         "price": 800
#     },
#     {
#         "name": "Iphone 12",
#         "price": 1500
#     },
#     {
#         "name": "Samsung S10",
#         "price": 1200
#     },
# ]))
