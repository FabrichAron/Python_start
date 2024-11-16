def hotel_astrum():
    print("Astrum mehmonhonasiga hush kelibsiz!")
    while True:
        print("""       
          Buyruq raqamini tanlang:
            1 -> mehmonlar ro'yxati
            2 -> mehmon qo'shish
            3 -> mehmonni ro'yxatdan chiqarish
        
            0 -> dasturdan chiqish""")
        selected_number = (input(">>> : "))
        if selected_number.isdigit():
            if selected_number == "1":
                print("""Ismi                    Xona raqami                    Xona turi
________________________________________________________________""")
                for i in list_guests:
                    print(f"""{i.get("name").ljust(24)}{str(i.get("number")).ljust(31)}{i.get("room_level")}""")
                print("________________________________________________________________")
            elif selected_number == "0":
                print("Dastur to'xtadi...")
                break
            elif selected_number == "2":
                name = input("Ismi: ")
                number = input("Xona raqami: ")
                room_level = input("Xona turi: ")
                if name.isalpha() and number.isdigit() and room_level.isalpha():
                    number = int(number)
                    if number not in rooms:
                        rooms.append(number)
                        list_guests.append({
                            "name": name,
                            "number": number,
                            "room_level": room_level
                        })
                    else:
                        print("Bu xona band, boshqa xona tanlang!")
                else:
                    print("Iltimos, yangi mijozni malumotini to'liq va to'g'ri to'ldiring!")

            elif selected_number == "3":
                name_del = input("Ismi: ")
                a = 0
                for i in list_guests:
                    if i.get("name") == name_del:
                        list_guests.pop(a)
                    a += 1
            else:
                print("Faqat buyruq raqamlaridan birini tanlang!")
        else:
            print("Faqat buyruq raqamlaridan birini tanlang!")


rooms = [12, 15, 20]

list_guests = [
    {
        "name": "John",
        "number": 12,
        "room_level": "standart"
    },
    {
        "name": "Doe",
        "number": 15,
        "room_level": "standart"
    },
    {
        "name": "Ali",
        "number": 20,
        "room_level": "comfort"
    },
]

hotel_astrum()
