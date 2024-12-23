import json


def load_questions(filename="tests.json"):
    with open(filename, "r") as file:
        return json.load(file)


def load_users(filename="users.json"):
    with open(filename, "r") as file:
        return json.load(file)


def add_or_get_users(users, username):
    if username not in users:
        users[username] = {"result": 0, "game_count": 0}
    return users


def save_users(users, filename="users.json"):
    with open(filename, "w") as file:
        return json.dump(users, file, indent=4)


def check_capitalize_strip_username(username):
    username = username.strip(" ")
    if username == "" or not username.isalpha():
        print("\033[91mIltimos, o'yinchini ismini to'g'ri kiriting!\033[0m")
        username = input("O'yinchini ismini kiriting: ")
        if username == "" or not username.isalpha():
            print("\033[91mO'yinchini ismini to'g'ri kiritmadingiz!\033[0m")
            main()
    username = username.capitalize()
    return username


def change_user_info(users, username, score):
    old_score = users[username]["result"]
    old_game_count = users[username]["game_count"]
    if old_score > score:
        users[username] = {"result": old_score, "game_count": old_game_count + 1}
        return users
    else:
        users[username] = {"result": score, "game_count": old_game_count + 1}
        return users


def old_info_of_user(users, username):
    game_count = users[username]["game_count"]
    max_score = users[username]["result"]
    return game_count, max_score


def print_old_info_of_user(game_count, max_score):
    print(f"""\033[1m\033[93mEski natijalaringiz:\033[0m
\033[93mO'yinlar soni: \033[0m{game_count}
\033[93mMaksimal ball: \033[0m{max_score}""")


def errors(error_count, choise):
    if error_count >= 2:
        print(
            f"Kechirasiz, siz \033[91m{error_count}\033[0m martta noto'g'ri buyruq kiritdingiz. \033[92mTo'g'ri buyruq raqamlarimiz 1, 2 va 0.\033[0m")
    else:
        if choise == "":
            print("\033[91mBo'sh buyruq qabul qilinmaydi.\033[0m Iltimos, buyruqni to'g'ri kiriting!")
        else:
            print(f"     \033[91m \033[4m{choise}\033[0m bu xato buyruq. Buyruqni to'g'ri kiriting!")


