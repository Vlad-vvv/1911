class MyException(Exception):
    def __init__(self, my_data):
        self.date = my_data

    def __str__(self):
        return f"{self.date} Це мій класс винятку"

a = int(input())
b = int(input())
try:
    try:
        if b == 0:
            raise MyException("15.02.2023")
            #raise ZeroDivisionError(f"Cпроба ділення на {b}")
        print(a/b)
        #print(name)

    except (ZeroDivisionError) as error:
        print(error)
    else:
        print("Проблем немає ")
    finally:
        print("Щось буде ")

except MyException as error:
    print(error)
except:
    print("Помилка")
'''        
except NameError:
    print("Не відоме ім'я ")'''

print("Кінець програми")