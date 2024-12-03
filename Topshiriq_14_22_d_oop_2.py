class Texnika:
    def __init__(self, brand, model, type_1):
        self.brand = brand
        self.model = model
        self.type_1 = type_1

    def info(self):
        print(f"Texnika \nBrand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Type: {self.type_1}")


class Notebooks(Texnika):
    def __init__(self, brand, model, type_1, video_card, ram, display):
        super().__init__(brand, model, type_1)
        self.video_card = video_card
        self.ram = ram
        self.display = display

    def more_info(self):
        print(f"\nNotebooks \nBrand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Type: {self.type_1}")
        print(f"Video card: {self.video_card}")
        print(f"Ram: {self.ram}")
        print(f"Display: {self.display}")


class Televisions(Texnika):
    def __init__(self, brand, model, type_1, size, display):
        super().__init__(brand, model, type_1)
        self.size = size
        self.display = display

    def more_info(self):
        print(f"\nTelevisions \nBrand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Type: {self.type_1}")
        print(f"Size: {self.size}")
        print(f"Display: {self.display}")


class Smartphones(Texnika):
    def __init__(self, brand, model, type_1, size, sim_count):
        super().__init__(brand, model, type_1)
        self.size = size
        self.sim_count = sim_count

    def more_info(self):
        print(f"\nSmartphones \nBrand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Type: {self.type_1}")
        print(f"Size: {self.size}")
        print(f"Sim count: {self.sim_count}")


# Texnika("Apple", "MacBook Pro", "laptop").info()
# Notebooks("Lenovo", "Legion", "laptop", "2 TB", "8 TB", "OLED").more_info()
# Televisions("Artel", "Smart TV", "television", "162.2mm x 75.7mm x 8.49mm", "AMOLED").more_info()
# Smartphones("Samsung", "S25 Ultra", "smartphone", "162.2mm x 75.7mm x 8.49mm", "2").more_info()


class Transport:
    def __init__(self, brand, model, type_1):
        self.brand = brand
        self.model = model
        self.type_1 = type_1

    def info(self):
        print(f"Transport \nBrand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Type: {self.type_1}")


class ElentroCars(Transport):
    def __init__(self, brand, model, type_1, battery_life, chargin_time):
        super().__init__(brand, model, type_1)
        self.battery_life = battery_life
        self.chargin_time = chargin_time

    def more_info(self):
        print(f"\nElentroCars \nBrand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Type: {self.type_1}")
        print(f"Battery life: {self.battery_life}")
        print(f"Charging time: {self.chargin_time}")


class SportCars(Transport):
    def __init__(self, brand, model, type_1, motor, color):
        super().__init__(brand, model, type_1)
        self.motor = motor
        self.color = color

    def more_info(self):
        print(f"\nSportCars \nBrand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Type: {self.type_1}")
        print(f"Motor: {self.motor}")
        print(f"Color: {self.color}")


class Truck(Transport):
    def __init__(self, brand, model, type_1, motor, height, long, wieght):
        super().__init__(brand, model, type_1)
        self.motor = motor
        self.height = height
        self.long = long
        self.wieght = wieght

    def more_info(self):
        print(f"\nTruck \nBrand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Type: {self.type_1}")
        print(f"Motor: {self.motor}")
        print(f"Height: {self.height}")
        print(f"Long: {self.long}")
        print(f"Wieght: {self.wieght}")


# Transport("Chevrolet", "Laccetti", "car").info()
# ElentroCars("BYD", "Chazor", "electrocar", "120 km", "12 h").more_info()
# SportCars("AUDI", "Audi R8", "sportcar", "V10 5.2 l", "Floret Silver").more_info()
# Truck("Ford", "Ford Ranger", "Heavy Duty Dually", "Vulcan V6 4,0", "1848 mm", "5389 mm", "1350-2505 kg").more_info()


class University:
    def __init__(self, university):
        self.university = university

    def info(self):
        print(f"University \nUniversity: {self.university}")


class Staff(University):
    def __init__(self, university, first_name, last_name, age):
        super().__init__(university)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def more_info(self):
        print(f"\nStaff \nUniversity: {self.university}")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")


class Student(Staff):
    def __init__(self, university, first_name, last_name, age, group):
        super().__init__(university, first_name, last_name, age)
        self.group = group

    def more_info(self):
        print(f"\nStudent \nUniversity: {self.university}")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Group: {self.group}")


class Teacher(Staff):
    def __init__(self, university, first_name, last_name, age, position, subject):
        super().__init__(university, first_name, last_name, age)
        self.position = position
        self.subject = subject

    def more_info(self):
        print(f"\nTeacher \nUniversity: {self.university}")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Position: {self.position}")
        print(f"Subject: {self.subject}")


class OtherStaff(Staff):
    def __init__(self, university, first_name, last_name, age, position):
        super().__init__(university, first_name, last_name, age)
        self.position = position

    def more_info(self):
        print(f"\nOther Staff \nUniversity: {self.university}")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Position: {self.position}")


# University("Oxford").info()
# Staff("MIT", "Ali", "Bekov", "32").more_info()
# Student("Stanford", "John", "Uvikly", "25", "Lower").more_info()
# Teacher("Cembridge", "Alan", "Dilndor", "52", "Professor", "History").more_info()
# OtherStaff("Harvard", "Clara", "Brown", "46", "Professor").more_info()


class Object(University):
    def __init__(self, university, name):
        super().__init__(university)
        self.name = name

    def object_info(self):
        print(f"\nObject \nUniversity: {self.university}")
        print(f"Name: {self.name}")


class Computer(Object):
    def __init__(self, university, name, soni, tizimi, holati):
        super().__init__(university, name)
        self.name = name
        self.soni = soni
        self.tizimi = tizimi
        self.holati = holati

    def object_more_info(self):
        print(f"\nComputer \nUniversity: {self.university}")
        print(f"Name: {self.name}")
        print(f"Soni: {self.soni}")
        print(f"Tizimi: {self.tizimi}")
        print(f"Holati: {self.holati}")


class Mebel(Object):
    def __init__(self, university, name, soni, turi, holati):
        super().__init__(university, name)
        self.name = name
        self.soni = soni
        self.turi = turi
        self.holati = holati

    def object_more_info(self):
        print(f"\nMebel \nUniversity: {self.university}")
        print(f"Name: {self.name}")
        print(f"Soni: {self.soni}")
        print(f"Turi: {self.turi}")
        print(f"Holati: {self.holati}")

# Object("MIT", "Massachusetts Institute of Technology").object_info()
# Computer("MIT", "Massachusetts Institute of Technology", "2400", "IT", "Good").object_more_info()
# Mebel("MIT", "Massachusetts Institute of Technology", "180", "classic", "Good").object_more_info()
