from load_users import load_users


def rating():
    users = load_users()  # Userlarning ro'yxati
    print("------------+----------+------------")
    print("\033[96m    name\033[0m    |\033[96m  played\033[0m  |\033[96m best score\033[0m")
    for i in users:
        print(f"""------------+----------+------------\033[93m \033[1m
{i.ljust(12)}\033[0m|    \033[1m\033[93m{str(users[i]["game_count"]).ljust(6)}\033[0m|     \033[1m\033[93m{str(users[i]["result"]).ljust(5)}\033[0m""")
    print("------------+----------+------------")
