from game import game
from errors import errors
from rating import rating
from load_users import load_users
from save_users import save_users
from print_game_name import print_game_name
from change_user_info import change_user_info
from add_or_get_users import add_or_get_users
from old_info_of_user import old_info_of_user
from print_information import print_information


def check_capita_strip_name(username):
    username = username.strip(" ")
    if username == "" or not username.isalpha():
        print("\033[91mIltimos, o'yinchini ismini to'g'ri kiriting!\033[0m")
        username = input("O'yinchini ismini kiriting: ")
        if username == "" or not username.isalpha():
            print("\033[91mO'yinchini ismini to'g'ri kiritmadingiz!\033[0m")
            main()
    username = username.capitalize()
    return username


def main():
    users = load_users()  # Userlarning ro'yxati
    error_count = 0  # Xatolar sonini bilishimiz uchun o'zgaruvchi
    while True:  # Tizimdagi amallar ketmaketligini qachonki shart bajarilmaguncha cheksiz davom ettiradi
        print_information()  # Tizim ishga tushganda birinchi bo'lib consolda malumot e'lon qiladi
        choise = input('\033[92m' + ">>> " + '\033[0m')  # Buyruq raqamini qabul qiladi

        if choise == "1":
            error_count = 0  # Xatolar sonini nolga tenglaydi
            username = input("O'yinchining ismini kiriting: ")  # Userning ismini qabul qiladi
            username = check_capita_strip_name(username)
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
if __name__ == "__main__": # yozilgan kodlarni ishga tushiradi
    main()