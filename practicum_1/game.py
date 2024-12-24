from load_questions import load_questions
from print_old_info_of_user import print_old_info_of_user


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
