import os
import mysql.connector

class Users:
    def __init__(self):
        self.Name = None
        self.Surname = None
        self.Age = None
        self.Log = None
        self.Password = None

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
        name = input("Enter name: ").strip().lower()
        while not name.isalpha() or len(name) < 3:
            self.cls()
            print(f"To'g'ri kiriting...")
            name = input("Enter name: ").strip().lower()

        self.cls()
        surname = input("Enter surname: ")
        while not surname.isalpha() or len(surname) < 3:
            self.cls()
            surname = input("Enter surname: ")

        self.cls()
        age = input("Enter age: ").strip()
        while not age.isnumeric():
            self.cls()
            age = input("Enter age: ").strip()

        self.cls()
        login = input("Enter login: ").strip().lower()
        while not login.isalnum():
            self.cls()
            login = input("Enter login: ").strip().lower()

        self.cls()
        password1 = input("Enter password: ").strip().lower()
        while self.str_empty(password1):
            self.cls()
            password1 = input("Enter password: ").strip().lower()

        self.Name = name
        self.Surname = surname
        self.Age = int(age)
        self.Log = login
        self.Password = password1


        mydb = self.database()
        mycursor = mydb.cursor()
        mycursor.execute(f"insert into useres(name, surname, age, login, password)values('{self.Name}', '{self.Surname}', '{self.Age}', '{self.Log}', '{self.Password}')")
        mydb.commit()

    @staticmethod
    def database():
        my_db = mysql.connector.connect(
            host="localhost",
            user="Avazbek",
            password="12345678",
            database="login"
        )




















    def log_in(self):
        pass


































    def change_log(self):
        print("changlog")

    def log_out(self):
        print("logout")

    def del_accunt(self):
        print("del")

    @staticmethod
    def cls():
        os.system("clear")

    @staticmethod
    def str_empty(str_):
        return not bool(str_)























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




































