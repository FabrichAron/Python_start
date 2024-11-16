# a = 4  #global
#
# def f1():
# 	print(a)
#
# def f2():
# 	global a
# 	a+=1
# print(a)
# f2()
# print(a)

# a = 4
# def f1():
# 	global a
# 	a = 5
# 	print(a) # local -> 5
#
# print(a) #global -> 4


# def f(x):
#     d = 2
#     def g(y):
#         return y + x + c + d
#     return g
# a = 5
# b = 1
# c = 3
#
# h=f(a)
# natija = h(b)
# print(natija )  # Output is 1
#
# # yoki
# natija = f(a)(b)
# print(natija )  # Output is 1


# def f(x):
#     z = 2
#
#     def g(y):  # g hali closure emas
#         return z * x + y
#
#     return g
#
#
# a = 5
# b = 1
# h = f(a)  # endi h closure bo'ldi, qaysiki g ga teng bo'lgan.
# h(b) # Output is 11
#
# print(h.__code__.co_freevars)  # ('x', 'z')
# # ularning qiymatlari esa:
# print(h.__closure__[0].cell_contents)  # 5
# print(h.__closure__[1].cell_contents)  # 2


# def compose(g, f):
#     def h(*args, **kwargs): #closure funksiya
#         return g(f(*args, **kwargs))
#     return h
#
# km_to_m= lambda x: x * 1000
# m_to_sm= lambda x: x * 100
#
# km_to_sm = compose(m_to_sm, km_to_m)
# print(km_to_sm(12))   # Output 1 200 000


