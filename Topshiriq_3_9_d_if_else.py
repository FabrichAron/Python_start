# 1-misol A soni berilgan. Uni musbat yoki manfiy ekanligini aniqlang.
# son = int(input("Sonni kiriting: "))
# if son < 0:
#     print("Kiritilgan son manfiy")
# elif son == 0:
#     print(f"{son} musbat ham manfiy ham emas!")
# else:
#     print("Kiritilgan son musbat")
#
# # 2-misol A soni berilgan. Uni toq yoki juft ekanligni aniqlang.
# son = int(input("Sonni kiriting: "))
# if son % 2 == 0:
#     print("Kiritilgan son juft")
# else:
#     print("Kiritilgan son toq")
#
# # 3-misol A soni berilgan (1-7). Bu son haftaning qaysi kuni ekanligini aniqlang.
# son = int(input("Sonni kiriting: "))
# if son == 1:
#     print("Dushanba")
# elif son == 2:
#     print("Seshanba")
# elif son == 3:
#     print("Chorshanba")
# elif son == 4:
#     print("Payshanba")
# elif son == 5:
#     print("Juma")
# elif son == 6:
#     print("Shanba")
# elif son == 7:
#     print("Yakshanba")
# else:
#     print("Bunday hafta kuni yo'q")
#
# # 4-misol A soni berilgan. A musbat bolsa unga 2 qoshilsin, agar u manfiy bo’lsa unda 2 ayrilsin.
# son = int(input("Sonni kiriting: "))
# if son < 0:
#     son -= 2
#     print(son)
# elif son == 0:
#     print(f"{son} musbat ham manfiy ham emas!")
# else:
#     son += 2
#     print(son)
#
# # 5-misol A va B sonlari berilgan. Bu A > 3 va B <= 6 shartimizga to’g’ri keladimi yoki yoqmi aniqlang.
# son = int(input("Sonni kiriting: "))
# if 3 < son <= 6:
#     print(True)
# else:
#     print(False)
#
# # 6-misol A va B sonlari berilgan. Bu A < 2 va B >= -2 shartimizga to’g’ri keladimi yoki yoqmi aniqlang.
# a = int(input("A sonini kiriting: "))
# b = int(input("B sonini kiriting: "))
# if a < 2 and b >= -2:
#     print(True)
# else:
#     print(False)
#
# # 7-misol A va B sonlari berilgan. Ulardan birinchi katta keyin kichikgini print qiling.
# a = int(input("A sonini kiriting: "))
# b = int(input("B sonini kiriting: "))
# if a < b:
#     print(f'Kattasi {b}, kichigi {a}')
# elif a == b:
#     print("Ikki son teng!")
# else:
#     print(f'Kattasi {a}, kichigi {b}')
#
# # 8-misol A va B sonlari berilgan (float tipida). Ularning qaysi birida qo’ldiq qismi kichik bo’lsa shu sonni aniqlang.
# a = str(float(input("A sonini kiriting: ")))
# b = str(float(input("B sonini kiriting: ")))
# natija_a = a.find(".")
# natija_b = b.find(".")
# kesish_a = a[natija_a + 1::]
# kesish_b = b[natija_b + 1::]
# if kesish_a < kesish_b:
#     print(a)
# if kesish_a == kesish_b:
#     print("Ikki sonning qoldiq qismi teng!")
# else:
#     print(b)
#
# # 9-misol A, B va C sonlari berilgan. A < B < C shartimizga to’g’ri keladimi yoki yo'qmi aniqlang.
# a = int(input("A sonini kiriting: "))
# b = int(input("B sonini kiriting: "))
# c = int(input("C sonini kiriting: "))
# if a < b < c:
#     print(True)
# else:
#     print(False)
#
# # 10-misol A, B va C sonlari berilgan. B soni, A va C ni o’rtasidami yoki yo'q aniqlang.
# a = int(input('A sonini kiriting: '))
# b = int(input('B sonini kiriting: '))
# c = int(input('C sonini kiriting: '))
# if a < b < c:
#     print(True)
# elif c < b < a:
#     print(True)
# else:
#     print(False)
#
# # 11-misol A, B va C sonlari berilgan. Ulardan nechtasi musbat ekanligni aniqlang.
# a = int(input("A sonini kiriting: "))
# b = int(input("B sonini kiriting: "))
# c = int(input("C sonini kiriting: "))
# if a < 0 and b < 0 and c < 0:
#     print("musbat sonlar yo'q")
# elif a >= 0 and b < 0 and c < 0:
#     print("musbat sonlar 1 ta")
# elif a >= 0 and b >= 0 and c < 0:
#     print("musbat sonlar 2 ta")
# elif a >= 0 and b >= 0 and c >= 0:
#     print("musbat sonlar 3 ta")
#
# # 12-misol A, B va C sonlari berilgan. Ulardan ikki eng katta sonlarni yig’indisini aniqlang.
# a = int(input("A sonini kiriting: "))
# b = int(input("B sonini kiriting: "))
# c = int(input("C sonini kiriting: "))
# if a > b > c or b > a > c:
#     print(a + b)
# elif a > c > b or c > a > b:
#     print(a + c)
# elif b > c > a or c > b > a:
#     print(b + c)
#
# # 14-misol A va B sonlari berilgan. A va B ni , yani ikkalasi ham tog’ sonlar ekanligini aniqlang.
# a = int(input("A sonini kiriting: "))
# b = int(input("B sonini kiriting: "))
# if a % 2 == 1 and b % 2 == 1:
#     print(True)
# else:
#     print(False)
#
# # 15-misol A va B sonlari berilgan. A yoki B ni toq son ekanligini aniqlang.
# a = int(input("A sonini kiriting: "))
# b = int(input("B sonini kiriting: "))
# qoldiq_a = a % 2
# qoldiq_b = b % 2
# if qoldiq_a == 1 and qoldiq_b == 1:
#     print("A va B sonlar toq")
# elif qoldiq_a == 1 and qoldiq_b == 0:
#     print("Faqat A son toq")
# elif qoldiq_a == 0 and qoldiq_b == 1:
#     print("Faqat B son toq")
# elif qoldiq_a == 0 and qoldiq_b == 0:
#     print("A va B sonlar toq emas")
#
# # 16-misol A, B va C sonlari berilgan. A, B va C sonlarini musbatmi shuni aniqlang.
# a = int(input("A sonini kiriting: "))
# b = int(input("B sonini kiriting: "))
# c = int(input("C sonini kiriting: "))
# if a >= 0 and b >= 0 and c >= 0:
#     print("A, B va C sonlar musbat")
# else:
#     print("Musbat emas")
#
# # 17-misol A soni berilgan. Uni juft va 2 xonalik son ekanligni aniqlang.
# a = int(input("A sonini kiriting: "))
# if a % 2 == 0 and 10 <= a < 100:
#     print(f"{a} - juft ikki xonali son")
# elif a % 2 == 0:
#     print(f"{a} - juft son ammo ikki xonali son emas")
# else:
#     print("Juft emas ")
#
# # 18-misol A soni berilgan. Uni toq va 3 xonali son ekanligini aniqlang.
# a = int(input("A sonini kiriting: "))
# if a % 2 == 1 and 100 <= a < 1000:
#     print(f"{a} - toq uch xonali son")
# elif a % 2 == 1:
#     print(f"{a} - toq son ammo uch xonali son emas")
# else:
#     print("Toq emas ")
#
# # 19-misol Uch xonalik son berilgan. Uning raqamlari bir xil emasligni aniglang.
# son = (input("Sonini kiriting: "))
# first_el = son.count(son[0])
# if first_el == len(son):
#     print("Barcha raqamlari bir xil!")
# else:
#     print("Raqamlari bir xil emas!")
#
# # 20-misol 1-999 ga son berilgan. Uni musbat yoki manfiyligni va nechi xonaligini aniqlang.
# son = str(float(input("Sonini kiriting: ")))
# qidiruv = son.find(".")
# son = int(float(son))
# print(f"{son} soni {qidiruv} xonali son")
#
# # # # # #   Savol: 16 xonali sondan ko'p xonali son kiritilsa faqat 1 qaytaryabdi,
# # # # # #          xonalar sonini qaytara olmayabdi. Nimaga?
#
# # 21-misol Uch xonalik son berilgan. Uning raqamlari o’sish yoki kamayish tartibidami aniqlang.
# #          (Universal kod, sonning xonalar soni ahamiyatsiz.)
# son = (input("Sonini kiriting: "))
# son_num = int(son)
# son_list = list(son)
# son_list.sort()
# x = int("".join(son_list))
# son_list.reverse()
# y = int("".join(son_list))
# if 0 <= son_num < 10:
#     print("Kiritilgan son faqat bitta raqamdan iborat")
# elif son_num == x:
#     print("Kiritilgan son raqamlari o'sish tartibida.")
# elif son_num == y:
#     print("Kiritilgan son raqamlari kamayish tartibida.")
# else:
#     print("Kiritilgan son raqamlari tartibsiz holatda.")
#
# # 22-misol To’rt xonalik son berilgan. Uning raqamlari chapga ham o’ngga ham bi xil o’qilishini aniqlang.
# #          (Universal kod, sonning xonalar soni ahamiyatsiz.)
# son = (input("Sonini kiriting: "))
# son_list = list(son)
# kesish = son_list[-(int(len(son_list) / 2))::]
# kesish.reverse()
# if son_list[:int((len(son_list)) / 2)] == kesish or len(son_list) == 1:
#     print(True)
# else:
#     print(False)
#
# # 23-misol X va Y sonlari berilgan. Bu sonlar koordinata o’qining qaysi chorakgida ekanligni aniqlang.
# x = int(input("x: "))
# y = int(input("y: "))
# if x > 0 and y > 0:
#     print("Nuqta 1 - chorakda joylashgan")
# elif x < 0 < y:
#     print("Nuqta 2 - chorakda joylashgan")
# elif x < 0 and y < 0:
#     print("Nuqta 3 - chorakda joylashgan")
# elif x > 0 > y:
#     print("Nuqta 4 - chorakda joylashgan")
# elif x == 0 and (y < 0 or y > 0):
#     print("Nuqta y o'qida joylashgan")
# elif y == 0 and (x < 0 or x > 0):
#     print("Nuqta x o'qida joylashgan")
#
# # 24-misol  X va Y sonlari berilgan. Ular shaxmat doskasi koordinatalari (X va Y , 1-8 oraliqda).
# #           (1, 1) koordinatani qora katak deb olsak, X va Y qaysi rangdegi katakda joylashgan.
# x = int(input("x: "))
# y = int(input("y: "))
# if 1 <= x <= 8 and 1 <= y <= 8:
#     if (x + y) % 2 == 0:
#         print("Qora katakda")
#     else:
#         print("Oq katakda")
# else:
#     print("x va y 1 dan 8 oralig'ida bo'lsin!")
#
# # 25-misol X1 va Y1, X2 va Y2 sonlari berilgan. Ular 1-8 oraliqda. X1,Y1 va X2,Y2 lar bir xil rangdagi katakdami shuni aniqlang.
# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))
# if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
#     if (x1 + y1) % 2 == 0:
#         if (x2 + y2) % 2 == 0:
#             print("Ikkisi ham qora katakda")
#         else:
#             print("Ikkalasi ham bir xil rangdagi katakda emas!")
#     elif (x2 + y2) % 2 == 1:
#         print("Ikkisi ham oq katakda")
#     else:
#         print("Ikkalasi ham bir xil rangdagi katakda emas!")
# else:
#     print("x1, y1, x2 va y2 lar 1 dan 8 oralig'ida bo'lsin!")
#
# # 26-misol Shoxni yurishini aniqlang.
# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))
# if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
#     if x1 - 1 <= x2 <= x1 + 1 and y1 - 1 <= y2 <= y1 + 1:
#         print("Bora oladi.")
#     else:
#         print("Bora olmaydi.")
# else:
#     print("x1, y1, x2 va y2 lar 1 dan 8 oralig'ida bo'lsin!")
#
# # 27-misol Filni yurishini aniqlang.
# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))
# if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
#     if abs(x1 - y1) == abs(x2 - y2):
#         print("Bora oladi.")
#     else:
#         print("Bora olmaydi.")
# else:
#     print("x1, y1, x2 va y2 lar 1 dan 8 oralig'ida bo'lsin!")
#
# # 28-misol Farzinni yurishini aniqlang.
# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))
# if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
#     if abs(x1 - y1) == abs(x2 - y2) or (x1 == x2 and 1 <= y2 <= 8) or (y1 == y2 and 1 <= x2 <= 8):
#         print("Bora oladi.")
#     else:
#         print("Bora olmaydi.")
# else:
#     print("x1, y1, x2 va y2 lar 1 dan 8 oralig'ida bo'lsin!")
#
# # 29-misol K va N sonlari kiritilgan. N soni (1-7) joylashgan, u 1 yanvaring haftaning qaysi kuni ekanligi.
# #          K soni (1-365) oraliqda va u yilgan kun. K soni qaysi haftaga to’g’ri kelishini aniqlang (Dushanba, …., Yakshanba.)
# n = int(input("N sonini kiriting: "))  # (1-7) oraliqda 1-yanvar hafta kuni raqami
# k = int(input("K sonini kiriting: "))  # (1-365) oraliqda yil kuni
# y = k % 7
# natija = n + y - 1
# natija = natija % 7
# if natija == 1:
#     print("Dushanba")
# elif natija == 2:
#     print("Seshanba")
# elif natija == 3:
#     print("Chorshanba")
# elif natija == 4:
#     print("Payshanba")
# elif natija == 5:
#     print("Juma")
# elif natija == 6:
#     print("Shanba")
# elif natija == 7:
#     print("Yakshanba")
