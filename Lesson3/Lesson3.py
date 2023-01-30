import random


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 1.0
        self.fun = 50.0
        self.alive = True

    def to_study(self):
        print("Я навчаюсь")
        self.progress += 0.2
        self.fun -= 4

    def to_sleep(self):
        print("Я пішов спати")
        self.fun += 3

    def to_have_fun(self):
        print("Я розважаюсь ")
        self.progress -= 0.1
        self.fun += 5

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

    def end_of_day(self):
        print(f'Задоволенність - {self.fun}')
        print(f'Прогрес        - {round(self.progress)}')

    def live(self, day):
        info = f'День {day} з життя {self.name}'
        print(f'{info:=^40}')
        choice = random.randint(1, 3)
        if choice == 1:
            self.to_study()
        elif choice == 2:
            self.to_sleep()
        elif choice == 3:
            self.to_have_fun()

        self.end_of_day()
        self.is_alive()



leonid = Student(name="Леонід")
for day in range(365):
    if leonid.alive == False:
        break
    leonid.live(day)
