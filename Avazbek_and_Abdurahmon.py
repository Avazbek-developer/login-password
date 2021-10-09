import os
import getpass
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
            self.log_out()
        elif user_wants == elements[4]:
            self.del_accunt()

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
        pass

    def change_log(self):
        print("changlog")

    def log_out(self):
        print("Siz tizimdan chiqib kettingiz!")
        exit()

    def del_accunt(self):
        pass

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
  <<<<<<<<<<<< Tizimga_kirish>>>>>>>>>>>> 

            Register           [1]
        -------------------------------
            Login              [2]
        -------------------------------  
            Change login       [3]
        -------------------------------
            Log out            [4]
        -------------------------------
            Delete account     [5]

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