def game(game_count, max_score):
    questions = load_questions()
    count_test = 0
    h_work_count = 0
    halp_total_num = 1
    equality = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
    }
    print_old_info_of_user(game_count, max_score)
    for i in questions:
        count_test += 1
        print(f"""\033[96m
Savol {count_test}/10:\033[0m \033[1m{i["question"]}\033[0m
\033[93m
a)\033[0m {i["answers"][0]["key"]}\033[93m
b)\033[0m {i["answers"][1]["key"]}\033[93m
c)\033[0m {i["answers"][2]["key"]}\033[93m
d)\033[0m {i["answers"][3]["key"]}\033[94m
h \033[0m-> yordam \033[92m({halp_total_num}/1)\033[0m""")
        answer_user = input("\033[36m Javobni kiriting: \033[0m")
        if answer_user == "":
            print(f"\033[91mNoto'g'ri javob.\033[0m Sizning to'plagan balingiz \033[92m{count_test - 1}\033[0m")
            print("")
            return count_test - 1
        elif answer_user not in ["a", "b", "c", "d", "h"]:
            print(
                "----------------------------------------------------------------------------------------------")
            print(f"\033[91mNoto'g'ri javob.\033[0m Sizning to'plagan balingiz \033[92m{count_test - 1}\033[0m")
            return count_test - 1
        else:
            if answer_user == "h" and h_work_count != 1:
                halp_total_num -= 1
                h_work_count += 1
                count_sikl_n = 0
                array_variants = ["a", "b", "c", "d"]
                for n in i["answers"]:
                    count_sikl_n += 1
                    if n["isTrue"] and count_sikl_n < 4:
                        print(f"""\033[93m
{array_variants[count_sikl_n - 1]})\033[0m {i["answers"][count_sikl_n - 1]["key"]}\033[93m
{array_variants[count_sikl_n]})\033[0m {i["answers"][count_sikl_n]["key"]}\033[93m""")
                        answer_user = input("\033[36m Javobni kiriting: \033[0m")
                        if answer_user == "":
                            print(
                                f"\033[91mNoto'g'ri javob.\033[0m Sizning to'plagan balingiz \033[92m{count_test - 1}\033[0m")
                            print("")
                            return count_test - 1
                        elif answer_user not in ["a", "b", "c", "d"]:
                            print(
                                "----------------------------------------------------------------------------------------------")
                            print(
                                f"\033[91mNoto'g'ri javob.\033[0m Sizning to'plagan balingiz \033[92m{count_test - 1}\033[0m")
                            return count_test - 1
                        else:
                            if i["answers"][equality[answer_user]]["isTrue"]:
                                if count_test == 10:
                                    print(
                                        f"\033[92mTo'g'ri javob, siz millionersiz.\033[0m\033[0m Sizning to'plagan balingiz \033[92m{count_test}\033[0m")
                                    return count_test
                                else:
                                    print("\033[92mTo'g'ri javob.\033[0m")
                                    break
                            else:
                                print(
                                    "----------------------------------------------------------------------------------------------")
                                print(
                                    f"\033[91mNoto'g'ri javob.\033[0m Sizning to'plagan balingiz \033[92m{count_test - 1}\033[0m")
                                return count_test - 1
                    elif n["isTrue"] and count_sikl_n == 4:
                        print(f"""\033[93m
{array_variants[count_sikl_n - 2]})\033[0m {i["answers"][count_sikl_n - 3]["key"]}\033[93m
{array_variants[count_sikl_n - 1]})\033[0m {i["answers"][count_sikl_n - 1]["key"]}\033[93m""")
                        answer_user = input("\033[36m Javobni kiriting: \033[0m")
                        if answer_user == "":
                            print(
                                f"\033[91mNoto'g'ri javob.\033[0m Sizning to'plagan balingiz \033[92m{count_test - 1}\033[0m")
                            print("")
                            return count_test - 1
                        elif answer_user not in ["a", "b", "c", "d"]:
                            print(
                                "----------------------------------------------------------------------------------------------")
                            print(
                                f"\033[91mNoto'g'ri javob.\033[0m Sizning to'plagan balingiz \033[92m{count_test - 1}\033[0m")
                            return count_test - 1
                        else:
                            if i["answers"][equality[answer_user]]["isTrue"]:
                                if count_test == 10:
                                    print(
                                        f"\033[92mTo'g'ri javob, siz millionersiz.\033[0m\033[0m Sizning to'plagan balingiz \033[92m{count_test}\033[0m")
                                    return count_test
                                else:
                                    print("\033[92mTo'g'ri javob.\033[0m")
                            else:
                                print(
                                    "----------------------------------------------------------------------------------------------")
                                print(
                                    f"\033[91mNoto'g'ri javob.\033[0m Sizning to'plagan balingiz \033[92m{count_test - 1}\033[0m")
                                return count_test - 1
            elif answer_user == "h" and h_work_count == 1:
                print("\033[91mSiz yordamdan foydalanib boldingiz!\033[0m")
                print(f"""\033[96m
Savol {count_test}/10:\033[0m \033[1m{i["question"]}\033[0m
\033[93m
a)\033[0m {i["answers"][0]["key"]}\033[93m
b)\033[0m {i["answers"][1]["key"]}\033[93m
c)\033[0m {i["answers"][2]["key"]}\033[93m
d)\033[0m {i["answers"][3]["key"]}""")
                answer_user = input("\033[36m Javobni kiriting: \033[0m")
                if answer_user == "":
                    print(f"\033[91mNoto'g'ri javob.\033[0m Sizning to'plagan balingiz \033[92m{count_test - 1}\033[0m")
                    print("")
                    return count_test - 1
                elif answer_user not in ["a", "b", "c", "d"]:
                    print(
                        "----------------------------------------------------------------------------------------------")
                    print(f"\033[91mNoto'g'ri javob.\033[0m Sizning to'plagan balingiz \033[92m{count_test - 1}\033[0m")
                    return count_test - 1
                else:
                    if i["answers"][equality[answer_user]]["isTrue"]:
                        if count_test == 10:
                            print(
                                f"\033[92mTo'g'ri javob, siz millionersiz.\033[0m\033[0m Sizning to'plagan balingiz \033[92m{count_test}\033[0m")
                            return count_test
                        else:
                            print("\033[92mTo'g'ri javob.\033[0m")
                    else:
                        print(
                            "----------------------------------------------------------------------------------------------")
                        print(
                            f"\033[91mNoto'g'ri javob.\033[0m Sizning to'plagan balingiz \033[92m{count_test - 1}\033[0m")
                        return count_test - 1

                print("----------------------------------------------------------------------------------------------")
            else:
                if i["answers"][equality[answer_user]]["isTrue"]:
                    if count_test == 10:
                        print(
                            f"\033[92mTo'g'ri javob, siz millionersiz.\033[0m\033[0m Sizning to'plagan balingiz \033[92m{count_test}\033[0m")
                        return count_test
                    else:
                        print("\033[92mTo'g'ri javob.\033[0m")
                else:
                    print(
                        "----------------------------------------------------------------------------------------------")
                    print(f"\033[91mNoto'g'ri javob.\033[0m Sizning to'plagan balingiz \033[92m{count_test - 1}\033[0m")
                    return count_test - 1
        print("----------------------------------------------------------------------------------------------")


