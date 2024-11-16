# # 1. stringlar ro'yxatini oladigan va ularni uzunligi bo'yicha guruhlaydigan str_counter(strs) funksiya yozing,
# # bunda kalitlar string uzunliklari va qiymatlar shu uzunlikdagi string keladi.
# # M: str_counter(["shaftoli", "olma", "nok" ]) -> {8:"shaftoli", 4: "olma", 3: "nok"}
#
# def str_counter(strs):
#     for i in strs:
#         natija = {len(i): i}
#         javob.update(natija)
#
#
# javob = {}
#
# str_counter(["shaftoli", "olma", "nok", "bodom"])
# print(javob)
#
#
# # 2. Bir xil uzunlikdagi ikkita listni parametr sifatida oladigan, kalitlar birinchi ro'yxatning elementlari va
# # qiymatlar ikkinchi ro'yxatning mos keladigan elementlari bo'lgan dict qaytaradigan merge_list(l1,l2) funksiya yarating.
# # M: list_1 = ["a", "b", "c"]
# #    list_2 = [1, 2, 3]
# #    merge_list(list_1 ,list_2)  -> {"a":1, "b":2, "c":3}
#
# def merge_list(l1, l2):
#     for i in range(int(len(l1))):
#         natija = {l1[i]: l2[i]}
#         javob.update(natija)
#
#
# javob = {}
# list_1 = ["a", "b", "c", "d", "e"]
# list_2 = [1, 2, 3, 4, 6]
# merge_list(list_1, list_2)
# print(javob)
#
#
# # 3. Foydalanuvchilarga kontaktlarni qo‘shish, yangilash, o‘chirish va qidirish
# # imkonini beruvchi dict ga asoslangan telefon kontaktlar ro'yxati dasturini yarating
# # M: contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"}
#
# def create_new_contact(name, number):
#     contacts.setdefault(name, number)
#     return contacts
#
#
# def update_contact(name, number):
#     natija = {name: number}
#     contacts.update(natija)
#     return contacts
#
#
# def delete_contact(name):
#     contacts.pop(name)
#     return contacts
#
#
# contacts = {"Nodir": "+998918602711", "Laziz": "+998908002534", "Jahon": "+998953052537"}
#
# while True:
#     print(f"""
#             -->  NOKIA contacts  <--
#                  1 -> Qidirish
#                  2 -> Qo'shish
#                  3 -> O'zgartirish
#                  4 -> O'chirish
#                  5 -> Ro'yxat
#                  6 -> Chiqish
# """)
#     ask = input("--> ")
#     if ask == "1":
#         find = input("Ism: ")
#         javob = contacts.get(find)
#         print(f"""        => {find}: {javob}""")
#
#     elif ask == "2":
#         ism = input("Ismi: ")
#         nomer = input("No'meri: ")
#         numbers = create_new_contact(ism, nomer)
#         print("Qo'shildi!")
#
#     elif ask == "3":
#         ism = input("Ismi: ")
#         nomer = input("No'meri: ")
#         update_contact(ism, nomer)
#         print("Yangilandi!")
#
#     elif ask == "4":
#         ism = input("Ismi: ")
#         delete_contact(ism)
#         print("O'chirildi!")
#
#     elif ask == "5":
#         n = 0
#         for k, v in contacts.items():
#             n += 1
#             print(f'''       {n}.{k}: {v}''')
#
#     elif ask == "6":
#         break
#
#     else:
#         print("Only choose => 1, 2, 3, 4, 5, 6")
#         continue

# # 4. Raqamlar ro'yxatini oladigan va ro'yxatdagi har bir raqamning takrorlanish sonini o'z ichiga
# # olgan dict qaytaradigan counter_dict(nums) nomli funksiya yozing.
# # M: counter_dict([2,1,1,1) -> {2:1, 1:3} Chunki listda 1ta 2 va 3ta 1bor.
#
# from collections import Counter
#
# arr = [1, 1, 1, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5]
# counter = Counter(arr)
# print(counter)
#
#
# # 5. Ballar dict ni(kalit = talaba nomi, qiymat = ball) parametr sifatida oladigan va eng yaxshi ikkita
# # o'quvchining ismlari ro'yxatini qaytaradigan max_ball_students(talabalar) funksiya yozing.
# # max_ball_students({"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80 }) -> {"Zafar":80, "Nodir":76}
#
# def max_ball_students(talabalar, talabalar2):
#     mv1 = max(talabalar.values())
#     for k, v in talabalar.items():
#         if v == mv1:
#             javob1 = {k: v}
#             natija.update(javob1)
#             talabalar2.pop(k)
#     mv2 = max(talabalar2.values())
#     for k, v in talabalar2.items():
#         if v == mv2:
#             javob2 = {k: v}
#             natija.update(javob2)
#     return natija
#
#
# natija = {}
# royxat1 = {"Akmal": 64, "Botir": 91, "Tohir": 55, "Nodir": 76, "Zafar": 80}
# royxat2 = royxat1.copy()
#
# print(max_ball_students(royxat1, royxat2))
