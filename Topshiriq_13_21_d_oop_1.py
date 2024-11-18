from functools import reduce


class Oson1:
    a = 2

    def print_a(self):
        print(self.a)


Oson1.print_a(Oson1)


class Oson2:
    a = 2
    b = 3

    def plus_minus(self):
        print(self.a + self.b)


Oson2.plus_minus(Oson2)


class Oson3:
    a = -2

    def plus_minus(self):
        if self.a >= 0:
            print(f"{self.a} musbat son")
        else:
            print(f"{self.a} manfiy son")


Oson3.plus_minus(Oson3)


class Oson4:
    a = 5

    def odd_even(self):
        if self.a % 2 == 0:
            print(f"{self.a} juft son")
        else:
            print(f"{self.a} toq son")


Oson4.odd_even(Oson4)


class Oson5:
    a = 2
    b = 3

    def daraja(self):
        print(self.a ** self.b)


Oson5.daraja(Oson5)


class MyClass6:
    words = ["one"]

    def add_word(self, word="two"):
        self.words.append(word)
        print(self.words)

    def remove(self, word="one"):
        self.words.remove(word)
        print(self.words)


MyClass6.add_word(MyClass6)

MyClass6.remove(MyClass6)


class MyClass7:
    myDict = {"one": "two"}

    def add_elem(self):
        self.myDict.setdefault("two", "three")
        print(self.myDict)

    def update_elem(self, key, value):
        if key in self.myDict.keys():
            self.myDict.update({key: value})
            print(self.myDict)
        else:
            print(self.myDict)


MyClass7.add_elem(MyClass7)
MyClass7.update_elem(MyClass7, "one", "four")


class MyClass8:
    numbers = [1, 2, 3, 4, 5, 6]

    def compare_lists(self, new_list):
        list1 = reduce(lambda x, y: x + y, new_list)
        list2 = reduce(lambda x, y: x + y, self.numbers)
        if list1 < list2:
            print("numbers new_listdan katta")
        elif list1 > list2:
            print("new_list numbersdan katta")
        elif list1 == list2:
            print("new_list numbersga teng")


MyClass8.compare_lists(MyClass8, [1, 2, 3, 4, 5, 6, 7])


class MyClass9:
    list1 = [1, 2, 3, 4, 5, 6, 7, 10, 8, 0, 9, 15, 12, 11]
    list2 = [4, 5, 6, 7, 10, 8, 0, 9, 15, 12, 11, 19, 23, 25]

    def list1_max(self):
        max_list1 = max(self.list1)
        return max_list1

    def list2_max(self):
        max_list2 = max(self.list2)
        return max_list2

    def sum_of_two_max(self, first, second):
        sum_maxes = first + second
        print(sum_maxes)


max_num1 = MyClass9.list1_max(MyClass9)
max_num2 = MyClass9.list2_max(MyClass9)
MyClass9.sum_of_two_max(MyClass9, max_num1, max_num2)


class MyClass10:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    def divide(self, d):
        new_list = []
        for i in self.numbers:
            if i % d == 0:
                new_list.append(i)
        return new_list


print(MyClass10.divide(MyClass10, 4))
