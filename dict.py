import os
import sys

import mysql.connector


class Our_dictionary:
    def __init__(self):
        self.eng_word = None
        self.uz_word = None

    def system_entrance(self):
        self.cls()
        options = ['1', '2', '3', '4']
        self.print_messege()
        input_choice = input(">>>: ").strip()
        while self.is_string_empty(input_choice) or input_choice not in options:
            self.cls()
            self.print_messege()
            input_choice = input(">>>: ").strip()

        if input_choice == options[0]:
            return self.add_new_word()
        elif input_choice == options[1]:
            return self.search_word()
        elif input_choice == options[2]:
            return self.show_words()
        else:
            return self.go_out()

    def add_new_word(self):
        self.cls()
        input_eng_word = input("English: ").strip().lower()
        while self.is_string_empty(input_eng_word) or not input_eng_word.isalpha():
            self.cls()
            input_eng_word = input("English: ").strip().lower()

        input_uz_word = input("Uzbek: ").strip().lower()
        while self.is_string_empty(input_uz_word) or not input_uz_word.isalpha():
            self.cls()
            input_uz_word = input("Uzbek: ").strip().lower()

        self.eng_word = input_eng_word
        self.uz_word = input_uz_word

        my_db = self.entrance_database()
        mycursor = my_db.cursor()
        mycursor.execute(f"INSERT INTO words(English, Uzbek) VALUES ('{self.eng_word}', '{self.uz_word}')")
        my_db.commit()
        self.system_entrance()

    def show_words(self):
        self.cls()
        my_db = self.entrance_database()
        mycursor = my_db.cursor()
        mycursor.execute("select * from words")
        print("\n")
        for soz in mycursor:
            print("\t", soz[0], "\t|", soz[1])

        space = input("\nEnter")
        self.system_entrance()

    def search_word(self):
        self.cls()
        input_eng = input("English: ").strip().lower()
        while self.is_string_empty(input_eng) or not input_eng.isalpha():
            self.cls()
            input_eng = input("English: ").strip().lower()

        my_db = self.entrance_database()
        mycursor = my_db.cursor()
        mycursor.execute(f"select * from words where English='{input_eng}'")
        for soz in mycursor:
            print("\t", soz[0].capitalize(), "\t|", soz[1].capitalize())

    def go_out(self):
        self.cls()
        print("\n\n\t\tHave a good day!")
        sys.exit()

    @staticmethod
    def print_messege():
        print("""
        Add new word [1]
        Search word  [2]
        Show word    [3]
        Go out       [4]
        """)

    @staticmethod
    def cls():
        os.system("clear")

    @staticmethod
    def is_string_empty(str_):
        return not bool(str_)

    # @staticmethod
    # def entrance_database():
    #     return mysql.connector.connect(
    #         host="localhost",
    #         user="Avazbek",
    #         password="12345678",
    #         database="lugat"
    #     )

    @staticmethod
    def entrance_database():
        return mysql.connector.connect(
            host="localhost",
            user="Fayzullo",
            password="77777777",
            database="Register"
        )


dict1 = Our_dictionary()
dict1.system_entrance()