import os
import mysql.connector
import time

class Logiin_and_password:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.login = None
        self.password = None

    def tizimga_kirish(self):
        self.cls()
        self.dizayn()
        comand = ['1', '2', '3', '4', '5']
        tanlov_bolim = input(">>> ").strip()
        while tanlov_bolim not in comand:
            self.cls()
            self.dizayn()
            tanlov_bolim = input(">>> ").strip()
        if tanlov_bolim == '1':
            self.registratsiya()
        elif tanlov_bolim == '2':
            self.lo_gin()
        elif tanlov_bolim == '3':
            self.edit_log_pas()
        elif tanlov_bolim == '4':
            self.loginni_ochirish()
        else:
            self.logindan_chiqish()

    def registratsiya(self):
        self.cls()

        for i in "\tRegister":
            print(f"{i}", end='')
            time.sleep(0.1)
        input_name = input("\nIsmingizni kiriting: ").strip().lower()
        while not input_name.isalpha() or len(input_name) < 3:
            self.cls()
            input_name = input("Ismingini kiriting: ").strip().lower()
#========================================================
        self.cls()
        input_surname = input("Familyangizni kiriting: ").strip().lower()
        while not input_surname.isalpha() or len(input_name) < 3:
            self.cls()
            input_surname = input("Familyangizni kiriting: ").strip().lower()
#=======================================================
        self.cls()
        input_age = input("Yosh: ").strip()
        while input_age.isalpha() or not input_age.isdigit():
            self.cls()
            input_age = input("Yosh: ").strip()
# =======================================================
        self.cls()
        input_log = input("Login: ").strip().lower()
        while not input_log.isalpha():
            self.cls()
            input_log = input("Login: ").strip().lower()
# =======================================================
        self.cls()
        input_pas = input("Password: ").strip()
        while self.empty_imput(input_pas):
            self.cls()
            input_pas = input("Password: ").strip()
        print("Tizimga hush kelibsiz!")

    def lo_gin(self):
        self.cls()
        for i in "\tLogin":
            print(f"{i}", end='')
            time.sleep(0.1)


    def edit_log_pas(self):
        self.cls()
        for i in "\tChage login":
            print(f"{i}", end='')
            time.sleep(0.1)


    def logindan_chiqish(self):
        self.cls()
        for i in "\tLogin out":
            print(f"{i}", end='')
            time.sleep(0.1)


    def loginni_ochirish(self):
        self.cls()
        for i in "\tDelete login":
            print(f"{i}", end='')
            time.sleep(0.1)

    @staticmethod
    def empty_imput(str_):
        return not bool(str_)

    @staticmethod
    def dizayn():
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

    def database(self):
        my_db = mysql.connector.connect(
            host="localhost",
            user="Avazbek",
            password="12345678",
            database="login"
        )

    @staticmethod
    def cls():
        return os.system("clear")

login = Logiin_and_password()
login.tizimga_kirish()






























































































