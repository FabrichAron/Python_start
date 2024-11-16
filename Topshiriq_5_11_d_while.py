# # 1. While siklidan foydalanib print qiling. N soniga chegarani kiriting:
# # 1
# # 22
# # 333
# # 4444
# # 55555
#
# n = int(input("N sonini kiriting: "))
# son = []
# a = 0
# b = 0
# while a < n:
#     b = 0
#     a += 1
#     son.clear()
#     while b < a:
#         b += 1
#         son.append(str(a))
#         if len(son) == a:
#             x = "".join(son)
#             print(x)
#
# # 2. While dan foydalanib sondagi raqamlar yig'indisini topadigan dastur tuzing.
# # input: 555   output: 15
# # input: 8125   output: 16
#
# son = (input("Son kiriting: "))
# x = list(son)
# n = 0
# a = 0
# while a < len(x):
#     m = int(x[a])
#     n += m
#     a += 1
# print(n)
#
# # 3. While orqali 1 dan 100 gacha bo'lgan toq solar yig'indisini topuvchi dastur tuzing
# son = int(input("Son kiriting: "))
# x = 0
# a = 0
# while x < son:
#     x += 1
#     if x % 2 == 1:
#         a += x
# print(a)
#
# # 4. While orrqali Ro'yxatdagi 2-eng katta sonni topuvchi dastur yozing
# tartib = [5, 3, 22, 10, 8, 61, 4, 3, 11, 1, 9, 7]
# son = 0
# a = 0
# while son < len(tartib):
#     if tartib[son] > a:
#         a = tartib[son]
#     son += 1
# tartib.remove(a)
# son = 0
# a = 0
# while son < len(tartib):
#     if tartib[son] > a:
#         a = tartib[son]
#     son += 1
# print(a)
#
# # 5. Taxmin qilish o'yinini simulyatsiya qiladigan dastur yarating.
# # Dastur 1 dan 100 gacha bo'lgan tasodifiy sonni yaratishi va
# # foydalanuvchidan raqamni taxmin qilishni so'rashi kerak.
# # Agar foydalanuvchi taxmini haqiqiy raqamdan yuqori bo'lsa, dastur "Juda baland!" va
# # foydalanuvchidan yana taxmin qilishni so'rang. Xuddi shunday, agar foydalanuvchining
# # taxmini haqiqiy raqamdan past bo'lsa, dastur "Juda past!" va foydalanuvchidan yana taxmin
# # qilishni so'rang. Dastur foydalanuvchidan to'g'ri raqamni topmaguncha taxmin qilishni so'rashi kerak.
#
# import random
#
# x = []
# a = 1
# while a < 101:
#     x.append(a)
#     a += 1
# print(x)
# taxmin = random.choice(x)
# while True:
#     son = int(input("1 dan 100 oralig'idagi sonni toping!: "))
#     if son > taxmin:
#         print("Juda baland")
#     elif son < taxmin:
#         print("Juda past")
#     elif son == taxmin:
#         print("To'g'ri topdingiz! tamom")
#         break
