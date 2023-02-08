class Human:
    height = 170
    age = 30
    gladness = 10


class Student(Human):
    age = 17


class Aspirant(Student):
    height = 180

    def __init__(self):
        print(self.height)
        print(self.age)
        print(self.gladness)

    def _hello(self):
        print("_Hello")

    def __hello(self):
        print("__Hello")


class Worker(Human):
    age = 50


class Hello_Kitty:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"

    def __init__(self):
        self.kity = "Kity"
        self._kity = "_Kity"
        self.__kity = "__Kity"

    def print(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.kity)
        print(self._kity)
        print(self.__kity)

    def __method(self):
        print("Method")


class Hi(Hello_Kitty):
    def hi_print(self):
        super().__method()
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.kity)
        print(self._kity)
        print(self.__kity)

class Computer:
    def __init__(self):
        super().__init__()
        self.RAM = "16 Gb"

    def calc(self):
        print("Calculate.....")


class Monitor:
    def __init__(self,):
        super().__init__()
        self.modul = None
        self.resolution = "8k"

    def display(self):
        print("Print result")


class SmartPhone(Computer, Monitor):
    def info(self):
        print(self.RAM)
        print(self.resolution)
        print(self.modul)

phone = SmartPhone(modul="Aplle")
phone.info()


'''
#hello = Hello_Kitty()
#hello.print()

hi = Hi()
hi.hi_print()

asp = Aspirant()
asp.age = 1000000


asp._hello()
asp.__hello()

st = Student
wr = Worker
print(st.height, st.age)
print(wr.height, wr.age)'''