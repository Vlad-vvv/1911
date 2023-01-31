import random


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 1.0
        self.fun = 70.0
        self.money = 200
        self.alive = True

    def to_study(self):
        print("Я навчаюсь")
        self.progress += 0.2
        self.fun -= 4

    def to_sleep(self):
        print("Я пішов спати")
        self.fun += 3
        self.money -=4

    def to_have_fun(self):
        print("Я розважаюсь ")
        self.progress -= 0.1
        self.fun += 5
        self.money -= 25

    def to_have_money(self):
        print("Я заробряю гроші")
        self.money += 20
        self.progress += 0.1
        self.fun -= 5

    def is_alive(self):
        if self.progress < 0:
            print("Ви відрахований ")
            self.alive = False
        if self.progress > 5:
            print("Ура я достроково заверщив навчання")
            self.alive = False
        if self.fun < 40:
            print("В мене депрессія")
            self.alive = False
        if self.money < 20:
                print("У мене мало грошей")
                self.money += 20
                self.progress += 0.1
                self.fun -= 5

    def end_of_day(self):
        print(f'Задоволенність - {self.fun}')
        print(f'Прогрес        - {round(self.progress)}')
        print(f'Гроші          - {round(self.money)}')

    def live(self, day):
        info = f'День {day} з життя {self.name}'
        print(f'{info:=^40}')
        choice = random.randint(1, 4)
        if choice == 1:
            self.to_study()
        elif choice == 2:
            self.to_sleep()
        elif choice == 3:
            self.to_have_fun()
        elif choice == 4:
            self.to_have_money()

        self.end_of_day()
        self.is_alive()



leonid = Student(name="Леонід")
for day in range(365):
    if leonid.alive == False:
        break
    leonid.live(day)