def rating():
    users = load_users()  # Userlarning ro'yxati
    print("------------+----------+------------")
    print("\033[96m    name\033[0m    |\033[96m  played\033[0m  |\033[96m best score\033[0m")
    for i in users:
        print(f"""------------+----------+------------\033[93m \033[1m
{i.ljust(12)}\033[0m|    \033[1m\033[93m{str(users[i]["game_count"]).ljust(6)}\033[0m|     \033[1m\033[93m{str(users[i]["result"]).ljust(5)}\033[0m""")
    print("------------+----------+------------")


def print_information():
    print("\033[96m" + """              Buyruqni tanlang:  \033[0m \033[93m
                1 -> O'yinni boshlash
                2 -> Reyting
                \033[0m \033[94m
                0 -> Dasturdan chiqish""" + "\033[0m")


def print_game_name():
    print("\033[1m\033[95m\"Kim millioner bo'lishni hohlaydi\" o'yiniga hush kelibsiz!\033[0m")


def main():
    users = load_users()  # Userlarning ro'yxati
    error_count = 0  # Xatolar sonini bilishimiz uchun o'zgaruvchi
    while True:  # Tizimdagi amallar ketmaketligini qachonki shart bajarilmaguncha cheksiz davom ettiradi
        print_information()  # Tizim ishga tushganda birinchi bo'lib consolda malumot e'lon qiladi
        choise = input('\033[92m' + ">>> " + '\033[0m')  # Buyruq raqamini qabul qiladi

        if choise == "1":
            error_count = 0  # Xatolar sonini nolga tenglaydi
            username = input("O'yinchini ismini kiriting: ")  # Userning ismini qabul qiladi
            username = check_capitalize_strip_username(username)
            """Username bo'sh emasligini tekshiradi, agar bo'sh bo'lsa o'yin qaytadan ishga tushadi"""
            users = add_or_get_users(users, username)
            """Yangi user kirganda oldin o'yin o'ynaganmi yo'qmi tekshiradi, agar o'ynamagan bo'lsa jsonga yangi user qo'shadi"""
            game_count, old_score = old_info_of_user(users, username)
            """Userning jsondagi malumotlari (o'yinlar soni va maksimal ball)"""
            score = game(game_count, old_score)  # Userning o'yindan so'ng to'plagan bali
            users = change_user_info(users, username, score)
            """Userning ro'yhatdagi malumotlar(o'yinlar soni va maksimal ball)ni yangilab qaytaradi"""
            save_users(users)  # Userlarni ro'yxatini jsonga o'tkazib saqlaydi

        elif choise == "2":  # O'yin reytingini ko'rish buyruqi tanlansa ishga tushadi
            error_count = 0  # Xatolar sonini nolga tenglaydi
            rating()  # O'yin reytingini print qiluvchi funksiya

        elif choise == "0":  # Tizimni to'xtadigan buyrug'i tanlansa ishga tushadi
            print("\033[91m \033[1m    Dastur to'xtadi." + "\033[0m")  # Dastur to'xtaganini e'lon qiladi
            break  # Dasturni to'xtatadi.

        else:
            error_count += 1  # Xatolar soniga 1 qo'shib qo'yadi
            errors(error_count, choise)  # Buyruq kiritishdagi xatolarga javob qaytaradi


print_game_name()  # Tizim ishga tushganda o'yinni nomini print qiladi
main()  # yozilgan kodlarni ishga tushiradi
