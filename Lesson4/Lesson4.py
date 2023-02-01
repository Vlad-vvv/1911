class Human:
    def __init__(self, name='No name'):
        self.name = name


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []

    def add_passenger(self, *humans):
        for passenger in humans:
            self.passenger.append(passenger)

    def print_passenger(self):
        if self.passenger == []:
            print('Автомобіль зараз порожний')
        else:
            print(f'Зараз на {self.brand} їдуть такі люди')
            for passenger in self.passenger:
                print(passenger.name)


human1 = Human("Влад")
human2 = Human("Саша")
car = Car("BMW")
car.add_passenger(human1, human2)

car.print_passenger()