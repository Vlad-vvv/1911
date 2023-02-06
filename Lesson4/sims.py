import random


class Human:
    def __init__(self, name, house=None, car=None, job=None):
        self.name = name
        self.house = house
        self.car = car
        self.job = job
        self.money = 100
        self.fun = 50
        self.satiety = 50

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self, purchase):
        pass

    def cleaning(self):
        pass

    def to_repair(self):
        pass

    def chill(self):
        pass

    def get_house(self):
        self.house = House()

    def get_car(self):
        self.car = Car(brand_of_cars)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def is_alive(self):
        if self.fun < 0:
            print("Депрессія")
            return False
        if self.satiety < 0:
            print("Помер від голоду")
            return False
        if self.money < -200:
            print("Банкрот")
            return False

    def day_info(self, day_number):
        day_str = f"День {day_number}--й з життя {self.name}-а"
        print(f"{day_str:=^50}", "\n")
        human_str = f"{self.name}а"
        print(f"{human_str:=^50}", "\n")
        print(f"Задоволення - {self.fun}")
        print(f"Cитість - {self.satiety}")
        print(f"Гроші - {self.money}")
        house_str = f"Інформація про будинок "
        print(f"{house_str:=^50}", "\n")
        print(f"Їжа - {self.house.food}")
        print(f"Порядок - {self.house.mess}")
        car_str = f"Інформація про автівку {self.car.brand}"
        print(f"{car_str:=^50}", "\n")
        print(f"Пальне - {self.car.fuel}")
        print(f"Стан - {self.car.strength}")



    def live(self, day_number):
        if self.is_alive() == False:
            return False
        if self.house is None:
            self.get_house()
            print("У мене є дім")
        if self.car is None:
            self.get_car()
            print(f"У мене {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"Моя робота {self.job.job}, із зарплатнею{self.job.salary}$")
        self.day_info(day_number)
        if self.money < 0:
            print("Я йду на роботу")
            self.work()
        #elif




brand_of_cars = {"BMW": {"fuel": 100, "strenght": 100, "consumption": 6},
                 "Audi": {"fuel": 80, "strenght": 80, "consumption": 7},
                 "Mercedes": {"fuel": 100, "strenght": 100, "consumption": 5},
                 "Запорожець": {"fuel": 50, "strenght": 60, "consumption": 8}}


class Car:
    def __init__(self, brand_of_cars):
        self.brand = random.choice(list(brand_of_cars))
        self.fuel = brand_of_cars[self.brand]["fuel"]
        self.strength = brand_of_cars[self.brand]["strenght"]
        self.consumption = brand_of_cars[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Немає пального або автомобіль зламався  ")
            return False


class House:
    def __init__(self):
        # їжа
        self.food = 0
        # забрудненність
        self.mess = 0


job_list = {"Розробник на Python": {"salary": 100, "fun_less": 10},
             "Водій": {"salary": 60, "fun_less": 5},
             "Художник": {"salary": 90, "fun_less": 1},
             "Продавець": {"salary": 50, "fun_less": 8}}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.fun_less = job_list[self.job]["fun_less"]


vlad = Human("Влад")
for day in range(1, 366):
    if vlad.live(day) == False:
        break