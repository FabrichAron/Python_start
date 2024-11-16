# 1 append # Ro'yhatning oxiriga 1 ta berilgan elementni qo'shib ro'yhatni qaytaradi.
avtomobil = ['Tiko', 'Damas', 'Nexia']
avtomobil.append("Matiz")
print("1:", avtomobil)

# 2 clear # Ro'yhatdagi barcha elementlarni o'chirib, bo'sh ro'yhatni qaytaradi.
avtomobil = ['Tiko', 'Damas', 'Nexia']
avtomobil.clear()
print("2:", avtomobil)

# 3 copy # Ro'yhatdan nusxa olib yangi nusxa ro'yhatni qaytaradi.
avtomobil = ['Tiko', 'Damas', 'Nexia']
avto_marka = avtomobil.copy()
print("3:", avto_marka)

# 4 count # Ro'yhatdan qidirilgan elementning sonini qaytaradi.
avtomobil = ['Tiko', 'Damas', 'Tiko', 'Nexia', 'Tiko']
avto_marka = avtomobil.count('Tiko')
print("4:", avto_marka)

# 5 extend # Ro'yhatga boshqa ro'yhatni qo'shib qaytaradi.
avtomobil = ['Tiko', 'Damas', 'Nexia']
uy_hayvon = ['It', 'Mushuk', 'Ot', 'Tovuq']
avtomobil.extend(uy_hayvon)
print("5:", avtomobil)

# 6 index # Ro'yhatdan qidirilgan elementning indeksini qaytaradi u yo'q bo'lsa xatolik qaytaradi.
avtomobil = ['Tiko', 'Damas', 'Nexia']
natija = avtomobil.index("Damas")
print("6:", natija)

# 7 insert # Ro'yhatga qo'shishga berilgan elementni berilgan indeksga qo'shib qaytaradi.
avtomobil = ['Tiko', 'Damas', 'Nexia']
avtomobil.insert(2, "Matiz")
print("7:", avtomobil)

# 8 pop # Ro'yhatdan ko'rsatilgan indexdagi elementni kesib olib ro'yhatni qaytaradi.
avtomobil = ['Tiko', 'Damas', 'Nexia']
avtomobil.pop(1)
print("8:", avtomobil)

# 9 remove # Ro'yhatdan ko'rsatilgan elementni o'chirib tashlab ro'yhatni qaytaradi.
avtomobil = ['Tiko', 'Damas', 'Nexia']
avtomobil.remove('Damas')
print("9:", avtomobil)

# 10 reverse # Ro'yhatni ketma-ketligini teskarisiga o'girib qaytaradi.
avtomobil = ['Tiko', 'Damas', 'Nexia']
avtomobil.reverse()
print("10:", avtomobil)

# 11 sort # Ro'yhatni alifbo tartibida va yoki sonlarni o'sib borish tartibida qaytaradi.
avtomobil = ['Tiko', 'Damas', 'Nexia', 'Audi', 'Tesla', 'BMW', '7', '1', '8', '3', '5', '2']
avtomobil.sort()
print("11:", avtomobil)

my_list = [1, 2, 3, 4, 5]
int_result = int(''.join(map(str, my_list)))
print("Result:", int_result)


# # Dictionary Dict Methods

# # clear()      Lug'atdagi barcha elementlarni o'chirib, bo'sh ro'yhatni qaytaradi.
# # copy()       Lug'atdan nusxa olib yangi nusxa lug'atni qaytaradi.
# # fromkeys()   Ikkita ro'yxat yoki setni bitta lug'at qilib qaytaradi. dict.fromkeys(keys, value)
# # get()        Lug'atdan so'ralgan key ni value sini qaytaradi.
# # items()      Lug'atning key va value sini juftlik qilib qaytaradi.
# # keys()       Lug'atning key larini qaytaradi.
# # pop()        Lug'atdan pop ga berilgan key ni qirqib olib valueni qaytaradi.
# # popitem()    Lug'atdan oxirgi key va valueni kesib olib qaytaradi.
# # setdefault() Lug'atning oxiriga yangi key va value ni qo'shib qaytaradi, agar bor key bo'lsa hech narsa o'zgarmaydi.
# # update()     Lug'atning oxiriga yangi key va value ni qo'shib qaytaradi, agar bor key bo'lsa yangi berilagn value ni qaytaradi.
# # values()     Lug'atdagi value larni qaytaradi.

