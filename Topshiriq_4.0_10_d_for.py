# # 1-misol K va N soni berilgan (N > 0). K sonini N marta print qiling.
# K = int(input("K soni:"))
# N = int(input("N soni:"))
# if N > 0:
#     for i in range(N):
#         print(K)
# else:
#     print("Iltimos, N ga noldan katta son kiriting")
#
# # 2-misol 1 dan n gacha bo`lgan toq sonlar yig`indisini toping.
# n = int(input("n soni: "))
# son = 0
# for i in range(n + 1):
#     if i % 2 == 1:
#         son += i
# print(son)
#
# # 3-misol 1 dan n gacha bo`lgan 3 ga bo`linadigan lekin 9 ga bo`linmidigan sonlar yig`indisini toping.
# n = int(input("n soni: "))
# son = 0
# for i in range(n + 1):
#     if i % 3 == 0 and i % 9 != 0:
#         son += i
# print(son)
#
# # 4-misol 1 dan n gacha bo`lgan sonlarni kvadratlari yig`indisini toping.
# n = int(input("n soni: "))
# son = 0
# for i in range(n + 1):
#     son = i ** 2 + son
# print(son)
#
# # 5-misol So'z kiritaman. Undan keyin 1 dan – so'zni uzunligigacha bo'lgan son kiritishimni so'rasin. Kiritilgan sonni
# #         tartibidagi harifni so'zdan olib tashlasin.
# word = input("So'z kiriting: ")
# son = int(input(f"1 dan {len(word)} gacha sonlardan birini kiriting: "))
# tartib = []
# for i in word:
#     if i == word[son - 1]:
#         continue
#     tartib.append(i)
# x = "".join(tartib)
# print(x)
#
# # 6-misol agar online magazindan kiyim olsangiz va butun narx 100000 dan ko`p bo`lsa sizga 10% skidka qilib bersin.
# #         agar 50000 dan ko`p bo`lsa sizga 5% skidka qilib bersin. agar undan kam bo`lsa o`zini narxida bersin.
# Umumiy_narx = int(input("Umumiy narxni kiriting: "))
# if Umumiy_narx >= 100000:
#     print(f"Siz 10 % li aksiya ishtirokchisisiz, umumiy to'lovingiz {Umumiy_narx * 0.9} so'm")
# elif 50000 <= Umumiy_narx < 100000:
#     print(f"Siz 5 % li aksiya ishtirokchisisiz, umumiy to'lovingiz {Umumiy_narx * 0.95} so'm")
# else:
#     print(f"Sizning umumiy to'lovingiz {Umumiy_narx} so'm")
#
# # 7-misol Sonlar berilgan A va B (A < B). A va B oraligida joylashgan sonlarni kamayish tartibida print qilin (A va B)
# #         shu oraliqqa kirmasin. Shu sonlarni sonini (uzunligini) print qiling.
# A = int(input("A soni: "))
# B = int(input("B soni: "))
# sonlar = []
# if A < B:
#     for i in range(A + 1, B):
#         sonlar.append(str(i))
#     sonlar.reverse()
#     x = " ".join(sonlar)
#     print(f"Oraliqdagi sonlar: {x}")
#     print(f"Sonlar uzunligi {len(sonlar)} ta")
# else:
#     print("A sonini B dan kichkina kiriting.")
#
# # 8-misol Son berilgan – u 1 kg konfetni narxi. 1, 2, ….. , 10 kg uchun narxni print qiling.
# narx = int(input("1 kg konfetning narxi: "))
# for i in range(1, 11):
#     print(f"{i} kg konfet narxi {i * narx} so'm")
#
# # 9-misol Son berilgan – u 1 kg konfet narxi . 0.1, 0.2, …. , 1 kg uchun narxni print qiling.
# narx = int(input("1 kg konfetning narxi: "))
# for i in range(1, 11):
#     print(f"{i / 10} kg konfet narxi {i * narx * 0.1} so'm")
#
# # 10-misol Butun sonlar berilgan A va B (A < B). A va B oralig’idagi butun sonlar kvadratini va ularning yig’indisini
# #          print qiling. A va B ham bu oraliqga kirsin. Masalan: 1, 2, 3 -> 1, 4, 9 -> 14
# A = int(input("A soni: "))
# B = int(input("B soni: "))
# sonlar = []
# son_kvadrat = []
# jamlanma = 0
# if A < B:
#     for i in range(A, B + 1):
#         son_kvadrat.append(str(i ** 2))
#         sonlar.append(str(i))
#         jamlanma = (jamlanma + (i ** 2))
#     x = ", ".join(sonlar)
#     y = ", ".join(son_kvadrat)
#     print(f"{x} -> {y} -> {jamlanma}")
# else:
#     print("A sonini B dan kichkina kiriting.")
#
# # 11-misol Butun son berilgan A va N (N >0). Sikldan foydalangan holda A ni 1 – N bolgan darajasini print qililar
# A = int(input("A soni: "))
# N = int(input("N soni: "))
# son = 1
# if N > 0:
#     for i in range(1, N + 1):
#         son = son * A
#     print(son)
# else:
#     print("Iltimos, N ga noldan katta son yozing")
#
# # 12-misol Butun son berilgan N (N > 0). 1 – N gacha bo'lgan sonlar ko'paytmasini toping.
# N = int(input("N soni: "))
# son = 1
# if N > 0:
#     for i in range(1, N + 1):
#         son = son * i
#     print(son)
# else:
#     print("Iltimos, N ga noldan katta son kiriting.")
