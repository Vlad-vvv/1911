import random

class Human:
    def __init__(self, name, house=None, car=None, job=None):
        self.name = name
        self.house = house
        self.car = car
        self.job = job
        self.money = 150
        self.fun = 50
        self.satiety = 50


brand_of_cars = {"BMW":{"fuel":100, "strenght":100, "consumption":6},
                 "Audi":{"fuel":80, "strenght":80, "consumption":7},
                 "Mercedes":{"fuel":100, "strenght":100, "consumption":5},
                 "Запорожець":{"fuel":50, "strenght":60, "consumption":8}}

class Car:
    def __init__(self, brand_of_cars):
        self.brand = random.choice(list(brand_of_cars))
        self.fuel =  brand_of_cars[self.brand]["fuel"]
        self.strength = brand_of_cars[self.brand]["strenght"]
        self.consumption = brand_of_cars[self.brand]["consumption"]


    def drive(self):
        pass

class House:
    def __init__(self):
        # їжа
        self.food = 0
        # забрудненність
        self.mess = 0

job_list =  {"Розробник на Python":{"salary":100, "fun_less":10},
             "Водій":{"salary":60, "fun_less":5},
             "Художник":{"salary":90, "fun_less":1},
             "Продавець":{"salary":50, "fun_less":8}}
class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.fun_less = job_list[self.job]["fun_less"]