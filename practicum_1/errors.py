def errors(error_count, choise):
    if error_count >= 2:
        print(
            f"Kechirasiz, siz \033[91m{error_count}\033[0m martta noto'g'ri buyruq kiritdingiz. \033[92mTo'g'ri buyruq raqamlarimiz 1, 2 va 0.\033[0m")
    else:
        if choise == "":
            print("\033[91mBo'sh buyruq qabul qilinmaydi.\033[0m Iltimos, buyruqni to'g'ri kiriting!")
        else:
            print(f"     \033[91m \033[4m{choise}\033[0m bu xato buyruq. Buyruqni to'g'ri kiriting!")
