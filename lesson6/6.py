class Human:
    height = 170
    __age = 30
    gladness = 50



class Student(Human):
    pass


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


class Hello_Kity:
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


class Hi(Hello_Kity):
    def hi_print(self):
        super().__method()
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.kity)
        print(self._kity)
        print(self.__kity)


class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__()
        self.model = model
        self.RAM = "16 Gb"

    def calc(self):
        print("Calculate....")


class Monitor:
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.resolution = "8K"

    def display(self):
        print("Print result")


class SmartPhone(Computer, Monitor):
    def info(self):
        print(self.RAM)
        print(self.resolution)
        print(self.model)



phone = SmartPhone(model="Apple 15")
phone.info()


#hello = Hello_Kity()
#hello.print()

#hi = Hi()
#hi.hi_print()

#asp = Aspirant()
#asp.age = 10000


'''st = Student()
wr = Worker()
print(st.age)
print(wr.age)'''