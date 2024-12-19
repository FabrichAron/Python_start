import json

user = {
    "name": "player_name",
    "pleyed": 1,
    "best_score": 3
},

user_2 = {
    "name": "Ali",
    "pleyed": 1,
    "best_score": 3
}

# Change jsonStr to pyDict
with open("tests.json", "r") as tests_file:
    testsPy = json.load(tests_file)

# Create user
with open("users.json", "w") as users_file:
    json.dump(user, users_file, indent=4)

with open("users.json", "r") as file:
    users = json.load(file)

users.append(user_2)

with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

# print(testsPy[0]["question"])
# print(testsPy[0]["answers"][0])
print("\033[1m" + "\033[95m" + "\"Kim millioner bo'lishni hohlaydi\" o'yiniga hush kelibsiz!")
while True:
    print("\033[96m" + """              Buyruqni tanlang:  \033[0m \033[93m
            1 -> O'yinni boshlash
            2 -> Reyting
            \033[0m \033[91m
            0 -> Dasturdan chiqish""" + "\033[0m")
    go_num = input('\033[92m' + ">>> " + '\033[0m')
    if go_num == "1":
        print("\033[1m" + "\033[95m" + "1" + "\033[0m")
    elif go_num == "2":
        print("2")
    elif go_num == "0":
        break
    else:
        print("      Iltimos, buyruq raqamini to'g'ri kiriting!")

    # player_name = input("O'yinchini ismini kiriting: ")
    # print("O'yinlar soni: 0")
    # print("savol 1/10")
    #
    # print("""Savol
    #
    # a) salom
    # b) qwerty
    # c) qwerty
    # d) qwerty
    # h - yordam
    # """)
    # javob_1 = input("Javobni kiriting: ")
    #
    # print("Javobingiz to'g'ri!!!")
    # print("Noto'g'ri javob.")
    #
    # print("Siz yordamdan foydalanib bo'ldingiz")
    # break
