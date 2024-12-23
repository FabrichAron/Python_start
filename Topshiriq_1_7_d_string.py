# 1 capitalize # Matinni faqat 1-so'zining 1-harfini katta qolgan barcha harf va zo'zlarni kichik harf qilib qaytaradi.
test_matn = "saloM dunyo"
natija = test_matn.capitalize()
print("1:", natija)

# 2 casefold # Matinni barcha harfini kichik qilib qaytaradi.
test_matn = "SaLom DunYo"
natija = test_matn.casefold()
print("2:", natija)

# 3 center # Matinni berilgan oraliqning markaziga joylab qaytaradi.
test_matn = "Salom Dunyo"
natija = test_matn.center(20)
print("3:", natija)

# 4 count # Matindan qidirilgan belgi yoki so'zning nechta borligini sonini qaytaradi.
test_matn = "Salom Dunyo Salom Dunyo Salom Dunyo Salom Dunyo"
natija = test_matn.count("Dun")
print("4:", natija)

# 5 encode # Matindagi noodatiy harflarni enkodga o'girib qaytaradi.
test_matn = "Salom Dûnyo"
natija = test_matn.encode()
print("5:", natija)

# 6 endswith # Matinning oxirida so'ralgan belgi bor yoki yo'qligini qaytaradi.
test_matn = "Salom Dunyo."
natija = test_matn.endswith(".")
print("6:", natija)

# 7 expandtabs # Matindagi 'tab'larning 'size'ini berilgan oraliqda qaytaradi.
test_matn = "S\ta\tl\to\tm\t D\tu\tn\ty\to\t."
natija = test_matn.expandtabs(5)
print("7:", natija)

# 8 find # Matindan qidirilgan belgining indeksini qaytaradi. Qidirilgan belgi yo'q bo'lsa -1 qaytaradi.
test_matn = "Salom Dunyo."
natija = test_matn.find("l", 1, 6)
print("8:", natija)

# 9 rfind # Matindan qidirilgan belgining indeksini qaytaradi, qidiruv o'ng tomondan boshlanadi. Qidirilgan belgi yo'q bo'lsa -1 qaytaradi.
test_matn = "Bir Ikki Uch To'rt Besh Uch"
natija = test_matn.rfind("Uch")
print("9:", natija)

# 10 format
test_matn = "Salom {} Ali"
natija = test_matn.format("do'stim")
print("10:", natija)

# 11 format_map
misol = {'x':1,'y':-2, 'z':3}
matn = '{x} {y} {z}'
natija = matn.format(**misol)
print("11:", natija)

# 12 index
test_matn = "Salom Dunyo."
natija = test_matn.index("Dunyo")
print("12:", natija)

# 13 rindex
test_matn = "Bir Ikki Uch To'rt Besh"
natija = test_matn.rindex("To'rt")
print("13:", natija)

# 14 isalnum
test_matn = "SalomDunyo11"
natija = test_matn.isalnum()
print("14:", natija)

# 15 isalpha
test_matn = "SalomDunyo54"
natija = test_matn.isalpha()
print("15:", natija)

# 16 isascii
test_matn = "SalomDunyo"
natija = test_matn.isascii()
print("16:", natija)

# 17 isdecimal
test_matn = "123411"
natija = test_matn.isdecimal()
print("17:", natija)

# 18 isdigit
test_matn = "123411"
natija = test_matn.isdigit()
print("18:", natija)

# 19 isidentifier
test_matn = "b123411"
natija = test_matn.isidentifier()
print("19:", natija)

# 20 isnumeric
test_matn = "123411"
natija = test_matn.isnumeric()
print("20:", natija)

# 21 isprintable
test_matn = "Salom Dunyo!"
natija = test_matn.isprintable()
print("21:", natija)

# 22 isspace
test_matn = "      "
natija = test_matn.isspace()
print("22:", natija)

# 23 istitle
test_matn = "Salom Dunyo!"
natija = test_matn.istitle()
print("23:", natija)

# 24 isupper
test_matn = "SALOM DUNYO!"
natija = test_matn.isupper()
print("24:", natija)

# 25 join
test_matn = ("Bir", "Ikki", "Uch")
x = " * ".join(test_matn)
print("25:", x)

# 26 ljust
test_matn = "SALOM"
natija = test_matn.ljust(30)
print("26:", natija, "DUNYO!")

# 27 rjust
test_matn = "Salom Dunyo"
natija = test_matn.rjust(25, "*")
print("27:", natija, "!")

# 28 lower
test_matn = "SAlOm dUnYO!"
natija = test_matn.lower()
print("28:", natija)

# 29 islower
test_matn = "salom dunyo 323"
natija = test_matn.islower()
print("29:", natija)

# 30 maketrans
test_matn = "SALOM PUNYO!"
natija = str.maketrans("P", "D")
print("30:", test_matn.translate(natija))

# 31 partition
test_matn = "Bir Ikki Uch To'rt Besh"
natija = test_matn.partition("Uch")
print("31:", natija)

# 32 rpartition
test_matn = "Bir Ikki Uch To'rt Besh"
natija = test_matn.rpartition("Olti")
print("32:", natija)

# 33 replace
test_matn = "Salom Dunyo Salom Dunyo Salom Dunyo!"
natija = test_matn.replace("Dunyo", "Do'stim", 2)
print("33:", natija)

# 34 split
test_matn = "Bir Ikki Uch To'rt Besh"
natija = test_matn.split(" ", 1)
print("34:", natija)

# 35 rsplit
test_matn = "Bir Ikki Uch To'rt Besh"
natija = test_matn.rsplit(' ')
print("35:", natija)

# 36 splitlines
test_matn = "Bir Ikki Uch\nTo'rt Besh"
natija = test_matn.splitlines()
print("36:", natija)

# 37 startswith
test_matn = "Bir Ikki Uch To'rt Besh"
natija = test_matn.startswith("Uch", 9, 15)
print("37:", natija)
# 38 strip
test_matn = "      !!!!.....SALOM....,,,,,!!!!!      "
natija = test_matn.strip("!., ")
print("38:", natija, "DUNYO!")

# 39 rstrip
test_matn = "DUNYO!      ...,,qqp     "
natija = test_matn.rstrip(".,qp ")
print("39:", "SALOM", natija)

# 40 lstrip
test_matn = "     ...,,qqp DUNYO!      "
natija = test_matn.lstrip(".,qp ")
print("40:", "SALOM", natija)

# 41 swapcase
test_matn = "Bir Ikki Uch To'rt Besh"
natija = test_matn.swapcase()
print("41:", natija)

# 42 title
test_matn = "bir ikki uch"
natija = test_matn.title()
print("42:", natija)

# 43 translate
test_matn = {83:  115}
natija = "Hello Sam!"
print("43:", natija.translate(test_matn))

# 44 upper
test_matn = "bir ikki uch"
natija = test_matn.upper()
print("44:", natija)

# 45 zfill
test_matn = "54670"
natija = test_matn.zfill(10)
print("45:", natija)