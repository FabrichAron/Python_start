class Texnika:

    def __init__(self, brand, model, type_1):
        self.brand = brand
        self.model = model
        self.type_1 = type_1

    def info(self):
        print(self.brand)
        print(self.model)
        print(self.type_1)


class Notebooks(Texnika):

    def __init__(self, brand, model, type_1, video_card, ram, display):
        super().__init__(brand, model, type_1)
        self.video_card = video_card
        self.ram = ram
        self.display = display

    def more_info(self):
        print(self.brand)
        print(self.model)
        print(self.type_1)
        print(self.video_card)
        print(self.ram)
        print(self.display)


class Televisions(Texnika):

    def __init__(self, brand, model, type_1, size, display):
        super().__init__(brand, model, type_1)
        self.size = size
        self.display = display

    def more_info(self):
        print(self.brand)
        print(self.model)
        print(self.type_1)
        print(self.size)
        print(self.display)


class Smartphones(Texnika):

    def __init__(self, brand, model, type_1, size, sim_count):
        super().__init__(brand, model, type_1)
        self.size = size
        self.sim_count = sim_count

    def more_info(self):
        print(self.brand)
        print(self.model)
        print(self.type_1)
        print(self.size)
        print(self.sim_count)



Texnika("Apple", "MacBook Pro", "laptop").info()
Notebooks("Apple", "MacBook Pro", "laptop", "2 TB", "8 TB", "OLED").more_info()
Televisions("Apple", "MacBook Pro", "laptop", "162.2mm x 75.7mm x 8.49mm", "AMOLED").more_info()
Smartphones("Apple", "MacBook Pro", "laptop", "162.2mm x 75.7mm x 8.49mm", "2").more_info()






