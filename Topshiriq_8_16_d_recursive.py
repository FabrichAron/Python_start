# def quick_sort(lst):
#     if len(lst) <= 1:
#         return lst
#     else:
#         pivot = lst[0]
#         left = [x for x in lst[1:] if x <= pivot]
#         right = [x for x in lst[1:] if x > pivot]
#         return quick_sort(left) + [pivot] + quick_sort(right)
#
#
# print(quick_sort([4, 7, 1, 9, 2, 5, 6, 3]))

# def fibonacci(n, cache={}):
#     if n in cache:
#         return cache[n]
#     if n == 0:
#         result = 0
#     elif n == 1:
#         result = 1
#     else:
#         result = fibonacci(n - 1) + fibonacci(n - 2)
#     cache[n] = result
#     return result
#
# print(fibonacci(999))


# def fibonacci1(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci1(n - 1) + fibonacci1(n - 2)
#
#
# print(fibonacci1(40))


# def hanoi(a, fr, tr, ar):
#     # Agar siz faqat bitta haydovchini ko'chirish kerak bo'lsa
#     if a == 1:
#         # 1 diskni ko'chirish uchun chop etish
#         print(f"1 diskni {fr} qatordan {tr} qatorga qo'ying")
#         return  # Rekursiyani tugatish
#
#     # Oraliq sifatida tr dan foydalanib (a-1) disklarni fr minorasidan ar minorasiga o'tkazamiz
#     hanoi(a - 1, fr, ar, tr)
#
#     # Qolgan eng katta diskni minoradan tr minorasiga o'tkazamiz
#     print(f"{a} diskni {fr} qatordan {tr} qatorga qo'ying")
#
#     # Oraliq sifatida fr dan foydalanib, (a-1) disklarni ar minorasidan tr minorasiga o'tkazamiz
#     hanoi(a - 1, ar, tr, fr)
#
#
# # Disklar sonini kiritish
# a = int(input("Disklar sonini kiriting: "))
#
# # Biz A, B, C disklari va minoralari uchun Xanoi algoritmini ishga tushiramiz
# hanoi(a, 'A', 'B', 'C')
