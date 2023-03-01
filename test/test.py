import sqlite3
import colorama
from colorama import Fore, Back, Style

connection = sqlite3.connect("database.sl3", 5)
cur = connection.cursor()

#cur.execute("create table users (login text, password text);")
#class Entrance:
#def check(self):

string = input(Fore.MAGENTA + Back.BLACK + 'Для входу нажміть клавішу "В", а для регестрации нажмить "Р": ')
#text = input('Для входу нажміть клавішу "B", а для регестрации нажмить "P": ')
if "Р" in string:
    login = input('Ваш логин: ')
    password = input('Ваш пароль: ')
    cur.execute(f"insert into users (login, password) values ( '{login}', '{password}');")
    connection.commit()
if "В" in string:
    #login = input('Ваш логин: ')
    passwordd = input('Ваш пароль: ')
    cur.execute(f"select login from users where password='{passwordd}';")
    connection.commit()
    res = cur.fetchall()
    print(f"{res} ваш логин")
    print('Ви у базі даних')