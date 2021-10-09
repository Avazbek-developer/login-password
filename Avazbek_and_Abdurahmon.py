import os
import getpass
import time

import mysql.connector

class Users:
    def __init__(self):
        self.Name = None
        self.Surname = None
        self.Age = None
        self.Log = None
        self.Password = None
        self.parollar = []
        self.loginlar = []
        self.logins_and_pass = []
        self.logins_and_passes()

    def tizimga_kirish(self):
        self.cls()
        self.dizayner()
        elements = ['1', '2', '3', '4', '5']
        user_wants = input(">>> ")
        while user_wants not in elements:
            print("To'g'ri kiriting.")
            self.cls()
            self.dizayner()
            user_wants = input(">>> ")
        if user_wants == elements[0]:
            self.register()
        elif user_wants == elements[1]:
            self.log_in()
        elif user_wants == elements[2]:
            self.change_log()
        elif user_wants == elements[3]:
            self.del_accunt()
        elif user_wants == elements[4]:
            self.log_out()
    def register(self):
        self.cls()
        name = input("Ism: ").strip().lower()
        while not name.isalpha() or len(name) < 3:
            self.cls()
            print("To'g'riligiga ishoch hosil qiling...")
            name = input("Ism: ").strip().lower()

        self.cls()
        surname = input("Familya: ")
        while not surname.isalpha() or len(surname) < 3:
            self.cls()
            surname = input("Familya: ")

        self.cls()
        age = input("Yosh: ").strip()
        while not age.isnumeric():
            self.cls()
            age = input("Yosh: ").strip()

        self.cls()
        login = input("Login: ").strip().lower()
        while not login.isalnum() or login in self.loginlar:
            self.cls()
            print("Xato qayta kiriting!")
            login = input("Login: ").strip().lower()

        self.cls()
        password1 = getpass.getpass("Parol: secret").strip().lower()
        password2 = getpass.getpass("Parol: secret").strip().lower()
        while self.str_empty(password1) or password2 != password1 or password1 in self.parollar:
            self.cls()
            password1 = getpass.getpass("Parol: secret").strip().lower()
            password2 = getpass.getpass("Parol: secret").strip().lower()
        self.cls()
        self.Name = name
        self.Surname = surname
        self.Age = age
        self.Log = login
        self.Password = password1
        exit()
        my_db = self.database()
        mycursor = my_db.cursor()
        mycursor.execute(f"insert into users(name, surname, age, login, password)values('{self.Name}','{self.Surname}','{self.Age}','{self.Log}','{self.Password}')")
        my_db.commit()
        print("\t--Tizimga hush kelibsiz--")

    def logins_and_passes(self):
        my_db = self.database()
        mycursor = my_db.cursor()
        mycursor.execute("select login,password from users")
        for i in mycursor:
            self.logins_and_pass.append(i)
        for j in self.logins_and_pass:
            self.loginlar.append(j[0])
            self.parollar.append(j[1])

    def log_in(self):
        self.cls()
        login = input("Login: ").strip().lower()
        while not login.isalnum() or login not in self.loginlar:
            self.cls()
            print("Xato kiritdingiz qayta kiriting!")
            login = input("Login: ").strip().lower()

        mydb = self.database()
        mycursor = mydb.cursor()
        mycursor.execute(f"select password from users where login='{login}'")
        dbpas = None
        for i in mycursor:
            dbpas = i[0]
        self.cls()
        password = getpass.getpass("Parol: secret")
        while password != dbpas:
            self.cls()
            print(f"Xato kiritdingiz qayta kiriting!")
            password = getpass.getpass("Parol: secret")
        self.cls()
        print("Tizimga hush kelibsiz!")
    def change_log(self):
        self.cls()
        login = input("Login: ").strip().lower()
        while not login.isalnum() or login not in self.loginlar:
            self.cls()
            print("Xato kiritdingiz qayta kiriting!")
            login = input("Login: ").strip().lower()

        mydb = self.database()
        mycursor = mydb.cursor()
        mycursor.execute(f"select password from users where login='{login}'")
        dbpas = None
        for i in mycursor:
            dbpas = i[0]
        self.cls()
        password = getpass.getpass("Parol: secret")
        while password != dbpas:
            self.cls()
            print(f"Xato kiritdingiz qayta kiriting!")
            password = getpass.getpass("Parol: secret")
        self.cls()

        new_log = input("Yangi login: ")
        while not new_log.isalnum() or new_log in self.loginlar:
            self.cls()
            print("Bunday login mavjud qayta kiriting!")
            new_log = input("Yangi login: ")
        self.cls()
        new_pass = input("Yangi password: ")
        while self.str_empty(new_pass):
            self.cls()
            print("Xato kiritdingiz qayta urinib ko'ring!")
            new_pass = input("Yangi password: ")
        self.cls()
        my_db = self.database()
        mycurs = my_db.cursor()
        mycurs.execute(f"update users set login='{new_log}',password='{new_pass}' where login='{login}'")
        my_db.commit()
        print("Login muvofiqiyatli yangilarndi!")

    def log_out(self):
        print("Siz tizimdan chiqib kettingiz!")
        time.sleep(.2)

    def del_accunt(self):
        self.cls()
        login = input("Login: ").strip().lower()
        while not login.isalnum() or login not in self.loginlar:
            self.cls()
            print("Xato kiritdingiz qayta kiriting!")
            login = input("Login: ").strip().lower()

        mydb = self.database()
        mycursor = mydb.cursor()
        mycursor.execute(f"select password from users where login='{login}'")
        dbpas = None
        for i in mycursor:
            dbpas = i[0]
        self.cls()
        password = getpass.getpass("Parol: secret")
        while password != dbpas:
            self.cls()
            print(f"Xato kiritdingiz qayta kiriting!")
            password = getpass.getpass("Parol: secret")
        self.cls()
        input("Enter")
        my_db = self.database()
        mycurs = my_db.cursor()
        mycurs.execute(f"delete from users where login='{login}'")
        my_db.commit()
        print("Login o'chdi karochche")
    @staticmethod
    def cls():
        os.system("clear")

    @staticmethod
    def str_empty(str_):
        return not bool(str_)

    @staticmethod
    def database():
        return mysql.connector.connect(
            host="localhost",
            user="Avazbek",
            password="12345678",
            database="login"
        )
    @staticmethod
    def dizayner():
        print("""
              ---Najot Ta'lim---                    
            ----------------------
             Register         [1]  
            ----------------------
             Login            [2]  
            ----------------------
             Change Login     [3]  
            ----------------------
             Delete login     [4]
            ----------------------
             Log out          [5]  
            ----------------------
        """)



user = Users()
user.tizimga_kirish()


















# while login in self.logins:
#     print("Bunday login mavjud qayta kiriting!")
#     self.cls()
#     login = input("Enter login: ").strip().lower()
#     while not login.isalnum():
#         self.cls()
#         login = input("Enter login: ").strip().lower()

# while password1 in self.passwords:
#     print("Bunday parol mavjud qayta kiriting!")
#     self.cls()
#     password1 = input("Enter password: ").strip().lower()
#     password2 = input("Configure password: ").strip().lower()
#     while self.str_empty(password1) or password2 != password1:
#         self.cls()
#         password1 = input("Enter password: ").strip().lower()
#         password2 = input("Configure password: ").strip().lower()
